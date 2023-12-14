sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql
sudo systemctl enable mysql
sudo apt install python3
sudo apt install python3-pip
pip3 install mysql-connector-python

sudo mysql -u root -p
CREATE DATABASE yourdb;
CREATE USER 'youruser'@'localhost' IDENTIFIED BY 'yourpassword';
GRANT ALL PRIVILEGES ON yourdb.* TO 'youruser'@'localhost';
FLUSH PRIVILEGES;

USE yourdb;  -- Switch to the 'yourdb' database
CREATE TABLE your_table_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);
INSERT INTO your_table_name (name) VALUES
    ('swarada'),
    ('shravani'),
    ('vaishnavi'),
    ('yashashwi'),
    ('datta'),
    ('jyot');

EXIT;

import mysql.connector

# Define the connection parameters
config = {
    'user': 'youruser',
    'password': 'yourpassword',
    'host': 'localhost',
    'database': 'yourdb'
}

# Create a connection to the MySQL server
conn = mysql.connector.connect(**config)

# Create a cursor to interact with the database
cursor = conn.cursor()

# Example: Execute a SQL query
cursor.execute("SELECT * FROM your_table_name")

# Fetch and print results
for row in cursor.fetchall():
    print(row)

# Close cursor and connection
cursor.close()
conn.close()

python3 -m venv myenv
source myenv/bin/activate
pip install mysql-connector-python

python3 your_script.py