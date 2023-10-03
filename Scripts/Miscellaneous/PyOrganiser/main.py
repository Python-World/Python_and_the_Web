import json
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

qt_creator_file = "media/mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)
tick = QtGui.QImage("media/tick.png")
untick = QtGui.QImage("media/todo.png")


class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, *args, todos=None, database=None, **kwargs):
        super(TodoModel, self).__init__(*args, **kwargs)
        self.todos = todos or []
        self.database = database or {}

    def data(self, index, role):
        if role == Qt.DisplayRole:
            _, text = self.todos[index.row()]
            return text

        if role == Qt.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return tick
            return untick

    def rowCount(self, index):
        return len(self.todos)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.onDateChanged()
        self.dateEdit.dateChanged.connect(self.onDateChanged)
        self.todoView.setModel(self.model)
        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)
        self.inCompleteButton.pressed.connect(self.incomplete)

    def add(self):
        """
        Add an item to our todo list, getting the text from the QLineEdit .todoEdit
        and then clearing it.
        """
        text = self.todoEdit.text()
        if text:  # Don't add empty strings.
            # Access the list via the model.
            self.model.todos.append((False, text))
            # Trigger refresh.
            self.model.layoutChanged.emit()
            # Empty the input
            self.todoEdit.setText("")
            self.save()
            self.changeProgress()

    def delete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            # Indexes is a list of a single item in single-select mode.
            index = indexes[0]
            # Remove the item and refresh.
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()
            self.save()
            self.changeProgress()

    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            text = self.model.todos[row][1]
            self.model.todos[row] = (True, text)
            # .dataChanged takes top-left and bottom right, which are equal
            # for a single selection.
            self.model.dataChanged.emit(index, index)
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()
            self.save()
            self.changeProgress()

    def incomplete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            text = self.model.todos[row][1]
            self.model.todos[row] = (False, text)
            # .dataChanged takes top-left and bottom right, which are equal
            # for a single selection.
            self.model.dataChanged.emit(index, index)
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()
            self.save()
            self.changeProgress()

    def changeProgress(self):
        total = len(self.model.todos)
        done = 0
        for item in self.model.todos:
            if item[0]:
                done += 1
        self.progressBar.setValue(int(float(done / total) * 100))

    def onDateChanged(self):
        self.date = self.dateEdit.dateTime().toString("dd-MM-yyyy")
        self.model = TodoModel()
        self.load()
        self.todoView.setModel(self.model)

    def load(self):
        try:
            with open("data.db", "r") as f:
                jsondata = json.load(f)
                try:
                    k = jsondata[self.date][0]
                except KeyError:
                    jsondata[self.date] = [{"name": None, "todos": []}]
                k = jsondata[self.date][0]
                self.model.database = jsondata
                self.model.todos = k["Topics"]
                self.changeProgress()
        except Exception as e:
            print(e)

    def save(self):
        with open("data.db", "w") as f:
            json.dump(self.model.database, f)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
