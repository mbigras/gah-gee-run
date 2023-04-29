import os
import socket

import flask

app = flask.Flask(os.environ.get("APP", "gah-gee-run"))
app.config["ENV"] = os.environ.get("ENV", "")
app.config["TAG"] = os.environ.get("TAG", "")
app.config["FEATURES"] = os.environ.get("FEATURES", "")
app.config["SECRETS"] = os.environ.get("SECRETS", "")
app.config["ENTRYPOINT"] = os.environ.get("ENTRYPOINT", "")
app.config["ILLUSTRATIVE_ARGS"] = os.environ.get("ILLUSTRATIVE_ARGS", "")
app.json_provider_class.compact = False # see https://stackoverflow.com/questions/76134147/how-do-you-work-around-deprecated-prettyprint-regular-flask-setting/76134552#76134552
app.json.sort_keys = False

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def hello(path):
    return flask.jsonify(
        app=app.name,
        tag=app.config["TAG"],
        env=app.config["ENV"],
        features=app.config["FEATURES"],
        secrets=app.config["SECRETS"],
        entrypoint=app.config["ENTRYPOINT"],
        args=app.config["ILLUSTRATIVE_ARGS"],
        host=socket.gethostname(),
        path=path,
        params=flask.request.args,
    )
