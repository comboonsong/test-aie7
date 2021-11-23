import flask
app = flask.Flask(__name__)

@app.route("/")
def test():
    data = {'items':['bottle','cup'],'count':{'bottle':1,'cup':2}}
    return data
