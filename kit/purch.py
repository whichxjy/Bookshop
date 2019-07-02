from PySide2 import QtWidgets
import pymysql

from ui.purchdialog import Ui_PurchaseDialog
from kit import db

class PurchaseDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_PurchaseDialog()
        self.ui.setupUi(self)
        self.ui.submit_Btn.clicked.connect(self.on_submit_btn_clicked)

    def on_submit_btn_clicked(self):
        book_id_LE_text = self.ui.book_id_LE.text()
        # If book_id_LE_text is not filled, return
        if not book_id_LE_text:
            QtWidgets.QMessageBox.about(self, "Sorry", "Please fill out the \"Book ID\" field")
            return
        # If book_id_LE_text is not an integer, return
        try:
            book_id = int(book_id_LE_text)
        except ValueError:
            return
        quantity = self.ui.quantity_SB.value()
        # Purchase book(s)
        self.purchase_book(book_id, quantity)
        # Clear all the fields
        self.ui.book_id_LE.clear()
        self.ui.quantity_SB.setValue(1)

    def purchase_book(self, book_id, quantity):
        # Connect to database
        conn = db.connect_to_db()
        try:
            # Check if the book id exists
            with conn.cursor() as cursor:
                sql = """
                    SELECT EXISTS(
                        SELECT 1
                        FROM book
                        WHERE book_id = {0}
                    ) as exist
                    """.format(book_id)
                cursor.execute(sql)
                result = cursor.fetchone()
                if not result['exist']:
                    raise Exception('No such Book ID')
            
            # Choose the supplier with the lowest offer price if there're
            # one or more suppliers that offer this book
            with conn.cursor() as cursor:
                sql = """
                    SELECT suppl_id
                    FROM supply
                    WHERE book_id = {0}
                    ORDER BY offer_price
                    LIMIT 1
                    """.format(book_id)
                cursor.execute(sql)
                result = cursor.fetchone()
                if result is None:
                    raise Exception('No supplier offers this book')
                else:
                    suppl_id = result['suppl_id']

            # Add purchase record to purchase record table
            with conn.cursor() as cursor:
                sql = """
                    INSERT INTO purchase_record
                    (suppl_id, book_id, purch_quantity)
                    VALUES
                    ({0}, {1}, {2})
                    """.format(suppl_id, book_id, quantity)
                cursor.execute(sql)

            # Update stock table
            with conn.cursor() as cursor:
                sql = """
                    UPDATE stock
                    SET book_quantity = book_quantity + {0}
                    WHERE book_id = {1}
                    """.format(quantity, book_id)
                cursor.execute(sql)

            conn.commit()

            QtWidgets.QMessageBox.about(self, "OK", "Success!")
        except pymysql.Error:
            conn.rollback()
            QtWidgets.QMessageBox.about(self, "Sorry", "There's something wrong with the database")
        except Exception as err:
            QtWidgets.QMessageBox.about(self, "Sorry", str(err))
        finally:
            conn.close()