from cloudbot import hook
import time

@hook.irc_raw("JOIN")
def join(message, nick, mask, notice, chan):
	noobs = ['Mibbit', 'webchat']
	if chan == "#cauldron":
                if any(x in mask for x in noobs):	
                        time.sleep(2)
                        message("Hello and welcome to #Cauldron IRC "+nick+". Please read http://cauldron.minecraftforge.net/threads/irc-guidelines.18/ BEFORE doing anything else")
                        message("Cauldron is dead don't ask about downloads, support isn't guaranteed")