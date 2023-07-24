#!/bin/bash

# Function to install MySQL Server
install_mysql_server() {
    sudo apt update
    sudo apt install mysql-server -y
}

# Function to change MySQL root password
change_mysql_root_password() {
    echo "Enter new password for MySQL root user:"
    mysql --user=root <<_EOF_
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'passwordis@2018';
FLUSH PRIVILEGES;
_EXIT_
_EOF_
    echo "MySQL root password changed successfully!"
}

# Function to create database and table
create_database_and_table() {
    echo "Enter the name of the database you want to create:"
    DATABASE_NAME= 'farooq'
    echo "Enter the name of the table you want to create:"
    TABLE_NAME= 'summer_gala'

    # Replace 'your_mysql_root_password' with the password you set during MySQL installation
    MYSQL_ROOT_PASSWORD='passwordis@2018'

    # Install MySQL client (if not already installed)
    sudo apt install mysql-client -y

    # Start MySQL service
    sudo service mysql start

    # Create the database
    mysql -u root -p$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS $DATABASE_NAME;"

    # Create the table (modify the table schema as per your requirement)
    mysql -u root -p$MYSQL_ROOT_PASSWORD -e "USE $DATABASE_NAME; CREATE TABLE IF NOT EXISTS $TABLE_NAME (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT);"

    # Optional: Insert sample data into the table
    mysql -u root -p$MYSQL_ROOT_PASSWORD -e "USE $DATABASE_NAME; INSERT INTO $TABLE_NAME (name, age) VALUES ('John Doe', 30), ('Jane Smith', 25);"

    # Stop MySQL service
    sudo service mysql stop

    echo "Database '$DATABASE_NAME' and table '$TABLE_NAME' created successfully!"
}

# Main Script

# Install MySQL server
install_mysql_server

# Change MySQL root password
change_mysql_root_password

# Create database and table
create_database_and_table

