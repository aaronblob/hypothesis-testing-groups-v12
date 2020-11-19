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
    name_in_url = 'Demographics'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    # age
    age = models.IntegerField()
    # gender
    gender = models.IntegerField(blank=True) # 1 = w, 2 = m, 3 = d, blank = sonst
    # employment
    education = models.IntegerField() # 1 = Schule beendet ohne Abschluss, 2 = Noch Schüler, 3 = Volks- oder Hauptschulabschluss, 4 = Mittlere Reife, Realschul- oder gleichwertiger Abschluss, 5 = Abgeschlossene Lehre, 6 = Fachabitur, Fachhochschulreife, 7 = Abitur, Hochschulreife, 8 = Fachhochschul-/Hochschulabschluss
    student = models.IntegerField() # 1 = ja, 2 = nein

    subject = models.StringField(initial = None)

    politicalOrientation = models.IntegerField(initial = 0)

    executiveSelf = models.IntegerField()
    executiveOther = models.IntegerField()
    violentProtester = models.IntegerField()

    contactPoliceBrutality = models.IntegerField() # 1 = Ja Zeuge, 2 = Ja Opfer, 3 = Ja Zeuge u Opfer, 4 = Nein

    # Fluency in German
    GermanMuttersprache = models.IntegerField() # = 1 Ja, 2 = Nein
    GermanFluency = models.IntegerField() # 1 = sehr schlecht, 9 = sehr gut
