# Importing some useful libraries
from textblob import TextBlob
from flask import Flask, request, jsonify

# App name
app = Flask(__name__)
# Creating a method 
@app.route("/analyse", methods=['POST','GET'])

# Creating a function named analyse_sentiment
def analyse_sentiment():

# Using request method getting json file
    sentence = request.get_json()['sentence']
# Using textblob library finding polarity 
    polarity = TextBlob(sentence).sentences[0].polarity
    es_blob = TextBlob(sentence).translate(to='zh-CN')
    return jsonify(     # returning the function
        sentence=sentence,
        spanishTranslation="{0}".format(es_blob),    # Use of .format method
        polarity=polarity
    )
# Run as a local host at 5000 port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)