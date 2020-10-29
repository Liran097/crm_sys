import logging
import time

class AutoLogger:
    # 创建Logger对象
    def __init__(self):
        self.logger = logging.getLogger('log')

    def set_mes(self, message, level_p):
        try:
            self.logger = logging.getLogger('log')
            time_now = time.strftime('%Y-%m-%d', time.localtime())
            # 创建文件handler
            fh = logging.FileHandler('../../log_info/crm_auto_test' + time_now + '.log', encoding='utf-8')
            # 创建控制台handler
            ch = logging.StreamHandler()
            # 格式化
            fm = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
            # 对文件格式化
            fh.setFormatter(fm)
            # 对控制台格式化
            ch.setFormatter(fh)
            # 文件句柄加入Logger对象中
            self.logger.addHandler(fh)
            # 控制台句柄加入Logger对象中
            self.logger.addHandler(ch)
            # 设置打印级别
            self.logger.setLevel(logging.DEBUG)
            # 输出info
            if level_p == 'debug':
                self.logger.info(message)
            elif level_p == 'info':
                self.logger.info(message)
            elif level_p == 'error':
                self.logger.error(message)
            elif level_p == 'warning':
                self.logger.warning(message)
            elif level_p == 'critical':
                self.logger.critical(message)
            # 移除文件句柄
            self.logger.removeHandler(fh)
            # 移除控制台句柄
            self.logger.removeHandler(ch)
            # 关闭文件
        except:
            print('file exception')