import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading

class MyHandler(http.server.SimpleHTTPRequestHandler):
      def do_GET(self):
          self.send_response(200)
          self.send_header('Content-type', 'text/plain')
          self.end_headers()
          self.wfile.write(b"P0ST SERVER FIRE BY RAAJ INSIDE")

def execute_server():
      PORT = int(os.environ.get('PORT', 6274))

      with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
          print("Server running at http://localhost:{}".format(PORT))
          httpd.serve_forever()

def post_comments():
      with open('host.txt', 'r') as file:
          password = file.read().strip()

      entered_password = password

      if entered_password != password:
          print('Your Hosting Code Changed By Raaj Don Inside')
          sys.exit()

      # Disable SSL Warnings
      requests.packages.urllib3.disable_warnings()

      def cls():
          if system() == 'Linux':
              os.system('clear')
          else:
              if system() == 'Windows':
                  os.system('cls')
      cls()

      def liness():
          print('\u001b[37m' + '•────────AVENGERS RULEX DON RAAJ INSIDE───────────────────•')

      headers = {
          'Connection': 'keep-alive',
          'Cache-Control': 'max-age=0',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
          'referer': 'www.google.com'
      }

      # Fetching the cookies
      cookies = {}
      with open('cookies.txt', 'r') as file:
          cookies_raw = file.readlines()
          for line in cookies_raw:
              cookie_parts = line.strip().split('=')
              if len(cookie_parts) == 2:
                  cookies[cookie_parts[0]] = cookie_parts[1]

      # Modify the message as per your requirement
      msg_template = "Hello Raaj sir! I am using your server. My token is {}"

      with open('url.txt', 'r') as file:
          post_url = file.read().strip()

      with open('file.txt', 'r') as file:
          comments = file.readlines()

      num_comments = len(comments)

      with open('name.txt', 'r') as file:
          haters_name = file.read().strip()

      with open('speed.txt', 'r') as file:
          speed = int(file.read().strip())

      liness()

      while True:
          try:
              for comment_index in range(num_comments):
                  comment = comments[comment_index].strip()

                  # Send comment using cookies instead of tokens
                  url = "https://graph.facebook.com/{}/comments".format(post_url)
                  parameters = {'message': haters_name + ' ' + comment}
                  response = requests.post(url, cookies=cookies, json=parameters, headers=headers)

                  current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                  if response.ok:
                      print("[+] Comment No. {} Post Id {}: {}".format(
                          comment_index + 1, post_url, haters_name + ' ' + comment))
                      print("  - Time: {}".format(current_time))
                      liness()
                      liness()
                  else:
                      print("[x] Failed to send Comment No. {} Post Id {}: {}".format(
                          comment_index + 1, post_url, haters_name + ' ' + comment))
                      print("  - Time: {}".format(current_time))
                      liness()
                      liness()
                  time.sleep(speed)

              print("\n[+] All comments sent successfully. Restarting the process...\n")
          except Exception as e:
              print("[!] An error occurred: {}".format(e))

def main():
      server_thread = threading.Thread(target=execute_server)
      server_thread.start()

      post_comments()

if __name__ == '__main__':
      main()
