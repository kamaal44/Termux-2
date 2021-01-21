The following issue exists in the android-msm-wahoo-4.4-pie branch of https://android.googlesource.com/kernel/msm (and possibly others):

There is a use-after-free of the wait member in the binder_thread struct in the binder driver at /drivers/android/binder.c. 

As described in the upstream commit: 
“binder_poll() passes the thread->wait waitqueue that
can be slept on for work. When a thread that uses
epoll explicitly exits using BINDER_THREAD_EXIT,
the waitqueue is freed, but it is never removed
from the corresponding epoll data structure. When
the process subsequently exits, the epoll cleanup
code tries to access the waitlist, which results in
a use-after-free.”

The following proof-of-concept will show the UAF crash in a kernel build with KASAN (from initial upstream bugreport at https://lore.kernel.org/lkml/20171213000517.GB62138@gmail.com/):
        #include <fcntl.h>
        #include <sys/epoll.h>
        #include <sys/ioctl.h>
        #include <unistd.h>

        #define BINDER_THREAD_EXIT 0x40046208ul

        int main()
        {
                int fd, epfd;
                struct epoll_event event = { .events = EPOLLIN };

                fd = open("/dev/binder0", O_RDONLY);
                epfd = epoll_create(1000);
                epoll_ctl(epfd, EPOLL_CTL_ADD, fd, &event);
                ioctl(fd, BINDER_THREAD_EXIT, NULL);
        }

This issue was patched in Dec 2017 in the 4.14 LTS kernel [1], AOSP android 3.18 kernel [2], AOSP android 4.4 kernel [3], and AOSP android 4.9 kernel [4], but the Pixel 2 with most recent security bulletin is still vulnerable based on source code review. 

Other devices which appear to be vulnerable based on source code review are (referring to 8.x releases unless otherwise stated):
1) Pixel 2 with Android 9 and Android 10 preview (https://android.googlesource.com/kernel/msm/+/refs/heads/android-msm-wahoo-4.4-q-preview-6/)
2) Huawei P20
3) Xiaomi Redmi 5A
4) Xiaomi Redmi Note 5
5) Xiaomi A1
6) Oppo A3
7) Moto Z3
8) Oreo LG phones (run same kernel according to website)
9) Samsung S7, S8, S9 


*We have evidence that this bug is being used in the wild. Therefore, this bug is subject to a 7 day disclosure deadline. After 7 days elapse or a patch has been made broadly available (whichever is earlier), the bug report will become visible to the public.*


Confirmed this proof-of-concept works on Pixel 2 with build walleye_kasan-userdebug 10 QP1A.191105.0035899767, causing KASAN crash. Proof of concept C code and new.out attached. KASAN console output attached.


I received technical information from TAG and external parties about an Android exploit that is attributed to NSO group. These details included facts about the bug and exploit methodology, including but not limited to:
 * It is a kernel privilege escalation using a use-after free vulnerability, accessible from inside the Chrome sandbox.
 * The bug was allegedly being used or sold by the NSO Group. 
 * It works on Pixel 1 and 2, but not Pixel 3 and 3a. 
 * It was patched in the Linux kernel >= 4.14 without a CVE. 
 * CONFIG_DEBUG_LIST breaks the primitive.
 * CONFIG_ARM64_UAO hinders exploitation.
 * The vulnerability is exploitable in Chrome's renderer processes under Android's 'isolated_app' SELinux domain, leading to us suspecting Binder as the vulnerable component.
 * The exploit requires little or no per-device customization.
 * A list of affected and unaffected devices and their versions, and more. A non-exhaustive list is available in the description of this issue.

Using these details, I have determined that the bug being used is almost certainly the one in this report as I ruled out other potential candidates by comparing patches. A more detailed explanation of this bug and the methodology to identify it will be written up in a forthcoming blog post when I find the time. 

We do not currently have a sample of the exploit. Without samples, we have neither been able to confirm the timeline nor the payload.

The bug is a local privilege escalation vulnerability that allows for a full compromise of a vulnerable device. If the exploit is delivered via the web, it only needs to be paired with a renderer exploit, as this vulnerability is accessible through the sandbox. 

I’ve attached a local exploit proof-of-concept to demonstrate how this bug can be used to gain arbitrary kernel read/write when run locally. It only requires untrusted app code execution to exploit CVE-2019-2215. I’ve also attached a screenshot (success.png) of the POC running on a Pixel 2, running Android 10 with security patch level September 2019 (google/walleye/walleye:10/QP1A.190711.020/5800535:user/release-keys).


Vendor statement from Android:

"This issue is rated as High severity on Android and by itself requires installation of a malicious application for potential exploitation. Any other vectors, such as via web browser, require chaining with an additional exploit. We have notified Android partners and the patch is available on the Android Common Kernel. Pixel 3 and 3a devices are not vulnerable while Pixel 1 and 2 devices will be receiving updates for this issue as part of the October update."


Proof of Concept:
https://github.com/offensive-security/exploitdb-bin-sploits/raw/master/bin-sploits/47463.zip