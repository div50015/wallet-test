import time
from selene import browser, have
import os
from selene import command

def test_complete_todo():
    browser.open('/')
    # уменьшение размера изображения в 0.8 раза
    # browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.8)"')
    # ожидание в течение 10 секунд 3х реклпмных банеров и их удаление (вторая строка)
    # browser.all('[id^google_ads][id$=container__]').with_(timeout=10).wait_until(have.size_less_than_or_equal(3))
    # browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    browser.all('.v-btn.v-btn--router.v-btn--text.v-btn--tile.theme--light.v-size--default')[3].click()
    time.sleep(10)