from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from gui import Ui_MainWindow
from config_gui import Ui_Dialog
import sys
import socket
from threading import Thread
import haversine
import math
import decimal
from decimal import *
import datetime


class ConfigDialog(QDialog):
    HOST = '127.0.0.1'

    def __init__(self, object):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.close_btn.clicked.connect(self.close)
        self.ui.start_server_btn.clicked.connect(self.connect_to_UDP)

        self.label = object

        self.first_point = (0, 0)
        self.second_point = (0, 0)
        self.first_timestamp = datetime.datetime(1900,1,1,1,1,1,0)
        self.two_points =[]
        self.total_distance =0
        # UDP_PORT = 3003 defalut port for StarPack 192.168.110.38
        # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        # sock.bind(("", UDP_PORT))   #use empyt string for UDP, this means that the local address is used not external

        # while True:
        #     data, addr = sock.recvfrom(512)  # buffer size
        #     split_line = str(data.splitlines()[0]).split(',')
        #     print(split_line)
        #     lat = float(split_line[7]) / 100
        #     long = float(split_line[9]) / 100
        #     print(f'Lat: {lat}, long {long}')

    def connect_to_UDP(self):
        """
        Invoked after pressing the Start Server button. Taake the port number and starts
        seperate thread for port listening
        """
        port = self.ui.tCPListeningPortSpinBox.value()
        try:
            t = Thread(target=self.start_receiving_UDP, args=[port])
            t.daemon = True
            t.start()
        except OSError as err:
            print('Error with starting a thread', err)

    def start_receiving_UDP(self, port):
        """
        Starts a new thread for the while loop. Accepts a single client
        """
        print('Deamon started....')
        self.ui.start_server_btn.setText('Listening to UDP packets...')
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind(("", port))  # use empyt string for UDP, this means that the local address is used not external

            while True:
                data, addr = s.recvfrom(512)  # buffer size
                split_line = str(data.splitlines()[0]).split(',')
                print(split_line)
                lat_raw = float(
                    split_line[7])  # moves the decimal so the packed [dm] looks like degrees minutes decimal format
                long_raw = float(
                    split_line[9])  # moves the decimal so the packed [dm] looks like degrees minutes decimal format
                time_stamp = datetime.datetime(int(split_line[6]), int(split_line[5]), int(split_line[4]),
                                               int(split_line[3][:2]), int(split_line[3][2:4]), int(split_line[3][4:6]),
                                               0)
                position = self.convert_packed_dm_to_dd(lat_raw, long_raw)  #converted position of the vessel in decimal degrees
                self.calculate_distance(time_stamp, position)

    def calculate_distance(self, timestamp, point):
        self.two_points.append(point)
        if len(self.two_points)<2:
            return
        else:
            self.total_distance += haversine.haversine(self.two_points[1], self.two_points[0])
            print(f'Distance in m: {self.total_distance * 1000}')
            # self.label.display(100)
            self.label.display(self.total_distance * 1000)

    def convert_packed_dm_to_dd(self, lat_raw, long_raw):
        """
        Converts two differnt geopgraphical coordinate formats i.e. packed degree decimal minute from Fugro StarPack
        to decimal degree format accepted by haversine library
        :param lat: Lattitude in compact dm format 5205.781083 ddmm.mmmmm [dm] WGS84
        :param long: Longitude in compact dm format 00424.365168 ddmm.mmmmm [dm] WGS84
        :return: Tuple of lat an long in decimal degrees DD.mmmmm
        """
        decimal.getcontext().prec = 8
        # ////////////////LATITUDE/////////////////////////////
        decimal_minutes, degrees_minutes = math.modf(
            lat_raw)  # extract degrees (degrees_minutes) and decimal minutes (decimal_minutes)
        degrees_minutes_str = str(degrees_minutes)

        degrees = int(degrees_minutes_str[0:2])
        minutes = Decimal(degrees_minutes_str[2:5])

        lat_dd = degrees + ((minutes + Decimal(decimal_minutes)) / 60)  # conversion to decimal degrees

        # ////////////////LONGITUDE////////////////////////////
        decimal_minutes_long, degrees_minutes_long = math.modf(long_raw)
        remiander, degrees_long = math.modf(degrees_minutes_long / 100)
        degrees_minutes_str_long = str(degrees_minutes_long / 100)

        minutes_long = Decimal((degrees_minutes_str_long.split('.')[1]))
        # minutes_long = Decimal(degrees_minutes_str_long[3:5])

        long_dd = Decimal(degrees_long) + ((minutes_long + Decimal(decimal_minutes_long)) / 60)

        print(f'Lat and long in packed DMS with decimal point: {lat_raw}, long {long_raw}')
        print(f'Decimal degrees : {lat_dd} and {long_dd}')
        return (lat_dd, long_dd)

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

        self.dialog = ConfigDialog(self.ui.current_km_label)

    def check_display(self):
        index = 100
        self.ui.current_km_label.display(index)

    def show_config(self):
        self.dialog.show()


app = QtWidgets.QApplication([])
application = VesselKMRun()
application.setWindowTitle('VesselKmRun')

application.show()
sys.exit(app.exec())
