from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class ExplanationArticleRatingPage1(Page):
    form_model = "player"
    form_fields = ["ratingPreview1",
                   "ratingPreview2",
                   "ratingPreview3",
                   "ratingPreview13",
                   "ratingPreview14",
                   "ratingPreview15"]
    def is_displayed(self):
        return self.participant.vars["searchResultsPackage"] == 1

class ExplanationArticleRatingPage2(Page):
    form_model = "player"
    form_fields = ["ratingPreview4",
                   "ratingPreview5",
                   "ratingPreview6",
                   "ratingPreview16",
                   "ratingPreview17",
                   "ratingPreview18"]
    def is_displayed(self):
        return self.participant.vars["searchResultsPackage"] == 2

class ExplanationArticleRatingPage3(Page):
    form_model = "player"
    form_fields = ["ratingPreview7",
                   "ratingPreview8",
                   "ratingPreview9",
                   "ratingPreview19",
                   "ratingPreview20",
                   "ratingPreview21"]
    def is_displayed(self):
        return self.participant.vars["searchResultsPackage"] == 3

class ExplanationArticleRatingPage4(Page):
    form_model = "player"
    form_fields = ["ratingPreview10",
                   "ratingPreview11",
                   "ratingPreview12",
                   "ratingPreview22",
                   "ratingPreview23",
                   "ratingPreview24"]    
    def is_displayed(self):
        return self.participant.vars["searchResultsPackage"] == 4


page_sequence = [ExplanationArticleRatingPage1,
                 ExplanationArticleRatingPage2,
                 ExplanationArticleRatingPage3,
                 ExplanationArticleRatingPage4]
