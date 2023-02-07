from flask import Flask, request, send_file
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)


@app.route("/api/analyses")
def getAnalyses():
    db = client["sentiment"]
    analyses = db["analyses"]
    allAnalyses = analyses.find()
    allAnalyses = list(allAnalyses)
    if len(allAnalyses) == 0:
        return {"status": 404, "result": "No analyses found"}
    return {"status": 200, "analyses": allAnalyses}


@app.route("/api/analyses", methods=["POST"])
def postAnalyses():
    json = request.get_json()
    db = client["sentiment"]
    analyses = db["analyses"]
    analyses.insert_one({
        "piece": json["piece"],
        "analysis": json["analysis"],
        "comments": json["comments"],
        "custom_id": json["custom_id"]
    })
    return {"status": 200}


if __name__ == "__main__":
    app.run(port=8889, debug=True)