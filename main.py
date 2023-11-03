import os
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from views import enable1, disable1, status, set_brightness, set_flash, set_potentiometer

# template_dir = os.path.abspath(os.path.dirname(__file__))
# app = Flask(__name__, template_folder=os.path.join(template_dir, 'templates'))
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
app.add_url_rule('/led_bin_ON', 'enable1', enable1, methods=['POST'])
app.add_url_rule('/led_bin_OFF', 'disable1', disable1, methods=['POST'])
app.add_url_rule('/get_status', 'status', status, methods=['POST'])
app.add_url_rule('/set_brightness', 'set_brightness', set_brightness, methods=['POST'])
app.add_url_rule('/set_flash', 'set_flash', set_flash, methods=['POST'])
app.add_url_rule('/set_potentiometer', 'set_potentiometer', set_potentiometer, methods=['POST'])


swaggerui_blueprint = get_swaggerui_blueprint(
    '/swagger',
    '/static/swagger.json',
    config={
        'app_name': "Flask Serial API"
    }
)


app.register_blueprint(swaggerui_blueprint)


if __name__ == "__main__":
    app.run(debug=True)
