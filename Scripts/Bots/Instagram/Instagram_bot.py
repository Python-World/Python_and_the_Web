from selenium import webdriver
import pathlib
from time import sleep
from cryptography.fernet import Fernet
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InstaBot:
    def __init__(self, username, pw):
        path = pathlib.Path().absolute()
        try:
            self.driver = webdriver.Chrome(
                r"{}\{}".format(path, "chromedriver.exe")
            )
        except:
            try:
                self.driver = webdriver.Firefox(
                    r"{}\{}".format(path, "geckodriver.exe")
                )
            except:
                try:
                    self.driver = webdriver.Opera(
                        r"{}\{}".format(path, "operadriver.exe")
                    )
                except:
                    print("Webdriver not found")

        print(
            "\n----Please wait for the menu, as we are signing in through your id----"
        )
        self.driver.get("https://instagram.com")
        self.wait = WebDriverWait(self.driver, 10).until

        self.wait(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@name='username']")
            )
        ).send_keys(username)
        self.driver.find_element_by_xpath(
            "//input[@name='password']"
        ).send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        try:
            self.driver.find_element_by_xpath(
                "//input[@aria-label='Security Code']"
            )
            print("\nEnter the otp and login to continue\n")
            for _ in range(2):
                WebDriverWait(self.driver, 50).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[contains(., 'Not Now')]")
                    )
                ).click()
            self.driver.minimize_window()
        except:
            for _ in range(2):
                self.wait(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[contains(., 'Not Now')]")
                    )
                ).click()
            self.driver.minimize_window()

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//img[@alt='Instagram']").click()
        self.driver.maximize_window()
        self.wait(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, " div:nth-child(5) > span > img")
            )
        ).click()
        self.driver.find_element_by_xpath("//div[text()='Profile']").click()
        self.wait(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@href,'/following')]")
            )
        ).click()
        following = self._get_names()
        self.wait(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@href,'/followers')]")
            )
        ).click()
        followers = self._get_names()
        not_following_back = [
            user for user in following if user not in followers
        ]
        you_not_following_back = [
            user for user in followers if user not in following
        ]
        self.driver.find_element_by_xpath("//img[@alt='Instagram']").click()

        with open("Not Following Back", "w") as f1:
            f1.write("\n".join(not_following_back))

        with open("You not Following Back", "w") as f2:
            f2.write("\n".join(you_not_following_back))
        self.driver.minimize_window()

        print(
            "People who aren't following back ({}) :\n".format(
                len(not_following_back)
            )
        )
        print("\n".join(not_following_back))
        print("\n\nDo you want to UNFOLLOW them all??")
        ans1 = input("Y/N : ")
        if ans1 in ("Y", "y"):
            InstaBot.unfollow(self, not_following_back)
        elif ans1 in ("N", "n"):
            pass

        print(
            "\n\n\n\nPeople whom you don't follow back ({}) :\n".format(
                len(you_not_following_back)
            )
        )
        print("\n".join(you_not_following_back))
        print("\n\nDo you want to FOLLOW BACK them all??")
        ans2 = input("Y/N : ")
        if ans2 in ("Y", "y"):
            InstaBot.follow_back(self, you_not_following_back)
        elif ans2 in ("N", "n"):
            pass

    def _get_names(self):
        scroll_box = self.wait(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[4]/div/div/div[2]")
            )
        )
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script(
                """
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """,
                scroll_box,
            )
        links = scroll_box.find_elements_by_tag_name("a")
        names = [name.text for name in links if name.text != ""]
        # close button
        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div[1]/div/div[2]/button"
        ).click()
        return names

    def unfollow(self, not_following_back):
        self.driver.find_element_by_xpath("//img[@alt='Instagram']").click()
        self.driver.maximize_window()
        for i in not_following_back:
            self.wait(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[contains(text(),'Search')]")
                )
            ).click()
            self.wait(
                EC.element_to_be_clickable(
                    (By.XPATH, "//input[@placeholder='Search']")
                )
            ).click()
            self.wait(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@href='/{}/']".format(i))
                )
            ).click()
            self.wait(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//span[@class='glyphsSpriteFriend_Follow u-__7']",
                    )
                )
            ).click()
            sleep(1)
            self.wait(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(text(),'Unfollow')]")
                )
            ).click()
            sleep(1)
        self.driver.minimize_window()
        self.driver.find_element_by_xpath("//img[@alt='Instagram']").click()

    def follow_back(self, you_not_following_back):
        self.driver.find_element_by_xpath("//img[@alt='Instagram']").click()
        self.driver.maximize_window()
        for i in you_not_following_back:
            self.wait(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[contains(text(),'Search')]")
                )
            ).click()
            self.driver.find_element_by_xpath(
                "//input[@placeholder='Search']"
            ).send_keys(i)
            self.wait(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@href='/{}/']".format(i))
                )
            ).click()
            self.wait(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(text(),'Follow Back')]")
                )
            ).click()
        self.driver.minimize_window()
        self.driver.find_element_by_xpath("//img[@alt='Instagram']").click()

    def spamming(self):
        recipients = input("Recipients (seperate by < , >)").split(",")
        print(recipients)
        msg = input("Message : ")
        count = int(input("How many messages : "))
        print(
            "\n----Be patient, your request is under process as you can spectate----\n"
        )
        self.driver.find_element_by_xpath("//img[@alt='Instagram']").click()
        self.driver.maximize_window()
        for i in recipients:
            self.wait(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[contains(text(),'Search')]")
                )
            ).click()
            self.driver.find_element_by_xpath(
                "//input[@placeholder='Search']"
            ).send_keys(i)
            self.wait(
                EC.presence_of_element_located(
                    (By.XPATH, "//a[@class='yCE8d  ']")
                )
            ).click()
            self.wait(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(text(),'Message')]")
                )
            ).click()
            self.wait(
                EC.element_to_be_clickable(
                    (By.XPATH, "//textarea[@placeholder='Message...']")
                )
            ).click()
            for _ in range(count):
                self.driver.find_element_by_xpath(
                    "//textarea[@placeholder='Message...']"
                ).send_keys(msg)
                self.wait(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[contains(text(),'Send')]")
                    )
                ).click()
        self.driver.minimize_window()
        self.driver.find_element_by_xpath("//img[@alt='Instagram']").click()

    def log_out(self):
        self.driver.find_element_by_xpath("//img[@alt='Instagram']").click()
        self.wait(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[@class='_2dbep qNELH']")
            )
        ).click()
        log_out = "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div"
        self.wait(EC.element_to_be_clickable((By.XPATH, log_out))).click()
        Users()


class Users:
    def __init__(self):
        self.users = {}
        count = self.check_user()
        if count == 0:
            print("No user found, please add atleast 1 user")
            add_user()

        f = open("Users", "r")
        print("\nSelect user : ")
        for i in range(len(self.users)):
            print("( {} ) {}".format(i + 1, list(self.users.keys())[i]))
        print(
            """\n(a) To Add user      (r) To Remove user      (q) Quit application
        (re) Refresh the list(if the list didn't update)\n"""
        )
        ans = input(":-   ")
        try:
            if ans in ("Q", "q"):
                pass
            else:
                if ans in ("a", "A"):
                    add_user()
                    self.check_user()
                    Users()
                elif ans in ("R", "r"):
                    self.remove_user()
                    Users()
                elif ans in ("re", "RE", "Re"):
                    self.refresh()
                self.bot = InstaBot(
                    list(self.users.keys())[int(ans) - 1],
                    list(self.users.values())[int(ans) - 1],
                )
                f.close()
                self.start_cmd()
        except:
            print(
                "Some error occurred, please enter numeric input to choose among the options."
            )
            Users()

    def check_user(self):
        key = "LO8QifH5rNwyNUhbs8GeDKExO1vToMA6AmdvaR1brgU="
        with open("Users", "r") as f:
            data = f.readlines()
            if len(data) != 0:
                for i in range(0, len(data) - 1, 2):
                    decrypted = Fernet(key).decrypt(
                        (str(data[i + 1])[0:-1].strip()).encode()
                    )
                    self.users[str(data[i])[0:-1].strip()] = str(
                        decrypted.decode()
                    )
            else:
                return 0

    def remove_user(self):
        key = "LO8QifH5rNwyNUhbs8GeDKExO1vToMA6AmdvaR1brgU="
        print("\n\nUser id's stored: ")
        usersl = list(self.users.keys())
        for i in range(len(usersl)):
            print("( {} ) {}".format(i + 1, usersl[i]))
        remove = int(input("User that to be removed: "))
        self.users.pop(list(self.users.keys())[remove - 1])
        with open("Users", "w") as f:
            for i in self.users:
                usr = self.users.get(i)
                encrypted = Fernet(key).encrypt(usr.encode())
                f.write(i + "\n" + encrypted.decode() + "\n")
        self.check_user()

    def start_cmd(self):
        print(
            "\n\nChoose an action \n(1) Follow Back stats [OPTIONAL->Unfollow/Follow back]\n(2) Spam Bot\n(3) Change User\n"
        )
        a = int(input(" :-   ").strip())
        try:
            if a == 1:
                print(
                    "\n----Please wait, this command will take several seconds----\n"
                )
                self.bot.get_unfollowers()
            elif a == 2:
                self.bot.spamming()
            elif a == 3:
                self.bot.log_out()
        except:
            print("Some error occurred\n Please try again")
            input("\n\n")
        self.start_cmd()

    def refresh(self):
        self.check_user()
        Users()


def add_user():
    key = "LO8QifH5rNwyNUhbs8GeDKExO1vToMA6AmdvaR1brgU="
    with open("Users", "a") as f:
        a = int(input("No. of users to be added : "))
        for i in range(a):
            username = input("Enter username {}: ".format(i + 1))
            f.write(username + "\n")
            password = input(
                "Enter password of username( {} ): ".format(username)
            )
            encrypted = Fernet(key).encrypt(password.encode())
            f.write(encrypted.decode() + "\n")
    Users().check_user()


print(
    """
 _____             _                                        ______         _   
|_   _|           | |                                       | ___ \       | |  
  | |  _ __   ___ | |_  __ _   __ _  _ __  __ _  _ __ ___   | |_/ /  ___  | |_ 
  | | | '_ \ / __|| __|/ _` | / _` || '__|/ _` || '_ ` _ \  | ___ \ / _ \ | __|
 _| |_| | | |\__ \| |_| (_| || (_| || |  | (_| || | | | | | | |_/ /| (_) || |_ 
 \___/|_| |_||___/ \__|\__,_| \__, ||_|   \__,_||_| |_| |_| \____/  \___/  \__|
 ==============================__/ |===========================================                                           
                              |___/               By : YASH JOGLEKAR                             
                                                  ``````````````````
"""
)

try:
    f = open("Users", "r")
    f.close()
except:
    f = open("Users", "w")
    f.close()
sleep(1.5)
start = Users()
print("\n------------------THANKS FOR USING MY BOT------------------\n")
sleep(2)
