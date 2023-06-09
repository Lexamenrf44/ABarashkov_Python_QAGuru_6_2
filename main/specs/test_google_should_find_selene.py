from selene import browser
from selene import be, have
from main.pages.app.common import App


def test_search_with_results():
    browser.element(App.search_field).should(be.blank)
    browser.element(App.search_field).type('yashaka/selene')
    browser.element(App.search_button).click()
    browser.element(App.search_list_found).should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_without_results():
    browser.element(App.search_field).should(be.blank)
    browser.element(App.search_field).type('124wfqw r12r asf')
    browser.element(App.search_button).click()
    browser.element(App.search_list_empty).should(have.text('did not match any documents.'))
