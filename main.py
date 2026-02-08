import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

FOLDER_PATH = "./Solution" 
LOG_FILE = "history_log.txt"
WAIT_TIME = 95 

def load_history():
    if not os.path.exists(LOG_FILE): return []
    with open(LOG_FILE, "r") as f: return f.read().splitlines()

def save_history(filename):
    with open(LOG_FILE, "a") as f: f.write(filename + "\n")

def submit_process(driver, wait, files, language_label, extension_name):
    done_list = load_history()
    print(f"\n>>> [PHASE {extension_name}] Tìm thấy {len(files)} bài. Đã làm: {len([f for f in files if f in done_list])}")

    for filename in files:
        if filename in done_list: continue

        problem_code = os.path.splitext(filename)[0] 
        
        try:
            file_path = os.path.join(FOLDER_PATH, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                source_code = f.read()
        except Exception as e:
            print(f"⚠️ Lỗi đọc file {filename}: {e}")
            continue

        print(f"\n--- Đang nộp bài: {problem_code} ({extension_name}) ---")

        try:
            driver.get("https://codefun.vn/submit")

            if "login" in driver.current_url:
                print("⚠️ Bị đá về Login. Dừng tool.")
                return False

            code_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Pxxxxx']")))
            code_input.clear()
            code_input.send_keys(problem_code)

            try:
                select_element = driver.find_element(By.TAG_NAME, "select")
                Select(select_element).select_by_visible_text(language_label)
            except:
                time.sleep(1)
                select_element = driver.find_element(By.TAG_NAME, "select")
                Select(select_element).select_by_visible_text(language_label)

            wait.until(EC.presence_of_element_located((By.ID, "brace-editor")))
            time.sleep(1)
            
            js_code = source_code.replace("\\", "\\\\").replace("'", "\\'").replace('"', '\\"').replace("\n", "\\n").replace("\r", "")
            driver.execute_script(f"ace.edit('brace-editor').setValue('{js_code}');")

            submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
            time.sleep(0.5)
            submit_btn.click()
            
            print(f"✅ Đã bấm nộp {filename}")
            save_history(filename)

            print(f"💤 Nghỉ {WAIT_TIME} giây...")
            for i in range(WAIT_TIME, 0, -1):
                if i % 10 == 0: print(f"{i}...", end=" ", flush=True)
                time.sleep(1)
            print("Tiếp tục!")

        except Exception as e:
            print(f"❌ Lỗi ở bài {filename}: {e}")
            time.sleep(5)
    
    return True

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    print(">>> Đang mở Codefun...")
    driver.get("https://codefun.vn/login")

    print("\n" + "="*60)
    print("🔴 TRẠNG THÁI: CHỜ ĐĂNG NHẬP THỦ CÔNG...")
    print("👉 Tool sẽ tự chạy khi thấy nút 'Logout'.")
    print("="*60 + "\n")

    try:
        WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Logout')]"))
        )
        print("✅ Đã đăng nhập thành công!")
        time.sleep(2) 
    except TimeoutException:
        print("❌ Hết giờ. Chạy lại tool nhé.")
        driver.quit()
        return

    all_files = os.listdir(FOLDER_PATH)
    
    cpp_files = [f for f in all_files if f.endswith(".cpp")]
    py_files = [f for f in all_files if f.endswith(".py")]

    print("\n" + "="*40)
    print(f"🐍 BẮT ĐẦU PHASE 2: Nộp {len(py_files)} bài Python")
    print("="*40)
    submit_process(driver, wait, py_files, "Python 3", ".PY")

    print("\n>>> HOÀN THÀNH TOÀN BỘ CÔNG VIỆC!")
    driver.quit()

if __name__ == "__main__":
    main()