from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Hi!"

@app.route('/items')
def data1():
    #data = {'items':['bottle','cup'],'count':{'bottle':1,'cup':2}}
    items = {'items':['bottle','cup']}
    return jsonify(items)

@app.route('/count')
def data2():
    #data = {'items':['bottle','cup'],'count':{'bottle':1,'cup':2}}
    count = {'count': ['bottle=1','cup=2']}
    return jsonify(count)

if  __name__ == '__main__':
    app.run(threaded=True)
