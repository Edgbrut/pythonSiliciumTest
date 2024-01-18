import datetime
import time


class Base:
    def __init__(self, driver):
        self.driver = driver

    """Method Get Current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL: " + get_url)

    """Method Assert URL"""
    def get_assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("URL Assertion Confirmed")

    """Method Assert Word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Page Name Assertion: " + value_word)

    """Method Screenshot"""
    def get_screenshot(self):
        time.sleep(3)
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M")
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Lenovo\\PycharmProjects\\pythonSiliciumTest\\screen\\' + name_screenshot)
        print("Screenshot Complete: " + name_screenshot)

    """Method Check If Button Or CheckBox Selected And Assertion"""
    def get_btn_selected(self, btn, name):
        value_btn = btn
        name_btn = value_btn.text
        assert name_btn == name
        print("Button Name Assertion: " + name_btn)

        if value_btn.is_selected():
            pass
            print(name_btn + " Button Is Selected")
        else:
            value_btn.click()
            print("Selected: " + name_btn)
