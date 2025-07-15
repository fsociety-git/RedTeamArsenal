# This is a wrapper if needed beyond the module
import nmap

def run_nmap_scan(target, arguments="-sV"):
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments=arguments)
    return scanner