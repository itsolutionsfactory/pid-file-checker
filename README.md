# pid-file-checker

```
$ pfc --help                                                                                                                                                                                                                              2021-01-13 15:51:34
usage: Check for the presence of a pid file.
The file must contain one and only one integer which must be the pid of a running process. Otherwise, return a code != 0.
Meant to be used in a healthcheck context like with Docker or Kubernetes.
       [-h] pid_file

positional arguments:
  pid_file    The pid file you want to monitor

optional arguments:
  -h, --help  show this help message and exit
```
