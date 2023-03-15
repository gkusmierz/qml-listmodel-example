from PySide6.QtCore import QObject, Property, Slot

from .device_listmodel import DeviceListModel


class Controller(QObject):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._listmodel = DeviceListModel()
    
    @Property(QObject, constant=True)
    def listmodel(self):
        return self._listmodel

    @Slot(int, bool)
    def connect_device(self, list_index, connected):
        self._listmodel.set_device_connected(list_index, connected)

    @Slot(int)
    def add_after_index(self, list_index):
        self._listmodel.add_device_after_index(list_index, "new name", "new serial", False)

    @Slot(bool)
    def connect_all_devices(self, connected):
        self._listmodel.set_all_connected(connected)
