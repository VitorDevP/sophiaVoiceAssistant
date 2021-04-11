from actions.weather import weather as weather
from tools.load import loadFile

loadModel = loadFile('models/dictionary.json')

def intentWeather():
    response = weather.get()
    return response

def callActions():
    return [loadModel['weathers']['inputs'], intentWeather()]
