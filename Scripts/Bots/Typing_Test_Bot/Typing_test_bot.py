from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


class Typing_Test_Typer:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        # Open typingtest.com
        self.chrome = webdriver.Chrome(options=chrome_options)
        self.chrome.get("https://typingtest.com")
        # Click 'Start Typing Test'
        while True:
            try:
                play_button = self.chrome.find_element_by_class_name(
                    "start-btn"
                )
                play_button.click()
                break
            except Exception:
                time.sleep(2)

    def take_test(self):
        # Load textbox element
        while True:
            try:
                text_area = self.chrome.find_element_by_id("test-edit-area")
                break
            except Exception:
                time.sleep(2)
        # Type in the textbox
        while True:
            try:
                # Select highlighted word
                highlighted_word = self.chrome.find_element_by_class_name(
                    "test-text-area-font-highlighted"
                )
                # Enter to start a new paragraph
                if highlighted_word.tag_name == "i":
                    text_area.send_keys(Keys.ENTER)
                    continue
                # Enter highlighted word in text box
                word_text = str(highlighted_word.text)
                text_area.send_keys(word_text)
                text_area.send_keys(Keys.SPACE)
            except Exception:
                break


def main():
    typer = Typing_Test_Typer()
    typer.take_test()


if __name__ == "__main__":
    main()
