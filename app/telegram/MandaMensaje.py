import requests
import sys

CHAT_ID  = '334128013'
BOT_TOKEN = '1103426072:AAGHww2-clH0Obv15Lwthbw2XplQwQux-mI'

def sendTextTelegram(mensaje):
    send_text = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&parse_mode=Markdown&text=%s' % (BOT_TOKEN, CHAT_ID, mensaje)
    response = requests.get(send_text)
    return response.json()
    

if __name__ == '__main__':
	mensaje = sys.argv[1]
	respuesta = sendTextTelegram(mensaje)
	print(respuesta)
