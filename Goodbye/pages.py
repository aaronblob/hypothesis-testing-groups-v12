from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


### Testing ###


### App-Pages ###

class RewardPage(Page):
    form_model = "player"
    form_fields = ["reward"]

    # display if participant is from studienportal
    def is_displayed(self):
        return self.participant.vars["prolific"] == 2




class GoodbyePageVPN(Page):
    form_model = "player"
    form_fields = []

    # display page conditionally
    def is_displayed(self):
        return self.player.reward == 1 and self.participant.vars["prolific"] == 2




class GoodbyePageMoney(Page):
    form_model = "player"
    form_fields = []

    # timeout
    #timeout_seconds = 1200

    def is_displayed(self):
        return self.player.reward == 2 and self.participant.vars["prolific"] == 2


class GoodbyePageNothing(Page):
    form_model = "player"
    form_fields = []

    # timeout
    #timeout_seconds = 1200

    def is_displayed(self):
        return self.player.reward == 0 and self.participant.vars["prolific"] == 2



class VorletztePage(Page):
    form_model = "player"
    form_fields = ["anmerkungen"]



class LastPage(Page):
    form_model = "player"

    # display if participant is from studienportal
    def is_displayed(self):
        return self.participant.vars["prolific"] == 1


class Debriefing(Page):
    form_model = "player"



### Page sequence ###
page_sequence = [Debriefing,
                 VorletztePage,
                 RewardPage,
                 GoodbyePageVPN,
                 GoodbyePageMoney,
                 GoodbyePageNothing,
                 LastPage]
