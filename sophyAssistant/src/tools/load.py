import json

def loadFile(filename):
    with open('./sophyAssistant/src/'+filename) as json_file:
        data = json.load(json_file)
        return data