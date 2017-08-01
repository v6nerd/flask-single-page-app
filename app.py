import time
import requests
import requests_cache

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


requests_cache.install_cache('crowdstrike_cache', backend='sqlite', expire_after=43200)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        #Inputs
        ip = request.args.get('ip')
	domain = request.args.get('domain')
	hash = request.args.get('hash')
	email = request.args.get('email')

	#API calls (if not in cache)
	now = time.ctime(int(time.time()))
        api_url_ip = "https://www.threatcrowd.org/searchApi/v2/ip/report/?ip={0}".format(ip)
        api_url_domain = "https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={0}".format(domain)
	api_url_hash = "https://www.threatcrowd.org/searchApi/v2/file/report/?resource={0}".format(hash)
	api_url_email = "https://www.threatcrowd.org/searchApi/v2/email/report/?email={0}".format(email)
	if ip:
        	response = requests.get(api_url_ip)
        	print("Time: {0} / Used Cache: {1}".format(now, response.from_cache))
	elif domain:
		response = requests.get(api_url_domain)
		print("Time: {0} / Used Cache: {1}".format(now, response.from_cache))
	elif hash:
		response = requests.get(api_url_hash)
		print("Time: {0} / Used Cache: {1}".format(now, response.from_cache))
	elif email:
		response = requests.get(api_url_email)
                print("Time: {0} / Used Cache: {1}".format(now, response.from_cache))

	# return json
    	return jsonify(response.json())

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)
