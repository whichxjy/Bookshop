-- -- -- -- -- -- -- -- -- -- [ Drop All Tables ] -- -- -- -- -- -- -- -- -- --

DROP TABLE IF EXISTS `supply`;
DROP TABLE IF EXISTS `stock`;
DROP TABLE IF EXISTS `order_record`;
DROP TABLE IF EXISTS `purchase_record`;
DROP TABLE IF EXISTS `return_record`;
DROP TABLE IF EXISTS `book`;
DROP TABLE IF EXISTS `supplier`;

-- -- -- -- -- -- -- -- -- -- [ Book Table ] -- -- -- -- -- -- -- -- -- --

CREATE TABLE book(
    book_id INT NOT NULL AUTO_INCREMENT,
    book_title VARCHAR(255) NOT NULL,
    book_author VARCHAR(255) NOT NULL,
    book_price DECIMAL(6, 2) NOT NULL,
    PRIMARY KEY (book_id)
) ENGINE = InnoDB, DEFAULT CHARSET = UTF8MB4;

-- -- -- -- -- -- -- -- -- -- [ Supplier Table ] -- -- -- -- -- -- -- -- -- --

CREATE TABLE supplier(
    suppl_id INT NOT NULL AUTO_INCREMENT,
    suppl_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (suppl_id)
) ENGINE = InnoDB, DEFAULT CHARSET = UTF8MB4;

-- -- -- -- -- -- -- -- -- -- [ Supply Table ] -- -- -- -- -- -- -- -- -- --

CREATE TABLE supply(
    suppl_id INT NOT NULL,
    book_id INT NOT NULL,
    offer_price DECIMAL(6, 2) NOT NULL,
    PRIMARY KEY (suppl_id, book_id),
    FOREIGN KEY (suppl_id) REFERENCES supplier(suppl_id),
    FOREIGN KEY (book_id) REFERENCES book(book_id) ON DELETE CASCADE
) ENGINE = InnoDB, DEFAULT CHARSET = UTF8MB4;

-- -- -- -- -- -- -- -- -- -- [ Stock Table ] -- -- -- -- -- -- -- -- -- --

CREATE TABLE stock(
    book_id INT NOT NULL,
    book_quantity INT NOT NULL DEFAULT 0,
    PRIMARY KEY (book_id),
    FOREIGN KEY (book_id) REFERENCES book(book_id) ON DELETE CASCADE
) ENGINE = InnoDB, DEFAULT CHARSET = UTF8MB4;

-- -- -- -- -- -- -- -- -- -- [ Order Record Table ] -- -- -- -- -- -- -- -- -- --

CREATE TABLE order_record(
    order_num INT NOT NULL AUTO_INCREMENT,
    book_id INT NOT NULL,
    order_quantity INT NOT NULL,
    order_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (order_num),
    FOREIGN KEY (book_id) REFERENCES book(book_id) ON DELETE CASCADE
) ENGINE = InnoDB, DEFAULT CHARSET = UTF8MB4;

-- -- -- -- -- -- -- -- -- -- [ Purchase Record Table ] -- -- -- -- -- -- -- -- -- --

CREATE TABLE purchase_record(
    purch_num INT NOT NULL AUTO_INCREMENT,
    suppl_id INT NOT NULL,
    book_id INT NOT NULL,
    purch_quantity INT NOT NULL,
    purch_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (purch_num),
    FOREIGN KEY (suppl_id) REFERENCES supplier(suppl_id) ON DELETE CASCADE,
    FOREIGN KEY (book_id) REFERENCES book(book_id) ON DELETE CASCADE
) ENGINE = InnoDB, DEFAULT CHARSET = UTF8MB4;

-- -- -- -- -- -- -- -- -- -- [ Return Record Table ] -- -- -- -- -- -- -- -- -- --

CREATE TABLE return_record(
    ret_num INT NOT NULL AUTO_INCREMENT,
    book_id INT NOT NULL,
    ret_quantity INT NOT NULL,
    ret_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ret_num),
    FOREIGN KEY (book_id) REFERENCES book(book_id) ON DELETE CASCADE
) ENGINE = InnoDB, DEFAULT CHARSET = UTF8MB4;