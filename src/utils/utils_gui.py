from PySide6.QtWidgets import QFileDialog, QLabel
from main import Application


#读取文件夹 并设置到label上
def read_and_set_folder_path(window: Application, messege: str, label: QLabel):
    path = QFileDialog.getExistingDirectory(window, messege)
    label.setText(path)
    return path
