from random import *
import json

films=[]


def save():
    with open("films.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(films,ensure_ascii=False))
    print("РќР°С€Р° С„РёР»СЊРјРѕС‚РµРєР° Р±С‹Р»Р° СѓСЃРїРµС€РЅРѕ СЃРѕС…СЂР°РЅРµРЅР° РІ С„Р°Р№Р»Рµ films.json")

def load():
    global films
    with open("films.json","r",encoding="utf-8") as fh:
        films=json.load(fh)
    print("Р¤РёР»СЊРјРѕС‚РµРєР° Р±С‹Р»Р° СѓСЃРїРµС€РЅРѕ Р·Р°РіСЂСѓР¶РµРЅР°")   

try:
    load()
except:
    films.append("РњР°С‚СЂРёС†Р°")
    films.append("РЎРѕР»СЏСЂРёСЃ")
    films.append("Р’Р»Р°СЃС‚РµР»РёРЅ РєРѕР»РµС†")
    films.append("РўРµС…Р°СЃСЃРєР°СЏ СЂРµР·РЅСЏ Р±РµРЅР·РѕРїРёР»РѕР№")
    films.append("РЎР°РЅС‚Р° Р‘Р°СЂР±Р°СЂР°") 


while True:
    command=input("Р’РІРµРґРёС‚Рµ РєРѕРјР°РЅРґСѓ ")
    if command=="/start":
        print("Р‘РѕС‚-С„РёР»СЊРјРѕС‚РµРєР° РЅР°С‡Р°Р» СЃРІРѕСЋ СЂР°Р±РѕС‚Сѓ")
    elif command=="/stop":
        save()
        print("Р‘РѕС‚ РѕСЃС‚Р°РЅРѕРІРёР» СЃРІРѕСЋ СЂР°Р±РѕС‚Сѓ. Р—Р°С…РѕРґРёС‚Рµ РµС‰Рµ, Р±СѓРґРµРј СЂР°РґС‹!")
        break
    elif command=="/all":
        print("Р’РѕС‚ С‚РµРєСѓС‰РёР№ СЃРїРёСЃРѕРє С„РёР»СЊРјРѕРІ")
        print(films)
    elif command =="/add":
        f=input("Р’РІРµРґРёС‚Рµ РЅР°Р·РІР°РЅРёРµ С„РёР»СЊРјР° ")
        films.append(f)
        print("Р¤РёР»СЊРј Р±С‹Р» СѓСЃРїРµС€РЅРѕ РґРѕР±Р°РІР»РµРЅ РІ РєРѕР»Р»РµРєС†РёСЋ!")
    elif command=="/help":
        print("Р·РґРµСЃСЊ РєР°РєРѕР№-С‚Рѕ РјР°РЅСѓР»")
    elif command=="/delete":
        f=input("Р’РІРµРґРёС‚Рµ РЅР°Р·РІР°РЅРёРµ С„РёР»СЊРјР°, РєРѕС‚РѕСЂС‹Р№ РЅР°РґРѕ СѓРґР°Р»РёС‚СЊ ")
        '''
        if f in films:
            films.remove(f)
            print("Р¤РёР»СЊРј Р±С‹Р» СѓСЃРїРµС€РЅРѕ СѓРґР°Р»РµРЅ!")
        else:
            print("РўР°РєРѕРіРѕ С„РёР»СЊРјР° РЅРµС‚ РІ С„РёР»СЊРјРѕС‚РµРєРµ!")
        '''
        try:
            films.remove(f)
            print("Р¤РёР»СЊРј Р±С‹Р» СѓСЃРїРµС€РЅРѕ СѓРґР°Р»РµРЅ!")
        except:
            print("РўР°РєРѕРіРѕ С„РёР»СЊРјР° РЅРµС‚ РІ С„РёР»СЊРјРѕС‚РµРєРµ!")
    elif command=="/random":
       # rnd=randint(0,len(films)-1)
       # print("РЎР»РµРїРѕР№ Р¶СЂРµР±РёР№ РїРѕРєР°Р·Р°Р» РІР°Рј С„РёР»СЊРј -" + films[rnd])
       print("РЎР»РµРїРѕР№ Р¶СЂРµР±РёР№ РїРѕРєР°Р·Р°Р» РІР°Рј С„РёР»СЊРј -" + choice(films) )
    elif command =="/save":
        save()
    elif command=="/load":
        load()
    else:
        print("РќРµРѕРїРѕР·РЅР°РЅРЅР°СЏ РєРѕРјР°РЅРґР°. РџСЂРѕСЃСЊР±Р° РїРѕРіР»Р°РґРёС‚СЊ РјР°РЅСѓР»Р° С‡РµСЂРµР· /help")