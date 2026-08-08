CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(100),
    country VARCHAR(50)
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    amount NUMERIC(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);

INSERT INTO
    customers
VALUES (1, 'Amina', 'Sweden'),
    (2, 'Sara', 'Norway'),
    (3, 'John', 'Denmark'),
    (4, 'David', 'Finland');

INSERT INTO
    orders
VALUES (1, 1, '2025-01-10', 250),
    (2, 1, '2025-02-15', 100),
    (3, 2, '2025-03-20', 500);