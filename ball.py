""" Ball 8 emulation """
from random import choice


class Ball(object):
    """ Ball 8 emulation class """
    answers = (
        _('It is certain'),
        _('It is decidedly so'),
        _('Without a doubt'),
        _('Yes - definitely'),
        _('You may rely on it'),
        _('As I see it, yes'),
        _('Most likely'),
        _('Outlook good'),
        _('Yes'),
        _('Signs point to yes'),
        _('Reply hazy, try again'),
        _('Ask again later'),
        _('Better not tell you now'),
        _('Cannot predict now'),
        _('Concentrate and ask again'),
        _('Don\'t count on it'),
        _('My reply is no'),
        _('My sources say no'),
        _('Outlook not so good'),
        _('Very doubtful'),
    )

    def shake(self):
        """ Shake ball and get random answer """
        return choice(self.answers)
