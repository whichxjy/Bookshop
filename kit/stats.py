from PySide2 import QtWidgets
import pymysql

from ui.statsdialog import Ui_StatisticDialog
from kit import db

class StatisticsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_StatisticDialog()
        self.ui.setupUi(self)
        self.ui.submit_Btn.clicked.connect(self.on_submit_btn_clicked)

    def on_submit_btn_clicked(self):
        self.ui.sales_LE.clear()
        self.ui.quantity_LE.clear()
        self.ui.ranking_table.setRowCount(0)
        date = self.ui.date_edit.date()
        self.setEnabled(False)
        self.show_stats(date.year(), date.month())
        self.setEnabled(True)

    def show_stats(self, year, month):
        # Connect to database
        conn = db.connect_to_db()
        try:
            # Check if there're one or more order records in this date
            with conn.cursor() as cursor:
                sql = """
                    SELECT EXISTS(
                        SELECT 1
                        FROM order_record
                        WHERE YEAR(order_date) = {0} AND MONTH(order_date) = {1}
                    ) as exist
                    """.format(year, month)
                cursor.execute(sql)
                result = cursor.fetchone()
                if not result['exist']:
                    raise Exception('No order order in this month')

            # Calculate total sales in this month
            with conn.cursor() as cursor:
                sql = """
                    SELECT SUM(book_price * order_quantity) AS total_sales
                    FROM book NATURAL JOIN order_record
                    WHERE YEAR(order_date) = {0} AND MONTH(order_date) = {1}
                    """.format(year, month)
                cursor.execute(sql)
                result = cursor.fetchone()
                self.show_total_sales(result["total_sales"])
            
            # Caculate total quantity of books were sold
            with conn.cursor() as cursor:
                sql = """
                    SELECT SUM(order_quantity) AS total_quantity
                    FROM order_record
                    WHERE YEAR(order_date) = {0} AND MONTH(order_date) = {1}
                    """.format(year, month)
                cursor.execute(sql)
                result = cursor.fetchone()
                self.show_total_quantity(result["total_quantity"])

            # Get Ranking
            with conn.cursor() as cursor:
                sql = """
                    SELECT book_title, book_author, SUM(order_quantity) AS sales
                    FROM book NATURAL JOIN order_record
                    WHERE YEAR(order_date) = {0} AND MONTH(order_date) = {1}
                    GROUP BY book_id, book_title, book_author
                    ORDER BY SUM(order_quantity) DESC
                    """.format(year, month)
                cursor.execute(sql)
                result = cursor.fetchall()
                self.show_ranking(result)

        except pymysql.Error:
            conn.rollback()
            QtWidgets.QMessageBox.about(self, "Sorry", "There's something wrong with the database")
        except Exception as err:
            QtWidgets.QMessageBox.about(self, "Sorry", str(err))
        finally:
            conn.close()

    def show_total_sales(self, total_sales):
        self.ui.sales_LE.setText(str(total_sales))

    def show_total_quantity(self, total_quantity):
        self.ui.quantity_LE.setText(str(total_quantity))

    def show_ranking(self, ranking):
        if ranking is None:
            return
        # Put data into the table
        for row_idx, row in enumerate(ranking):
            self.ui.ranking_table.insertRow(row_idx)
            self.ui.ranking_table.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(row["book_title"]))
            self.ui.ranking_table.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(row["book_author"]))
            self.ui.ranking_table.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(str(row["sales"])))