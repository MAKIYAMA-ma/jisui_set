from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import os

# 保存先フォルダ
DOWNLOAD_FOLDER = "題名"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Seleniumセットアップ
driver = webdriver.Edge()  # 適切なWebDriverを指定
driver.get("初期URL")  # 開始するURL

# WebDriverWait の設定
wait = WebDriverWait(driver, 300)  # 最大5分待機
pre_img_url = ""

while True:
    try:
        # 画像要素が表示されるのを待つ
        img_element = wait.until(
            EC.presence_of_element_located((By.ID, "img"))
        )

        # 画像のURLを取得
        img_url = img_element.get_attribute("src")
        print(f"Downloading image: {img_url}")

        # 画像をダウンロード
        print(f"Downloading image: {img_url}")
        img_data = requests.get(img_url).content
        img_name = os.path.join(DOWNLOAD_FOLDER, os.path.basename(img_url))
        if img_name == pre_img_url:
            break
        pre_img_url = img_name

        with open(img_name, 'wb') as img_file:
            img_file.write(img_data)

        print(f"Image saved as: {img_name}")

        # 次のページへのリンクをクリック
        next_element = driver.find_element(By.ID, "next")
        next_href = next_element.get_attribute("href")

        # ページ遷移
        print(f"Navigating to: {next_href}")
        driver.get(next_href)

        time.sleep(5)  # 適宜待機

    except Exception as e:
        print(f"An error occurred: {e}")
        break

# ドライバを閉じる
driver.quit()
