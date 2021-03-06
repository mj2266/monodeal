import os
from PyQt5 import uic, QtWidgets, QtCore

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir, "cardList.ui"))


class cardListWindow(Base, Form):
    def __init__(self, parent=None, msg="foo"):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        print(msg)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = cardListWindow()
    w.show()
    sys.exit(app.exec_())
