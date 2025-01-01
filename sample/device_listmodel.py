from enum import IntEnum, auto
from PyQt6.QtCore import Qt, QAbstractListModel, QModelIndex


class DeviceItemRoles(IntEnum):
    NAME = Qt.ItemDataRole.UserRole
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
        self._add_device("name1", 123, False)
        self._add_device("name2", 456, True)
        self._add_device("name3", 789, False)

    def roleNames(self):
        return {role.value: name for role, name in _role_names.items()}

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def data(self, index, role):
        if not index.isValid() or index.row() >= len(self._data):
            return None

        device = self._data[index.row()]
        return device.get(DeviceItemRoles(role), None)

    def _add_device(self, name, serial, connected):
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
            return
        
        self._data[list_index][DeviceItemRoles.CONNECTED] = connected
        self.dataChanged.emit(self.index(list_index), self.index(list_index), [DeviceItemRoles.CONNECTED.value])

    def set_all_connected(self, connected):
        for device in self._data:
            device[DeviceItemRoles.CONNECTED] = connected
        self.dataChanged.emit(self.index(0), self.index(self.rowCount() - 1), [DeviceItemRoles.CONNECTED.value])