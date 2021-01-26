Sources:
https://bugs.chromium.org/p/project-zero/issues/detail?id=796
https://bugs.chromium.org/p/project-zero/issues/detail?id=795

The usermode audio subsystem for the "Samsung Android Professional Audio" is 
based on JACK, which appears to be designed for single-user usage. The common 
JACK configuration on Linux systems appears to be a JACK server running under 
the current user account, and interacting with JACK clients from the same user 
account; so with a minimal privilege difference; this is not the case with the 
configuration on Android, where the JACK service runs as a more privileged user 
in a less restrictive SELinux domain to the clients that can connect to it.

The shared memory implementation (implemented by com.samsung.android.IAndroidShm
system service) allows any application to access/modify/map shared memory pages 
used by JACK, regardless of which application created those shared memory pages.

(NB: This possibly results in breaking the Android permissions model and 
permitting applications without the required capability to access microphone 
input; this was not investigated further.)

There are multiple possible ways to corrupt the internal state of any of the 
shared-memory backed c++ objects in use; attached is a PoC that uses the shared 
memory service to map the JackEngineControl object in use, and modify the value 
of the fDriverNum member, which is used in several places without validation. 

This is highly likely not the only variable stored in shared memory that is used
without proper validation; and the function shown below is definitely not the
only place that this particular variable is used dangerously. To secure this 
interface it will be necessary to review all uses of variables stored in these
shared memory interfaces.

/*!
\brief Engine control in shared memory.
*/

PRE_PACKED_STRUCTURE
struct SERVER_EXPORT JackEngineControl : public JackShmMem
{
    // Shared state
    jack_nframes_t fBufferSize;
    jack_nframes_t fSampleRate;
    bool fSyncMode;
    bool fTemporary;
    jack_time_t fPeriodUsecs;
    jack_time_t fTimeOutUsecs;
    float fMaxDelayedUsecs;
    float fXrunDelayedUsecs;
    bool fTimeOut;
    bool fRealTime;
    bool fSavedRealTime;  // RT state saved and restored during Freewheel mode
    int fServerPriority;
    int fClientPriority;
    int fMaxClientPriority;
    char fServerName[JACK_SERVER_NAME_SIZE+1];
    JackTransportEngine fTransport;
    jack_timer_type_t fClockSource;
    int fDriverNum;
    bool fVerbose;

    // CPU Load
    jack_time_t fPrevCycleTime;
    jack_time_t fCurCycleTime;
    jack_time_t fSpareUsecs;
    jack_time_t fMaxUsecs;
    jack_time_t fRollingClientUsecs[JACK_ENGINE_ROLLING_COUNT];
    unsigned int fRollingClientUsecsCnt;
    int	fRollingClientUsecsIndex;
    int	fRollingInterval;
    float fCPULoad;

    // For OSX thread
    UInt64 fPeriod;
    UInt64 fComputation;
    UInt64 fConstraint;

    // Timer
    JackFrameTimer fFrameTimer;

#ifdef JACK_MONITOR
    JackEngineProfiling fProfiler;
#endif

    ...

This is quite a convenient exploitation primitive, as a small negative value 
will cause the code in several places to index backwards from a known array;
when (any of the similar functions to the below are called, table is pointing
to the fClientTable array inside a JackEngine instance)

void JackTransportEngine::MakeAllLocating(JackClientInterface** table)
{
    for (int i = GetEngineControl()->fDriverNum; i < CLIENT_NUM; i++) {
        JackClientInterface* client = table[i];
        if (client) {
            JackClientControl* control = client->GetClientControl();
            control->fTransportState = JackTransportStopped;
            control->fTransportSync = true;
            control->fTransportTimebase = true;
            jack_log("MakeAllLocating ref = %ld", i);
        }
    }
}

class SERVER_EXPORT JackEngine : public JackLockAble
{
    friend class JackLockedEngine;

    private:

        JackGraphManager* fGraphManager;
        JackEngineControl* fEngineControl;
        char fSelfConnectMode;
        JackClientInterface* fClientTable[CLIENT_NUM];

We can see that just behind the fClientTable, we have two pointers to other
objects; a JackEngineControl and a JackGraphManager, both of which are backed by
shared memory. Since we are treating the pointer read from table as a c++ object
with a vtable pointer, this lets us trivially gain control of the flow of 
execution.

 Fatal signal 11 (SIGSEGV), code 1, fault addr 0x41414140 in tid 27197 (jackd)
 *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
 Build fingerprint: 'samsung/zeroltexx/zerolte:6.0.1/MMB29K/G925FXXU3DPAD:user/release-keys'
 Revision: '10'
 ABI: 'arm'
 pid: 27181, tid: 27197, name: jackd  >>> /system/bin/jackd <<<
 AM write failed: Broken pipe
 signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 0x41414140
     r0 f3f1a000  r1 f48c2010  r2 f48c2010  r3 41414141
     r4 f3f1a000  r5 00000036  r6 f3dbf930  r7 00000078
     r8 f72c8b9c  r9 f6f1a308  sl f3d3f000  fp f719a991
     ip f71d7a0c  sp f3dbf7d8  lr f7196c43  pc 41414140  cpsr 800f0030
 
 backtrace:
     #00 pc 41414140  <unknown>
     #01 pc 0003cc41  /system/lib/libjackserver.so (Jack::JackTransportEngine::MakeAllLocating(Jack::JackClientInterface**)+52)
     #02 pc 0003cda1  /system/lib/libjackserver.so (Jack::JackTransportEngine::CycleEnd(Jack::JackClientInterface**, unsigned int, unsigned int)+228)
     #03 pc 00048bd5  /system/lib/libjackserver.so
     #04 pc 00049211  /system/lib/libjackserver.so (Jack::JackEngine::Process(unsigned long long, unsigned long long)+228)
     #05 pc 000442fd  /system/lib/libjackserver.so
     #06 pc 00044f49  /system/lib/libjackserver.so (Jack::JackAudioDriver::ProcessGraphSyncMaster()+40)
     #07 pc 00044f0d  /system/lib/libjackserver.so (Jack::JackAudioDriver::ProcessGraphSync()+20)
     #08 pc 00044e87  /system/lib/libjackserver.so (Jack::JackAudioDriver::ProcessSync()+94)
     #09 pc 00044bbf  /system/lib/libjackserver.so (Jack::JackAudioDriver::Process()+22)
     #10 pc 0004fff1  /system/lib/libjackserver.so (Jack::JackThreadedDriver::Process()+24)
     #11 pc 0005051f  /system/lib/libjackserver.so (Jack::JackThreadedDriver::Execute()+18)
     #12 pc 00040a0f  /system/lib/libjackserver.so (Jack::JackAndroidThread::ThreadHandler(void*)+126)
     #13 pc 0003fc53  /system/lib/libc.so (__pthread_start(void*)+30)
     #14 pc 0001a38b  /system/lib/libc.so (__start_thread+6)
 
 Tombstone written to: /data/tombstones/tombstone_05

################################################################################################################

The usermode audio subsystem for the "Samsung Android Professional Audio" is 
based on JACK, which appears to be designed for single-user usage. The common 
JACK configuration on Linux systems appears to be a JACK server running under 
the current user account, and interacting with JACK clients from the same user 
account; so with a minimal privilege difference; this is not the case with the 
configuration on Android, where the JACK service runs as a more privileged user 
in a less restrictive SELinux domain to the clients that can connect to it.

The JACK shared memory implementation uses the struct jack_shm_info_t defined in
/common/shm.h to do some bookkeeping

PRE_PACKED_STRUCTURE
struct _jack_shm_info {
    jack_shm_registry_index_t index;       /* offset into the registry */
    uint32_t size;
#ifdef __ANDROID__
    jack_shm_fd_t fd;
#endif
    union {
        void *attached_at;  /* address where attached */
        char ptr_size[8];
    } ptr;  /* a "pointer" that has the same 8 bytes size when compling in 32 or 64 bits */
} POST_PACKED_STRUCTURE;

typedef struct _jack_shm_info jack_shm_info_t;

This struct is stored at the start of every JackShmAble object.

/*!
\brief
A class which objects possibly want to be allocated in shared memory derives from this class.
*/

class JackShmMemAble
{
    protected:

        jack_shm_info_t fInfo;

    public:

        void Init();

        int GetShmIndex()
        {
            return fInfo.index;
        }

        char* GetShmAddress()
        {
            return (char*)fInfo.ptr.attached_at;
        }

        void LockMemory()
        {
            LockMemoryImp(this, fInfo.size);
        }

        void UnlockMemory()
        {
            UnlockMemoryImp(this, fInfo.size);
        }

};

This means that whenever the JACK server creates an object backed by shared 
memory, it also stores a pointer to that object (in the address space of the 
JACK server), allowing a malicious client to bypass ASLR in the JACK server 
process. 

The PoC provided for the other reported JACK issue uses this to bypass ASLR in 
the JACK server process.


Proof of Concept:
https://github.com/offensive-security/exploitdb-bin-sploits/raw/master/bin-sploits/40066.zip