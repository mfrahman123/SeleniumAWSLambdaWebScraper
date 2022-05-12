from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending"

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')

  driver =   webdriver.Chrome(options=chrome_options)
  return driver

def get_videos(driver):
  driver.get(YOUTUBE_TRENDING_URL)
  VIDEO_TAG = 'ytd-video-renderer'
  videos = driver.find_elements(by=By.TAG_NAME, value=VIDEO_TAG)
  return videos


#Title, URL, Thumbnail_url, Channel, views, uploaded
def get_data(video):
  title_tag = video.find_element(By.ID, 'video-title')
  title = title_tag.text
  url = title_tag.get_attribute('href')
  thumbnail = video.find_element(By.ID, 'img').get_attribute('src')
  channel = video.find_element(By.CLASS_NAME, 'ytd-channel-name').find_element(By.TAG_NAME, 'a').text
  
  
    
    
    

  return {
    'title' : title,
    'url' : url,
    'thumbnail' : thumbnail,
    'channel' : channel,
    # 'views' : views,
    # 'upload' : upload
  }
  
  
    
  
  


if __name__ == "__main__":
  print("Getting Driver")
  driver = get_driver()

  print("Fetching vids")
  videos = get_videos(driver)

  #Video 1
  views_and_upload_tag_vid_1 = videos[0].find_elements(By.CSS_SELECTOR, "div#metadata-line span.style-scope.ytd-video-meta-block")
  views_vid_1 = views_and_upload_tag_vid_1[0].text
  upload_vid_1 = views_and_upload_tag_vid_1[1].text

  print(views_vid_1, upload_vid_1)

  #Video 2
  views_and_upload_tag_vid_2 = videos[1].find_elements(By.CSS_SELECTOR, "div#metadata-line span.style-scope.ytd-video-meta-block")
  views_vid_2 = views_and_upload_tag_vid_2[0].text
  upload_vid_2 = views_and_upload_tag_vid_2[1].text

  print(views_vid_2,upload_vid_2)

  #Video 3
  views_and_upload_tag_vid_3 = videos[2].find_elements(By.CSS_SELECTOR, "div#metadata-line span.style-scope.ytd-video-meta-block")
  views_vid_3 = views_and_upload_tag_vid_3[0].text
  upload_vid_3 = views_and_upload_tag_vid_3[1].text

  print(views_vid_3,upload_vid_3)

  video_data = [get_data(vid) for vid in videos[:3]]

  # video_data[0]['views'] = views_vid_1
  # video_data[0]['upload'] = upload_vid_1
  # video_data[1]['views'] = views_vid_2
  # video_data[1]['upload'] = upload_vid_2
  # video_data[2]['views'] = views_vid_3
  # video_data[2]['upload'] = upload_vid_3
  

  count = 0 
  for x in range(len(video_data)):
    count += 1
    if count == 1:
      video_data[x]['views'] = views_vid_1
      video_data[x]['upload'] = upload_vid_1
    elif count == 2:
      video_data[x]['views'] = views_vid_2
      video_data[x]['upload'] = upload_vid_2
    elif count == 3:
      video_data[x]['views'] = views_vid_3
      video_data[x]['upload'] = upload_vid_3
    else:
      break

  print(video_data)
      
    

  
  


  
 