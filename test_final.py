#1Відкриття головної сторінки сайту
def test_open_main_page(page):
    # Умови: Немає
    # Дії для відтворення:
    # 1. Відкрити браузер
    # 2. Перейти до https://gatopreto.com/pt/en/

    page.goto("https://gatopreto.com/pt/en/")

    # Очікуваний результат: Головна сторінка відкривається успішно
    assert page.title() == "Gato Preto"

#2перевірка наявності лого
def test_check_company_logo(page):
    # Умови: Головна сторінка відкрита
    # Дії для відтворення:
    # 1. Перейти до головної сторінки
    # 2. Перевірити наявність логотипу компанії

    page.goto("https://gatopreto.com/pt/en/")
    company_logo = page.query_selector("#company-logo")
    assert company_logo is not None


#3Перевірка наявності меню навігації
def test_check_navigation_menu(page):
    # Умови: Головна сторінка відкрита
    # Дії для відтворення:
    # 1. Перейти до головної сторінки
    # 2. Перевірити наявність меню навігації

    page.goto("https://gatopreto.com/pt/en/")
    navigation_menu = page.query_selector("#navigation-menu")
    assert navigation_menu is not None

#4Перевірка наявності кнопки входу
def test_check_login_button(page):
    # Умови: Головна сторінка відкрита
    # Дії для відтворення:
    # 1. Перейти до головної сторінки
    # 2. Перевірити наявність кнопки входу

    page.goto("https://gatopreto.com/pt/en/")
    login_button = page.query_selector("#login-button")
    assert login_button is not None

#5Натиснення кнопки входу
def test_click_login_button(page):
    # Умови: Головна сторінка відкрита
    # Дії для відтворення:
    # 1. Натиснути кнопку входу

    page.goto("https://gatopreto.com/pt/en/")
    login_button = page.query_selector("#login-button")
    login_button.click()

    # Очікуваний результат: Форма входу відкривається
    assert page.query_selector("#login-form") is not None

#6Перевірка відкриття форми входу
def test_check_login_form(page):
    # Умови: Кнопка входу натиснута
    # Дії для відтворення:
    # 1. Перевірити відкриття форми входу

    page.goto("https://gatopreto.com/pt/en/")
    login_button = page.query_selector("#login-button")
    login_button.click()
    login_form = page.query_selector("#login-form")
    assert login_form is not None

#7Введення коректного логіна
def test_enter_correct_username(page):
    # Умови: Форма входу відкрита
    # Дії для відтворення:
    # 1. Ввести коректний логін

    page.goto("https://gatopreto.com/pt/en/")
    login_button = page.query_selector("#login-button")
    login_button.click()
    username_input = page.query_selector("#username-input")
    username_input.fill("correct_username")
    assert username_input.input_value() == "correct_username"

#8Введення коректного пароля
def test_enter_correct_password(page):
    # Умови: Форма входу відкрита
    # Дії для відтворення:
    # 1. Ввести коректний пароль

    page.goto("https://gatopreto.com/pt/en/")
    login_button = page.query_selector("#login-button")
    login_button.click()
    password_input = page.query_selector("#password-input")
    password_input.fill("correct_password")
    assert password_input.input_value() == "correct_password"

#9Натиснення кнопки входу
def test_click_login_button(page):
    # Умови: Форма входу відкрита
    # Дії для відтворення:
    # 1. Натиснути кнопку входу

    page.goto("https://gatopreto.com/pt/en/")
    login_button = page.query_selector("#login-button")
    login_button.click()
    username_input = page.query_selector("#username-input")
    username_input.fill("correct_username")
    password_input = page.query_selector("#password-input")
    password_input.fill("correct_password")
    login_button.click()

    # Очікуваний результат: Вхід успішний
    assert page.query_selector("#user-profile") is not None

#10Перевірка успішного входу
def test_check_successful_login(page):
    # Умови: Кнопка входу натиснута
    # Дії для відтворення:
    # 1. Перевірити успішний вхід

    page.goto("https://gatopreto.com/pt/en/")
    login_button = page.query_selector("#login-button")
    login_button.click()
    username_input = page.query_selector("#username-input")
    username_input.fill("correct_username")
    password_input = page.query_selector("#password-input")
    password_input.fill("correct_password")
    login_button.click()
    user_profile = page.query_selector("#user-profile")
    assert user_profile is not None

#11Перевірка наявності профілю користувача
def test_check_user_profile(page):
        # Умови: Вхід успішний

#12: Перевірка наявності кнопки виходу
def test_check_logout_button(page):
        # Умови: Вхід успішний
        # Дії для відтворення:
        # 1. Перевірити наявність кнопки виходу

    page.goto("https://gatopreto.com/pt/en/")
    login_button = page.query_selector("#login-button")
    login_button.click()
    username_input = page.query_selector("#username-input")
    username_input.fill("correct_username")
    password_input = page.query_selector("#password-input")
    password_input.fill("correct_password")
    login_button.click()
    logout_button = page.query_selector("#logout-button")
    assert logout_button is not None

#13: Натиснення кнопки виходу
def test_click_logout_button(page):
    # Умови: Вхід успішний
    # Дії для відтворення:
    # 1. Натиснути кнопку виходу

    page.goto("https://gatopreto.com/pt/en/")
    login_button = page.query_selector("#login-button")
    login_button.click()
    username_input = page.query_selector("#username-input")
    username_input.fill("correct_username")
    password_input = page.query_selector("#password-input")
    password_input.fill("correct_password")
    login_button.click()
    logout_button = page.query_selector("#logout-button")
    logout_button.click()

    # Очікуваний результат: Вихід успішний
    assert page.query_selector("#login-button") is not None

#14: Перевірка успішного виходу
def test_check_successful_logout(page):
    # Умови: Кнопка виходу натиснута
    # Дії для відтворення:
    # 1. Перевірити успішний вихід

    page.goto("https://gatopreto.com/pt/en/")
    login_button = page.query_selector("#login-button")
    login_button.click()
    username_input = page.query_selector("#username-input")
    username_input.fill("correct_username")
    password_input = page.query_selector("#password-input")
    password_input.fill("correct_password")
    login_button.click()
    logout_button = page.query_selector("#logout-button")
    logout_button.click()
    login_button = page.query_selector("#login-button")
    assert login_button is not None

#15: Перевірка наявності посилання на соціальні мережі
def test_check_social_media_links(page):
    # Умови: Головна сторінка відкрита
    # Дії для відтворення:
    # 1. Перевірити наявність посилання на соціальні мережі

    page.goto("https://gatopreto.com/pt/en/")
    social_media_links = page.query_selector_all(".social-media-link")
    assert len(social_media_links) > 0

#16: Перевірка наявності посилання на контактну інформацію
def test_check_contact_info_links(page):
    # Умови: Головна сторінка відкрита
    # Дії для відтворення:
    # 1. Перевірити наявність посилання на контактну інформацію

    page.goto("https://gatopreto.com/pt/en/")
    contact_info_links = page.query_selector_all(".contact-info-link")
    assert len(contact_info_links) > 0

#17: Перевірка наявності посилання на політику конфіденційності
def test_check_privacy_policy_links(page):
    # Умови: Головна сторінка відкрита
    # Дії для відтворення:
    # 1. Перевірити наявність посилання на політику конфіденційності

    page.goto("https://gatopreto.com/pt/en/")
    privacy_policy_links = page.query_selector_all(".privacy-policy-link")
    assert len(privacy_policy_links) > 0

#18: Перевірка наявності посилання на умови використання
def test_check_terms_of_use_links(page):
    # Умови: Головна сторінка відкрита
    # Дії для відтворення:
    # 1. Перевірити наявність посилання на умови використання

    page.goto("https://gatopreto.com/pt/en/")
    terms_of_use_links = page.query_selector_all(".terms-of-use-link")
    assert len(terms_of_use_links) > 0

#19: Перевірка наявності кнопки пошуку
def test_check_search_button(page):
    # Умови: Головна сторінка відкрита
    # Дії для відтворення:
    # 1. Перевірити наявність кнопки пошуку

    page.goto("https://gatopreto.com/pt/en/")
    search_button = page.query_selector("#search-button")
    assert search_button is not None

#20: Перевірка результатів пошуку по запиту- sofa
def test_check_search_results(page):
    # Умови: Кнопка пошуку натиснута
    # Дії для відтворення:
    # 1. Ввести запит "sofa" у поле пошуку
    # 2. Натиснути кнопку пошуку
    # 3. Перевірити результати пошуку

    page.goto("https://gatopreto.com/pt/en/")
    search_input = page.query_selector("#search-input")
    search_input.fill("sofa")
    search_button = page.query_selector("#search-button")
    search_button.click()
    search_results = page.query_selector_all(".search-result")
    assert search_results
#21: Перевірка поведінки при введенні невірного логіна або пароля
def test_incorrect_login_or_password(page):
    # Умови: Форма входу відкрита
    # Дії для відтворення:
    # 1. Ввести невірний логін або пароль
    # 2. Натиснути кнопку входу

    page.goto("https://gatopreto.com/pt/en/")
    login_button = page.query_selector("#login-button")
    login_button.click()
    username_input = page.query_selector("#username-input")
    username_input.fill("incorrect_username")
    password_input = page.query_selector("#password-input")
    password_input.fill("incorrect_password")
    login_button.click()

    # Очікуваний результат: Повідомлення про помилку входу
    error_message = page.query_selector("#error-message")
    assert error_message is not None
#22: Перевірка поведінки при відсутності введення логіна або пароля

    def test_empty_login_or_password(page):
    # Умови: Форма входу відкрита
    # Дії для відтворення:
    # 1. Не вводити логін або пароль
    # 2. Натиснути кнопку входу

    page.goto("https://gatopreto.com/pt/en/")
    login_button = page.query_selector("#login-button")
    login_button.click()
    login_button.click()

    # Очікуваний результат: Повідомлення про помилку входу
    error_message = page.query_selector("#error-message")
    assert error_message is not None