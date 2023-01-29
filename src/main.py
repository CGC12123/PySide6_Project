from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet

from application import Application
from page_1.page1_main import Page1



if __name__ == '__main__':
    q_appication = QApplication()
    apply_stylesheet(q_appication, theme='dark_teal.xml')

    app = Application()
    page_1 = Page1(app)

    app.show()
    q_appication.exec()