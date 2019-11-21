from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
import json
# import RPi.GPIO as GPIO

app = Flask(__name__)
api = Api(app)

#Define Light Actuator GPIOs
redLight = 13
greenLight = 17
yellowLight = 19
blueLight = 27
allChannel = 99

#Define Command for each channel
commandRedLightOn = ["hidupkan lampu merah", "lampu merah on", "nyalakan lampu merah"]
commandGreenLightOn = ["hidupkan lampu hijau", "lampu hijau on", "nyalakan lampu hijau"]
commandYellowLightOn = ["hidupkan lampu kuning", "lampu kuning on", "nyalakan kuning merah"]
commandBlueLightOn = ["hidupkan lampu biru", "lampu biru on", "nyalakan lampu biru"]
commandAllChannelOn = ["hidupkan semua lampu", "semua lampu on", "nyalakan semua lampu"]

commandRedLightOff = ["matikan lampu merah", "lampu merah off"]
commandGreenLightOff = ["matikan lampu hijau", "lampu hijau off"]
commandYellowLightOff = ["matikan lampu kuning", "lampu kuning off"]
commandBlueLightOff = ["matikan lampu biru", "lampu biru off"]
commandAllChannelOff = ["matikan semua lampu", "semua lampu off"]

Setup GPIOs
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
	        	'isAllLightsOn' : True if redLightStatus == 1 and
	        	greenLightStatus == 1 and
	        	yellowLightStatus == 1 and
	        	blueLightStatus == 1 else  False,
	        }
        }
        return jsonify(data)

api.add_resource(ChannelStatus, '/channel_status')

def get_data(data):
	json_data = json.loads(data)
	print("Deserialized data: {}".format(data))
	return json_data

@app.route('/voice_command', methods = ["POST"])
def post():
	json_data = get_data(request.data)
	print(json_data)
	command = json_data["command"]
	message = ''

	if command in commandRedLightOn:
		on(redLight)
		message = 'Lampu merah sudah dinyalakan'
	elif command in commandGreenLightOn:
		on(greenLight)
		message = 'Lampu hijau sudah dinyalakan'
	elif command in commandYellowLightOn:
		on(yellowLight)
		message = 'Lampu kuning sudah dinyalakan'
	elif command in commandBlueLightOn:
		on(blueLight)
		message = 'Lampu biru sudah dinyalakan'
	elif command in commandAllChannelOn:
		on(redLight, greenLight, yellowLight, blueLight)
		message = 'Semua lampu sudah dinyalakan'
	elif command in commandRedLightOff:
		off(redLightStatus)
		message = 'Lampu merah sudah dimatikan'
	elif command in commandGreenLightOff:
		off(greenLight)
		message = 'Lampu hijau sudah dimatikan'
	elif command in commandYellowLightOff:
		off(yellowLight)
		message = 'Lampu kuning sudah dimatikan'
	elif command in commandBlueLightOff:
		off(blueLight)
		message = 'Lampu biru sudah dimatikan'
	elif command in commandAllChannelOff:
		off(redLight, greenLight, yellowLight, blueLight)
		message = 'Semua lampu sudah dimatikan'
	else:
		return jsonify({'status':300, 'message':'Perintah tidak dimengerti'})

	return jsonify({'status':200, 'message': message})

if __name__ == '__main__':
    app.run(debug=True, port=4040, host='0.0.0.0')
