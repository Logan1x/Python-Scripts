from dictionary import definition
from PyQt5 import QtCore, QtWidgets


class Dict_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dictionary")
        Dialog.resize(344, 249)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 321, 236))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 4)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchText = QtWidgets.QLineEdit(self.widget)
        self.searchText.setText("")
        self.searchText.setObjectName("searchText")
        self.horizontalLayout.addWidget(self.searchText)
        self.searchButton = QtWidgets.QPushButton(self.widget)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.resultText = QtWidgets.QTextBrowser(self.widget)
        self.resultText.setObjectName("resultText")
        self.verticalLayout.addWidget(self.resultText)

        # output fonts
        font = self.resultText.font()
        font.setPointSize(20)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.searchText, self.searchButton)

        # events
        self.searchButton.clicked.connect(self.show_definition)

    def show_definition(self):
        word = self.searchText.text()
        defn = definition(word)

        if defn != '':
            self.resultText.setText(defn)
        else:
            self.resultText.setText('definition not found')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.searchText.setPlaceholderText(
            _translate("Dialog", "word to search"))
        self.searchButton.setText(_translate("Dialog", "search"))
