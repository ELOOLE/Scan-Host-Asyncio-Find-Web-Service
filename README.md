# Scan-Host-Asyncio-Find-Web-Service
Scan host asyncio to find all web services

Każdy request jest z innym losowym agentem. 

Przykład użycia:
```
python3.12 scan_host_async.py -t 3 -sh ateneum.bip.gov.pl
```

standardowo timeout jest 5 s, w powyższym przykładzie zmieniono to na 3 s.
Przełącznik -sh (single host) jest wskazaniem celu do skanownia. 
