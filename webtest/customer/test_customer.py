import sys
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
sys.path.append('D:\\.jenkins\\workspace')
from crm_sys.base.usebrowser import UseBrowser
from crm_sys.util.excel_operation import OperationExcel
from crm_sys.webpage.customeroperation.customer import CustomerPage


class TestCustomer(unittest.TestCase):

    def setUp(self) -> None:
        self.op = OperationExcel('../../config/test_case_customer.xlsx', '用例参数')
        self.cus = CustomerPage()

    def test_add_customer(self):
        self.cus.add_customer(customer_name=self.op.get_cell(1, 4),
                              customer_email=self.op.get_cell(1, 5),
                              customer_birthday=self.op.get_cell(1, 6),
                              customer_addman=self.op.get_cell(1, 7))
        self.assertEqual(True, self.cus.check_customer())

    def test_modify_customer(self):
        self.cus.modify_customer(self.op.get_cell(3, 4))
        self.assertEqual(self.op.get_cell(3, 5), self.cus.lp.bo.get_alert_text())
        self.cus.lp.bo.alert_clicked()

    def tearDown(self) -> None:
        UseBrowser.driver.quit()


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(TestCustomer)
    suite.addTests(test_case)
    date_now = time.strftime('%Y-%m-%d', time.localtime())
    with open('../../report/report_customer.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=0, title='UI自动化测试', description='ui自动化测试')
        runner.run(suite)
