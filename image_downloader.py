import requests
import os
from urllib.parse import urlparse

# Ask for URL and filename
url = input("Image URL: ").strip()
if not url.startswith(('http://', 'https://')):
    url = 'https://' + url

filename = input("Save as (leave blank to auto-name): ").strip()
if not filename:
    filename = os.path.basename(urlparse(url).path) or "image.jpg"

# Create folder to save images
folder = os.path.expanduser("~/Desktop/images_from_downloader")
os.makedirs(folder, exist_ok=True)

# Full save path
save_path = os.path.join(folder, filename)
print(f"Saving to: {save_path}")

# Try to download the image
try:
    r = requests.get(url)
    if r.status_code == 200:
        with open(save_path, "wb") as img_file:
            img_file.write(r.content)
        print(f"Image saved! Check {save_path}")
    else:
        print(f"Failed to download. Status code: {r.status_code}")

except Exception as e:
    print(f"Download failed: {e}")
