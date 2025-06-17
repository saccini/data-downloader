# Divvy Trip Data Downloader

This project downloads and extracts Divvy trip data CSV files using Python. It's fully containerized using Docker for consistent, reproducible execution.

---

## 🚀 How to Run (Using Docker)

### 1. Clone the Repository

If you haven’t already:

```bash
git clone https://github.com/saccini/data-downloader.git
```

### 2. Build and Run the Project

Use Docker Compose:

```bash
docker-compose up --build
```
This will:

- Build the Docker image
- Run main.py inside the container
- Download and extract CSVs into downloads/ folder


### 3. Output

Extracted .csv files will appear in the downloads/ folder (ignored by Git).

🐳 Project Structure


```
data-downloader/
├── main.py              # Main Python script
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build instructions
├── docker-compose.yml   # Docker Compose setup
├── .gitignore           # Excludes downloads and more
├── .dockerignore        # Optimizes Docker build
├── downloads/           # Downloaded CSVs (auto-generated)
└── README.md            # You're here!
```

📦 Dependencies

All Python dependencies are listed in requirements.txt. These are installed inside the Docker container automatically.

🧼 Clean Up

To stop the container:
```
docker-compose down
```
To delete downloaded files (optional):
```
rm -rf downloads/
```
💡 Notes

Invalid or broken URLs are handled gracefully with error messages.
Make sure Docker and Docker Compose are installed on your system.
