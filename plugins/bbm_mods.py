from cloudbot import hook

@hook.command("ICBM")
def icbm(text, message):
    message("ICBM was taken over by DarkCow from calclavia");
    message("Downlaods can be found here http://builtbroken.com/pages/icbm/1.7/");
    message("1.6.4 is not supported");

@hook.command("VoltzEngine", "ve")
def ve(text, message):
    message("VoltzEngine is the core of every builtbroken mod.")
    message("No it is not named after Voltz the modpack.")
    message("Downloads can be found here http://builtbroken.com/pages/voltzengine/1.7/downloads.php")
    
@hook.command("MadScience", "ms")
def ms(text, message):
    message("MadScience is a mod made by Maxwolf.")
    message("The channel is #MadScience.")
    message("The 1.7.10 version is not public.")