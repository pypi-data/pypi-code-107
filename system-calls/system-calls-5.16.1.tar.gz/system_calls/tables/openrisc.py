# Content autogenerated. Do not edit.

syscalls_openrisc = {
    "accept": 202,
    "accept4": 242,
    "acct": 89,
    "add_key": 217,
    "adjtimex": 171,
    "bind": 200,
    "bpf": 280,
    "brk": 214,
    "capget": 90,
    "capset": 91,
    "chdir": 49,
    "chroot": 51,
    "clock_adjtime": 266,
    "clock_adjtime64": 405,
    "clock_getres": 114,
    "clock_getres_time64": 406,
    "clock_gettime": 113,
    "clock_gettime64": 403,
    "clock_nanosleep": 115,
    "clock_nanosleep_time64": 407,
    "clock_settime": 112,
    "clock_settime64": 404,
    "clone": 220,
    "clone3": 435,
    "close": 57,
    "close_range": 436,
    "connect": 203,
    "copy_file_range": 285,
    "delete_module": 106,
    "dup": 23,
    "dup3": 24,
    "epoll_create1": 20,
    "epoll_ctl": 21,
    "epoll_pwait": 22,
    "epoll_pwait2": 441,
    "eventfd2": 19,
    "execve": 221,
    "execveat": 281,
    "exit": 93,
    "exit_group": 94,
    "faccessat": 48,
    "faccessat2": 439,
    "fadvise64_64": 223,
    "fallocate": 47,
    "fanotify_init": 262,
    "fanotify_mark": 263,
    "fchdir": 50,
    "fchmod": 52,
    "fchmodat": 53,
    "fchown": 55,
    "fchownat": 54,
    "fcntl64": 25,
    "fdatasync": 83,
    "fgetxattr": 10,
    "finit_module": 273,
    "flistxattr": 13,
    "flock": 32,
    "fremovexattr": 16,
    "fsconfig": 431,
    "fsetxattr": 7,
    "fsmount": 432,
    "fsopen": 430,
    "fspick": 433,
    "fstat64": 80,
    "fstatat64": 79,
    "fstatfs64": 44,
    "fsync": 82,
    "ftruncate64": 46,
    "futex": 98,
    "futex_time64": 422,
    "futex_waitv": 449,
    "get_mempolicy": 236,
    "get_robust_list": 100,
    "getcpu": 168,
    "getcwd": 17,
    "getdents64": 61,
    "getegid": 177,
    "geteuid": 175,
    "getgid": 176,
    "getgroups": 158,
    "getitimer": 102,
    "getpeername": 205,
    "getpgid": 155,
    "getpid": 172,
    "getppid": 173,
    "getpriority": 141,
    "getrandom": 278,
    "getresgid": 150,
    "getresuid": 148,
    "getrlimit": 163,
    "getrusage": 165,
    "getsid": 156,
    "getsockname": 204,
    "getsockopt": 209,
    "gettid": 178,
    "gettimeofday": 169,
    "getuid": 174,
    "getxattr": 8,
    "init_module": 105,
    "inotify_add_watch": 27,
    "inotify_init1": 26,
    "inotify_rm_watch": 28,
    "io_cancel": 3,
    "io_destroy": 1,
    "io_getevents": 4,
    "io_pgetevents": 292,
    "io_pgetevents_time64": 416,
    "io_setup": 0,
    "io_submit": 2,
    "io_uring_enter": 426,
    "io_uring_register": 427,
    "io_uring_setup": 425,
    "ioctl": 29,
    "ioprio_get": 31,
    "ioprio_set": 30,
    "kcmp": 272,
    "kexec_file_load": 294,
    "kexec_load": 104,
    "keyctl": 219,
    "kill": 129,
    "landlock_add_rule": 445,
    "landlock_create_ruleset": 444,
    "landlock_restrict_self": 446,
    "lgetxattr": 9,
    "linkat": 37,
    "listen": 201,
    "listxattr": 11,
    "llistxattr": 12,
    "lookup_dcookie": 18,
    "lremovexattr": 15,
    "lsetxattr": 6,
    "madvise": 233,
    "mbind": 235,
    "membarrier": 283,
    "memfd_create": 279,
    "migrate_pages": 238,
    "mincore": 232,
    "mkdirat": 34,
    "mknodat": 33,
    "mlock": 228,
    "mlock2": 284,
    "mlockall": 230,
    "mmap2": 222,
    "mount": 40,
    "mount_setattr": 442,
    "move_mount": 429,
    "move_pages": 239,
    "mprotect": 226,
    "mq_getsetattr": 185,
    "mq_notify": 184,
    "mq_open": 180,
    "mq_timedreceive": 183,
    "mq_timedreceive_time64": 419,
    "mq_timedsend": 182,
    "mq_timedsend_time64": 418,
    "mq_unlink": 181,
    "mremap": 216,
    "msgctl": 187,
    "msgget": 186,
    "msgrcv": 188,
    "msgsnd": 189,
    "msync": 227,
    "munlock": 229,
    "munlockall": 231,
    "munmap": 215,
    "name_to_handle_at": 264,
    "nanosleep": 101,
    "nfsservctl": 42,
    "open_by_handle_at": 265,
    "open_tree": 428,
    "openat": 56,
    "openat2": 437,
    "or1k_atomic": 244,
    "perf_event_open": 241,
    "personality": 92,
    "pidfd_getfd": 438,
    "pidfd_open": 434,
    "pidfd_send_signal": 424,
    "pipe2": 59,
    "pivot_root": 41,
    "pkey_alloc": 289,
    "pkey_free": 290,
    "pkey_mprotect": 288,
    "ppoll": 73,
    "ppoll_time64": 414,
    "prctl": 167,
    "pread64": 67,
    "preadv": 69,
    "preadv2": 286,
    "prlimit64": 261,
    "process_madvise": 440,
    "process_mrelease": 448,
    "process_vm_readv": 270,
    "process_vm_writev": 271,
    "pselect6": 72,
    "pselect6_time64": 413,
    "ptrace": 117,
    "pwrite64": 68,
    "pwritev": 70,
    "pwritev2": 287,
    "quotactl": 60,
    "quotactl_fd": 443,
    "read": 63,
    "readahead": 213,
    "readlinkat": 78,
    "readv": 65,
    "reboot": 142,
    "recvfrom": 207,
    "recvmmsg": 243,
    "recvmmsg_time64": 417,
    "recvmsg": 212,
    "remap_file_pages": 234,
    "removexattr": 14,
    "renameat": 38,
    "renameat2": 276,
    "request_key": 218,
    "restart_syscall": 128,
    "rseq": 293,
    "rt_sigaction": 134,
    "rt_sigpending": 136,
    "rt_sigprocmask": 135,
    "rt_sigqueueinfo": 138,
    "rt_sigreturn": 139,
    "rt_sigsuspend": 133,
    "rt_sigtimedwait": 137,
    "rt_sigtimedwait_time64": 421,
    "rt_tgsigqueueinfo": 240,
    "sched_get_priority_max": 125,
    "sched_get_priority_min": 126,
    "sched_getaffinity": 123,
    "sched_getattr": 275,
    "sched_getparam": 121,
    "sched_getscheduler": 120,
    "sched_rr_get_interval": 127,
    "sched_rr_get_interval_time64": 423,
    "sched_setaffinity": 122,
    "sched_setattr": 274,
    "sched_setparam": 118,
    "sched_setscheduler": 119,
    "sched_yield": 124,
    "seccomp": 277,
    "semctl": 191,
    "semget": 190,
    "semop": 193,
    "semtimedop": 192,
    "semtimedop_time64": 420,
    "sendfile64": 71,
    "sendmmsg": 269,
    "sendmsg": 211,
    "sendto": 206,
    "set_mempolicy": 237,
    "set_robust_list": 99,
    "set_tid_address": 96,
    "setdomainname": 162,
    "setfsgid": 152,
    "setfsuid": 151,
    "setgid": 144,
    "setgroups": 159,
    "sethostname": 161,
    "setitimer": 103,
    "setns": 268,
    "setpgid": 154,
    "setpriority": 140,
    "setregid": 143,
    "setresgid": 149,
    "setresuid": 147,
    "setreuid": 145,
    "setrlimit": 164,
    "setsid": 157,
    "setsockopt": 208,
    "settimeofday": 170,
    "setuid": 146,
    "setxattr": 5,
    "shmat": 196,
    "shmctl": 195,
    "shmdt": 197,
    "shmget": 194,
    "shutdown": 210,
    "sigaltstack": 132,
    "signalfd4": 74,
    "socket": 198,
    "socketpair": 199,
    "splice": 76,
    "statfs64": 43,
    "statx": 291,
    "swapoff": 225,
    "swapon": 224,
    "symlinkat": 36,
    "sync": 81,
    "sync_file_range": 84,
    "syncfs": 267,
    "sysinfo": 179,
    "syslog": 116,
    "tee": 77,
    "tgkill": 131,
    "timer_create": 107,
    "timer_delete": 111,
    "timer_getoverrun": 109,
    "timer_gettime": 108,
    "timer_gettime64": 408,
    "timer_settime": 110,
    "timer_settime64": 409,
    "timerfd_create": 85,
    "timerfd_gettime": 87,
    "timerfd_gettime64": 410,
    "timerfd_settime": 86,
    "timerfd_settime64": 411,
    "times": 153,
    "tkill": 130,
    "truncate64": 45,
    "umask": 166,
    "umount2": 39,
    "uname": 160,
    "unlinkat": 35,
    "unshare": 97,
    "userfaultfd": 282,
    "utimensat": 88,
    "utimensat_time64": 412,
    "vhangup": 58,
    "vmsplice": 75,
    "wait4": 260,
    "waitid": 95,
    "write": 64,
    "writev": 66,
}
