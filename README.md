Enviroment Configuration
======
1. We use mysql server as database, use command `sudo apt-get install mysql-server` to install
2. We use python 2.7 with package mysqldb
    * use command `sudo apt-get install libmysqlclient-dev python-dev`
    * then command `sudo pip install mysql`
    * use command `sudo apt-get install pip` if you have no pip
3. Use command `mysql -u root -p credit < credit.sql` to load the `credit.sql` database
4. Use command `mysqldump -u root -p credit > credit.sql` to backup mysql database

Source Code
====

1. The database api is in file `./source/databaseapi.py` which has two classes
    * `Card` which handle card operations in the database
    * `User` which handle user operation and login operation
    * Use `from databaseapi import Card, User` to import these classes



