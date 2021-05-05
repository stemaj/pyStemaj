from xbmc import Keyboard
from xbmcgui import ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory, setResolvedUrl

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
