## Image Downloader
This project is a simple image downloader that fetches images from URLs and saves them to your desktop.

### Key Features
✅ Automatic filename generation if no name is provided  
✅ Ensures URLs are properly formatted before attempting download  
✅ Creates a dedicated folder for organization  
✅ Clear feedback on download success or failure  

### What I Learned

1. **URL Handling & Input Validation**  
   Ensuring user input is correct is crucial. For example, I learned that URLs entered without `http://` or `https://` need to be corrected to prevent errors. I achieved this with:
   ```python
   if not url.startswith(('http://', 'https://')):
       url = 'https://' + url
   ```
   This improved usability by reducing input errors.

2. **Filename Generation**  
   I discovered that URLs don't always end with a clean filename. Using `urlparse` helped extract the filename, and I added a fallback to "image.jpg" to ensure a valid save name:
   ```python
   filename = os.path.basename(urlparse(url).path) or "image.jpg"
   ```

3. **File Management**  
   Creating a dedicated folder for downloads improved organization and ensured downloaded files wouldn’t clutter the desktop. I used:
   ```python
   folder = os.path.expanduser("~/Desktop/images_from_downloader")
   os.makedirs(folder, exist_ok=True)
   ```

4. **Error Handling**  
   I learned that network requests can fail for various reasons (e.g., invalid URLs, connectivity issues). Adding a `try/except` block improved reliability and provided clear error messages:
   ```python
   try:
       r = requests.get(url)
       if r.status_code == 200:
           with open(save_path, "wb") as img_file:
               img_file.write(r.content)
       else:
           print(f"Failed to download. Status code: {r.status_code}")
   except Exception as e:
       print(f"Download failed: {e}")
   ```

### How to Run the Code
1. Ensure Python and the `requests` library are installed.
2. Copy the script to your system.
3. Run the script and follow the prompts to:
   - Enter an image URL.
   - Choose a filename or allow the program to auto-generate one.
4. The image will be saved to your desktop inside the folder `images_from_downloader`.

### Final Thoughts
Building this tool improved my understanding of URL handling, file management, and error handling in Python.

