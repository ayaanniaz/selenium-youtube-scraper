# Selenium YouTube Scraper

This project is a Python-based web scraper that uses Selenium WebDriver to fetch trending YouTube videos. It extracts key details such as video titles, URLs, thumbnails, channel names, descriptions, views, and upload times. The data is saved in a CSV file, and the script can optionally email the data as an attachment.

## Features
- Scrapes trending videos from YouTube's Trending page.
- Extracts video information including:
  - Title
  - URL
  - Thumbnail URL
  - Channel Name
  - Description
  - View count
  - Upload time
- Saves the data into a `trending.csv` file.
- Sends the CSV file via email as an attachment.

## Prerequisites
Before you get started, make sure you have the following:
- Python 3.7 or higher
- Google Chrome installed
- ChromeDriver installed (version compatible with your Chrome)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/ayaanniaz/selenium-youtube-scraper.git
   cd selenium-youtube-scraper
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
(Though I did use a virtual environment in this project, using one is strongly recommended to safely store credentials and maintain isolated dependencies.)

3. Configure email settings:
   - Create a `.env` file in the project directory with your email credentials:
     ```plaintext
     SENDER_EMAIL=your_email@gmail.com
     RECEIVER_EMAIL=receiver_email@gmail.com
     EMAIL_PASSWORD=your_app_specific_password
     ```
   - Replace the placeholders with your actual email information. If you're using Gmail, make sure to enable "App Passwords" in your account settings.

4. Ensure that ChromeDriver is compatible with your Chrome browser version.

## How to Use

1. Run the scraper:
   ```bash
   python main.py
   ```

   The script will:
   - Fetch trending videos from YouTube.
   - Extract video details such as titles, URLs, and other metadata.
   - Save the information in a `trending.csv` file.

2. Email the results:
   - The script will automatically send the `trending.csv` file as an attachment to the configured email address.

## Project Structure
```
selenium-youtube-scraper/
├── main.py          # Main script for scraping and email functionality
├── requirements.txt # Python dependencies
├── .env             # Environment variables (excluded from version control)
└── README.md        # Project documentation
```

## Dependencies
This project relies on the following Python libraries:
- `selenium`
- `pandas`
- `smtplib`
- `email`
- `python-dotenv`

To install all dependencies, use:
```bash
pip install -r requirements.txt
```

## Deploying on a DigitalOcean Virtual Machine
This project was successfully deployed on a DigitalOcean Virtual Machine using PowerShell and a virtual environment. Below are the steps:

### 1. Create a Droplet
Log in to your DigitalOcean account and create a droplet with your preferred Linux distribution (e.g., Ubuntu).

### 2. Update the System
Once logged into the droplet via SSH, run the following commands to update and upgrade the system:
```bash
sudo apt update
sudo apt upgrade
```

### 3. Install Python and Pip
Install Python and Pip if they are not already installed:
```bash
sudo apt install python3
sudo apt install python3-pip
```

### 4. Set Up the Project
Navigate to the home directory and clone the repository:
```bash
cd /home
sudo apt install git
git clone https://github.com/ayaanniaz/selenium-youtube-scraper.git
cd selenium-youtube-scraper
```

### 5. Create a Virtual Environment
Create and activate a virtual environment to isolate the project dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 6. Install Dependencies
Install the required dependencies within the virtual environment:
```bash
pip install -r requirements.txt
```

### 7. Run the Script
To run the scraper:
```bash
python main.py
```
The script will generate the `trending.csv` file and send it via email.

### 8. Automate Using Cron (Optional)
To schedule the script to run periodically, use `cron`:
```bash
crontab -e
```
Add a cron job to execute the script daily. Eg:This runs everyday at 8 AM:
```bash
0 8 * * * /home/selenium-youtube-scraper/venv/bin/python /home/selenium-youtube-scraper/main.py
```
You can use this to generate cron schedule expressions: Crontab Guru - https://crontab.guru/


