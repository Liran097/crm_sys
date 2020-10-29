import re
import time

from crm_sys.db.db_operation import DbOperation
from crm_sys.util.excel_operation import OperationExcel
from crm_sys.webpage.usermanager.loginpage import LoginPage


class CustomerPage:
    def __init__(self):
        self.op = OperationExcel('../../config/test_case_customer.xlsx', '用例参数')
        self.do = DbOperation()
        self.lp = LoginPage()
        self.lp.login(self.op.get_cell(1, 2), self.op.get_cell(1, 3))

    def add_customer(self, **kwargs):
        self.input_value = kwargs
        self.do.delete_info('delete from customer_info where customer_name="{}"'.format(self.input_value.get('customer_name')))
        self.lp.bo.change_frame(self.lp.yp.get_locator('CustomerPage', 'leftFrame'))
        time.sleep(2)
        self.lp.bo.click_element(self.lp.yp.get_locator('CustomerPage', 'CustomerInfo'))
        time.sleep(2)
        self.lp.log.set_mes('click 客户信息', 'info')
        self.lp.bo.change_frame(self.lp.yp.get_locator('CustomerPage', 'mainFrame'))
        self.lp.bo.click_element(self.lp.yp.get_locator('CustomerPage', 'add_button'))
        self.lp.log.set_mes('click 添加', 'info')
        self.lp.bo.send_keys(self.lp.yp.get_locator('CustomerPage', 'name'), kwargs.get('customer_name', ''))
        self.lp.log.set_mes('input name' + kwargs.get('customer_name', ''), 'info')
        self.lp.bo.send_keys(self.lp.yp.get_locator('CustomerPage', 'e-mail'), kwargs.get('customer_email', ''))
        self.lp.log.set_mes('input email' + kwargs.get('customer_email', ''), 'info')
        self.lp.bo.change_readOnly('customerBirthday')
        self.lp.bo.send_keys(self.lp.yp.get_locator('CustomerPage', 'birthday'), kwargs.get('customer_birthday', ''))
        self.lp.log.set_mes('input time' + kwargs.get('customer_birthday', ''), 'info')
        self.lp.bo.send_keys(self.lp.yp.get_locator('CustomerPage', 'addman'), kwargs.get('customer_addman', ''))
        self.lp.log.set_mes('input customer_establisher' + kwargs.get('customer_addman', ''), 'info')
        self.lp.bo.click_element(self.lp.yp.get_locator('CustomerPage', 'add_submit'))
        self.lp.log.set_mes('click submit', 'info')

    def check_customer(self):
        alert_text = self.lp.bo.get_alert_text()
        self.lp.bo.alert_clicked()
        self.lp.bo.change_frame(self.lp.yp.get_locator('CustomerPage', 'leftFrame'))
        time.sleep(2)
        self.lp.bo.click_element(self.lp.yp.get_locator('CustomerPage', 'customer_care'))
        time.sleep(2)
        self.lp.bo.change_frame('mainFrame')
        res_s = self.lp.bo.get_text(self.lp.yp.get_locator('CustomerPage', 'result'))
        lst = re.findall('有 (\d+)条', res_s)
        number = int(lst[0])
        name_text = self.lp.bo.get_text(self.lp.yp.get_locator('CustomerPage', 'form_res').format(str(number)))

        if alert_text == '客户添加成功' and name_text == self.input_value.get('customer_name'):
            return True
        return False

    def modify_customer(self, customer_addr):
        self.lp.bo.change_frame(self.lp.yp.get_locator('CustomerPage', 'leftFrame'))
        time.sleep(2)
        self.lp.bo.click_element(self.lp.yp.get_locator('CustomerPage', 'CustomerInfo'))
        time.sleep(2)
        self.lp.log.set_mes('click 客户信息', 'info')
        self.lp.bo.change_frame(self.lp.yp.get_locator('CustomerPage', 'mainFrame'))
        self.lp.bo.send_keys(self.lp.yp.get_locator('CustomerPage', 'input_name'), '李四')
        self.lp.bo.click_element(self.lp.yp.get_locator('CustomerPage', 'search_button'))
        self.lp.bo.click_element(self.lp.yp.get_locator('CustomerPage', 'modify_button'))
        self.lp.log.set_mes('click 编辑', 'info')
        self.lp.bo.clear_initial_information(self.lp.yp.get_locator('CustomerPage', 'addr'))
        self.lp.bo.send_keys(self.lp.yp.get_locator('CustomerPage', 'addr'), customer_addr)
        self.lp.log.set_mes('input' + customer_addr, 'info')
        self.lp.bo.click_element(self.lp.yp.get_locator('CustomerPage', 'modify_submit'))
        self.lp.log.set_mes('click submit', 'info')
