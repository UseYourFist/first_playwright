import re
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_todo(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_label("Toggle Todo").check()
    # page.locator('').click()
def test_checkbox(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").click()
    page.locator("text=Checked checkbox").click()
    page.locator("text=Default radio").click()
    page.locator("text=Default checked radio").click()
    page.locator("text=Checked switch checkbox input").click()


def test_select(page):
    page.goto("https://zimaev.github.io/select/")
    page.select_option('#floatingSelect', value="3")
    page.select_option('#floatingSelect', index=1)
    page.select_option('#floatingSelect', label="Нашел и завел bug")

@pytest.mark.smoke
def test_multi(page):
    page.goto("https://zimaev.github.io/select/")
    page.select_option('#skills', ["playwright", "python"])