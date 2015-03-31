from cloudbot import hook

@hook.command("voltz")
def bbmVoltz(text, message, chan):
    if chan in ("#BBM-bots", "#BBM-Dev", "#BBM-Packs", "#BuiltBrokenModding", "#BuiltBroken"):
                message("Voltz for minecraft version 1.7.10 is in beta");
                message ("we are hoping to have a beta out sometime next month");
                return
    message("Command can only be run in Official BBM Channels. Join #bbm-bots to run the command.")

@hook.command("Ampz", "Ampzreloaded")
def bbmAmpzReloaded(text, message, chan):
    if chan in ("#BBM-bots", "#BBM-Dev", "#BBM-Packs", "#BuiltBrokenModding", "#BuiltBroken", "#dmodtest"):
                message("Ampz-reloaded is the new imporoved Ampz.")
                message("It is currently on hold.")
                return
    message("Command can only be run in Official BBM Channels. Join #bbm-bots to run the command.")

@hook.command("omhz")
def omhz(text, message, chan):
    if chan in ("#BBM-bots", "#BBM-Dev", "#BBM-Packs", "#BuiltBrokenModding", "#BuiltBroken"):
                message("currently on hold until Voltz is done.")
                return
    message("Command can only be run in Official BBM Channels. Join #bbm-bots to run the command.")
    
@hook.command("packs")
def bbmpacks(text, message, chan):
    if chan in ("#BBM-bots", "#BBM-Dev", "#BBM-Packs", "#BuiltBrokenModding", "#BuiltBroken"):
                message("For Voltz type .voltz")
                message("For AmpzReloaded info type either .Ampz or .Ampzreloaded")
                message("For omhz type .omhz")
                return
    message("Command can only be run in Official BBM Channels. Join #bbm-bots to run the command.")