# coding=UTF-8
import requests
import iftttkey
import _thread
import datetime
import time
def Kweather():
    """
    extract information from weather API
    high : high temp
    low : low temp
    text : rain or not
    """
    while True:
        hr = int(datetime.datetime.now().strftime("%H"))
        if hr == 23:
            from weather import Weather, Unit
            weather = Weather(unit=Unit.CELSIUS)
            lookup = weather.lookup_by_location('Taipei')
            condition = lookup.print_obj
            code = condition["item"]["forecast"][1]["text"]
            hightemp = condition["item"]["forecast"][1]["high"]
            lowtemp = condition["item"]["forecast"][1]["low"]
            
            print(hightemp,lowtemp,code)
            #Warning
            msg = ""
            if int(hightemp) > 32:
                msg = msg + "明天溫度: " + hightemp + " 早上可能會很熱哦, 敲鼻可以穿少一點 "
            if int(lowtemp) < 15:
                msg = msg + "明天溫度: " + lowtemp + " 會很冷哦, 敲鼻要記得多穿一點"
            if "Rain" in code or "Thunder" in code or "Showers" in code:
                msg = msg + "明天會下雨, 敲鼻記得帶傘"
            if msg != "":
                print(msg)
                SendMsg(msg)
            time.sleep(60*60)
    
def SendMsg(msg):
    
    url_ifttt = "https://maker.ifttt.com/trigger/stockLINE/with/key/"+iftttkey.key+"?value1="
    res1 = requests.get(url_ifttt+msg)
    
    return res1
    
if __name__ == "__main__":   
        
    _thread.start_new_thread(Kweather, ())
        