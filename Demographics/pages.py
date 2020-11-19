from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class Demographics(Page):
    form_model = "player"
    form_fields = ["age",
                   "gender",
                   "education",
                   "student",
                   "executiveSelf",
                   "executiveOther",
                   "contactPoliceBrutality",
                   "violentProtester",
                   "politicalOrientation",
                   "GermanFluency",
                   "GermanMuttersprache"]

    def before_next_page(self):
        import random
        from operator import itemgetter

        if self.session.vars["nextPreviewRating"] == 1:
            self.participant.vars["searchResultsPackage"] = 1
            self.session.vars["nextPreviewRating"] += 1
            print("Preview: \n")
            print(self.participant.vars["searchResultsPackage"])
        elif self.session.vars["nextPreviewRating"] == 2:
            self.participant.vars["searchResultsPackage"] = 2
            self.session.vars["nextPreviewRating"] += 1
            print("Preview: \n")
            print(self.participant.vars["searchResultsPackage"])
        elif self.session.vars["nextPreviewRating"] == 3:
            self.participant.vars["searchResultsPackage"] = 3
            self.session.vars["nextPreviewRating"] += 1
            print("Preview: \n")
            print(self.participant.vars["searchResultsPackage"])
        else:
            self.participant.vars["searchResultsPackage"] = 4
            self.session.vars["nextPreviewRating"] = 1
            print("Preview: \n")
            print(self.participant.vars["searchResultsPackage"])



page_sequence = [Demographics]
