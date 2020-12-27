# Project 2020 - Open Orders Management System
## Course: Data Representation

* Student Name: Paul Caulfield
* Student No: G00376342

* Lecturer: Andrew Beatty

An assignment submitted in part fulfilment of the requirements of the Higher Diploma in Science - Data Analytics: 2020-2021, Galway Mayo Institute of Technology.
  * Submitted: 29th December 2020

## Project Overview - Open Orders Management System
The objective of this project is as follows:
1. Create a web application called Open Orders Management System to perform CRUD operations on two database tables 'Orders' and 'Customers'. 
1. Normalise the two databases using Foreign Key to ensure that open orders cannot be created for a customer if customer doesn’t  exist in customer table. To achieve this I added a foreign key constraint as follows:  FOREIGN KEY (CUSTOMER_NUMBER) REFERENCES CUSTOMER(ID)  ON UPDATE CASCADE ON DELETE RESTRICT
1. Display value of Open Orders in Euros using latest USDEUR FX Exchange rate which can be refreshed daily using 3rd Party API Interface. The open order value is stored in base currency which is US Dollar (USD) in the database. The 3rd Party API I am using is [exchangeratesapi](https://exchangeratesapi.io/) which provides current and historical foreign exchange rates published by the European Central Bank[3]. 
1. Host the web application online. I have hosted a lite version of web application hosted on Pythonanywhere, enabling CRUD operations on one database table 'Orders'. Due to time constraints, I did not have time to test customer.html on pythonanywhere. I also did not implement login.html page as I encountered some errors and did not have time to troubleshoot them. 

![Image of currency](staticpages/currency.jpg)

## Contents 

*Main Web App - Local Host*
| File |      Title                | Description |Link|
|------|---------------------------|---------|------|
| 1    | server.py | A basic Flask server that has a REST API, (to perform CRUD operations) |https://github.com/pcaulfie/FX-Rates-API/blob/main/server.py|
| 2    | index.html | A web interface, using AJAX calls, to perform CRUD operations on orders table |https://github.com/pcaulfie/FX-Rates-API/blob/main/staticpages/index.html|
| 3    | customer.html | A web interface, using AJAX calls, to perform CRUD operations on orders table |https://github.com/pcaulfie/FX-Rates-API/blob/main/staticpages/customer.html|
| 4    | initdb.sql | A file containing the mysql commands used to create two tables in a mysql database |https://github.com/pcaulfie/FX-Rates-API/blob/main/initdb.sql|
| 5   | dbconfigtemplate | A file containing the configuration details needed to connect to the mysql database |https://github.com/pcaulfie/FX-Rates-API/blob/main/dbconfigtemplate.py|
| 6    | OrdersDao.py | A data access object (DAO) that provides an interface to the MYSQL database |https://github.com/pcaulfie/FX-Rates-API/blob/main/OrdersDao.py|
| 7    | TestOrdersDao.py | A file used to test the OrdersDao is working correctly before implementing it on a Flask server. |https://github.com/pcaulfie/FX-Rates-API/blob/main/TestOrdersDao.py|
| 8    | Requirements.txt | A file listing all packages needed to run the application |https://github.com/pcaulfie/FX-Rates-API/blob/main/requirements.txt|
| 9    |.gitignore | A file used to tell git which files are not needed to be added to the repository. |https://github.com/pcaulfie/FX-Rates-API/blob/main/.gitignore|

*Web App - Hosted Online*
| File |      Title                | Description |Link|
|------|---------------------------|---------|------|
| 1    | deploytoazure | Folder containing the files have been uploaded to Pythonanywhere|https://github.com/pcaulfie/FX-Rates-API/tree/main/deploytoazure|
| 2    | Internet shortcut  | Link to app hosted online on Pythonanywhere to app hosted online on Pythonanywhere |http://paulcaulfield.pythonanywhere.com/index.html|

*3rd Party API Working Files*
| File |      Title                | Description |Link|
|------|---------------------------|---------|------|
| 1    | 3rd Party API Folder | Folder containing the files have been uploaded to Pythonanywhere|https://github.com/pcaulfie/FX-Rates-API/tree/main/3rd%20Party%20API|
| 2    | getJSONfromAPI.html  | A test file used to test web interface, using AJAX calls, to extract FX Rates from 3rd party API |https://github.com/pcaulfie/FX-Rates-API/blob/main/3rd%20Party%20API/getJSONfromAPI.html|
| 3    | exchangeratesapi.py  | A python program to extract latest exchange rates in JSON |https://github.com/pcaulfie/FX-Rates-API/blob/main/3rd%20Party%20API/exchangeratesapi.py|
| 4   | latestRates.json  | A JSON file containing the output of exchangeratesapi.py  |https://github.com/pcaulfie/FX-Rates-API/blob/main/3rd%20Party%20API/latestRates.json|

### How to Clone This Repository
| Step |      Task                | Instructions |
|------|---------------------------|---------|
| 1    | Install Anaconda distribution of python which contains all the libraries used| [Anaconda](https://www.anaconda.com/distribution/)|
| 2    | Launch Cmder or other similar console| cmder|
| 3    | create a folder where you want to clone the repository| for example *cd folder/to/clone-into/*|
| 4    | Specify URL of the repository you want to clone| *git clone https://github.com/pcaulfie/FX-Rates-API*|

### Setting Up A Virtual Environment on Local Machine [1]
| Step |      Task                | Windows |Mac / Linux|
|------|---------------------------|---------|------|
| 1    | Make a virtual environment | python -m venv venv|python -m venv venv|
| 2    | Run a virtual environment  | .\venv\scripts\activate.bat |source .\venv\bin\activate|
| 3    | See the packages  | pip freeze |pip freeze|
| 4    | Save them to a file  | pip freeze > requirements.txt |pip freeze > requirements.txt|
| 5    | Load packages  | pip install - r requirements.txt |pip install - r requirements.txt|
| 6    | Exit  | deactivate |deactivate|
| 7    | Add /venv to .gitignore file  |  | |

### Requirements.txt
Here is a list of the packages needed to run this application. If mysql-connector-python is not installed on your machine you can install it using *pip install mysql-connector-python*

click==7.1.2 , Flask==1.1.2 , itsdangerous==1.1.0 , Jinja2==2.11.2, MarkupSafe==1.1.1, mysql-connector-python==8.0.22, protobuf==3.14.0, six==1.15.0, Werkzeug==1.0.1

### Set Up Flask Server [2]
| Step |      Task                | Windows |Mac / Linux|
|------|---------------------------|---------|------|
| 1    | change directory to venv  |  | |
| 2    | set environmental variables  | SET FLASK_APP=server|export FLASK_APP=server |
| 3    | set DEBUG MODE   | export FLASK_ENV=development |export FLASK_DEBUG=1 |
| 4    | run flask server   | flask run |flask run |


### Running Web App - Open Orders Management System
| Step |      Task                | Instructions |
|------|---------------------------|---------|
| 1    | open web app on local host   | http://127.0.0.1:5000/ |
| 2    | home page   | click on the login button   |
| 3    | Login   | enter username = admin & password = admin and click on login button   |
| 4    | Create New Order   | click on Create Button, then complete the form and click on create button or back button. Then refresh your browser to see the new order |
| 5    | Get Latest USD_EUR_FXRATE   |click on Latest USD_EUR_FXRATE button to display latest fx rate and date of last update |
| 6    | Update USD_EUR_FXRATE   |click on Update USD_EUR_FXRATE button to update the table, refresh your browser to see the updated table |
| 7    | Update   |click on Update button, then edit the order details in the form and click the update button to update the table, refresh your browser to see the updated row |
| 8    | Delete   |click on delete button to delete the order from the table, refresh your browser to see the updated table |
| 9    | Add / Update Customer   |click on Add / Update Customer button to open Customer List screen, where you can create / update or delete a customer, when finished refresh your browser to see the updated table |
| 10    | Open Orders   |click on Open Orders button to return to Open Orders Management System|
| 11    | Logout   |click on Logout button to end session|

### Running Web App on Pythonanywhere
| Step |      Task                | Windows |Mac / Linux|
|------|---------------------------|---------|------|
| 1    | open web app on host  |http://paulcaulfield.pythonanywhere.com/index.html  | |

## License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
- **[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)**

### References
[1] Beatty, A., “DR8.1 Virtual Environment ,”
2020, [Online; accessed 27-December-2020]. [Online]. Available: https://web.microsoftstream.com/video/bc3af8e1-2709-4caa-9af2-dd9510919a37?list=studio
[2] Beatty, A., “DR8.2 Flask clean ,”
2020, [Online; accessed 27-December-2020]. [Online]. Available: https://web.microsoftstream.com/video/a7d9ea86-c2f4-4104-888a-569b4a391808?list=studio
[3] Vain, M., “Foreign exchange rates API with currency conversion ,”
2017, [Online; accessed 27-December-2020]. [Online]. Available: https://exchangeratesapi.io/
[4] Github, “Cloning a repository ,”
2020, [Online; accessed 27-December-2020]. [Online]. Available: https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository
## Contact

Paul Caulfield -  paul.caulfield@se.com & g00376342@gmit.ie



