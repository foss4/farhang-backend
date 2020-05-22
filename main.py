import os

from sanic import Sanic

from dictionary.urls import dic_bp_v1

app = Sanic("YATIM")
dir_path = os.path.dirname(os.path.realpath(__file__)) + "/.env"
os.environ.setdefault("YATIM_SETTINGS", dir_path)
app.config.from_envvar('YATIM_SETTINGS')
app.blueprint(dic_bp_v1)

if __name__ == "__main__":
    app.run()
