-- -- -- -- -- -- -- -- -- -- [ Add some books ] -- -- -- -- -- -- -- -- -- --

INSERT INTO book
(book_title, book_author, book_price)
VALUES
("For Whom the Bell Tolls", "Ernest Hemingway", 20);

INSERT INTO book
(book_title, book_author, book_price)
VALUES
("On the Road", "Jack Kerouac", 30);

INSERT INTO book
(book_title, book_author, book_price)
VALUES
("The Baron in the Trees", "Italo Calvino", 40);

-- -- -- -- -- -- -- -- -- -- [ Add some Suppliers ] -- -- -- -- -- -- -- -- -- --

INSERT INTO supplier
(suppl_name)
VALUES
("Supplier-A");

INSERT INTO supplier
(suppl_name)
VALUES
("Supplier-B");

INSERT INTO supplier
(suppl_name)
VALUES
("Supplier-C");

-- -- -- -- -- -- -- -- -- -- [ Supply ] -- -- -- -- -- -- -- -- -- --

# Supplier-A

INSERT INTO supply
(suppl_id, book_id, offer_price)
VALUES
(1, 1, 15);

INSERT INTO supply
(suppl_id, book_id, offer_price)
VALUES
(1, 2, 20);

INSERT INTO supply
(suppl_id, book_id, offer_price)
VALUES
(1, 3, 35);

# Supplier-B

INSERT INTO supply
(suppl_id, book_id, offer_price)
VALUES
(2, 1, 16);

INSERT INTO supply
(suppl_id, book_id, offer_price)
VALUES
(2, 2, 18);

INSERT INTO supply
(suppl_id, book_id, offer_price)
VALUES
(2, 3, 35);

# Supplier-C

INSERT INTO supply
(suppl_id, book_id, offer_price)
VALUES
(3, 1, 17);

INSERT INTO supply
(suppl_id, book_id, offer_price)
VALUES
(3, 2, 25);

INSERT INTO supply
(suppl_id, book_id, offer_price)
VALUES
(3, 3, 30);

-- -- -- -- -- -- -- -- -- -- [ Stock ] -- -- -- -- -- -- -- -- -- --

INSERT INTO stock
(book_id, book_quantity)
VALUES
(1, 10);

INSERT INTO stock
(book_id, book_quantity)
VALUES
(2, 10);

INSERT INTO stock
(book_id, book_quantity)
VALUES
(3, 10);