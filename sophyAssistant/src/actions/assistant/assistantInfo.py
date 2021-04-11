from tools.load import loadFile

loadModel = loadFile('config.json')

def name():
    return "my name is "+loadModel['assistant']['name']