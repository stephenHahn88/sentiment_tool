from flask import Flask, request, send_file
from pymongo import MongoClient

from ENV_VARIABLE import password
from gather_frontend_data import getJSONTransitionMatrices

app = Flask(__name__)

# client = MongoClient('localhost', 27017)
client = MongoClient("mongodb+srv://bob:{password}@hahnmusic.lcqyy3z.mongodb.net/?retryWrites=true&w=majority")

choiceToPath = {
  "1": "src/media/Schubert_D911-01_HU33.wav",
  "2": "src/media/Schubert_D911-02_HU33.wav",
  "3": "src/media/Schubert_D911-03_HU33.wav",
  "4": "src/media/Schubert_D911-04_HU33.wav",
  "5": "src/media/Schubert_D911-05_HU33.wav",
  "6": "src/media/Schubert_D911-06_HU33.wav",
  "7": "src/media/Schubert_D911-07_HU33.wav",
  "8": "src/media/Schubert_D911-08_HU33.wav",
  "9": "src/media/Schubert_D911-09_HU33.wav",
  "10": "src/media/Schubert_D911-10_HU33.wav",
  "11": "src/media/Schubert_D911-11_HU33.wav",
  "12": "src/media/Schubert_D911-12_HU33.wav",
  "13": "src/media/Schubert_D911-13_HU33.wav",
  "14": "src/media/Schubert_D911-14_HU33.wav",
  "15": "src/media/Schubert_D911-15_HU33.wav",
  "16": "src/media/Schubert_D911-16_HU33.wav",
  "17": "src/media/Schubert_D911-17_HU33.wav",
  "18": "src/media/Schubert_D911-18_HU33.wav",
  "19": "src/media/Schubert_D911-19_HU33.wav",
  "20": "src/media/Schubert_D911-20_HU33.wav",
  "21": "src/media/Schubert_D911-21_HU33.wav",
  "22": "src/media/Schubert_D911-22_HU33.wav",
  "23": "src/media/Schubert_D911-23_HU33.wav",
  "24": "src/media/Schubert_D911-24_HU33.wav"
}

transition_matrix_json = getJSONTransitionMatrices()

@app.route("/api/analyses")
def getAnalyses():
    db = client["sentiment"]
    analyses = db["analyses"]
    allAnalyses = analyses.find()
    allAnalyses = list(allAnalyses)
    if len(allAnalyses) == 0:
        return {"status": 404, "result": "No analyses found"}
    for analysis in allAnalyses:
        analysis["_id"] = str(analysis["_id"])
    return {"status": 200, "analyses": allAnalyses}


@app.route("/api/song-analyses/<songNumber>")
def getSongAnalyses(songNumber: str):
    db = client["sentiment"]
    analyses = db["analyses"]
    allAnalyses = analyses.find(
        {
            "piece": choiceToPath[songNumber]
        }
    )
    allAnalyses = list(allAnalyses)
    if len(allAnalyses) == 0:
        return {"status": 404, "result": "No analyses found"}
    for analysis in allAnalyses:
        analysis["_id"] = str(analysis["_id"])
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