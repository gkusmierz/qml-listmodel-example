from PyQt6.QtCore import QObject, pyqtProperty, pyqtSlot
from random import randint

from .device_listmodel import DeviceListModel

class Controller(QObject):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._listmodel = DeviceListModel()
    
    @pyqtProperty(QObject, constant=True)
    def listmodel(self):
        return self._listmodel

    @pyqtSlot(int, bool)
    def connect_device(self, list_index, connected):
        self._listmodel.set_device_connected(list_index, connected)

    @pyqtSlot(int)
    def add_after_index(self, list_index):
        self._listmodel.add_device_after_index(list_index, "new name", randint(100, 999), False)

    @pyqtSlot(bool)
    def connect_all_devices(self, connected):
        self._listmodel.set_all_connected(connected)