from actions.timedate import timeDate as timeDate
from tools.load import loadFile

loadModel = loadFile('models/dictionary.json')

def intent():
    response = timeDate.getDate()
    return response

def callActions():
    return [loadModel['time']['inputs'], intent()]
