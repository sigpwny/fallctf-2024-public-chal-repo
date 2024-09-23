from quart import Quart, send_file, request
import os

app = Quart(__name__)


@app.route('/image')
async def image():
    image_file = request.args.get('image_file', 'cat1.jpg')
    # ADVANCED FILTERS (100% FOOLPROOF)

    # filenames should not start with slashes
    image_file = image_file.lstrip('/')

    # filenames should not end in .txt, so chop it off the end if we see it
    if image_file.endswith('.txt'):
        image_file = image_file[:-4]

    # filenames should not contain the word 'flag'
    image_file = image_file.replace('flag', '')

    # we shouldn't allow the file name to contain '../'
    while '../' in image_file:
        image_file = image_file.replace('../', '')

    # hoomans are now only able to access cat images :DDD
    image_path = os.path.abspath(os.path.join('static/images/', image_file))
    if not os.path.exists(image_path):
        return f'File not found at {image_path}', 404
    return await send_file(image_path)


@app.route('/')
async def index():
    return await send_file('static/index.html')
