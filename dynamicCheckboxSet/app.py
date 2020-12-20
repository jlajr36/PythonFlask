from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/updatePage', methods=['GET','POST'])
def moredata():
    if request.method == 'POST':
        pageData = request.form
        pageData = str(pageData)

        jsonOut = "{"

        gtFlag = "Greentext:"
        locGt = pageData.find(gtFlag)
        endGt = pageData.find(",",locGt)
        gtState = pageData[locGt+len(gtFlag):endGt]

        jsonOut = jsonOut + "\"" + gtFlag[:-1] + "\":" + "\"" + gtState + "\","
        
        btFlag = "Bluetext:"
        locBt = pageData.find(btFlag)
        endBt = pageData.find(",",locBt)
        btState = pageData[locBt+len(btFlag):endBt]

        jsonOut = jsonOut + "\"" + btFlag[:-1] + "\":" + "\"" + btState + "\","

        rtFlag = "Redtext:"
        locRt = pageData.find(rtFlag)
        endRt = pageData.find(",",locRt)
        rtState = pageData[locRt+len(rtFlag):endRt]

        jsonOut = jsonOut + "\"" + rtFlag[:-1] + "\":" + "\"" + rtState + "\","

        ytFlag = "Yellowtext:"
        locYt = pageData.find(ytFlag)
        endYt = pageData.find(",",locYt)
        ytState = pageData[locYt+len(ytFlag):endYt]
        ytState = ytState[:-1]

        jsonOut = jsonOut + "\"" + ytFlag[:-1] + "\":" + "\"" + ytState + "\"}"

        return jsonOut

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)