# 🌍 Ubuntu-Inspired Image Fetcher Assignment

## ✨ Description
The Wisdom of Ubuntu: *"I am because we are"*  

In the spirit of Ubuntu, which emphasizes **community and sharing**, this Python program connects to the global community of the internet, respectfully fetches shared resources (images), and organizes them for later appreciation.  

---

## 🎯 Task Requirements
- Prompt the user for a URL containing an image  
- Create a directory called **Fetched_Images** if it doesn't exist  
- Download the image from the provided URL  
- Save it to the Fetched_Images directory with an appropriate filename  
- Handle errors gracefully, respecting that not all connections succeed  

---

## 🛠️ Technologies & Libraries
- **Python 3**  
- **requests** library (for fetching images)  
- **os** (for directory handling)  

Install dependencies if needed:  
```bash
pip install requests
```

---

## 📜 Example Code
```python
import os
import requests

def fetch_image():
    # Prompt the user for an image URL
    url = input("🌍 Enter the image URL: ").strip()

    # Create directory if not exists
    folder = "Fetched_Images"
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"📁 Created directory: {folder}")

    try:
        # Fetch the image using requests
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()

        # Extract filename from URL
        filename = url.split("/")[-1]
        if not filename or "." not in filename:
            filename = "downloaded_image.jpg"

        filepath = os.path.join(folder, filename)

        # Save image to disk
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"✅ Image successfully saved to: {filepath}")

    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL. Please include 'http://' or 'https://'")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Network error: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

if __name__ == "__main__":
    fetch_image()
```

---

## 🚀 How to Run
1. Save the script as `ubuntu_image_fetcher.py`  
2. Run it in your terminal:  
   ```bash
   python ubuntu_image_fetcher.py
   ```  
3. Enter an image URL when prompted  
4. The image will be saved in the **Fetched_Images** folder  

---

## ✅ Learning Outcomes
By completing this assignment, you will practice:  
1. Using **Python libraries** like `requests` for HTTP requests  
2. Handling **files and directories** in Python  
3. Writing **error handling** for real-world reliability  
4. Applying the **Ubuntu philosophy** of sharing and community in programming  

---

💡 *This project highlights how Python empowers us to interact with the global community respectfully and responsibly.*  
