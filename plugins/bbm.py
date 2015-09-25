from cloudbot import hook

bbmChannels = ["#bbm-bots","#bbm-dev","#builtbroken","#builtbrokenmodding","#bbm-packs","#icbm","#artillects "]

@hook.command("bbmstaff")
def bbmStaff(text, message, chan):
    if any(x in chan for x in bbmChannels):
            message("Owners: Dmodoomsirius, DarkGuardsman");
            #message("Texture Artist: Morton0000");
            message("Senior Developers: Kolatra")
            message("Junior Developers: TheCowGod, Hennamann")
    else:
            message("Command can only be run in Official BBM Channels. Join #bbm-bots to run the command.")



@hook.command("sponsor")
def sponsor(text, message, chan):
    if any(x in chan for x in bbmChannels):
            message("BuildBrokenModding servers both Beta test servers and build server");
            message("is sponsored by Akliz.");
            message("http://www.akliz.net/bbm")
    else:
            message("Command can only be run in Official BBM Channels. Join #bbm-bots to run the command.")
            
@hook.command("bbmchan")
def chans(text, message):
    message("The official BuiltBroken Channels are: " + " , ".join(bbmChannels))
    
@hook.command("bbmhelp")
def bbmhelp(text, message, bot):
    message("If you are looking for who is the staff type " + bot.config["connections"][0]["command_prefix"] + "bbmstaff")
    message ("if you are looking for our sponsors please type " + bot.config["connections"][0]["command_prefix"] + "sponsor")
    message("If you are looking for our official channels please do  " + bot.config["connections"][0]["command_prefix"] + "bbmchan")
