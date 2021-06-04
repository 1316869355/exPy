# -*- coding: UTF-8 -*-

import uiautomator2 as u2
d = u2.connect_usb('a89496937d28')
print(d.info)
#d.wakup()
screen_status = d.info.get('screenOn')
print(screen_status)
if (screen_status):
    #d.screen_off()
    d.press("home")
    #d.press(0x17, 0x02) # press keycode 0x07('0') with META ALT(0x02)
else:
    d.screen_on()
    d.unlock()
    

##d.screen.on()
#d.screen.off()
#d.sleep()
##d.wakeup()
##d.screen.
