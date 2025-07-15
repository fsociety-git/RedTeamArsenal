import argparse
from modules.scanner import scan_network
from modules.vuln_detector import detect_vulnerabilities

def main():
    parser = argparse.ArgumentParser(description="Advanced Penetration Testing Toolkit")
    subparsers = parser.add_subparsers(dest="command")

    # Scan command
    scan_parser = subparsers.add_parser("scan", help="Network scanning")
    scan_parser.add_argument("--target", required=True, help="Target IP or range")
    scan_parser.add_argument("--ports", default="1-1024", help="Port range")

    # Detect command
    detect_parser = subparsers.add_parser("detect", help="Vulnerability detection")
    detect_parser.add_argument("--target", required=True, help="Target URL or IP")

    args = parser.parse_args()

    if args.command == "scan":
        print("Scanning...")
        results = scan_network(args.target, args.ports)
        print(results)
    elif args.command == "detect":
        print("Detecting vulnerabilities...")
        results = detect_vulnerabilities(args.target)
        print(results)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()