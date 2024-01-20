# This file is placed in the Public Domain.
#
# pylint: disable=C,R


"fleet"


from ..brokers import Fleet


def flt(event):
    try:
        event.reply(Fleet.objs[int(event.args[0])])
    except (IndexError, ValueError):
        event.reply(",".join(Fleet.objs))
