from cloudbot import hook


def mode_cmd(mode, text, text_inp, chan, conn, notice):
    """ generic mode setting function """
    split = text_inp.split(" ")
    if split[0].startswith("#"):
        channel = split[0]
        target = split[1]
        notice("Attempting to {} {} in {}...".format(text, target, channel))
        conn.send("MODE {} {} {}".format(channel, mode, target))
    else:
        channel = chan
        target = split[0]
        notice("Attempting to {} {} in {}...".format(text, target, channel))
        conn.send("MODE {} {} {}".format(channel, mode, target))


def mode_cmd_no_target(mode, text, text_inp, chan, conn, notice):
    """ generic mode setting function without a target"""
    split = text_inp.split(" ")
    if split[0].startswith("#"):
        channel = split[0]
        notice("Attempting to {} {}...".format(text, channel))
        conn.send("MODE {} {}".format(channel, mode))
    else:
        channel = chan
        notice("Attempting to {} {}...".format(text, channel))
        conn.send("MODE {} {}".format(channel, mode))
        
@hook.command(permissions=["op_mute", "op"], autohelp=False)
def invite(text, conn, chan, notice):
    """[channel] - unmutes [channel], or in the caller's channel if no channel is specified"""
    mode_cmd_no_target("+I", "invite", text, chan, conn, notice)