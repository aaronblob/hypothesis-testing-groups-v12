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
    name_in_url = 'Consent'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    # list for codes which will be filled later
    codes = models.LongStringField()

    def creating_session(self):

        # get players to enter them later
        players = self.get_players()


        # give players labels
        # for p in players:
        #     p.participant.vars["label"] = "Teilnehmer*in {}".format(p.participant.id_in_session)
        self.group_randomly(fixed_id_in_group = True)


        # generate code list
        self.session.vars["codeList"] = []

        for p in players:
            p.participant.vars["selectedArticlesList"] = []
            p.participant.vars["timeout"] = 0


        # generate random code for player -------------------------------------
        import random
        from random import shuffle
        import string
        from operator import itemgetter


        for p in players:

            # define function for random code generation
            def random_string(stringLength = 8):
                letters = string.ascii_uppercase
                return "".join(random.choice(letters) for i in range(stringLength))

            # generatre random code
            randomString = random_string(8)

            # give random code to player
            p.participant.vars["generatedCode"] = randomString
            # attach code to code list in order to later check it
            self.session.vars["codeList"].append(randomString)
            # -----------------------------------------------------------------

        # shuffle code list to make it impossible to track code via entrance-time
        shuffle(self.session.vars["codeList"])
        # write to variable which is easily analyzable
        self.codes = str(self.session.vars["codeList"])



        # generate list for random and balanced groups -------------------------
        self.session.vars["groupConditionsList"] = [
            "hypPolBrut",
            "hypLegBrut"]
        # self.session.vars["groupConditionsShuffeld"] = random.shuffle(self.session.vars["groupConditionList"])
        self.session.vars["groupConditionCounter"] = 0
        # ---------------------------------------------------------------------




        # same for individuals in the singleplayer condition ------------------
        self.session.vars["singleplayerConditionsList"] = [
            "hypPolBrut",
            "hypLegBrut"
        ]
        # self.session.vars["conditionsShuffeldSingleplayer"] = random.shuffle(self.session.vars["singleplayerConditionList"])
        self.session.vars["conditionCounterSingleplayer"] = 0
        # ---------------------------------------------------------------------


        # list of articles group will receive, allowing for testing of pol brut hypothesis
        self.session.vars["articlesListPolBrut"] = [
            "Polizist schlägt Demonstranten ins Gesicht", "Szenen wie in Minneapolis", "Polizist*innen attackieren Demonstrierende", "Räumung eines Straßenzugs eskaliert",
            "Demonstration am Samstag: Gewalt durch Beamte", "Schwere Verletzungen nach Polizeieinsatz", "Fragwürdige Festnahmemethoden", "Neuer Videoausschnitt der Großdemonstration aufgetaucht",
            "Polizei treibt Demonstrierende in die Enge", "Friedliche Proteste von Polizei aufgelöst", "Video dokumentiert Polizeieinsatz", "Sitzblockade mit Pfefferspray aufgelöst"
            ]
        # list of articles group will receive, allowing for testing of leg brut hypothesis
        self.session.vars["articlesListLegBrut"] = [
            "Vermummte Demonstrierende festgesetzt", "Polizei setzt Wasserwerfer ein", "Eskalation verhindert", "Polizei setzt sich zur Wehr",
            "Polizei in Straßenkämpfe verwickelt", "Demonstration aufgelöst", "Polizei muss brutal reagieren", "Gewalt eskaliert bei Demonstration",
            "Wasserwerfer und Schlagstöcke kommen zum Einsatz", "Kontrolle nur mühsam erkämpft - Polizei setzt Gewalt ein", "Polizei-Reaktion auf Flaschenwürfe", "Polizeieinsatz am Samstag: Verletzte auf beiden Seiten"
            ]

        for p in players:
            p.participant.vars["shuffledArticlesListPolBrut"] = random.sample(self.session.vars["articlesListPolBrut"],12)
            p.participant.vars["shuffledArticlesListLegBrut"] = random.sample(self.session.vars["articlesListLegBrut"],12)


        # every participant should only rate six out of 24 preview search-results
        self.session.vars["nextPreviewRating"] = 1






class Group(BaseGroup):
    # def live_decision(self, data, x):
    #     if data == 1:
    #         return {0: "Ein*e Teilnehmer*in hat sich bereits entschieden"}
    #     elif data == 2:
    #         return {0: "Beide Teilnehmer*innen haben sich bereits entschieden"}
    #     else:
    #         pass

    pass

class Player(BasePlayer):

    prolific = models.IntegerField()

    #test = models.StringField(blank = True)
    codes = models.LongStringField()

    GermanMothertongueNiveau = models.IntegerField()

    # mobile version. If = 2 then get on page where you are forced to quit
    mobileVersion = models.IntegerField()

    # Consent
    consent = models.BooleanField(choices = [[True, "Ja"],
                                             [False, "Nein, ich beende die Studie jetzt (Dies ist können Sie nicht rückgängig machen)"]])
    consentRefused=models.LongStringField(blank=True)

    # Comprehension Questions
    priorPB1 = models.IntegerField()
    priorPB2 = models.IntegerField()
    priorPB3 = models.IntegerField()

    certaintyPriorsPB1 = models.IntegerField(initial=None)
    certaintyPriorsPB2 = models.IntegerField(initial=None)
    certaintyPriorsPB3 = models.IntegerField(initial=None)


    # problem with police brutality in Germany
    berechtigungPriorsHypoPB = models.IntegerField()
    certaintyPriorsHypoPB = models.IntegerField()

    # prolific id
    prolificID = models.StringField(blank = True)


    # Testing -------------------
    # groupDecision
    groupDecision = models.IntegerField()
