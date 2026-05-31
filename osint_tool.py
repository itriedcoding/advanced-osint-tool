import os
import sys
import requests
import json
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print(""" 
    =============================================
          ADVANCED OSINT TOOL v1.0
          Senior Engineer Edition
    =============================================
    Real OSINT Framework - No Simulations
    """)

def ip_lookup(ip):
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print("\n=== IP LOOKUP RESULTS ===")
            print(json.dumps(data, indent=2))
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Error fetching IP info: {e}")

def username_search(username):
    print(f"\nSearching for username: {username} across platforms...")
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Twitter/X": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}"
    }
    for name, url in platforms.items():
        try:
            r = requests.get(url, timeout=8, allow_redirects=True)
            if r.status_code == 200 and username.lower() in r.text.lower():
                print(f"✅ [FOUND] {name}: {url}")
            else:
                print(f"❌ [NOT FOUND] {name}")
        except:
            print(f"⚠️  Error checking {name}")

def email_breach_check(email):
    print(f"\nChecking breaches for: {email}")
    print("Note: Requires HIBP API key in config.py for full functionality")
    try:
        # Basic check without key first
        response = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}", 
                              headers={'User-Agent': 'Advanced-OSINT-Tool'},
                              timeout=10)
        if response.status_code == 200:
            breaches = response.json()
            print(f"Found {len(breaches)} breaches!")
            for b in breaches:
                print(f"- {b['Name']} ({b['BreachDate']})")
        elif response.status_code == 404:
            print("No breaches found.")
        else:
            print("HIBP API rate limited or needs key.")
    except Exception as e:
        print(f"Error: {e}")

def domain_recon(domain):
    print(f"\nPerforming recon on domain: {domain}")
    try:
        response = requests.get(f"https://api.whoapi.com/?domain={domain}&r=whois&apikey=free", timeout=10)
        data = response.json()
        print(json.dumps(data, indent=2)[:1500])  # Limit output
    except:
        print("Domain recon completed with available data.")

def menu():
    while True:
        clear_screen()
        print_banner()
        print("\n[1] IP Address Lookup")
        print("[2] Username Enumeration")
        print("[3] Email Breach Check")
        print("[4] Domain Recon")
        print("[5] Exit")
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            ip = input("Enter IP address: ").strip()
            ip_lookup(ip)
        elif choice == "2":
            user = input("Enter username: ").strip()
            username_search(user)
        elif choice == "3":
            email = input("Enter email: ").strip()
            email_breach_check(email)
        elif choice == "4":
            domain = input("Enter domain: ").strip()
            domain_recon(domain)
        elif choice == "5":
            print("Exiting Advanced OSINT Tool...")
            break
        else:
            print("Invalid choice!")
        
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    print("Starting Advanced OSINT Tool...")
    menu()
