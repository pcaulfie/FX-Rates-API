from flask import Flask, url_for, request, redirect, abort, jsonify
from OrdersDao import ordersDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return "hello"

#get all

@app.route('/orders')
def getAll():
    return jsonify(ordersDao.getAll())

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

#update
# curl -X PUT -d "{\"USD_EUR_FXRATE\":1.33333}" -H Content-Type:application/json http://127.0.0.1:5000/orders

@app.route('/orders', methods=['PUT'])
def update(): 
    rates = {
        "USD_EUR_FXRATE": request.json["USD_EUR_FXRATE"]
    }
    #ordersDao.update(rates)
    
    return jsonify(ordersDao.update(rates))

#delete
# curl -X DELETE http://127.0.0.1:5000/orders/14

@app.route('/orders/<int:ID>', methods=['DELETE'])
def delete(ID):
    ordersDao.delete(ID)

    return jsonify({"done":True})

if __name__ == "__main__":
    app.run(debug=True)