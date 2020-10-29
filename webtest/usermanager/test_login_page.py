import sys

sys.path.append('D:\\PythonFile')
from crm_sys.base.usebrowser import UseBrowser
from crm_sys.util.excel_operation import OperationExcel


import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from crm_sys.webpage.usermanager.loginpage import LoginPage


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.op = OperationExcel('../../config/test_case_login.xlsx', '用例参数')
        self.lp = LoginPage()

    def test_login_all_null(self):
        self.lp.login(self.op.get_cell(1, 2), self.op.get_cell(1, 3))
        self.assertEqual(self.op.get_cell(1, 4), self.lp.bo.get_alert_text())
        self.lp.bo.alert_clicked()

    def test_login_username_null(self):
        self.lp.login(self.op.get_cell(2, 2), self.op.get_cell(2, 3))
        self.assertEqual(self.op.get_cell(2, 4), self.lp.bo.get_alert_text())
        self.lp.bo.alert_clicked()

    def test_login_password_null(self):
        self.lp.login(self.op.get_cell(3, 2), self.op.get_cell(3, 3))
        self.assertEqual(self.op.get_cell(3, 4), self.lp.bo.get_alert_text())
        self.lp.bo.alert_clicked()

    def test_login_error(self):
        self.lp.login(self.op.get_cell(4, 2), self.op.get_cell(4, 3))
        self.assertEqual(self.op.get_cell(4, 4), self.lp.bo.get_alert_text())
        self.lp.bo.alert_clicked()

    def test_login_success(self):
        self.lp.login(self.op.get_cell(5, 2), self.op.get_cell(5, 3))
        self.assertEqual(self.op.get_cell(5, 4), self.lp.login_correct_text('topFrame'))

    def tearDown(self) -> None:
        UseBrowser.driver.quit()


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    suite.addTests(test_case)
    date_now = time.strftime('%Y-%m-%d', time.localtime())
    with open('../../report/report_login.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=0, title='UI自动化测试', description='ui自动化测试')
        runner.run(suite)
