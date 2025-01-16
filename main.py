from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import json

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_videos(driver):
  driver.get(YOUTUBE_TRENDING_URL)
  VIDEO_DIV_TAG = 'ytd-video-renderer'
  videos =   driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)
  return videos

def parse_video(video):
  title_tag = video.find_element(By.ID,'video-title')
  title = title_tag.text
  url = title_tag.get_attribute('href')

  thumbnail_tag = video.find_element(By.TAG_NAME,'img')
  thumbnail_url = thumbnail_tag.get_attribute('src')

  channel_div = video.find_element(By.CLASS_NAME,'ytd-channel-name')
  channel_name = channel_div.text

  description = video.find_element(By.ID,'description-text').text
  metadata = video.find_element(By.ID, 'metadata-line')
  spans = metadata.find_elements(By.TAG_NAME, 'span')
  views = spans[0].text if len(spans) > 0 else "N/A"
  upload_time = spans[1].text if len(spans) > 1 else "N/A"

  return{
    'title':title,
    'url':url,
 'thumbnail_url':thumbnail_url,
    'channel':channel_name,
    'description':description,
    'views': views,
    'upload_time': upload_time
  }

def send_email():
  sender_email = "sendtrend395@gmail.com"
  receiver_email = "sendtrend395@gmail.com"
  subject = "Youtube Trending Videos"
  password = "YOUR GMAIL PASSWORD"
  body = 'Please find the attached file'

  # Create the MIMEMultipart object and set up the headers
  msg = MIMEMultipart()
  msg['From'] = sender_email
  msg['To'] = receiver_email
  msg['Subject'] = subject
  msg.attach(MIMEText(body, 'plain'))

  # File to be sent
  filename = "trending.csv"
  try:
      with open(filename, "rb") as attachment:
          # Instance of MIMEBase and named as p
          p = MIMEBase('application', 'octet-stream')

          # To change the payload into encoded form
          p.set_payload(attachment.read())

          # Encode into base64
          encoders.encode_base64(p)

          # Add header to the MIMEBase object
          p.add_header('Content-Disposition', f"attachment; filename= {filename}")

          # Attach the instance 'p' to instance 'msg'
          msg.attach(p)
  except FileNotFoundError:
      print(f"The file {filename} was not found.")
      return

  # Setup the MIME
  try:
      # Create SMTP session for sending the mail
      with smtplib.SMTP('smtp.gmail.com', 587) as server:
          server.starttls()  # Enable security
          server.login(sender_email, password)  # Login with email and password
          server.send_message(msg)  # Send the email

      print("Email sent successfully.")
  except Exception as e:
      print(f"Failed to send email. Error: {e}")

if __name__ == "__main__":
  print('Creating driver')
  driver = get_driver()
  print('Fetching the page') 
  videos = get_videos(driver)
  print(f'Found {len(videos)} videos')
  print('Parsing top 10 videos')
  videos_data = [parse_video(video) for video in videos[:10]]
  print(f'{videos_data}\n')
  
  print('Saving the data to a CSV')
  videos_df = pd.DataFrame(videos_data)
  print(videos_df)
  videos_df.to_csv('trending.csv',index = None)
  
  #body = json.dumps(videos_data,indent=2)
  print('Sending email')
  send_email()
