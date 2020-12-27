# Project 2020 
## Course: Data Representation

* Student Name: Paul Caulfield
* Student No: G00376342

* Lecturer: Andrew Beatty

An assignment submitted in part fulfilment of the requirements of the Higher Diploma in Science - Data Analytics: 2020-2021, Galway Mayo Institute of Technology.
  * Submitted: 29th December 2020

## Project Overview
The objective of this project is as follows:
1. Create a web application to perform CRUD operations on two database tables 'Orders' and 'Customers'. 
* Local Host instance, requires user to login: username = admin & password = admin 
1. Normalise databases using Foreign Key to ensure that open orders cannot be created for a customer if customer doesnt exist in customer table.
1. Display value of Open Orders in Euros using latest USDEUR FX Exchange rate which can be refreshed daily using 3rd Party API Interface. The open order value is stored in base currency which is US Dollar (USD) in the database. 
1. Lite version of web application hosted on Pythonanywhere, enables CRUD operations on one database table 'Orders'. 

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

1. Launch Cmder
1. Using cmder prompt, create a folder where you want to clone the repository - for example *cd folder/to/clone-into/*
1. Specify URL of the repository you want to clone using the following command: 
 * *git clone https://github.com/pcaulfie/FX-Rates-API*
 * This will download the project to a folder named after the Git repository ("FX-Rates-API" in this case). 
 * If you want a different folder name, simply specify it as the last parameter: *git clone https://github.com/pcaulfie/FX-Rates-API other-name*

## Installation

- I recommend that you install the [Anaconda](https://www.anaconda.com/distribution/) distribution of python which contains all the libraries used, as well as an instance of Jupyter notebook.
 


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

click==7.1.2
Flask==1.1.2
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
mysql-connector-python==8.0.22
protobuf==3.14.0
six==1.15.0
Werkzeug==1.0.1

### Set Up Flask Server 
| Step |      Task                | Windows |Mac / Linux|
|------|---------------------------|---------|------|
| 1    | change directory to venv  |  | |
| 2    | set environmental variables  | SET FLASK_APP=server|export FLASK_APP=server |
| 3    | set DEBUG MODE   | export FLASK_ENV=development |export FLASK_DEBUG=1 |
| 4    | run flask server   | flask run |flask run |
| 4    | run flask server   | flask run |flask run |


## License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
- **[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)**

### References
[1] Beatty, A., “DR8.1 Virtual Environment ,”
2020, [Online; accessed 27-December-2020]. [Online]. Available: https://web.microsoftstream.com/video/bc3af8e1-2709-4caa-9af2-dd9510919a37?list=studio
[2] Beatty, A., “DR8.2 Flask clean ,”
2020, [Online; accessed 27-December-2020]. [Online]. Available: https://web.microsoftstream.com/video/a7d9ea86-c2f4-4104-888a-569b4a391808?list=studio

## Contact

Paul Caulfield -  paul.caulfield@se.com & g00376342@gmit.ie



