from OrdersDao import ordersDao
#print("ok")

cust = {
    'CUSTOMER_NAME': "S.A.S.",
    'ZONE': "CENTRAL AND EASTERN EUROPE ISRAEL"
}

order1 = {
    'ORDER_NUMBER': 44732,
    'CUSTOMER_NUMBER': 1,
    'PART':"ED650J",
    'CURR_CODE': "USD",
    'OPEN_QTY': 467,
    'UNIT_PRICE_USD':89.54,
    'USD_EUR_FXRATE':1.2128
}

order2 = {
    'ORDER_NUMBER': 45482,
    'CUSTOMER_NUMBER': 2,
    'PART':"ED650J",
    'CURR_CODE': "USD",
    'OPEN_QTY': 1400,
    'UNIT_PRICE_USD':89.54,
    'USD_EUR_FXRATE':1.2128
}

#rates = {
#    'USD_EUR_FXRATE':1.25252,
#    'CURR_CODE': 'USD'
#
#}
rates2 = {
    'USD_EUR_FXRATE':1.25252
    

}

#returnValue = ordersDao.create(cust)
#returnValue = ordersDao.create(order1)
#returnValue = ordersDao.getAll()
#print(returnValue)
#returnValue = ordersDao.findById(2)
#print("find By Id")
#print(returnValue)
#returnValue = ordersDao.update(rates2)
#print(returnValue)
returnValue = ordersDao.delete(14)
#print(returnValue)
#returnValue = ordersDao.getAll()
print(returnValue)