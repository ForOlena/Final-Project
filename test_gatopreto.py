import pytest
from playwright.sync_api import sync_playwright, Page


@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


def test_gatopreto(browser):
    context = browser.new_context()
    page: Page = context.new_page()
    page.goto("https://gatopreto.com/pt/en/")

    # 1. Відкриття головної сторінки сайту
    assert page.url == "https://gatopreto.com/pt/en/"

    # 2. Перевірка наявності логотипу компанії
    logo_locator = page.locator("css=img[src*='logo']")
    assert logo_locator.count() == 1

    # 3. Перевірка наявності меню навігації
    menu_locator = page.locator("css=nav")
    assert menu_locator.count() == 1

    # 4. Перевірка наявності кнопки входу
    login_button_locator = page.locator("text=Entrar")
    assert login_button_locator.count() == 1

    # 5. Натиснення кнопки входу
    login_button_locator.click()

    # 6. Перевірка відкриття форми входу
    login_form_locator = page.locator("css=form[action*='login']")
    assert login_form_locator.count() == 1

    # 7. Введення коректного логіна
    username_locator = page.locator("css=input[name='lfynar@gmail.com']")
    username_locator.fill("lfynar@gmail.com")

    # 8. Введення коректного пароля
    password_locator = page.locator("css=input[name='QQQQQWWWWWeeeee11111']")
    password_locator.fill("QQQQQWWWWWeeeee11111")

    # 9. Натиснення кнопки входу
    login_button_locator.click()

    # 10. Перевірка успішного входу
    assert not page.url != "https://gatopreto.com/pt/en/dashboard"

    # 11. Перевірка наявності профілю користувача
    profile_locator = page.locator("css=img[src*='profile']")
    assert profile_locator.count() == 1

    # 12. Перевірка наявності кнопки виходу
    logout_button_locator = page.locator("text=Sair")
    assert logout_button_locator.count() == 1

    # 13. Натиснення кнопки виходу
    logout_button_locator.click()

    # 14. Перевірка успішного виходу
    assert page.url == "https://gatopreto.com/pt/en/"

    # 15. Перевірка наявності посилання на соціальні мережі
    social_media_locator = page.locator("css=a[href*='facebook']")
    assert social_media_locator.count() == 1

    # 16. Перевірка наявності посилання на контактну інформацію
    contact_locator = page.locator("css=a[href*='contact']")
    assert contact_locator.count() == 1

    # 17. Перевірка наявності посилання на політику конфіденційності
    privacy_locator = page.locator("css=a[href*='privacy']")
    assert privacy_locator.count() == 1

    # 18. Перевірка наявності посилання на умови використання
    terms_locator = page.locator("css=a[href*='terms']")
    assert terms_locator.count() == 1

    # 19. Перевірка наявності кнопки пошуку
    search_button_locator = page.locator("css=button[type='submit']")
    assert search_button_locator.count() == 1

    # 20. Перевірка результатів пошуку
    search_input_locator = page.locator("css=input[name='search']")
    search_input_locator.fill("test search")
    search_button_locator.click()
    assert page.url == "https://gatopreto.com/pt/en/search?q=test+search"

    context.close()
