from scanner import run_scan
from report_generator import generate_report, save_report

print("=" * 50)
print("   NMAP + AI PENETRATION TEST REPORTER")
print("=" * 50)

print("\nThis tool scans a target and generates an AI security report.")
print("Only scan YOUR OWN devices!\n")

target = input("Enter target IP (press Enter for your own PC): ").strip()

if target == "":
    target = "127.0.0.1"

print("\n[*] Target set to: " + target)

scan_results = run_scan(target)

if not scan_results:
    print("[!] No results found. Check your target IP.")
else:
    print("[OK] Scan complete!")
    report = generate_report(scan_results, target)
    print("\n" + "=" * 50)
    print("SECURITY REPORT")
    print("=" * 50)
    print(report)
    save_report(report, target)
    print("\n[OK] All done! Check the reports folder.")
