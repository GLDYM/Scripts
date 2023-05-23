import re
import json



def list_output():
    jsonfile = open(r'./IconRendererOutput/minecraft.json', mode='r+', encoding='utf8')
    jsonlines = jsonfile.readlines()
    jsonfile.close()
    txt = open(r'./IconRendererOutput/minecraft.txt', mode='w+', encoding='utf8')
    txt2 = open(r'./IconRendererOutput/统计方块列表.txt', mode='w+', encoding='utf8')

    txtlines = ''''''
    txt2lines = ''''''

    for line in jsonlines:
        map = json.loads(line)
        if map["type"] == "Block":
            txtlines = txtlines + map["registerName"] + '\n'
            txt2lines = txt2lines + map["name"] + ' ' + map['englishName'] + '\n'
    txt.write(txtlines)
    txt.close()
    txt2.write(txt2lines)
    txt2.close()
    return None

def delete_function():
    txtfile = open(r'./IconRendererOutput/minecraft.txt', mode='r', encoding='utf8')
    global idlines
    idlines = txtfile.readlines()
    txtfile.close()    
    delfunctionfile = open(r'./PlaceBoard/data/place/functions/delete.mcfunction', mode='w+', encoding='utf8')

    functionlines = ''''''

    for id in idlines:
        if id != '':
            functionlines = functionlines + r'scoreboard objectives remove ' + id[10:]
    functionlines = functionlines + r'scoreboard objectives remove placeboard'

    delfunctionfile.write(functionlines)
    delfunctionfile.close()

    return None

def tick_function():
    tickfunctionfile = open(r'./PlaceBoard/data/place/functions/tick.mcfunction', mode='w+', encoding='utf8')

    functionlines = ''''''

    for id in idlines:
        if id != '':
            functionlines = functionlines + r'scoreboard players add @a[scores={' + id[10:-1] + '=1..}] placeboard 1' + '\n'
            functionlines = functionlines + r'scoreboard players set @a[scores={' + id[10:-1] + '=1..}] ' + id[10:-1] + ' 0' + '\n'

    tickfunctionfile.write(functionlines)
    tickfunctionfile.close()

    return None

def load_function():
    loadfunctionfile = open(r'./PlaceBoard/data/place/functions/load.mcfunction', mode='w+', encoding='utf8')

    functionlines = ''''''

    for id in idlines:
        if id != '':
            functionlines = functionlines + 'scoreboard objectives add ' + id[10:-1] + ' minecraft.used:minecraft.' + id[10:-1] + '\n'
    functionlines = functionlines + r'scoreboard objectives add placeboard dummy {"text":"建筑榜","color":"red"}' + '\n'
    functionlines = functionlines + r'scoreboard objectives setdisplay sidebar placeboard'

    loadfunctionfile.write(functionlines)
    loadfunctionfile.close

    return None


list_output()
delete_function()
tick_function()
load_function()    