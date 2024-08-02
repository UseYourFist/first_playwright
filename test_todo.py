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


def test_multi(page):
    page.goto("https://zimaev.github.io/select/")
    page.select_option('#skills', ["playwright", "python"])


def test_drag_and_drop(page):
    page.goto('https://zimaev.github.io/draganddrop/')
    page.drag_and_drop('#drag', '#drop')


def test_dialog(page):
    page.goto('https://zimaev.github.io/dialog/')
    page.on('dialog', lambda dialog: dialog.accept())
    page.get_by_text('Диалог Confirmation').click()


def test_select_file(page):
    page.goto('https://zimaev.github.io/upload/')
    page.set_input_files('#formFile', 'hello.txt')
    page.locator("#file-submit").click()


def test_table(page):
    page.goto('https://zimaev.github.io/table/')
    row = page.locator("tr")
    print(row.all_text_contents())


def test_new_tab(page):
    page.goto("https://zimaev.github.io/tabs/")
    with page.context.expect_page() as tab:
        page.get_by_text("Переход к Dashboard").click()

    new_tab = tab.value
    assert new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?"
    sign_out = new_tab.locator('.nav-link', has_text='Sign out')
    assert sign_out.is_visible()


# FIELD_LOCATOR = '.new-todo'
#
# @pytest.mark.fail
# def test_two_task(page):
#     page.goto('https://demo.playwright.dev/todomvc/#/')
#     page.locator(FIELD_LOCATOR).fill('сварить пельмени')
#     page.locator(FIELD_LOCATOR).press('Enter')
#     page.locator(FIELD_LOCATOR).fill('бахнуть пельмени')
#     page.locator(FIELD_LOCATOR).press('Enter')
#     page.pause()
#     expect(page.locator('[data-testid="todo-title"]')).to_have_count(3)


@pytest.mark.smoke
class TestForThree:
    FIELD_LOCATOR = '.new-todo'

    def test_check_url(self, page):
        page.goto('https://demo.playwright.dev/todomvc/#/')
        expect(page, 'Другой урл').to_have_url('https://demo.playwright.dev/todomvc/#/')

    def test_empty(self, page):
        page.goto('https://demo.playwright.dev/todomvc/#/')
        expect(page.locator(self.FIELD_LOCATOR)).to_be_empty()

    @pytest.mark.fail
    def test_two_task(self, page):
        page.goto('https://demo.playwright.dev/todomvc/#/')
        page.locator(self.FIELD_LOCATOR).fill('сварить пельмени')
        page.locator(self.FIELD_LOCATOR).press('Enter')
        page.locator(self.FIELD_LOCATOR).fill('бахнуть пельмени')
        page.locator(self.FIELD_LOCATOR).press('Enter')
        expect(page.locator('[data-testid="todo-title"]')).to_have_count(3)

    def test_one_done_task(self, page):
        page.goto('https://demo.playwright.dev/todomvc/#/')
        page.locator(self.FIELD_LOCATOR).fill('сварить пельмени')
        page.locator(self.FIELD_LOCATOR).press('Enter')
        page.locator('[type="checkbox"]').nth(0).click()
        expect(page.get_by_test_id('todo-item').nth(0)).to_have_class('completed')
