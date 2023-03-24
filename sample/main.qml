import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: mainWindow
    visible: true
    title: qsTr("Sample app")
    width: 640
    height: 320
    color: "whitesmoke"

    RowLayout {
        anchors.fill: parent

        ListView {
            id: deviceList
            Layout.fillHeight: true
            Layout.fillWidth: true
            Layout.preferredWidth: 2

            model: controller.listmodel
            delegate: Item {
                width: deviceList.width
                height: 24

                Text {
                    text: `${index}: ${name} (${serial}) - ${connected ? "OK" : "NOT FOUND"}`
                    font.pointSize: 16
                }

                MouseArea {
                    id: listDelegateMouseArea
                    anchors.fill: parent
                    hoverEnabled: true
                    onClicked: deviceList.currentIndex = index
                }
            }

            highlight: Rectangle { color: "lightBlue" }
        }  // ListView

        ColumnLayout {
            Layout.fillHeight: true
            Layout.fillWidth: true
            Layout.preferredWidth: 1

            Button {
                text: "Connect device"
                Layout.fillWidth: true
                onClicked: controller.connect_device(deviceList.currentIndex, true)
            }

            Button {
                text: "Disconnect device"
                Layout.fillWidth: true
                onClicked: controller.connect_device(deviceList.currentIndex, false)
            }

            Button {
                text: "Connect all devices"
                Layout.fillWidth: true
                onClicked: controller.connect_all_devices(true)
            }

            Button {
                text: "Disconnect all devices"
                Layout.fillWidth: true
                onClicked: controller.connect_all_devices(false)
            }

            Button {
                text: "Add device after selected"
                Layout.fillWidth: true
                onClicked: controller.add_after_index(deviceList.currentIndex)
            }

            Item {
                Layout.fillHeight: true
            }

        }  // ColumnLayout
    }  // RowLayout
}  // ApplicationWindow
