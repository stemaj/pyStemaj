import routing
from xbmc import Keyboard
from xbmcgui import ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory, setResolvedUrl

plugin = routing.Plugin()

class Film():
    def __init__(self, film, link, plot, poster):
        self.film = film
        self.link = link
        self.plot = plot
        self.poster = poster

def tastaturEingabe() -> str:
    keyb = Keyboard()
    keyb.doModal()
    if keyb.isConfirmed():
        return keyb.getText()
    else:
        return ''

def fuelleGuiMitListeVonFilmen(arr) -> []:
    for x in arr:
        listItem = ListItem(label=x.film)
        listItem.setArt({'poster':x.poster})
        listItem.setInfo('video',infoLabels={ 'plot': x.plot })
        listItem.setProperty('IsPlayable', 'true')
        addDirectoryItem(plugin.handle, plugin.url_for(play_video, x.link), listItem)
    endOfDirectory(plugin.handle)

def spieleVideo(videoUrl):
    play_item = ListItem(path=videoUrl)
    play_item.setProperty('IsPlayable', 'true')
    setResolvedUrl(plugin.handle, True, listitem=play_item)
