# pg_basebackup
# Autogenerated from man page /data/data/com.termux/files/usr/share/man/man1/pg_basebackup.1.gz
complete -c pg_basebackup -s D --description 'Sets the target directory to write the output to.'
complete -c pg_basebackup -o 'R
.br
--write-recovery-conf' --description 'Creates a standby.'
complete -c pg_basebackup -s T --description 'Relocates the tablespace in directory olddir to newdir during the backup.'
complete -c pg_basebackup -l waldir --description 'Sets the directory to write WAL (write-ahead log) files to.'
complete -c pg_basebackup -o 'z
.br
--gzip' --description 'Enables gzip compression of tar file output, with the default compression lev…'
complete -c pg_basebackup -s Z --description 'Enables gzip compression of tar file output, and specifies the compression le…'
complete -c pg_basebackup -s c --description 'Sets checkpoint mode to fast (immediate) or spread (the default) (see Section…'
complete -c pg_basebackup -o 'C
.br
--create-slot' --description 'Specifies that the replication slot named by the --slot option should be crea…'
complete -c pg_basebackup -s l --description 'Sets the label for the backup.'
complete -c pg_basebackup -o 'n
.br
--no-clean' --description 'By default, when pg_basebackup aborts with an error, it removes any directori…'
complete -c pg_basebackup -o 'N
.br
--no-sync' --description 'By default, pg_basebackup will wait for all files to be written safely to dis…'
complete -c pg_basebackup -o 'P
.br
--progress' --description 'Enables progress reporting.'
complete -c pg_basebackup -s r --description 'Sets the maximum transfer rate at which data is collected from the source ser…'
complete -c pg_basebackup -s S --description 'This option can only be used together with -X stream.'
complete -c pg_basebackup -o 'v
.br
--verbose' --description 'Enables verbose mode.'
complete -c pg_basebackup -l manifest-checksums --description 'Specifies the checksum algorithm that should be applied to each file included…'
complete -c pg_basebackup -l manifest-force-encode --description 'Forces all filenames in the backup manifest to be hex-encoded.'
complete -c pg_basebackup -l no-estimate-size --description 'Prevents the server from estimating the total amount of backup data that will…'
complete -c pg_basebackup -l no-manifest --description 'Disables generation of a backup manifest.'
complete -c pg_basebackup -l no-slot --description 'Prevents the creation of a temporary replication slot for the backup.'
complete -c pg_basebackup -l no-verify-checksums --description 'Disables verification of checksums, if they are enabled on the server the bas…'
complete -c pg_basebackup -s d --description 'Specifies parameters used to connect to the server, as a connction string; th…'
complete -c pg_basebackup -s h --description 'Specifies the host name of the machine on which the server is running.'
complete -c pg_basebackup -s p --description 'Specifies the TCP port or local Unix domain socket file extension on which th…'
complete -c pg_basebackup -s s --description 'Specifies the number of seconds between status packets sent back to the sourc…'
complete -c pg_basebackup -s U --description 'Specifies the user name to connect as.'
complete -c pg_basebackup -o 'w
.br
--no-password' --description 'Prevents issuing a password prompt.'
complete -c pg_basebackup -o 'W
.br
--password' --description 'Forces pg_basebackup to prompt for a password before connecting to the source…'
complete -c pg_basebackup -o 'V
.br
--version' --description 'Prints the pg_basebackup version and exits.'
complete -c pg_basebackup -o '?
.br
--help' --description 'Shows help about pg_basebackup command line arguments, and exits.'
complete -c pg_basebackup -s X --description 'oc o 2. 3.'
complete -c pg_basebackup -l pgdata --description '.'
complete -c pg_basebackup -s F --description '.'
complete -c pg_basebackup -l format --description '.'
complete -c pg_basebackup -s R --description '.'
complete -c pg_basebackup -l write-recovery-conf --description '.'
complete -c pg_basebackup -l tablespace-mapping --description '.'
complete -c pg_basebackup -l wal-method --description '.'
complete -c pg_basebackup -s z --description '.'
complete -c pg_basebackup -l gzip --description '.'
complete -c pg_basebackup -l compress --description '.'
complete -c pg_basebackup -l checkpoint --description '.'
complete -c pg_basebackup -s C --description '.'
complete -c pg_basebackup -l create-slot --description '.'
complete -c pg_basebackup -l slot --description 'option should be created before starting the backup.'
complete -c pg_basebackup -l label --description '.'
complete -c pg_basebackup -s n --description '.'
complete -c pg_basebackup -l no-clean --description '.'
complete -c pg_basebackup -s N --description '.'
complete -c pg_basebackup -l no-sync --description '.'
complete -c pg_basebackup -s P --description '.'
complete -c pg_basebackup -l progress --description '.'
complete -c pg_basebackup -l max-rate --description '.'
complete -c pg_basebackup -s v --description '.'
complete -c pg_basebackup -l verbose --description '.'
complete -c pg_basebackup -l dbname --description '.'
complete -c pg_basebackup -l host --description '.'
complete -c pg_basebackup -l port --description '.'
complete -c pg_basebackup -l status-interval --description '.'
complete -c pg_basebackup -l username --description '.'
complete -c pg_basebackup -s w --description '.'
complete -c pg_basebackup -l no-password --description '.'
complete -c pg_basebackup -s W --description '.'
complete -c pg_basebackup -l password --description '.'
complete -c pg_basebackup -s V --description '.'
complete -c pg_basebackup -l version --description '.'
complete -c pg_basebackup -s '?' --description '.'
complete -c pg_basebackup -l help --description '.'
