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

# ✅ Load Required Data from Files
post_id = read_file("post.txt")  # Facebook Post ID
comments = read_file("comments.txt").splitlines()  # List of comments
commenter_name = read_file("name.txt")  # Name of the commenter
cookie = os.getenv("COOKIE")  # Facebook Cookie from Environment Variables

if not post_id or not comments or not commenter_name or not cookie:
    print("[❌] Missing required data! Exiting...")
    exit()

# ✅ Load Delay from time.txt
delay = read_time("time.txt")

if delay is None or delay <= 0:
    print("[❌] Invalid delay! Exiting...")
    exit()

# ✅ HTTP Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 Chrome/103.0.5060.71 Mobile Safari/537.36"
}

# ✅ Function to Get `EAAG` Access Token
def get_eaag_token():
    try:
        response = requests.get(
            "https://business.facebook.com/business_locations",
            headers=headers,
            cookies={"Cookie": cookie}
        )
        token_match = re.search(r'(EAAG\w+)', response.text)
        if token_match:
            return token_match.group(1)
        else:
            print("[❌] Failed to extract EAAG token!")
            return None
    except RequestException as e:
        print(f"[❌] Error fetching EAAG token: {e}")
        return None

# ✅ Get Valid EAAG Token
access_token = get_eaag_token()
if not access_token:
    print("[❌] Exiting... Invalid EAAG Token!")
    exit()

# ✅ Function to Post Comment
def post_comment(comment):
    data = {"message": f"{commenter_name}: {comment}", "access_token": access_token}
    try:
        response = requests.post(
            f"https://graph.facebook.com/{post_id}/comments/",
            data=data
        )
        if response.status_code == 200:
            print(f"✅ Comment Posted: {commenter_name}: {comment}")
        else:
            print(f"❌ Failed to Comment: {response.text}")
    except RequestException as e:
        print(f"[❌] Error Posting Comment: {e}")

# ✅ Commenting Loop with Delay
for comment in comments:
    post_comment(comment)
    time.sleep(delay)
