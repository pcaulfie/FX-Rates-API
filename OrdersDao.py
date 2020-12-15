import mysql.connector
from mysql.connector import cursor

class OrdersDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user= 'root',
            password = 'root',
            database ='open_orders'
            # add configuration file instead of hardcoding the above
        )
        #print ("connection made")

    def create(self, customer):
        cursor = self.db.cursor()
        sql = "insert into customer (CUSTOMER_NAME, ZONE) values (%s,%s)"
        values = [
            customer['CUSTOMER_NAME'],
            customer['ZONE'],           
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def create(self, orders):
        cursor = self.db.cursor()
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
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from orders'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

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
        cursor = self.db.cursor()
        sql = 'select * from orders where ID = %s'
        values = [ID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)

    def findByCust(self, CUSTOMER_NUMBER):
        cursor = self.db.cursor()
        sql = 'select * from orders where CUSTOMER_NUMBER = %s'
        values = [ CUSTOMER_NUMBER ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)    

    #def update(self, orders):
    #   cursor = self.db.cursor()
    #   sql = "update orders set USD_EUR_FXRATE = %s where CURR_CODE = %s"
    #   values = [
    #       orders['USD_EUR_FXRATE'],
    #       orders['CURR_CODE']         
    #   ]
    #   cursor.execute(sql, values)
    #   self.db.commit()
    #   return orders

    def update(self, orders):
       cursor = self.db.cursor()
       sql = "update orders set USD_EUR_FXRATE = %s"
       values = [
           orders['USD_EUR_FXRATE']
                  
       ]
       cursor.execute(sql, values)
       self.db.commit()
       return orders

    def delete(self, ID):
       cursor = self.db.cursor()
       sql = 'delete from orders where ID = %s'
       values = [ID]
       cursor.execute(sql, values)
       
       return {}

ordersDao = OrdersDao()    

    