#Imports cloudbots hook
from cloudbot import hook

@hook.command("takingoff")
def takingoff(text, message):
    message(text +  " is taking off please be patient.")
    
@hook.command("praise")
def praise(text, message):
    message("All praise " + text +  " our lord and saviour.")
    
@hook.command("unpraise")
def unpraise(text, message):
    message("Don't praise. " + text +  " is satan.")
        
@hook.command("Riot")
def riot(text, message):
    message("༼ つ ◕_◕ ༽つ " + text +  " OR RIOT. ༼ つ ◕_◕ ༽つ")
