import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_todo(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_label("Toggle Todo").check()
    # page.locator('').click()

# asd