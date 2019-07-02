# Bookshop Management System

This is a bookshop management system with GUI, powered by Qt and PyMySQL.

## Dependency

- PySide2 (Qt for Python)
- PyMySQL
- MySQL

## Test

- Initialize database in MySQL.

```mysql
mysql> CREATE DATABASE bookshop;
mysql> USE bookshop;
mysql> SOURCE sql/init_bookshop.sql;
mysql> SOURCE sql/test_bookshop.sql;
```

- Fill in the required fields in `kit/db.py`.

- Run the program.

```
python bookshop.py
```