"""
Ubuntu-Inspired Image Fetcher
-----------------------------
The Wisdom of Ubuntu: "I am because we are"

This script fetches an image from a user-provided URL,
saves it into a folder called "Fetched_Images",
and handles errors gracefully.
"""

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
        response.raise_for_status()  # Raises error for 4xx/5xx responses

        # Extract filename from URL (default to 'downloaded_image.jpg' if none found)
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

# Run the program
if __name__ == "__main__":
    fetch_image()
