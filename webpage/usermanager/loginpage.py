from crm_sys.base.browseroperation import BrowserOperation
from crm_sys.base.usebrowser import UseBrowser
from crm_sys.config.log_crm import AutoLogger
from crm_sys.util.yaml_operation import YamlOperation


class LoginPage:
    def __init__(self):
        self.yp = YamlOperation('../../config/locator.yaml')
        self.log = AutoLogger()
        self.ub = UseBrowser()
        self.bo = BrowserOperation(UseBrowser.driver)
        self.bo.open_url('http://172.17.4.234:8080/crm/')

    def login(self, username, password):
        self.log.set_mes('---登录功能开始---', 'info')
        self.bo.send_keys(self.yp.get_locator('LoginPage', 'username'), username)
        self.log.set_mes('---输入用户名---' + username, 'info')
        self.bo.send_keys(self.yp.get_locator('LoginPage', 'password'), password)
        self.log.set_mes('---输入密码---' + password, 'info')
        self.bo.click_element(self.yp.get_locator('LoginPage', 'submit'))
        self.log.set_mes('---点击登录---', 'info')

    def login_correct_text(self,frame_name):
        self.bo.change_frame(frame_name)
        return self.bo.get_text('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div')
