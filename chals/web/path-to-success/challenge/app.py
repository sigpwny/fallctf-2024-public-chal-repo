from quart import Quart, send_file, request
import os

app = Quart(__name__)


@app.route('/image')
async def image():
    image_path = os.path.abspath('static/images/' + request.args.get('image_file', 'cat1.jpg'))
    if not os.path.exists(image_path):
        return f'File not found at {image_path}', 404
    return await send_file(image_path)


@app.route('/')
async def index():
    return await send_file('static/index.html')
