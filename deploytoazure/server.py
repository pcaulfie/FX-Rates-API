from flask import Flask, url_for, request, redirect, abort, jsonify
from OrdersDao import ordersDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return "hello"

#get all orders
@app.route('/orders')
def getAll():
    return jsonify(ordersDao.getAll())
#get all customers
@app.route('/customer')
def getCust():
    return jsonify(ordersDao.getCust())

#find by ID
@app.route('/orders/<int:ID>')
def findById(ID):
    return jsonify(ordersDao.findById(ID))



# create
# curl -X POST -d "{\"ORDER_NUMBER\":45482, \"CUSTOMER_NUMBER\":2, \"PART\":\"ED800J\", \"CURR_CODE\":\"USD\", \"OPEN_QTY\":150, \"UNIT_PRICE_USD\":102.16, \"USD_EUR_FXRATE\":1.2128}" -H "content-type:application/json" http://127.0.0.1:5000/orders

@app.route('/orders', methods=['POST'])
def create():
   
    if not request.json:
        abort(400)

    order = {
        "ORDER_NUMBER": request.json["ORDER_NUMBER"],
        "CUSTOMER_NUMBER": request.json["CUSTOMER_NUMBER"],
        "PART": request.json["PART"],
        "CURR_CODE": request.json["CURR_CODE"],
        "OPEN_QTY": request.json["OPEN_QTY"],
        "UNIT_PRICE_USD": request.json["UNIT_PRICE_USD"],
        "USD_EUR_FXRATE": request.json["USD_EUR_FXRATE"]
    }
    return jsonify(ordersDao.create(order))

    return "served by Create "

# create customer
@app.route('/customer', methods=['POST'])
def createcust():
    customer = {
        "CUSTOMER_NAME": request.json["CUSTOMER_NAME"],
        "ZONE": request.json["ZONE"]        
    }
    return jsonify(ordersDao.createcust(customer))

#update
# curl -X PUT -d "{\"USD_EUR_FXRATE\":1.33333}" -H Content-Type:application/json http://127.0.0.1:5000/orders

@app.route('/orders', methods=['PUT'])
def update(): 
    rates = {
        "USD_EUR_FXRATE": request.json["USD_EUR_FXRATE"]
    }
    #ordersDao.update(rates)
    
    return jsonify(ordersDao.update(rates))

#updateById
# curl -X PUT -d "{\"ORDER_NUMBER\":45482, \"CUSTOMER_NUMBER\":2, \"PART\":\"ED800J\", \"CURR_CODE\":\"USD\", \"OPEN_QTY\":150, \"UNIT_PRICE_USD\":102.16, \"USD_EUR_FXRATE\":1.33333}" -H "content-type:application/json" http://127.0.0.1:5000/orders/3

@app.route('/orders/<int:ID>', methods=['PUT'])
def updateById(ID):
    foundOrder=ordersDao.findById(ID)
    print (foundOrder)
    if foundOrder == {}:
        return jsonify({}), 404
    currentOrder = foundOrder
    if 'ORDER_NUMBER' in request.json:
        currentOrder['ORDER_NUMBER'] = request.json['ORDER_NUMBER']
    if 'CUSTOMER_NUMBER' in request.json:
        currentOrder['CUSTOMER_NUMBER'] = request.json['CUSTOMER_NUMBER']
    if 'PART' in request.json:
        currentOrder['PART'] = request.json['PART']
    if 'CURR_CODE' in request.json:
        currentOrder['CURR_CODE'] = request.json['CURR_CODE']
    if 'OPEN_QTY' in request.json:
        currentOrder['OPEN_QTY'] = request.json['OPEN_QTY']
    if 'UNIT_PRICE_USD' in request.json:
        currentOrder['UNIT_PRICE_USD'] = request.json['UNIT_PRICE_USD']
    if 'USD_EUR_FXRATE' in request.json:
        currentOrder['USD_EUR_FXRATE'] = request.json['USD_EUR_FXRATE']
    
    ordersDao.updateById(currentOrder)
    
    return jsonify(currentOrder)


@app.route('/customer/<int:ID>', methods=['PUT'])
def updateCustId(ID):
    foundCust=ordersDao.findByCust(ID)
    # print (foundCust)
    if foundCust == {}:
        return jsonify({}), 404
    currentCust = foundCust
    if 'CUSTOMER_NAME' in request.json:
        currentCust['CUSTOMER_NAME'] = request.json['CUSTOMER_NAME']
    if 'ZONE' in request.json:
        currentCust['ZONE'] = request.json['ZONE']
        
    ordersDao.updateCustId(currentCust)
    
    return jsonify(currentCust)

#delete
# curl -X DELETE http://127.0.0.1:5000/orders/14

@app.route('/orders/<int:ID>', methods=['DELETE'])
def delete(ID):
    ordersDao.delete(ID)

    return jsonify({"done":True})

@app.route('/customer/<int:ID>', methods=['DELETE'])
def deleteCust(ID):    
    ordersDao.deleteCust(ID)

    return jsonify({"done":True})

if __name__ == "__main__":
    app.run(debug=True)