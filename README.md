# Scan-Host-Asyncio-Find-Web-Service
## Scan host asynchronous to find all web services
### Every request is send with random User-Agent

Example:
```
python3.12 scan_host_async.py -t 3 -sh www.address.com
```

### Switches:
> -t (timeout), default timeout is 5 seconds

> -sh (single host), set target

> [!NOTE]
>Example result:

```
[*] Scanning address: www.address.com
[*] IP addr: X.X.X.X
[*] Urls list to check: 131072
[*] Adding addr: https://www.address.com:65535   
[+] Alive addr http://www.address.com:80
[+] Alive addr http://www.address.com:443
[+] Alive addr http://www.address.com:2223
[+] Alive addr http://www.address.com:2222
[+] Alive addr http://www.address.com:28888
[+] Alive addr https://www.address.com:0
[+] Alive addr https://www.address.com:443
[+] Alive addr https://www.address.com:2223
[+] Alive addr https://www.address.com:18887
[*] Url: https://www.address.com:65535   
[*] Execution time: 33.99 minutes
```

> [!TIP]
> Time scan from ~9 min to ~35 min per host.
> Scan can be faster if you set only one protocol by default it scan two protocols http:// and https://

> [!IMPORTANT]
> utilization 1%.

> [!WARNING]
> It works. :)

# !
> [!CAUTION]
> Education use only.
