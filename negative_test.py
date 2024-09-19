#21: Перевірка поведінки при введенні невірного логіна або пароля
def test_incorrect_login_or_password (page):
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