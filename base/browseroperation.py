class BrowserOperation:
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    def open_url(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e, '地址错误')

    def send_keys(self, xpath, content):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(content)
        except Exception as e:
            print(e, '未定位到元素')

    def click_element(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print(e, '未定位到元素')

    def get_text(self, xpath):
        try:
            return self.driver.find_element_by_xpath(xpath).text
        except Exception as e:
            print(e, '未找到文本')

    def get_alert_text(self):
        try:
            return self.driver.switch_to.alert.text
        except Exception as e:
            print(e, '没有Alert信息')

    def alert_clicked(self):
        try:
            return self.driver.switch_to.alert.accept()
        except Exception as e:
            print(e, '没有Alert信息')

    def change_frame(self, frame_name):
        if '/' not in frame_name:
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame(frame_name)
        else:
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame(self.driver.find_element_by_xpath(frame_name))

    def change_readOnly(self,element_id):
        self.driver.execute_script("document.getElementById('{}').readOnly=false".format(element_id))

    def clear_initial_information(self,xpath):
        self.driver.find_element_by_xpath(xpath).clear()