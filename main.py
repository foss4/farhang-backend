from sanic import Sanic
from settings import DEBUG, HOST, PORT, ACCESS_LOG
from dictionary.urls import dic_bp_v1

app = Sanic(__name__)
app.blueprint(dic_bp_v1)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG, access_log=ACCESS_LOG)
