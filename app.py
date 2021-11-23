import flask
app = flask.Flask(__name__)

@app.route("/")
def index():
    data = {'items':['bottle','cup'],'count':{'bottle':1,'cup':2}}
    return data
if __name__ == '__main__':
    app.run(threaded=True)
