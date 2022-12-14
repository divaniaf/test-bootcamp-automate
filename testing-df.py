import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_sign_up(self):
        browser = self.browser  # buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar")  # buka situs
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[3]/div/div[2]/button").click()  # click sign up
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, "input#name_register").send_keys("Admin Tester")  # isi nama
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, "input#email_register").send_keys("admin.test@mailinator.com")  # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, "input#password_register").send_keys("123456")  # isi password
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "signup_register").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID, "swal2-title").text
        response_message = browser.find_element(By.ID, "swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'created user!')

    def test_a_success_login(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar")  # buka situs
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("admin.test@mailinator.com")  # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, "input#password").send_keys("123456")  # isi password
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "signin_login").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID, "swal2-title").text
        response_message = browser.find_element(By.ID, "swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_a_failed_login_with_wrong_password(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar")  # buka situs
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys(
            "admin.test@mailinator.com")  # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, "input#password").send_keys(
            "100000")  # isi password
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "signin_login").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID, "swal2-title").text
        response_message = browser.find_element(By.ID, "swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_a_failed_login_with_unregistered_email_and_password(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar")  # buka situs
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("alif@mailinator.com")  # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, "input#password").send_keys(
            "123456")  # isi password
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "signin_login").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID, "swal2-title").text
        response_message = browser.find_element(By.ID, "swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')
    
    def test_a_resign_up(self):
        browser = self.browser  # buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar")  # buka situs
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[3]/div/div[2]/button").click()  # click sign up
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, "input#name_register").send_keys("Admin Tester")  # isi nama
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, "input#email_register").send_keys("admin.test@mailinator.com")  # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, "input#password_register").send_keys("123456")  # isi password
        time.sleep(1)
        # klik tombol sign in
        browser.find_element(By.ID, "signup_register").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID, "swal2-title").text
        response_message = browser.find_element(By.ID, "swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
