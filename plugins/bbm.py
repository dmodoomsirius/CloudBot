from cloudbot import hook


               
@hook.command("bbmstaff")
def bbmStaff(text, message, chan):
    if chan in ("#BBM-bots", "#BBM-Dev", "#BBM-Packs", "#BuiltBrokenModding", "#BuiltBroken"):
                message("Owners: Dmodoomsirius, DarkGuardsman");
                message("textureArtist: Morton0000");
                message("Developers: Snow, Hennamann")
    message("Command can only be run in Official BBM Channels. Join #bbm-bots to run the command.")

    
    

@hook.command("sponsor")
def sponsor(text, message, chan):
    if chan in ("#BBM-bots", "#BBM-Dev", "#BBM-Packs", "#BuiltBrokenModding", "#BuiltBroken"):
                    message("BuiltBroken servers both Beta test servers and build server");
                    message("is sponsored by Akliz.");
                    message("http://www.akliz.net/bbm")
    message("Command can only be run in Official BBM Channels. Join #bbm-bots to run the command.")
