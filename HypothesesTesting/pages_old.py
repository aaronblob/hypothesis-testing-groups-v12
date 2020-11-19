from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants




class MatchingWaitPage(WaitPage): # Achtung: Muss noch zur WaitPage gemacht werden!
    title_text = "Gleich geht es los!"
    body_text = "Bitte haben Sie ein wenig Geduld, Sie müssen noch kurz warten bis die anderen Teilnehmer*innen auch so weit sind. Bitte schließen oder minimieren Sie in keinem Fall das Browser-Fenster, sie warten maximal fünf Minuten (die Studiendauer von 30 Minuten verlängert sich hierdurch nicht, die Wartezeit ist mit einberechnet)!"

    # display page conditionally

    # group participants by arrival time
    group_by_arrival_time = True


    # global WaitPage-template
    template_name = "global/WaitPage.html"



class GroupHypothesisPickingPage(WaitPage):
    def is_displayed(self):
        return self.player.singleplayer == 0



    # as soon as enough players are here they get assigned to conditions
    after_all_players_arrive = "condition_picker"

    # global WaitPage-template
    template_name = "global/WaitPage.html"




class GroupExperimentExplanationPage(Page):
    form_model = "player"
    form_fields = []

    # display page conditionally
    def is_displayed(self):
        return self.player.singleplayer == 0




class SingleplayerExperimentExplanationPage(Page):
    form_model = "player"
    form_fields = []

    # display page conditionally
    def is_displayed(self):
        return self.player.singleplayer == 1

    def before_next_page(self):
        import random
        from operator import itemgetter
        # pick a condition for the singleplayer -------------------------------
        if self.session.vars["conditionCounterSingleplayer"] == 0:
            pickedCondition=itemgetter(0)(self.session.vars["singleplayerConditionsList"])
            self.session.vars["conditionCounterSingleplayer"]+=1
        else:
            pickedCondition=itemgetter(1)(self.session.vars["singleplayerConditionsList"])
            self.session.vars["conditionCounterSingleplayer"]=0
            random.shuffle(self.session.vars["singleplayerConditionsList"])
        # assign to player
        self.player.conditionHypothesis = pickedCondition
        print(pickedCondition)
        # ---------------------------------------------------------------------



class HypothesisPolBrutPage(Page):
    form_model = "player"
    form_fields = []
    # display page conditionally
    def is_displayed(self):
        return self.player.conditionHypothesis == "hypPolBrut"



class HypothesisLegBrutPage(Page):
    form_model = "player"
    form_fields = []
    # display page conditionally
    def is_displayed(self):
        return self.player.conditionHypothesis == "hypLegBrut"




class InitialArticlePage(Page):
    # display page conditionally
    pass



class FamiliarizeWithChatPage(Page):
    timeout_seconds = 60



class WaitBeforeFamiliarizePage(WaitPage):
    title_text = "Gleich geht es weiter!"
    body_text = "Bitte haben Sie ein wenig Geduld, Sie müssen noch kurz warten bis die anderen Teilnehmer*innen auch so weit sind. Bitte schließen oder minimieren Sie in keinem Fall das Browser-Fenster, sie warten maximal fünf Minuten (die Studiendauer von 30 Minuten verlängert sich hierdurch nicht)!"

    # global WaitPage-template
    template_name = "global/WaitPage.html"


class InstructionReminderPage(Page):
    form_model = "player"



class WaitBeforeChatPage(WaitPage):
    title_text = "Gleich geht es weiter!"
    body_text = "Bitte haben Sie ein wenig Geduld, Sie müssen noch kurz warten bis die anderen Teilnehmer*innen auch so weit sind. Bitte schließen oder minimieren Sie in keinem Fall das Browser-Fenster, sie warten maximal fünf Minuten (die Studiendauer von 30 Minuten verlängert sich hierdurch nicht)!"
    # display page conditionally

    # global WaitPage-template
    template_name = "global/WaitPage.html"

    # make articles to be shown ready
    after_all_players_arrive = "prepare_displayed_articles"




class ChatPage(Page): # ----------------------
    form_model = "player"
    form_fields = ["selectedArticle", "lastArticleChosenByTimeout"]
    # display page conditionally
    def is_displayed(self):
        return self.player.singleplayer == 0

    timer_text = 'Verbleibende Zeit:'

    #time-out
    timeout_seconds = 210
    def before_next_page(self):
        # if group can not decide in time
        if self.timeout_happened:
            # record that article was chosen by timeout
            if self.group.articleSelectionRound == 1:
                self.player.articleChosenByTimeout1 = 1
                self.player.lastArticleChosenByTimeout = 1
            elif self.group.articleSelectionRound == 2:
                self.player.articleChosenByTimeout2 = 1
                self.player.lastArticleChosenByTimeout = 1
            elif self.group.articleSelectionRound == 3:
                self.player.articleChosenByTimeout3 = 1
                self.player.lastArticleChosenByTimeout = 1
            elif self.group.articleSelectionRound == 4:
                self.player.articleChosenByTimeout4 = 1
                self.player.lastArticleChosenByTimeout = 1
            elif self.group.articleSelectionRound == 5:
                self.player.articleChosenByTimeout5 = 1
                self.player.lastArticleChosenByTimeout = 1
            elif self.group.articleSelectionRound == 6:
                self.player.articleChosenByTimeout6 = 1
                self.player.lastArticleChosenByTimeout = 1
            else:
                pass
        else:
            pass

    # live method
    live_method = 'live_decision'

# -----------------------------------------------------------------------------


class CheckArticleSelectionWaitPage1(WaitPage):
    title_text = "Bitte einen Moment Geduld!"
    body_text = "Ihre Gruppenmitglieder wählen gerade das Suchergebnis aus."

    def is_displayed(self):
        return self.player.singleplayer == 0

    after_all_players_arrive = "check_for_article_selection1"

    # global WaitPage-template
    template_name = "global/WaitPage.html"



class CheckArticleSelectionWaitPage2(WaitPage):
    title_text = "Bitte einen Moment Geduld!"
    body_text = "Ihre Gruppenmitglieder wählen gerade das Suchergebnis aus."

    def is_displayed(self):
        return self.player.singleplayer == 0 and self.player.disagreementArticle == 1

    after_all_players_arrive = "check_for_article_selection2"

    # global WaitPage-template
    template_name = "global/WaitPage.html"



class SelectArticleAfterDisagreementPage(Page):
    form_model = "player"
    form_fields = ["selectedArticle"]
    # display page conditionally
    def is_displayed(self):
        return self.player.singleplayer == 0 and self.player.disagreementArticle == 1

    timer_text = 'Verbleibende Zeit:'

    #time-out
    timeout_seconds = 30
    def before_next_page(self):
        # if group can not decide in time
        if self.timeout_happened:
            # record that article was chosen by timeout
            if self.group.articleSelectionRound == 1:
                self.player.articleChosenByTimeout1 = 1
                self.player.lastArticleChosenByTimeout = 1
            elif self.group.articleSelectionRound == 2:
                self.player.articleChosenByTimeout2 = 1
                self.player.lastArticleChosenByTimeout = 1
            elif self.group.articleSelectionRound == 3:
                self.player.articleChosenByTimeout3 = 1
                self.player.lastArticleChosenByTimeout = 1
            elif self.group.articleSelectionRound == 4:
                self.player.articleChosenByTimeout4 = 1
                self.player.lastArticleChosenByTimeout = 1
            elif self.group.articleSelectionRound == 5:
                self.player.articleChosenByTimeout5 = 1
                self.player.lastArticleChosenByTimeout = 1
            elif self.group.articleSelectionRound == 6:
                self.player.articleChosenByTimeout6 = 1
                self.player.lastArticleChosenByTimeout = 1
            else:
                pass
        else:
            pass




class SelectedArticlePage(Page):
    form_model = "player"
    form_fields = []
    # display page conditionally
    # def is_displayed(self):
    #     pass

    timeout_seconds = 40




class ChatAndDecisionPage(Page): # ----------------------
    form_model = "player"
    form_fields = ["groupDecision"]
    # display page conditionally
    def is_displayed(self):
        return self.player.singleplayer == 0

    # write all selected articles in variable so they can be saved in the data set
    def before_next_page(self):
        self.player.selectedArticlesList = str(self.participant.vars["selectedArticlesList"])



class GroupDecisionCheckWaitPage(WaitPage):
    form_model = "player"
    form_fields = []
    # display page conditionally
    def is_displayed(self):
        return self.player.singleplayer == 0

    after_all_players_arrive = "check_for_group_decision"



class ChatAndDecisionAfterDisagreementPage(Page): # ----------------------
    form_model = "player"
    form_fields = ["groupDecision"]
    # display page conditionally
    def is_displayed(self):
        return self.player.singleplayer == 0 and self.player.disagreementGroupDecision == 1



class SingleplayerArticleSelectionPage(Page):
    form_model = "player"
    form_fields = ["selectedArticle"]
    #display page conditionally
    def is_displayed(self):
        return self.player.singleplayer == 1

    timer_text = 'Verbleibende Zeit:'

    #time-out
    timeout_seconds = 210
    def before_next_page(self):
        # if group can not decide in time
        if self.timeout_happened:
            # record that article was chosen by timeout
            if self.group.articleSelectionRound == 1:
                self.player.articleChosenByTimeout1 = 1
                self.player.lastArticleChosenByTimeout = 1
            elif self.group.articleSelectionRound == 2:
                self.player.articleChosenByTimeout2 = 1
                self.player.lastArticleChosenByTimeout = 1
            elif self.group.articleSelectionRound == 3:
                self.player.articleChosenByTimeout3 = 1
                self.player.lastArticleChosenByTimeout = 1
            elif self.group.articleSelectionRound == 4:
                self.player.articleChosenByTimeout4 = 1
                self.player.lastArticleChosenByTimeout = 1
            elif self.group.articleSelectionRound == 5:
                self.player.articleChosenByTimeout5 = 1
                self.player.lastArticleChosenByTimeout = 1
            elif self.group.articleSelectionRound == 6:
                self.player.articleChosenByTimeout6 = 1
                self.player.lastArticleChosenByTimeout = 1
            else:
                pass
        else:
            pass



class CheckSingleplayerArticleSelectionWaitPage(WaitPage):
    title_text = ""
    body_text = ""

    def is_displayed(self):
        return self.player.singleplayer == 1

    after_all_players_arrive = "check_for_article_selection_singleplayer"

    # global WaitPage-template
    template_name = "global/WaitPage.html"



class PrepareArticlesSingleplayerWaitPage(WaitPage):
    title_text = ""
    body_text = ""
    # display page conditionally
    def is_displayed(self):
        return self.player.singleplayer == 1

    # global WaitPage-template
    template_name = "global/WaitPage.html"

    # make articles to be shown ready
    after_all_players_arrive = "prepare_displayed_articles"



class IndividualDecisionSingleplayerPage(Page):
    form_model = "player"
    form_fields = ["individualDecision",
                   "certaintyIndDec"]
    # display page conditionally
    def is_displayed(self):
        return self.player.singleplayer == 1


    # write all selected articles in variable so they can be saved in the data set
    def before_next_page(self):
        self.player.selectedArticlesList = str(self.participant.vars["selectedArticlesList"])


class IndividualDecisionMulitplayerPage(Page):
    form_model = "player"
    form_fields = ["individualDecision",
                   "certaintyIndDec"]
    # display page conditionally
    def is_displayed(self):
        return self.player.singleplayer == 0

    # write all selected articles in variable so they can be saved in the data set
    def before_next_page(self):
        self.player.selectedArticlesList = str(self.participant.vars["selectedArticlesList"])




class DependentVariablesPage(Page):
    form_model = "player"
    form_fields = ["policeBrutalityProblem",
                   "frequencyPoliceBrutality",
                   "actionsAgainstPoliceBrutality",
                   "moreCompetencesPolice",
                   "confidencePoliceBrutality",
                   "moreBrutalityPolice",
                   "equalitySearchResults",
                   "violenceAttitude1",
                   "violenceAttitude2",
                   "violenceAttitude3",
                   "trustArticles"]





class SearchPage(Page):
    form_model = "player"
    form_fields = ["search"]



page_sequence = [# match group members
                 MatchingWaitPage, # -> all players
                 GroupHypothesisPickingPage, # -> MP

                 # explanatory pages
                 GroupExperimentExplanationPage, # -> # Multiplayer
                 SingleplayerExperimentExplanationPage, # - Singleplayer

                 # first article to be shown
                 # InitialArticlePage, # -> all players

                 # Reminder Page with long instructions
                 InstructionReminderPage,

                 # Get acquainted to the Chat
                 WaitBeforeFamiliarizePage,
                 FamiliarizeWithChatPage,

                 # hypotheses explanation pages
                 HypothesisPolBrutPage, # -> all players
                 HypothesisLegBrutPage, # -> all players


                 # Wait before Chat so everybody is in at the same time
                 WaitBeforeChatPage, # -> MP


                 # 1 Round ----------------------------------------------------
                 ChatPage, # -> MP
                 CheckArticleSelectionWaitPage1, # -> MP
                 SelectArticleAfterDisagreementPage, # -> MP
                 CheckArticleSelectionWaitPage2, # -> MP
                 PrepareArticlesSingleplayerWaitPage, # -> SP ---------
                 SingleplayerArticleSelectionPage, # -> SP
                 CheckSingleplayerArticleSelectionWaitPage, # -> SP ---
                 SelectedArticlePage, # -> all players

                 # Wait before Chat so everybody is in at the same time
                 WaitBeforeChatPage, # -> MP

                 # 2 Round ----------------------------------------------------
                 ChatPage, # -> MP
                 CheckArticleSelectionWaitPage1, # -> MP
                 SelectArticleAfterDisagreementPage, # -> MP
                 CheckArticleSelectionWaitPage2, # -> MP
                 PrepareArticlesSingleplayerWaitPage, # -> SP ---------
                 SingleplayerArticleSelectionPage, # -> SP
                 CheckSingleplayerArticleSelectionWaitPage, # -> SP ---
                 SelectedArticlePage, # -> all players

                 # Wait before Chat so everybody is in at the same time
                 WaitBeforeChatPage, # -> MP

                 # 3 Round ----------------------------------------------------
                 ChatPage, # -> MP
                 CheckArticleSelectionWaitPage1, # -> MP
                 SelectArticleAfterDisagreementPage, # -> MP
                 CheckArticleSelectionWaitPage2, # -> MP
                 PrepareArticlesSingleplayerWaitPage, # -> SP ---------
                 SingleplayerArticleSelectionPage, # -> SP
                 CheckSingleplayerArticleSelectionWaitPage, # -> SP ---
                 SelectedArticlePage, # -> all players

                 # Wait before Chat so everybody is in at the same time
                 WaitBeforeChatPage, # -> MP

                 # 4 Round ----------------------------------------------------
                 ChatPage, # -> MP
                 CheckArticleSelectionWaitPage1, # -> MP
                 SelectArticleAfterDisagreementPage, # -> MP
                 CheckArticleSelectionWaitPage2, # -> MP
                 PrepareArticlesSingleplayerWaitPage, # -> SP ---------
                 SingleplayerArticleSelectionPage, # -> SP
                 CheckSingleplayerArticleSelectionWaitPage, # -> SP ---
                 SelectedArticlePage, # -> all players

                 # Wait before Chat so everybody is in at the same time
                 WaitBeforeChatPage, # -> MP


                 # 5 Round ----------------------------------------------------
                 ChatPage, # -> MP
                 CheckArticleSelectionWaitPage1, # -> MP
                 SelectArticleAfterDisagreementPage, # -> MP
                 CheckArticleSelectionWaitPage2, # -> MP
                 PrepareArticlesSingleplayerWaitPage, # -> SP ---------
                 SingleplayerArticleSelectionPage, # -> SP
                 CheckSingleplayerArticleSelectionWaitPage, # -> SP ---
                 SelectedArticlePage, # -> all players

                 # Wait before Chat so everybody is in at the same time
                 WaitBeforeChatPage, # -> MP


                 # 6 Round ----------------------------------------------------
                 ChatPage, # -> MP
                 CheckArticleSelectionWaitPage1, # -> MP
                 SelectArticleAfterDisagreementPage, # -> MP
                 CheckArticleSelectionWaitPage2, # -> MP
                 PrepareArticlesSingleplayerWaitPage, # -> SP ---------
                 SingleplayerArticleSelectionPage, # -> SP
                 CheckSingleplayerArticleSelectionWaitPage, # -> SP ---
                 SelectedArticlePage, # -> all players

                 # group needs to chat over decision to be made
                 # ChatAndDecisionPage, # -> MP
                 # check the group decision
                 # GroupDecisionCheckWaitPage, # -> MP
                 # if decision not matching decide as a group again
                 # ChatAndDecisionAfterDisagreementPage, # -> MP
                 # check the group decision
                 # GroupDecisionCheckWaitPage, # -> MP


                 # individual decisions
                 IndividualDecisionSingleplayerPage, # -> SP
                 IndividualDecisionMulitplayerPage, # -> MP

                 # Manipulation Checks and further questions
                 DependentVariablesPage

                 ]
