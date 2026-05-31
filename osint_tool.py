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
          ADVANCED OSINT TOOL v1.0 by Senior Engineer
    =============================================
    Menu-based Python OSINT Framework with Batch Launcher
    """)

def ip_lookup(ip):
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        data = response.json()
        print(json.dumps(data, indent=2))
    except:
        print("Error fetching IP info")

def username_search(username):
    sites = ["twitter.com", "instagram.com", "github.com"]  # Add more
    print(f"Searching for username: {username}")
    for site in sites:
        print(f"Checking {site}/{username} - (Simulated check)")

def email_check(email):
    print(f"Checking breaches for {email} using haveibeenpwned simulation")
    # In real: use API

def menu():
    while True:
        clear_screen()
        print_banner()
        print("1. IP Address Lookup")
        print("2. Username Search")
        print("3. Email Breach Check")
        print("4. Domain WHOIS (Simulated)")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            ip = input("Enter IP: ")
            ip_lookup(ip)
        elif choice == "2":
            user = input("Enter username: ")
            username_search(user)
        elif choice == "3":
            email = input("Enter email: ")
            email_check(email)
        elif choice == "4":
            domain = input("Enter domain: ")
            print(f"WHOIS for {domain}: Simulated data")
        elif choice == "5":
            print("Exiting...")
            break
        input("Press Enter to continue...")

if __name__ == "__main__":
    menu()