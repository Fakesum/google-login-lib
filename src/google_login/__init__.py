__version__ = "0.0.1a"

from seleniumbase import SB, BaseCase
from contextlib import contextmanager
import time

@contextmanager
def use_driver_with_login(username, password):
    with SB(uc=True) as driver:
        driver:BaseCase = driver
        driver.get("https://accounts.google.com/signin")
        driver.type('input[type="email"]', username)

        driver.click('[jsname="LgbsSe"]')

        driver.type('input[type="password"]', password)
        driver.click('[jsname="LgbsSe"]')

        while driver.get_current_url() != "https://myaccount.google.com/?utm_source=sign_in_no_continue":
            time.sleep(0.1)

        yield driver.driver