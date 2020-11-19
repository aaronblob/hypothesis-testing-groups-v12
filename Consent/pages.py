from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class Testpage(Page):
    form_model = "player"
    form_fields = [#"selectedSR"
    ]





class TestpageArticles(Page):
    # display page conditionally
    pass



class WelcomePage(Page):
    form_model = "player"
    form_fields = ["mobileVersion",
                   "prolific",
                   "prolificID",
                   "GermanMothertongueNiveau"]
    # display page conditionally

    def before_next_page(self):
        self.player.participant.vars["prolific"] = self.player.prolific

class EndByLanguage(Page):
    form_model = "player"

    def is_displayed(self):
        return self.player.GermanMothertongueNiveau == 2

class MobileEndPage(Page):
    form_model = "player"

    def is_displayed(self):
        return self.player.mobileVersion == 1



class ConsentPage(Page):
    form_model = "player"
    form_fields = ["consent"]

    # display page conditionally
    def is_displayed(self):
        return self.player.participant.vars["timeout"] == 0



class ConsentDeclinePage(Page):
    form_model = "player"
    form_fields = ["consentRefused"]

    # display only if consent is refused
    def is_displayed(self):
        return self.player.consent == False




class EndConsentPage(Page):
    form_model = "player"
    form_fields = []

    # display only if consent is refused
    def is_displayed(self):
        return self.player.consent == False



class StartDisclaimerPage(Page):
    form_model = "player"
    form_fields = []

    # display only if consent is accpeted
    def is_displayed(self):
        return self.player.consent == True



class PriorsPoliceBrutality(Page):
    form_model = "player"
    form_fields = ["berechtigungPriorsHypoPB",
                   "certaintyPriorsHypoPB"]

    # display only if consent is accpeted
    def is_displayed(self):
        return self.player.consent == True




class DefinitionPoliceBrutalityPage(Page):
    form_model = "player"
    form_fields = []

    # display only if consent is accpeted
    def is_displayed(self):
        return self.player.consent == True



class PriorsPage(Page):
    form_model = "player"
    form_fields = ["priorPB1",
                   "priorPB2",
                   "priorPB3",
                   "certaintyPriorsPB1",
                   "certaintyPriorsPB2",
                   "certaintyPriorsPB3"]

    # display only if consent is accpeted
    def is_displayed(self):
        return self.player.consent == True

    # create variable which can be checked on the waiting page
    def before_next_page(self):
        import time
        # this needs to be done on the last page prior to the WaitPage
        self.participant.vars["arrivalTime"] = time.time()

        # give participant a number so I can later display them the search-results to rate them
        if self.session.vars["nextPreviewRating"] < 5:
            self.participant.vars["searchResultsPackage"] = self.session.vars["nextPreviewRating"]
        else:
            self.session.vars["nextPreviewRating"] = 1
            self.participant.vars["searchResultsPackage"] = self.session.vars["nextPreviewRating"]


page_sequence = [#Testpage,# TestpageArticles,
                 WelcomePage,
                 EndByLanguage,
                 MobileEndPage,
                 ConsentPage,
                 ConsentDeclinePage,
                 EndConsentPage,
                 StartDisclaimerPage,
                 DefinitionPoliceBrutalityPage,
                 PriorsPoliceBrutality,
                 PriorsPage]
