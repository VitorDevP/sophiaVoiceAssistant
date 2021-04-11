from tools.load import loadFile
from actions.assistant import assistantInfo
loadModel = loadFile('models/dictionary.json')

def intent():
    response = assistantInfo.name()
    return response

def callActions():
    return [loadModel['assistant']['inputs'], intent()]
