from enum import IntEnum, auto
from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex


class DeviceItemRoles(IntEnum):
    NAME = Qt.UserRole
    SERIAL = auto()
    CONNECTED = auto()


_role_names = {
    DeviceItemRoles.NAME: b'name',
    DeviceItemRoles.SERIAL: b'serial',
    DeviceItemRoles.CONNECTED: b'connected'
}


class DeviceListModel(QAbstractListModel):
    def __init__(self):
        super().__init__()
        self._data = []
        self.add_device("name1", "serial1", False)
        self.add_device("name2", "serial2", True)
        self.add_device("name3", "serial3", False)

    def roleNames(self):
        return _role_names

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def data(self, index, role):
        if role not in list(DeviceItemRoles):
            return None

        try:
            device = self._data[index.row()]
        except IndexError:
            return None

        if role in device:
            return device[role]

        return None

    def add_device(self, name, serial, connected):
        new_row = {
            DeviceItemRoles.NAME: name,
            DeviceItemRoles.SERIAL: serial,
            DeviceItemRoles.CONNECTED: connected
        }
        self._data.append(new_row)
    
    def add_device_after_index(self, idx, name, serial, connected):
        index_of_new_device = idx + 1
        new_device = {
            DeviceItemRoles.NAME: name,
            DeviceItemRoles.SERIAL: serial,
            DeviceItemRoles.CONNECTED: connected
        }

        self.beginInsertRows(QModelIndex(), index_of_new_device, index_of_new_device)
        self._data.insert(index_of_new_device, new_device)
        self.endInsertRows()

    def set_device_connected(self, list_index, connected):
        if list_index < 0 or list_index >= len(self._data):
            return None
        
        self._data[list_index][DeviceItemRoles.CONNECTED] = connected
        self.dataChanged.emit(self.index(list_index), self.index(list_index), [])

    def set_all_connected(self, connected):
        for d in self._data:
            d[DeviceItemRoles.CONNECTED] = connected
        self.dataChanged.emit(self.index(0), self.index(self.rowCount() - 1), [])
