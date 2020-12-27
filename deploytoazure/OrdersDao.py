import mysql.connector
from mysql.connector import cursor
import dbconfig as cfg

class OrdersDao:
    db = ""
    def initConnectToDB(self):
        db = mysql.connector.connect(
            host=       cfg.mysql['host'],
            user=       cfg.mysql['username'],
            password=   cfg.mysql['password'],
            database=   cfg.mysql['database'],
            pool_name='my_connection_pool',
            pool_size=10
        )
        return db

    def getConnection(self):
        db = mysql.connector.connect(
            pool_name='my_connection_pool'
        )
        return db

    def __init__(self): 
        db=self.initConnectToDB()
        db.close()

    def create(self, customer):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "insert into customer (CUSTOMER_NAME, ZONE) values (%s,%s)"
        values = [
            customer['CUSTOMER_NAME'],
            customer['ZONE'],           
        ]
        cursor.execute(sql, values)
        self.db.commit()
        lastRowId=cursor.lastrowid
        db.close()
        return lastRowId

    def create(self, orders):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "insert into orders (ORDER_NUMBER,CUSTOMER_NUMBER,PART,CURR_CODE,OPEN_QTY,UNIT_PRICE_USD,USD_EUR_FXRATE) values (%s,%s,%s,%s,%s,%s,%s)"
        values = [
            orders['ORDER_NUMBER'],
            orders['CUSTOMER_NUMBER'],
            orders['PART'],
            orders['CURR_CODE'],
            orders['OPEN_QTY'],
            orders['UNIT_PRICE_USD'],
            orders['USD_EUR_FXRATE']           
        ]
        cursor.execute(sql, values)
        self.db.commit()
        lastRowId=cursor.lastrowid
        db.close()
        return lastRowId

    def getAll(self):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'select * from orders'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        db.close()
        return returnArray

    def convertToDict(self, result):
        colnames = ['ID','ORDER_NUMBER','CUSTOMER_NUMBER','PART','CURR_CODE','OPEN_QTY','UNIT_PRICE_USD','USD_EUR_FXRATE']
        order = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                order[colName] = value
        return order

    def findById(self, ID):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'select * from orders where ID = %s'
        values = [ID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        order=self.convertToDictionary(result)
        db.close()
        return order

    def updateById(self, orders):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "update orders set ORDER_NUMBER = %s, CUSTOMER_NUMBER = %s, PART = %s, CURR_CODE = %s, OPEN_QTY = %s, UNIT_PRICE_USD = %s,USD_EUR_FXRATE = %s where ID = %s"
        values = [
            orders['ORDER_NUMBER'],
            orders['CUSTOMER_NUMBER'],
            orders['PART'],
            orders['CURR_CODE'],
            orders['OPEN_QTY'],
            orders['UNIT_PRICE_USD'],
            orders['USD_EUR_FXRATE'],      
            orders['ID']         
        ]
        cursor.execute(sql, values)
        self.db.commit()
        db.close()
        return orders

    def update(self, orders):
       db = self.getConnection()
       cursor = db.cursor()
       sql = "update orders set USD_EUR_FXRATE = %s"
       values = [
           orders['USD_EUR_FXRATE']
                  
       ]
       cursor.execute(sql, values)
       self.db.commit()
       db.close()
       return orders

    def delete(self, ID):
       db = self.getConnection()
       cursor = db.cursor()
       sql = 'delete from orders where ID = %s'
       values = [ID]
       cursor.execute(sql, values)
       self.db.commit()
       db.close()
       return {}

ordersDao = OrdersDao()    

    