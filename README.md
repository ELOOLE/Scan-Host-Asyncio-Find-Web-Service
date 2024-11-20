# Scan-Host-Asyncio-Find-Web-Service
## Scan host asyncio to find all web services
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
[*] IP addr: 91.XXX.XXX.XXX
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
> Can scan faster if you set only one protocol. Default it scan http:// and https://

# !
> [!CAUTION]
> Education use only.
