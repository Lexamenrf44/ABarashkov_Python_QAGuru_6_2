from selene import browser
from selene import be, have

def test_search_with_results():
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    browser.quit()

def test_search_without_results():
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('124wfqw r12r asf').press_enter()
    browser.element('#topstuff').should(have.text('არ მოერგო არც ერთ დოკუმენტს'))
    browser.quit()