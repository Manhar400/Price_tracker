
import requests

import pandas as pd
import math
import  telegram as tl
url = "https://www.amazon.in/Notebook-Display-i5-11300H-Graphics-Fingerprint/dp/B098XL8VSM"
headers = {
    "cookie": 'ubid-acbin=259-6144617-9158047; lc-acbin=en_IN; at-acbin=Atza|IwEBIAddlQSWTk73InyRC22Pspe6kgk-7lj4m2C4zFWqtrCqzhijDjp3XCPxE6-b_awRaFz4Ni5zPIQ5drIDPeGkNFibJDku3U3rbfKGzPutsMKBnRNiRVeS4RETTwMU2KEWXmHMzjs1RYL5Ify-_2PbxJOeCckaQ6G13wXzxDZNa23jS7RZjInJuWP00vfzrRnpOk2LNiibNHk9pNWRtF3ReDJI; sess-at-acbin="KfezVkSyvJzgxXPEVGMjwRXWeAuUNkcG/WRR9/Knnpc="; sst-acbin=Sst1|PQEKTGn93bZFWAjWZHogn4nzCal-J7gaNpT5GXEK9rjBfNIEWROwfF1kAj7DOFFGnMOrkhyr1A8REoRiBg8xIzqOiN3nP_bZwZD-39bZS_QNGvKGoQRkcGx3ei1CvWrGeQD6EhytJjwXgFzLwWZy1NouXeyJho0KiK3lu-re5xiIevoowiwqTsWztAoSztgFnDbsd9_CANLxMxdkE2KxtabAmCjOY-6zFHmwgBIZGuaCXy8yE_v-euuYSF7ABhi6_30G3sr1Y0atmdND8-7o3q5uZIyKFnndPh72PJINcVxxU3k; i18n-prefs=INR; session-id=260-7516670-1822033; session-token=STbT+5jG76cDwNrMKaZeheHsqdTDS4NhYi/e4iS1GIX3yxAbDAmwAyMiLiBYmgTmL3YvCpTck4WltsjIfrsrYLN87dsLBu8EqDNDoPZsHkU+6qvgELTq0vs+KDDsna+e6+umKnyXSl1sxWj7frS7Y8VKvwucRVYTBGX6gI114Dk8BRF5v/LYP4dYsRo4FXED; csm-hit=tb:DS01D3A728E9S5CYZTP8+s-Z8019N7E5MR3N8NHPV13|1648365794878&t:1648365794878&adb:adblk_yes; session-id-time=2082787201l',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
}
headers2 = {
    "Cookie": 'Network-Type=4g; T=TI164837592762300284068869835718313518936741634509592193001626865263; Network-Type=4g; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; pxcts=5d2684a8-adb6-11ec-be3b-737553665266; _pxvid=5d267b08-adb6-11ec-be3b-737553665266; s_cc=true; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19079%7CMCMID%7C61733043255833788141420135728755501871%7CMCAAMLH-1648980728%7C12%7CMCAAMB-1648980728%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1648383129s%7CNONE%7CMCAID%7CNONE; S=d1t12Pz8/cD8/Oz8/M0k/aHM/P/xYeZT5mAoJQ7ro5fatRcx9xyyYyl1ccvR6cxfcfFZUcDX9wKA9EJyet3Bjj6OmGQ==; s_sq=%5B%5BB%5D%5D; gpv_pn=Product%20Page; gpv_pn_t=FLIPKART%3AProduct%20Page; _px3=280350f8febdee9d27691b6b0f0e0966d07c6f5f47945069a0c4d85f27c9233c:Qw3CfB+iEBvRGGCjjzCL1eZuOLfB1w0J+3/uMCEO8oEYbxEz1dHU3ah25A6INfHEgys3f4A/6tW/rdM4CEiAyQ==:1000:zKJmASTWVMo4CobQTTKimjGaHj2+thW57lTmygsvLgtjraahtcagpT45Eh8yCrUW5EZoZIMGf1mMKENVyPL85X0yh9xIOAhFpWN29J99b3YL5xFuicOufKII9rEdr6GkGHzbpGwKx30wynpF844qlbYyB5CTigpP+boF1f6sZUDvaIRmB8hd546pVPQHiyey5INEeZ02bgzDY/wSEpg8gQ==; SN=VI541AF4644FA54DE4BA72F90FE3CA566E.TOKBEFDF945A44A4944AF0BEF967C386AFB.1648377261.LO',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
}

def amazon(url):
    r = requests.get(url ,headers = headers)
    tp = r.text
    indx = tp.find('<span class="a-offscreen">')
    return float(tp[indx:].split('<span class="a-offscreen">')[1].split("</span>")[0].replace("₹" ,"").replace("," ,""))

def flipkart(url):
    r  = requests.get(url ,headers = headers2)
    r = r.text
    r = r.split("₹")[2].split("</div>")[0].replace("," ,"")
    return float(r)


def send_alert(message):
    TOKEN = "5239284:AAERQ4AxaH42r8SDX40T_ORkNEwqLWcMJjU"
    chat_id = "794541"
    send_text = message
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={send_text}"
    # url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    r = requests.get(url)
df = pd.read_csv("list.csv")

for url ,target in zip(df.PRODUCT ,df.TARGET):
    current_price = math.inf
    if 'amazon' in url:
        current_price = amazon(url)
    if 'flipkart' in url:
        current_price = flipkart(url)
    if current_price <= target:
        message = "PRICE IS LESS THAN YOUR TARGET PRICE CURRENT PRICE->{} target was->{} {}".format(current_price ,target,url);
        tl.send_message(message)


