from flask import Flask, url_for, request, redirect, abort, jsonify, session, render_template
from OrdersDao import ordersDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')
app.secret_key = 'someSecrtetasdrgsadfgsdfg3ko'
site = 'http://127.0.0.1:5000/index.html'
#host= window.location.origin
#site = host+"/index.html",
@app.route('/')
def index():
    count=0
    count+=1

    if not 'counter' in session:
        session['counter'] =0
        print("new session")

    sessionCount=session['counter']
    sessionCount+=1
    session['counter']=sessionCount

    if not 'username' in session:
        return '<h1> Open Orders Management System - Login Page</h1> '+\
        '<button>'+\
            '<a href="'+url_for('login')+'">' +\
                'login' +\
            '</a>' +\
        '</button>'
    
    return 'welcome ' + session['username'] +\
        '<br><a href="'+url_for('logout')+'">logout</a>'
    

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['username'] = request.form['username']
            return redirect(site)
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

@app.route('/clear')
def clear():
    #session.clear()
    session.pop('counter',None)   

    return "done" 

#get all

@app.route('/orders')
def getAll():
    if not 'username' in session:
        abort(401)
    return jsonify(ordersDao.getAll())

#get all

@app.route('/customer')
def getCust():
    if not 'username' in session:
        abort(401)
    return jsonify(ordersDao.getCust())

#find by ID

@app.route('/orders/<int:ID>')
def findById(ID):
    if not 'username' in session:
        return redirect('login')
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
   
    if not request.json:
        abort(400)

    customer = {
        "CUSTOMER_NAME": request.json["CUSTOMER_NAME"],
        "ZONE": request.json["ZONE"]        
    }
    return jsonify(ordersDao.createcust(customer))


#update
# curl -X PUT -d "{\"USD_EUR_FXRATE\":1.33333}" -H Content-Type:application/json http://127.0.0.1:5000/orders

@app.route('/orders', methods=['PUT'])
def update():
    if not 'username' in session:
        return redirect('login') 
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
    if not 'username' in session:
        return redirect('login')
    ordersDao.delete(ID)

    return jsonify({"done":True})

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/customer/<int:ID>', methods=['DELETE'])
def deleteCust(ID):
    if not 'username' in session:
        return redirect('login')
    ordersDao.deleteCust(ID)

    return jsonify({"done":True})

if __name__ == "__main__":
    app.run(debug=True)