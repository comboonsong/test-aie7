import flask
app = flask.Flask(__name__)

@app.route("/")
def test():
    data = {'items':['bottle','cup'],'count':{'bottle':1,'cup':2}}
    print(data)
    return data

if __name__ == "__main__":
    test()
