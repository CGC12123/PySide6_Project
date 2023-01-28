#pyside6
from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet

from modules.application import Application
from modules.pages.page1_single_addNum import Page1AddNum

if __name__ == '__main__':
    q_appication = QApplication()
    apply_stylesheet(q_appication, theme='dark_teal.xml')

    app = Application()
    P1 = Page1AddNum(app)

    app.show()
    q_appication.exec()