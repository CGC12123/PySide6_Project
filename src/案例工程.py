#pyside6
from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet

from module.ui.application import Application


if __name__ == '__main__':
    q_appication = QApplication()

    app = Application()
    apply_stylesheet(app, theme='dark_teal.xml')



    app.show()

    q_appication.exec()