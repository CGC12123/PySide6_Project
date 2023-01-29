from application import Application


class Page1():
    #增加数字1

    def __init__(self, app: Application):
        self.ui = app.ui

        self.ui.P1_bt_addNum.clicked.connect(self.add_num)

    def add_num(self):
        self.ui.P1_lb_showNum.setText(str(int(self.ui.P1_lb_showNum.text()) + 1))
