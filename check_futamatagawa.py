import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

options = uc.ChromeOptions()
options.add_argument("--headless")  # 非表示モード
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Renderの環境では、バイナリ（実行ファイル）の場所を指定する必要があります
options.binary_location = "/usr/bin/chromium"  # Render環境のデフォルトパス

# ドライバ起動
driver = uc.Chrome(options=options)

# アクセスするページ
url = "https://dshinsei.e-kanagawa.lg.jp/140007-u/offer/offerList_movePage?pageNo=3"
driver.get(url)

# 「予約可能な枠」が存在するか確認
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'offerList_detailTop')]"))
    )
    print("✅ 空きありの予約リンクを検出しました")
except:
    print("⚠ 空きなし（クリック可能な予約リンクなし）")

# ページHTMLを保存
html = driver.page_source
with open("output.html", "w", encoding="utf-8") as f:
    f.write(html)

driver.quit()
print("✅ HTMLを保存しました（output.html）")
