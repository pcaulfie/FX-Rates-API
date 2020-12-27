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
1. Normalise databases using Foreign Key to ensure that open orders cannot be created for a customer if customer doesnt exist in customer table.
1. Display value of Open Orders in Euros using latest USDEUR FX Exchange rate which can be refreshed daily using 3rd Party API Interface. The open order value is stored in base currency which is US Dollar (USD) in the database. 

![Image of currency](staticpages/currency.jpg)


## Introduction
This repository contains my submission for the Tasks assessment for Machine Learning and Statistics in 2020.

The repository contains the following:
## Contents


| Part |      Title                | Description |Link|
|------|---------------------------|---------|------|
| 1    | server.py | A basic Flask server that has a REST API, (to perform CRUD operations) |https://github.com/pcaulfie/FX-Rates-API/blob/main/server.py|
| 2    | index.html | A web interface, using AJAX calls, to perform CRUD operations on orders table |https://github.com/pcaulfie/FX-Rates-API/blob/main/staticpages/index.html|
| 3    | customer.html | A web interface, using AJAX calls, to perform CRUD operations on orders table |https://github.com/pcaulfie/FX-Rates-API/blob/main/staticpages/customer.html|
| 1    | initdb.sql | A file containing the mysql commands used to create two tables in a mysql database |https://github.com/pcaulfie/FX-Rates-API/blob/main/initdb.sql|
| 1    | dbconfigtemplate | A file containing the configuration details needed to connect to the mysql database |https://github.com/pcaulfie/FX-Rates-API/blob/main/dbconfigtemplate.py|
| 1    | OrdersDao.py | A data access object (DAO) that provides an interface to the MYSQL database |https://github.com/pcaulfie/FX-Rates-API/blob/main/OrdersDao.py|
| 1    | TestOrdersDao.py | A file used to test the OrdersDao is working correctly before implementing it on a Flask server. |https://github.com/pcaulfie/FX-Rates-API/blob/main/TestOrdersDao.py|
| 1    | Requirements.txt | A file listing all packages needed to run the application |https://github.com/pcaulfie/FX-Rates-API/blob/main/requirements.txt|
| 1    |.gitignore | A file used to tell git which files are not needed to be added to the repository. |https://github.com/pcaulfie/FX-Rates-API/blob/main/.gitignore|

*Main Web App - Local Host*

1. Gitignore file
1. Licence
1. Readme

*Web App - Online Host*
1. Folder called deploytoazure which contains the files which will uploaded to Pythonanywhere
1. Internet shortcut to app hosted online on Pythonanywhere - http://paulcaulfield.pythonanywhere.com/index.html


* 3rd Party API Working Files*
1. 3rd Party API folder containing python programs used to investigate 2 3rd party API's and JSON output.
1. API file xxxxx

### How to Clone This Repository

1. Launch Cmder
1. Using cmder prompt, create a folder where you want to clone the repository - for example *cd folder/to/clone-into/*
1. Specify URL of the repository you want to clone using the following command: 
 * *git clone https://github.com/pcaulfie/FX-Rates-API*
 * This will download the project to a folder named after the Git repository ("FX-Rates-API" in this case). 
 * If you want a different folder name, simply specify it as the last parameter: *git clone https://github.com/pcaulfie/FX-Rates-API other-name*

## Installation

- I recommend that you install the [Anaconda](https://www.anaconda.com/distribution/) distribution of python which contains all the libraries used, as well as an instance of Jupyter notebook.
 - VENV
### Requirements
click==7.1.2
Flask==1.1.2
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
mysql-connector-python==8.0.22
protobuf==3.14.0
six==1.15.0
Werkzeug==1.0.1

### References
[1] Wikipedia contributors, “Chi-squared test — Wikipedia, the free encyclopedia,”
2020, [Online; accessed 1-November-2020]. [Online]. Available: https://en.wikipedia.
org/w/index.php?title=Chi-squared test&oldid=983024096


## License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
- **[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)**

## Contact

Paul Caulfield -  paul.caulfield@se.com & g00376342@gmit.ie



