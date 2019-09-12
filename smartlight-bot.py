import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return
def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return

# Perintah untuk menggunakan pin board GPIO Raspberry Pi
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

redLight = 13
greenLight = 17
yellowLight = 19
blueLight = 27

# Pengaturan GPIO
GPIO.setup(redLight, GPIO.OUT)
GPIO.setup(greenLight, GPIO.OUT)
GPIO.setup(yellowLight, GPIO.OUT)
GPIO.setup(blueLight, GPIO.OUT)

GPIO.output(redLight, 1)
GPIO.output(greenLight, 1)
GPIO.output(yellowLight, 1)
GPIO.output(blueLight, 1)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command == 'redon':
      on(redLight)
      bot.sendMessage(chat_id, 'lampu merah sudah dinyalakan.')

    elif command == 'greenon':
      on(greenLight)
      bot.sendMessage(chat_id, 'lampu hijau sudah dinyalakan.')

    elif command == 'yellowon':
      on(yellowLight)
      bot.sendMessage(chat_id, 'lampu kuning sudah dinyalakan.')

    elif command == 'blueon':
      on(blueLight)
      bot.sendMessage(chat_id, 'lampu biru sudah dinyalakan.')

    elif command == 'redoff':
      off(redLight)
      bot.sendMessage(chat_id, 'lampu merah sudah dimatikan.')

    elif command == 'greenoff':
      off(greenLight)
      bot.sendMessage(chat_id, 'lampu hijau sudah dimatikan.')

    elif command ==  'yellowoff':
      off(yellowLight)
      bot.sendMessage(chat_id, 'lampu kuning sudah dimatikan.')

    elif command ==  'blueoff':
      off(blueLight)
      bot.sendMessage(chat_id, 'lampu biru sudah dimatikan.')

    elif command == 'alloff':
      off((redLight, greenLight, yellowLight, blueLight))
      bot.sendMessage(chat_id, 'semua lampu sudah dimatikan')

    elif command =='allon':
      on((redLight, greenLight, yellowLight, blueLight))
      bot.sendMessage(chat_id, 'semua lampu sudah dinyalakan')

    elif command =='/start':
      bot.sendMessage(chat_id, 'Siap menerima pesan Anda...')

    #elif command =='/help':
    #  bot.sendMessage(chat_id, '*Selamat datang di Smarthome Telegram \nKodingkita* \nDaftar perintah:\n*redon* untuk menyalakan lampu merah \n*greenon* untuk menyalakan lampu hijau\n*yellowon* untuk menyalakan lampu kuning\n*blueon* untuk menyalakan lampu biru\n*redoff* untuk mematikan lampu merah\n*greenoff* untuk mematikan lampu hijau\n*yellowoff* untuk mematikan lampu kuning\n*blueoff* untuk mematikan lampu biru\n*greenoff* untuk mematikan lampu merah\n*allon* untuk menyalakan semua lampu\n*alloff* untuk mematikan semua lampu', parse_mode= 'Markdown')

bot = telepot.Bot('YOUR KEY') # Ganti 'Bot Token' dengan kode token anda, misal bot = telepot.Bot('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9')
bot.message_loop(handle)
print('===============================================')
print('Selamat datang di Smarthome Telegram Kodingkita')
print('===============================================')
print(' ')
print('     + kirim pesan redon untuk menyalakan lampu merah')
print('     + kirim pesan greenon untuk menyalakan lampu hijau')
print('     + kirim pesan yellowon untuk menyalakan lampu')
print('     + kirim pesan blueon untuk menyalakan lampu')
print('     + kirim pesan redoff untuk menyalakan lampu')
print('     + kirim pesan greenoff untuk menyalakan lampu')
print('     + kirim pesan yellowoff untuk menyalakan lampu')
print('     + kirim pesan blueoff untuk menyalakan lampu')
print('     + kirim pesan allon untuk menyalakan semua lampu')
print('     + kirim pesan alloff untuk mematikan semua lampu')
print(' ')
print('Siap menerima pesan Anda...')

while 1:
     time.sleep(10)
