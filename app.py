import time
import requests
import requests_cache

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

requests_cache.install_cache('crowdstrike_cache', backend='sqlite', expire_after=42360)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        # user inputs
        ip = request.args.get('ip')
        #second = request.form.get('second')
        # api call
        url = "https://www.threatcrowd.org/searchApi/v2/ip/report/?ip={0}".format(ip)
        now = time.ctime(int(time.time()))
        response = requests.get(url)
        print("Time: {0} / Used Cache: {1}".format(now, response.from_cache))
        # return json
    return jsonify(response.json())
    #return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)
