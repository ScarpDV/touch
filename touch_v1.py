import time
import os
import requests
import pyfiglet
import subprocess  # For rebooting to fastboot

cat_frames = [
    r"""
     /\_/\  
    ( o.o ) 
     > ^ <  
    """,
    r"""
     /\_/\  
    ( -.- ) 
     > ^ <  
    """,
    r"""
     /\_/\  
    ( ^.^ ) 
     > ^ <  
    """,
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def network_check():
    try:
        requests.get('https://www.google.com', timeout=3)
        print("Network status: Connected")
    except requests.ConnectionError:
        print("Network status: Not connected")

def site_check(url):
    try:
        response = requests.get(url)
        print(f"Website: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Content Length: {len(response.content)} bytes")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def ip_info(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        data = response.json()
        print(f"IP: {data.get('ip', 'N/A')}")
        print(f"Hostname: {data.get('hostname', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"Location: {data.get('loc', 'N/A')}")
        print(f"Organization: {data.get('org', 'N/A')}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def reboot_to_fastboot():
    try:
        subprocess.run(["adb", "reboot", "bootloader"], check=True)  # Requires ADB installed and device connected
        print("Rebooting to fastboot mode...")
    except Exception as e:
        print(f"Error: {e}. Make sure ADB is installed and your device is connected.")

# Генерация ASCII-арта
touch_art = pyfiglet.figlet_format("TOUCH V 1", font="slant")

# Цикл анимации
while True:
    for frame in cat_frames:
        clear_screen()
        print(frame)
        time.sleep(0.5)

    clear_screen()
    print("\033[38;5;214m" + touch_art + "\033[0m")  # Красно-оранжевый текст
    print("\033[32m1: network check\033[0m")  # Зеленый текст
    print("\033[32m2: site check\033[0m")     # Зеленый текст
    print("\033[32m3: ip info\033[0m")        # Зеленый текст
    print("\033[32m4: reload to fastboot\033[0m")  # Зеленый текст

    choice = input("Choose an option (1, 2, 3, or 4): ")

    if choice == '1':
        network_check()
    elif choice == '2':
        url = input("Enter URL (e.g., http://example.com): ")
        site_check(url)
    elif choice == '3':
        ip = input("Enter IP address: ")
        ip_info(ip)
    elif choice == '4':
        reboot_to_fastboot()
    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")

    input("Press Enter to continue...")  # Ждать ввода пользователя перед повтором