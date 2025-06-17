import os
import requests
import zipfile
from io import BytesIO

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/202004-divvy-tripdata.zip",
    "https://divvy-tripdata.s3.amazonaws.com/202005-divvy-tripdata.zip",
    "https://divvy-tripdata.s3.amazonaws.com/202006-divvy-tripdata.zip",
]

DOWNLOAD_DIR = os.path.join(os.path.dirname(__file__), "downloads")


def create_download_dir():
    """Create the downloads directory if it doesn't exist."""
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
        print(f"Created directory: {DOWNLOAD_DIR}")


def get_filename_from_url(url):
    """Extract filename from URL."""
    return url.split("/")[-1]


def download_and_extract_zip(url):
    """Download zip file, extract CSV, and delete zip."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error on bad HTTP status

        filename = get_filename_from_url(url)
        zip_path = os.path.join(DOWNLOAD_DIR, filename)

        # Write zip file
        with open(zip_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")

        # Extract zip file
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(DOWNLOAD_DIR)
        print(f"Extracted: {filename}")

        # Delete zip file
        os.remove(zip_path)
        print(f"Deleted zip: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")
    except zipfile.BadZipFile as e:
        print(f"Failed to unzip {url}: {e}")


def main():
    create_download_dir()
    for url in download_uris:
        download_and_extract_zip(url)


if __name__ == "__main__":
    main()
