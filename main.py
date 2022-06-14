from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from data import username, password
import time
import random


class Bot():
    def __init__(self, username, password):

        self.username = username
        self.password = password
        # абсолютный пусть до драйвера
        self.browser = webdriver.Firefox(executable_path="C:\\Users\\Chihir\\PycharmProjects\\exam_project\\firefoxdriver\\geckodriver.exe")

    # метод закрытия браузера
    def close_browser(self):
        self.browser.close()
        self.browser.quit()

    # метод входа и авторизации
    def login(self):
        try:
            browser = self.browser
            browser.get("https://www.instagram.com/")
            time.sleep(random.randrange(3, 5))

            username_input = browser.find_element(by=By.NAME, value='username')
            username_input.clear()
            username_input.send_keys(username)

            time.sleep(random.randrange(3, 5))

            password_input = browser.find_element(by=By.NAME, value='password')
            password_input.clear()
            password_input.send_keys(password)

            password_input.send_keys(Keys.ENTER)
            time.sleep(7)

            not_remember_password = browser.find_element(By.XPATH, '//button[text()="Не сейчас"]').click()
            time.sleep(random.randrange(3, 5))
            uvedomlenie_o_likes_off = browser.find_element(By.XPATH, '//button[text()="Не сейчас"]').click()
            time.sleep(random.randrange(3, 5))

        except Exception as ex:
            print(ex)

    # метод поиска по хэштегу
    def hashtag_like(self, hashtag):
        try:
            browser = self.browser
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            time.sleep(5)
            #скролим страничку
            for i in range(1, 4):
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randrange(3, 5))


            hrefs = browser.find_elements_by_tag_name('a')# собираем ссылки в список posts_urls
            posts_urls = []
            for i in hrefs:
                href = i.get_attribute('href')

                if "/p/" in href:
                    posts_urls.append(href)

            # цикл по ссылкам постов, постановка лайка, подписка
            for url in posts_urls:
                try:
                    self.browser.get(url)
                    time.sleep(3)
                    like_button = browser.find_element(by=By.CLASS_NAME, value="_aamw")  # кнопка лайка
                    like_button.click()
                    follow_button = browser.find_element(by=By.CLASS_NAME, value="_aar2").click()#кнопка подписаться
                    time.sleep(random.randrange(3, 5))
                    # перейдем на страницу пользователя
                    go_to_profil = browser.find_element(by=By.CLASS_NAME, value="_aaqt").click()
                    time.sleep(random.randrange(5, 7))  # дадим профилю загрузиться - работает!
                    # посмотреть сторис
                    stories_click = browser.find_element(by=By.CLASS_NAME, value="_aa8h").click()
                    time.sleep(random.randrange(8, 10))
                    close_stories = browser.find_element(by=By.CLASS_NAME, value="_ac0g").click()
                    time.sleep(random.randrange(5, 7))

                    for i in range(1):#поскролили  страницу
                        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        time.sleep(random.randrange(3, 5))


                except Exception as ex:
                    print(ex)

        except Exception as ex:
            print(ex)

        # метод отписки, отписываемся от всех кто не подписан на нас
    def delet_user(self):
        browser = self.browser
        browser.get("https://www.instagram.com/chikhirchik/")

        followers_count = browser.find_element(by=By.CLASS_NAME, value="_aacl _aacp _aacu _aacx _aad6 _aade")
        followers_count = followers_count.find_elements_by_tag_name('title')# число подписчиков
        following_count = browser.find_element(by=By.CLASS_NAME, value="_aacl _aacp _aacu _aacx _aad6 _aade")
        following_count = following_count.find_elements_by_tag_name('span')# число подписок
        # две переменные
        followers_loops_count = int(followers_count / 12) + 1
        print(f"Число итераций для сбора подписчиков: {followers_loops_count}")
        following_loops_count = int(following_count / 12) + 1
        print(f"Число итераций для сбора подписок: {following_loops_count}")

        # СОБИРАЕМ СПИСОК ПОДПИСЧИКОВ

        # кликаем чтобы открыть список подписчиков
        followers_button = browser.find_element(by=By.CLASS_NAME, value="_aacl _aacp _aacu _aacx _aad6 _aade")
        following_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")


        followers_ul = browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")# ссылки на подписчиков
        following_ul = browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")# ссылки на мои подписки

        followers_urls = []
        try:
            followers_button.click()
            time.sleep(4)

            print("Запускаем сбор подписчиков...")
            for i in range(1, followers_loops_count + 1):
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);", followers_ul)
                time.sleep(random.randrange(2, 4))

                all_urls_div = followers_ul.find_elements_by_tag_name("li")

                for url in all_urls_div:
                    url = url.find_element_by_tag_name("a").get_attribute("href")
                    followers_urls.append(url)
                    time.sleep(random.randrange(3, 6))
        except Exception as ex:
            print(ex)


        # СОБИРАЕМ СПИСОК ПОДПИСОК
            following_urls = []
            try:
                following_button.click()
                time.sleep(random.randrange(3, 5))
                print("Запускаем сбор подписок")

                for i in range(1, following_loops_count + 1):
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);", following_ul)
                    time.sleep(random.randrange(2, 4))

                    all_urls_div = following_ul.find_elements_by_tag_name("li")

                    for url in all_urls_div:
                        url = url.find_element_by_tag_name("a").get_attribute("href")
                        following_urls.append(url)
            except Exception as ex:
                print(ex)

                # Сравниваем два списка, если пользователь есть в подписках,
                                # но его нет в подписчиках, заносим его в отдельный список.

                count = 0
                unfollow_list = []
                for user in following_urls:
                    if user not in followers_urls:
                        count += 1
                        unfollow_list.append(user)
                time.sleep(2)

                # заходим к каждому пользователю на страницу и отписываемся
                with open(f"{username}_unfollow_list.txt") as unfollow_file:
                    unfollow_users_list = unfollow_file.readlines()
                    unfollow_users_list = [row.strip() for row in unfollow_users_list]

                try:
                    count = len(unfollow_users_list)
                    for user_url in unfollow_users_list:
                        browser.get(user_url)
                        time.sleep(random.randrange(4, 6))

                        # кнопка отписки
                        unfollow_button = browser.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button")
                        unfollow_button.click()

                        time.sleep(random.randrange(4, 6))

                        # подтверждение отписки
                        unfollow_button_confirm = browser.find_element_by_xpath(
                            "/html/body/div[4]/div/div/div/div[3]/button[1]")
                        unfollow_button_confirm.click()

                        # time.sleep(random.randrange(120, 130))
                        time.sleep(random.randrange(4, 6))

                except Exception as ex:
                    print(ex)
                    self.close_browser()

    # def unfollow(self):
    #     browser = self.browser
    #     browser.get("https://www.instagram.com/chikhirchik/")
    #     # откроет список подписчиков
    #     followers = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[3]/a').click()
    #     scroll_box = browser.find_element(by=By.CLASS_NAME, value="_aano")
    #     browser.execute_script("window.scrollTo scroll_box(0, document.body.scrollHeight);")
    #     time.sleep(random.randrange(3, 5))
    #
    #     hrefs = browser.find_elements_by_tag_name('a')  # собираем ссылки в список posts_urls
    #     posts_urls = []
    #     for i in hrefs:
    #         href = i.get_attribute('href')
    #     print(posts_urls)

# Бот работает....
start = Bot(username, password)
start.login()
start.hashtag_like('bmw')
# start.delet_user()
start.close_browser()
