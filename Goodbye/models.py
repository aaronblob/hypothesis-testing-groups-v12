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
Simpsons Paradoxon
"""


class Constants(BaseConstants):
    name_in_url = 'Goodbye'
    players_per_group = 2
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Experiment fast abgeschlossen -> damit ich checken kann, wie lange jemand gebraucht hat
    timeEnded = models.FloatField()
    checkIfCodeIsXXX = models.LongStringField()

### Reward

    reward = models.IntegerField(label = "Welche Kompensation möchten Sie für die Teilnahme an der Studie erhalten?",
                                choices = [[1, "0,5 Versuchspersonenstunden"],[2, "4€ Amazon Gutschein"],[0, "Keine"]],
                                widget = widgets.RadioSelect)
    #studyInformation = models.BooleanField(label = "Möchten Sie weitere Informationen über den Studien-Zweck, die Forschungsfrage und das Design erhalten?",
                                           #choices = [[True, "Ja"], [False, "Nein"]])

    #timeEnded = models.IntegerField()

    #name = models.StringField(label = "Wie lautet Ihr Name (zur Ausstellung der Versuchspersonenstunde)?", initial = "", blank = True)

    #paypal = models.StringField(label = "Wie lautet Ihre Email-Adresse (für die PayPal-Überweisung)?", initial = "", blank = True)

    #email = models.StringField(label = "An welche Email-Adresse möchten Sie Informationen über die Studie geschickt bekommen?", blank = True)

    anmerkungen = models.LongStringField(initial="", blank=True)
