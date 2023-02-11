from .pages.main_page import MainPage
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# def basket_should_be_present(browser):
#     try:
#         browser.find_element(By.CSS_SELECTOR,"button.btn-add-to-basket")
#         return True
#     except NoSuchElementException:
#         return False
#
# def test_basket_shuld_be_visible(browser):
#     browser.get(link)
#     time.sleep(5)
#     assert basket_should_be_present(browser), "Basket element shuld be present."
#
# def go_to_login_page(browser):
#     login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()