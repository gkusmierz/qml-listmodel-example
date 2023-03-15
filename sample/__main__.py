from pathlib import Path
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuickControls2 import QQuickStyle
import sys

from .controller import Controller


def main():
    app = QGuiApplication(sys.argv)
    QQuickStyle.setStyle("Material")

    qml_app_engine = QQmlApplicationEngine()
    qml_context = qml_app_engine.rootContext()
    controller = Controller(parent=app)
    qml_context.setContextProperty("controller", controller)
    this_file_path = Path(__file__)
    main_qml_path = this_file_path.parent / 'main.qml'
    qml_app_engine.load(QUrl.fromLocalFile(str(main_qml_path)))
    if len(qml_app_engine.rootObjects()) == 0:
        sys.exit('Failed to start the UI.')

    sys.exit(app.exec())
