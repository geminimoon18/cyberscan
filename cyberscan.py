import socket
import re
import sys
import requests

# -------------------------
# PORT SCANNER
# -------------------------
def port_scanner(target, ports):
    print(f"\nScanning {target}...\n")

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[OPEN] Port {port}")
            sock.close()
        except Exception:
            pass


# -------------------------
# PASSWORD STRENGTH CHECKER
# -------------------------
def password_checker(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    if strength <= 2:
        print("Weak Password ❌")
    elif strength == 3 or strength == 4:
        print("Moderate Password ⚠️")
    else:
        print("Strong Password ✅")


# -------------------------
# BANNER GRABBER
# -------------------------
def banner_grabber(target, port):
    try:
        sock = socket.socket()
        sock.connect((target, port))
        banner = sock.recv(1024)
        print("Banner:", banner.decode().strip())
        sock.close()
    except:
        print("Unable to grab banner.")


# -------------------------
# IP GEOLOCATION
# -------------------------
def ip_geolocation(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        if data["status"] == "success":
            print("\nIP Geolocation Info:")
            print("Country:", data["country"])
            print("Region:", data["regionName"])
            print("City:", data["city"])
            print("ISP:", data["isp"])
            print("Latitude:", data["lat"])
            print("Longitude:", data["lon"])
        else:
            print("Invalid IP or unable to fetch data.")
    except Exception as e:
        print("Error:", e)


# -------------------------
# MAIN MENU LOOP
# -------------------------
def main():
    while True:
        print("""
=============================
      CyberScan Toolkit
=============================
1. Port Scanner
2. Password Strength Checker
3. Banner Grabber
4. IP Geolocation
5. Exit
""")

        choice = input("Select option: ")

        if choice == "1":
            target = input("Enter target IP: ")
            ports = [21, 22, 23, 25, 53, 80, 443]
            port_scanner(target, ports)

        elif choice == "2":
            password = input("Enter password: ")
            password_checker(password)

        elif choice == "3":
            target = input("Enter target IP: ")
            port = int(input("Enter port: "))
            banner_grabber(target, port)

        elif choice == "4":
            ip = input("Enter IP address: ")
            ip_geolocation(ip)

        elif choice == "5":
            print("Exiting CyberScan...")
            sys.exit()

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
