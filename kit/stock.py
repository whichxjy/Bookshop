from PySide2 import QtWidgets
import pymysql

from ui.stockdialog import Ui_StockDialog
from kit import db

class StockDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_StockDialog()
        self.ui.setupUi(self)
        self.show_stock()

    def show_stock(self):
        result = self.select_stock()
        if result is None:
            return
        # Put data into the table
        for row_idx, row in enumerate(result):
            self.ui.stock_table.insertRow(row_idx)
            self.ui.stock_table.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(str(row["book_id"])))
            self.ui.stock_table.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(row["book_title"]))
            self.ui.stock_table.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(row["book_author"]))
            self.ui.stock_table.setItem(row_idx, 3, QtWidgets.QTableWidgetItem(str(row["book_price"])))
            self.ui.stock_table.setItem(row_idx, 4, QtWidgets.QTableWidgetItem(str(row["book_quantity"])))


    def select_stock(self):
        # Connect to database
        conn = db.connect_to_db()
        try:
            # Select stock and books' information
            with conn.cursor() as cursor:
                sql = """
                    SELECT book_id, book_title, book_author, book_price, book_quantity
                    FROM book NATURAL JOIN stock
                    """
                cursor.execute(sql)
                result = cursor.fetchall()
        except pymysql.Error:
            conn.rollback()
            QtWidgets.QMessageBox.about(self, "Sorry", "There's something wrong with the database")
        except Exception as err:
            QtWidgets.QMessageBox.about(self, "Sorry", str(err))
        finally:
            conn.close()
        
        return result