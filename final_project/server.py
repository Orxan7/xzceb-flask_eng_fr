import json

from flask import Flask, render_template, request

from machinetranslation.translator import frenchToEnglish as f2e, englishToFrench as e2f


app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    res = e2f(textToTranslate)
    return res

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    res = f2e(textToTranslate)
    return res

@app.route("/")
def renderIndexPage():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
