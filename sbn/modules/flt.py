# This file is placed in the Public Domain.
#
#


"fleet"


from ..brokers import Fleet


def flt(event):
    try:
        event.reply(Fleet.objs[int(event.args[0])])
    except: 
        event.reply(",".join(Fleet.objs))
