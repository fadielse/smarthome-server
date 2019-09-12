from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
import json
import RPi.GPIO as GPIO

app = Flask(__name__)
api = Api(app)

#Define Light Actuator GPIOs
redLight = 13
greenLight = 17
yellowLight = 19
blueLight = 27
allChannel = 99

#Setup GPIOs
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(redLight, GPIO.OUT)
GPIO.setup(greenLight, GPIO.OUT)
GPIO.setup(yellowLight, GPIO.OUT)
GPIO.setup(blueLight, GPIO.OUT)

def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return
def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return

class ChannelStatus(Resource):
    def get(self):

        redLightStatus = GPIO.input(redLight)
        greenLightStatus = GPIO.input(greenLight)
        yellowLightStatus = GPIO.input(yellowLight)
        blueLightStatus = GPIO.input(blueLight)

        data = {
        	'data' : {
        		'lists' :  [
		        	{
		        		'name' : 'Lampu Merah',
			        	'channel' : redLight,
			        	'status' : redLightStatus,
			        },
			        {
			        	'name' : 'Lampu Hijau',
			        	'channel' : greenLight,
			        	'status' : greenLightStatus,
			        },
			        {
			        	'name' : 'Lampu Kuning',
			        	'channel' : yellowLight,
			        	'status' : yellowLightStatus,
			        },
			        {
			        	'name' : 'Lampu Biru',
			        	'channel' : blueLight,
			        	'status' : blueLightStatus,
			        },
	        	],
	        	'isAllLightsOn' : True if redLightStatus == 1 and greenLightStatus == 1 and yellowLightStatus == 1 and blueLightStatus == 1 else  False,
	        }
        }
        return jsonify(data)

api.add_resource(ChannelStatus, '/channel_status')

def get_data(data):
	json_data = json.loads(data)
	print("Deserialized data: {}".format(data))
	return json_data

@app.route('/channel_action', methods = ["POST"])
def post():
	json_data = get_data(request.data)
	print(json_data)
	channelNumber = int(json_data["channel"])
	light = redLight
	isOn = int(json_data["isOn"])
	message = ''

	if channelNumber == redLight:
		light = redLight
		message = 'Lampu merah sudah'
	elif channelNumber == greenLight:
		light = greenLight
		message = 'Lampu hijau sudah'
	elif channelNumber == yellowLight:
		light = yellowLight
		message = 'Lampu kuning sudah'
	elif channelNumber == blueLight:
		light = blueLight
		message = 'Lampu biru sudah'
	elif channelNumber == allChannel:
		light = (redLight, greenLight, yellowLight, blueLight)
		message = 'Semua lampu sudah'
	else:
		return jsonify({'status':300, 'message':'Lampu tidak ditemukan'})

	if isOn == 1:
		on(light)
		message = "%s dinyalakan" % (message)
	else:
		off(light)
		message =  "%s dimatikan" % (message)

	return jsonify({'status':200, 'message': message})

if __name__ == '__main__':
    app.run(debug=True, port=4040, host='0.0.0.0')
