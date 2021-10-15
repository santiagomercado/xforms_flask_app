from flask import Flask, request, send_from_directory, render_template, make_response
from flask_cors import CORS
from lxml import etree
from io import BytesIO

app = Flask(__name__, static_url_path='')
CORS(app)

@app.route("/", methods=['GET','POST'])
def index():
    # the submit button send the raw xml using a post method
    if request.method == 'POST':
        xml = etree.parse(BytesIO(request.get_data("utf-8")))
        print(etree.tostring(xml.getroot(),pretty_print=True).decode('utf-8'))
        return(request.get_data().decode("utf-8") + "sarasa")

    # serve the html with the xform
    if request.method == 'GET':
        template = render_template('dcc_form.xhtml')
        response = make_response(template)
        response.headers['Content-Type'] = 'text/xml'
        return response

@app.route("/xsltforms/<path:path>")
def serve_file(path):
    return send_from_directory('xsltforms-1.3/xsltforms', path)
