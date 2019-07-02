from PySide2 import QtWidgets

from ui.mainwindow import Ui_MainWindow
from kit.sale import SaleDialog
from kit.stock import StockDialog
from kit.purch import PurchaseDialog
from kit.ret import ReturnDialog
from kit.stats import StatisticsDialog

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sale_Btn.clicked.connect(self.on_sale_btn_clicked)
        self.ui.show_stock_Btn.clicked.connect(self.show_stock_btn_clicked)
        self.ui.purchase_Btn.clicked.connect(self.on_purchase_btn_clicked)
        self.ui.return_Btn.clicked.connect(self.on_return_btn_clicked)
        self.ui.statistics_Btn.clicked.connect(self.on_statistics_btn_clicked)
        
    def on_sale_btn_clicked(self):
        self.setEnabled(False)
        sale_dialog = SaleDialog(self)
        sale_dialog.show()
        sale_dialog.exec_()
        self.setEnabled(True)

    def show_stock_btn_clicked(self):
        self.setEnabled(False)
        stock_dialog = StockDialog(self)
        stock_dialog.show()
        stock_dialog.exec_()
        self.setEnabled(True)

    def on_purchase_btn_clicked(self):
        self.setEnabled(False)
        purchase_dialog = PurchaseDialog(self)
        purchase_dialog.show()
        purchase_dialog.exec_()
        self.setEnabled(True)

    def on_return_btn_clicked(self):
        self.setEnabled(False)
        return_dialog = ReturnDialog(self)
        return_dialog.show()
        return_dialog.exec_()
        self.setEnabled(True)

    def on_statistics_btn_clicked(self):
        self.setEnabled(False)
        statistics_dialog = StatisticsDialog(self)
        statistics_dialog.show()
        statistics_dialog.exec_()
        self.setEnabled(True)