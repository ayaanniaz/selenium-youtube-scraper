YOUTUBE_TRENDING_URL_URL = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'
response = requests.get(YOUTUBE_TRENDING_URL)
print('status code',response.status_code)

with open('trending.html','w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text,'html.parser')

print('Page title:',doc.title.text)

video_divs = doc.find_all('div',class_='ytd-video-renderer')
print(f'Found {len(video_divs)} videos')