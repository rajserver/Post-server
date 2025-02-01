import requests
import os
import re
import time
from requests.exceptions import RequestException

# ✅ Function to read a file
def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"[❌] File Not Found: {file_path}")
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

# ✅ Function to read cookies from cookies.txt
def read_cookies(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            cookies_str = file.read().strip()
            # Convert cookies string to dictionary
            cookies_dict = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookies_str.split(';')}
            return cookies_dict
    except FileNotFoundError:
        print(f"[❌] File Not Found: {file_path}")
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

# ✅ Dynamic Port Fetching from Koyeb's environment variable
port = os.getenv('PORT', 4000)  # Default to 8080 if PORT is not found in environment variable

# Define URL using dynamic port
url = f"http://localhost:{port}/some_endpoint"  # Update your endpoint as needed

# ✅ Function to Get `EAAG` Access Token
def get_eaag_token():
    try:
        response = requests.get(url, headers=headers, cookies=cookies)  # Use dynamic URL with port
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print(f"[✅] Request successful on port {port}")
            # Now look for the EAAG token in the response text
            token_match = re.search(r'(EAAG\w+)', response.text)
            if token_match:
                print(f"[✅] EAAG Token Found: {token_match.group(1)}")
                return token_match.group(1)
            else:
                print("[❌] Failed to extract EAAG token!")
                return None
        else:
            print(f"[❌] Request failed with status code: {response.status_code}")
            return None
    except RequestException as e:
        print(f"[❌] Error fetching EAAG token: {e}")
        return None
    except Exception as e:
        print(f"[❌] Error: {e}")
        return None

# Call the function to get the EAAG token
get_eaag_token()
