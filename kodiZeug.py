from xbmc import Keyboard

def tastaturEingabe():
    keyb = Keyboard()
    keyb.doModal()
    if keyb.isConfirmed():
        return keyb.getText()
    else:
        return ''

