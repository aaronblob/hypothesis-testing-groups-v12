from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Aaron Lob'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Article_Rating'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    ratingPreview1 = models.IntegerField()
    ratingPreview2 = models.IntegerField()
    ratingPreview3 = models.IntegerField()
    ratingPreview4 = models.IntegerField()
    ratingPreview5 = models.IntegerField()
    ratingPreview6 = models.IntegerField()
    ratingPreview7 = models.IntegerField()
    ratingPreview8 = models.IntegerField()
    ratingPreview9 = models.IntegerField()
    ratingPreview10 = models.IntegerField()
    ratingPreview11 = models.IntegerField()
    ratingPreview12 = models.IntegerField()
    ratingPreview13 = models.IntegerField()
    ratingPreview14 = models.IntegerField()
    ratingPreview15 = models.IntegerField()
    ratingPreview16 = models.IntegerField()
    ratingPreview17 = models.IntegerField()
    ratingPreview18 = models.IntegerField()
    ratingPreview19 = models.IntegerField()
    ratingPreview20 = models.IntegerField()
    ratingPreview21 = models.IntegerField()
    ratingPreview22 = models.IntegerField()
    ratingPreview23 = models.IntegerField()
    ratingPreview24 = models.IntegerField()
