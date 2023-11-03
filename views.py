from flask import Flask, render_template, request
import serial

app = Flask(__name__)
ser = serial.Serial('/dev/tty.usbserial-1120', 9600, timeout=1)


@app.route('/led_bin_ON', methods=['POST'])
def enable1():
    ser.write('led_bin_ON'.encode())
    return 'LED is ON', 200


@app.route('/led_bin_OFF', methods=['POST'])
def disable1():
    ser.write('led_bin_OFF'.encode())
    return 'LED is OFF', 200


@app.route('/get_status', methods=['POST'])
def status():
    ser.write('get_status'.encode())
    return 'LEDS status', 200


@app.route('/set_brightness', methods=['POST'])
def set_brightness():
    brightness = request.args.get('value', type=int)
    if 0 <= brightness <= 65535:
        ser.write(f'set_brightness {brightness}'.encode())
        return 'Brightness set successfully', 200
    else:
        return 'Invalid brightness value', 400


@app.route('/set_flash', methods=['POST'])
def set_flash():
    flash_mode = request.args.get('value', default=None, type=str)
    if flash_mode.lower() == 'true':
        ser.write('flash_led_bin_ON'.encode())
    elif flash_mode.lower() == 'false':
        ser.write('flash_led_bin_OFF'.encode())
    else:
        return 'Invalid value for flashing mode', 400
    return 'Flashing mode updated successfully', 200


@app.route('/set_potentiometer', methods=['POST'])
def set_potentiometer():
    potentiometer_mode = request.args.get('value', default=None, type=str)
    if potentiometer_mode.lower() == 'true':
        ser.write('led_potentiometer_ON'.encode())
    elif potentiometer_mode.lower() == 'false':
        ser.write('led_potentiometer_OFF'.encode())
    else:
        return 'Invalid value for potentiometer control', 400
    return 'Potentiometer control updated successfully', 200


# @app.route('/input_page', methods=['GET', 'POST'])
# def input_page():
#     return render_template('input_page.html')
#
#
# @app.route('/send_command', methods=['POST'])
# def send_command():
#     command = request.form['command']
#     ser.write(command.encode())
#     response = ser.readline().decode().strip()
#     return f'Команда "{command}" отправлена. Ответ: {response}', 200
