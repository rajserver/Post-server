import requests
import os
import re
import time
from requests.exceptions import RequestException, Timeout, ConnectionError

# ✅ Function to read a file
def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"[❌] File Not Found: {file_path}")
        return None
    except Exception as e:
        print(f"[❌] Error reading {file_path}: {e}")
        return None

# ✅ Function to Read Delay from time.txt
def read_time(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return float(file.read().strip())
    except FileNotFoundError:
        print(f"[❌] File Not Found: {file_path}")
        return None
    except ValueError:
        print("[❌] Invalid value in time.txt. Please enter a valid number.")
        return None
    except Exception as e:
        print(f"[❌] Error reading {file_path}: {e}")
        return None

# ✅ Function to read cookies from cookies.txt
def read_cookies(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            cookies_str = file.read().strip()
            # Convert cookies string to dictionary
            cookies_dict = {cookie.split('=')[0].strip(): cookie.split('=')[1].strip() for cookie in cookies_str.split(';') if '=' in cookie}
            return cookies_dict
    except FileNotFoundError:
        print(f"[❌] File Not Found: {file_path}")
        return None
    except Exception as e:
        print(f"[❌] Error reading {file_path}: {e}")
        return None

# ✅ Load Required Data from Files
post_id = read_file("post.txt")  # Facebook Post ID
comments = read_file("comments.txt").splitlines()  # List of comments
commenter_name = read_file("name.txt")  # Name of the commenter

# ✅ Load Delay and Cookies
delay = read_time("time.txt")
cookies = read_cookies("cookies.txt")

if not post_id or not comments or not commenter_name or not cookies:
    print("[❌] Missing required data! Exiting...")
    exit()

if delay is None or delay <= 0:
    print("[❌] Invalid delay! Exiting...")
    exit()

# ✅ HTTP Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 Chrome/103.0.5060.71 Mobile Safari/537.36"
}

port = os.getenv('PORT', 4000)  # Default to 4000 if PORT is not found in environment variable


url = f"http://localhost:{4000}/some_endpoint"  # Update endpoint as needed

# ✅ Function to get EAAG Token
def get_eaag_token():
    try:
        # Retry mechanism for network issues (3 retries)
        retries = 3
        for attempt in range(retries):
            try:
                response = requests.get(url, headers=headers, cookies=cookies, timeout=10)  # Added timeout

                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    print(f"[✅] Request successful on port {4000}")
                    
