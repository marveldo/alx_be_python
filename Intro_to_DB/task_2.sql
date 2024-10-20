USE alx_book_store;
CREATE TABLE IF NOT EXISTS Authors (
   author_id INT AUTO_INCREMENT PRIMARY KEY,
   author_name VARCHAR(215)
);

-- Now create the Books table
CREATE TABLE IF NOT EXISTS Books (
   book_id INT AUTO_INCREMENT PRIMARY KEY,
   title VARCHAR(130),
   author_id INT,  -- Foreign key to the Authors table
   price DOUBLE PRECISION,
   publication_date DATE,
   FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

-- Create Customers table
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);

-- Create Orders table, referencing Customers
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,  -- Foreign key to Customers
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Create Order_Details table, referencing both Orders and Books
CREATE TABLE IF NOT EXISTS Order_Details (
    orderdetail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,  -- Foreign key to Orders
    book_id INT,   -- Foreign key to Books
    quantity DOUBLE PRECISION,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);