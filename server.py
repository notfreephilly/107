from flask import Flask, request
import json

app = Flask(__name__) #__name__ this  is using the  name of the folder

@app.get("/")
def home():
    return "Hello from Flask"

@app.get('/testing')
def test():
    return "hello from another page"

@app.get('/about')
def about():
    me = {'name': 'Philip'}
    return json.dumps(me)

@app.get('/blog')
def blog():
    return "this is a blog"

@app.get('/version')
def version():
    version =  {'name': 'megatron', 'version': '2.1', 'build': 'm3g@tR0NNN'}
    return json.dumps(version)


# read and write to server
products = []
@app.get('/api/products')
def get_products():
    return json.dumps(products)

@app.post('/api/products')
def save_products():
    # should save a new product
    product = request.get_json()
    print (product)
    # mock the save
    products.append(product)
    return json.dumps(product)


    


app.run(debug = True) # apply the changes on the code, live

# API / Endpoints
# transform json / convert json into an object again