import csv
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Fungsi membaca CSV
def read_csv(filename):
    with open(filename, newline='', encoding='utf-8') as f:
        return [row for row in csv.reader(f)]

# Baca akun dan judul video
accounts = read_csv("akun.csv")  # Format: [email, password]
titles = [row[0] for row in read_csv("data.csv")]  # Ambil hanya judul

# Hitung pembagian video per akun
num_accounts = len(accounts)
videos_per_account = len(titles) // num_accounts
extra_videos = len(titles) % num_accounts
random.shuffle(titles)  # Acak judul untuk distribusi lebih merata

# Distribusikan video ke akun
video_distribution = {tuple(account): [] for account in accounts}
index = 0
for account in accounts:
    video_distribution[tuple(account)] = titles[index:index + videos_per_account]
    index += videos_per_account

# Tambahkan sisa video ke akun secara acak
for i in range(extra_videos):
    random.choice(list(video_distribution.values())).append(titles[index + i])

# Proses upload
for (email, password), videos in video_distribution.items():
    # Inisialisasi WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://old.bitchute.com/channel/")
    time.sleep(3)

    # Login
    driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(email)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(password)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button[type='button']").click()
    time.sleep(5)
    
    for title in videos:
        modif_kata = title.replace(' ', '_')
        kw = f'{title} Onlyfans Leaked - Update Files ++ Download'

        konten = f'''
        17 minutes ago - Access {title} Onlyfans Leaked content & files Update.

        LINK ⏩⏩ https://clipsmu.com/{modif_kata}

        2025 Updated! Today, you'll be able to download and preview all content from {title} in just a few clicks.
        '''
        
        driver.get("https://old.bitchute.com/channel/")
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".svg-inline--fa.fa-upload.fa-2x").click()
        time.sleep(5)
        driver.find_element(By.NAME, "videoInput").send_keys("video/video.mp4")
        driver.find_element(By.CSS_SELECTOR, "input[type='title']").send_keys(kw)
        time.sleep(20)
        driver.find_element(By.ID, "thumbnailButton").click()
        time.sleep(15)
        driver.find_element(By.ID, "description").send_keys(konten)
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(50)

    driver.quit()  # Tutup browser setelah semua video terupload untuk akun ini
