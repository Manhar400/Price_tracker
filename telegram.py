import requests
def send_message(message):
    TOKEN = "5AERQ4AxaH42r8SXXXDX40T_ORkNEwqLWcMJjU"
    chat_id = ""
    send_text = message
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={send_text}"
    # url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    r = requests.get(url)
