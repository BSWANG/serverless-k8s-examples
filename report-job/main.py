from flask import Flask
from flask import request

app = Flask(__name__)
report_list = ["reports list"]


@app.route("/report", methods=['POST'])
def report():
    report_list.append(request.get_data())
    return ""


@app.route("/")
def list_report():
    return  "<table border='1'><tr><td>" + \
    reduce(
        lambda a,b : a + "</td></tr><tr><td>" + b,
        report_list
    ) + \
    "</td></tr></table>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80")

