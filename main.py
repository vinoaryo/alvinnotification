import os
import platform
import json
import requests
from datetime import datetime

# Automatically detect the system name
system_name = platform.node() or os.getenv("COMPUTERNAME", "Unknown-PC")

# ntfy topic
topic = "AlvinPC"
url = f"https://ntfy.sh/{topic}"

# Message payload
message = f"{system_name} is online at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
payload = message

# Send request
headers = {
    "Content-Type": "text/plain;charset=UTF-8",
    "User-Agent": "Python/ntfy-client"
}

response = requests.put(url, data=json.dumps(payload), headers=headers)

# Show result
if response.status_code == 200:
    print(f"✅ Notification sent: {message}")
else:
    print(f"❌ Failed to send ({response.status_code}): {response.text}")
