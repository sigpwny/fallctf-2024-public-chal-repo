from playwright.sync_api import sync_playwright
import tempfile
from pathlib import Path
from flask import Flask, request, send_file

app = Flask(__name__)

def screenshot(url, dir):
	fname = dir / 'screenshot.png'
	with sync_playwright() as p:
		browser = p.chromium.launch()
		page = browser.new_page()
		page.goto(url)
		page.screenshot(path=fname)
		browser.close()

	return fname


@app.route("/screenshot", methods=['POST', 'GET'])
def render_screenshot():
	url = request.json.get('url')
	with tempfile.TemporaryDirectory() as tmpdirname:
		tmp_dir = Path(tmpdirname)
		fname = screenshot(url, tmp_dir)
		return send_file(fname)

@app.route('/')
def index():
	print('rendering index')
	return app.send_static_file('index.html')

# thanks carl, now that it's HTML they can't read my notes
# I hate supermegacorp. supermegacorp (aka big pwny) forced me to take time out away from valuable eduational experiences at the university to make this challenge.

# fallctf{b2bssrfaas_1s_th3_n3w_ssrfaas}
# fallctf{last_second_b2b_ssrfaas_fix}

if __name__ == '__main__':
	app.run(threaded=True, port=1337, host="0.0.0.0")