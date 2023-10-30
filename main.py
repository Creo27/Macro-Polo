import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
import sqlite3

class MacroPoloApp:
    def __init__(self):
        self.loader = QUiLoader()
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = self.loader.load("MacroPolo.ui", None)
        self.conn = sqlite3.connect('macab.db')
        self.cursor = self.conn.cursor()

        self.t1 = self.window.findChild(QtWidgets.QTableWidget, 't1')
        self.t1.setHorizontalHeaderLabels(['Key', 'Value'])

        self.cursor.execute("SELECT Key, Value FROM binds")
        rows = self.cursor.fetchall()
        self.t1.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.t1.setItem(i, j, item)
    def run(self):
        self.window.show()
        return self.app.exec()

if __name__ == "__main__":
    app = MacroPoloApp()
    app.run()