import base64
from io import BytesIO, StringIO
import flask
import json
from PIL import Image

from flask import Flask

from matplotlib.figure import Figure

app = Flask(__name__)


def draw_plot(a):
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, a])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

@app.route('/')
def index():
    return flask.render_template('index3.html')

@app.route('/', methods=['POST'])
def index_post():
    inp = int(flask.request.form['text'])
    plot_data = draw_plot(inp)

    data = {"plot_data": plot_data}

    with open('./data/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)

    return flask.redirect("/plot")
    # return flask.render_template('index3.html')

@app.route('/plot')
def plot_display():
    f = open('./data/data.json')
    data = json.load(f)
    plot_data = data['plot_data']
    image_path = r'./static/images/plot.png'
    
    decoded_string = BytesIO(base64.b64decode(plot_data))
    image = Image.open(decoded_string)
    image.save(image_path)

    return flask.render_template('index3_plot.html', plot_image=image_path)
    # return f"<img src='data:image/png;base64,{plot_data}'/>"


@app.route('/plot', methods=['POST'])
def plot_back():
    return flask.redirect("/")