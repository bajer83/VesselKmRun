from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from gui import Ui_MainWindow
from config_gui import Ui_Dialog
import sys
import socket

class ConfigDialog(QDialog):
    HOST = '127.0.0.1'

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.close_btn.clicked.connect(self.close)
        self.ui.start_server_btn.clicked.connect(self.start_server)

    def start_server(self):
        port = self.ui.tCPListeningPortSpinBox.value()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, port))
            s.listen()
            conn, addr = s.accept() #blocking function
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)

    def stop_server(self):
        pass

    def close(self):
        self.hide()

class VesselKMRun(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.new_session_btn.clicked.connect(self.check_display)
        self.ui.actionConfigure.triggered.connect(self.show_config)

        self.dialog = ConfigDialog()


    def check_display(self):
        self.ui.current_km_label.display(1000.0)

    def show_config(self):
        self.dialog.show()


app = QtWidgets.QApplication([])
application = VesselKMRun()
application.setWindowTitle('VesselKmRun')

application.show()
sys.exit(app.exec())