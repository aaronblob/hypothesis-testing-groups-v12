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
    name_in_url = 'HypothesesTesting'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    # match participants by arrivle time so nobody has to wait too long -------
    def group_by_arrival_time_method(self, waiting_players):
        import time
        # check if sufficent players are there to form a group
        if len(waiting_players) >= Constants.players_per_group:

            players = self.get_players()
            # if yes: form a group
            return waiting_players[:Constants.players_per_group]

        # for every player who is waiting check...
        for p in waiting_players:
            # ...whether their waiting-time surpasses x*y seconds
            if time.time() - p.participant.vars["arrivalTime"] > 5*60: # adjust time?
                # if it does make them singleplayer
                p.singleplayer = 1
                # and move them foreward
                return [p]
            else:
                pass
    # -------------------------------------------------------------------------


class Group(BaseGroup):
    # condition picking and grouping ------------------------------------------
    # take the variables created in "consent" when I was creating the session
    groupCondition = models.StringField()

    def condition_picker(self):
        import random
        from operator import itemgetter
        players = self.get_players()

        # check which condition is to be picked (condition counter)
        if self.session.vars["groupConditionCounter"] == 0:
            # every player in group receives same
            for p in players:
                pickedCondition = "hypLegBrut" # save hypothesis
                p.conditionHypothesis = "hypLegBrut" # save hypothesis
                p.nickname = "Teilnehmer*in {}".format(p.id_in_group) # give participants nickname
                self.session.vars["groupConditionCounter"] += 1 # increase counter by one so the next pick is the next item in the list
                print("--- Group Condition picked: ---\n")
                print(p.conditionHypothesis)
            self.groupCondition = pickedCondition # save hypothesis
        else:
            for p in players:
                pickedCondition = "hypPolBrut" # save hypothesis
                p.conditionHypothesis = "hypPolBrut" # save hypothesis
                p.nickname = "Teilnehmer*in {}".format(p.id_in_group) # give participants nickname
                self.session.vars["groupConditionCounter"] = 0 # reset condition counter
                print("--- Group Condition picked: ---\n")
                print(p.conditionHypothesis)
            self.groupCondition = pickedCondition # save hypothesis


        # ---------------------------------------------------------------------



    # check for disagreement in article selection -----------------------------
    def check_for_article_selection1(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)

        # reset disagreement-variable
        for p in self.get_players():
            p.disagreement1 = 0

        # if no article has been selected:
        if p1.selectedArticle == 99 or p2.selectedArticle == 99 or p3.selectedArticle == 99:
            for p in self.get_players():
                p.disagreementArticle += 1
                #p.timeoutRound1 += 1
                p.selectedArticle = 0

        # if all players select same article
        elif p1.selectedArticle == p2.selectedArticle == p3.selectedArticle:
            self.articleSelectionRound += 1

            for p in self.get_players():
                # selected article in list
                p.participant.vars["selectedArticlesList"].append(p.selectedArticle)

                # mark article as selected for
                if p.selectedArticle == 1:
                    p.firstArticle = 1

                elif p.selectedArticle == 2:
                    p.secondArticle = 1

                elif p.selectedArticle == 3:
                    p.thirdArticle = 1

                elif p.selectedArticle == 4:
                    p.fourthArticle = 1

                elif p.selectedArticle == 5:
                    p.fifthArticle = 1

                elif p.selectedArticle == 6:
                    p.sixthArticle = 1

                elif p.selectedArticle == 7:
                    p.seventhArticle = 1

                elif p.selectedArticle == 8:
                    p.eigthArticle = 1

                elif p.selectedArticle == 9:
                    p.ninethArticle = 1

                elif p.selectedArticle == 10:
                    p.tenthArticle = 1

                elif p.selectedArticle == 11:
                    p.eleventhArticle = 1

                elif p.selectedArticle == 12:
                    p.twelvethArticle = 1

                elif p.selectedArticle == 13:
                    p.thirteenthArticle = 1

                elif p.selectedArticle == 14:
                    p.forteentethArticle = 1

                elif p.selectedArticle == 15:
                    p.fifteenthArticle = 1

                elif p.selectedArticle == 16:
                    p.sixteenthArticle = 1

                elif p.selectedArticle == 17:
                    p.seventeenthArticle = 1

                elif p.selectedArticle == 18:
                    p.eighteenthArticle = 1

                elif p.selectedArticle == 19:
                    p.nineteenthArticle = 1

                elif p.selectedArticle == 20:
                    p.twentiethArticle = 1

                elif p.selectedArticle == 21:
                    p.twentyfirstArticle = 1

                elif p.selectedArticle == 22:
                    p.twentysecondArticle = 1

                elif p.selectedArticle == 23:
                    p.twentythirdArticle = 1

                elif p.selectedArticle == 24:
                    p.twentyforthArticle = 1

                else:
                    pass

        else:
            for p in self.get_players():
                p.disagreementArticle += 1
                p.selectedArticle = 0


    def check_for_article_selection2(self): # ---------------------------------
        import random

        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)

        # reset disagreement-variable
        for p in self.get_players():
            p.disagreementArticle = 0

        # if all players select same article
        if p1.selectedArticle == p2.selectedArticle == p3.selectedArticle:

            for p in self.get_players():
                # selected article in list
                p.participant.vars["selectedArticlesList"].append(p.selectedArticle)

                # mark article as selected for
                if p.selectedArticle == 1:
                    p.firstArticle = 1

                elif p.selectedArticle == 2:
                    p.secondArticle = 1

                elif p.selectedArticle == 3:
                    p.thirdArticle = 1

                elif p.selectedArticle == 4:
                    p.fourthArticle = 1

                elif p.selectedArticle == 5:
                    p.fifthArticle = 1

                elif p.selectedArticle == 6:
                    p.sixthArticle = 1

                elif p.selectedArticle == 7:
                    p.seventhArticle = 1

                elif p.selectedArticle == 8:
                    p.eigthArticle = 1

                elif p.selectedArticle == 9:
                    p.ninethArticle = 1

                elif p.selectedArticle == 10:
                    p.tenthArticle = 1

                elif p.selectedArticle == 11:
                    p.eleventhArticle = 1

                elif p.selectedArticle == 12:
                    p.twelvethArticle = 1

                elif p.selectedArticle == 13:
                    p.thirteenthArticle = 1

                elif p.selectedArticle == 14:
                    p.forteentethArticle = 1

                elif p.selectedArticle == 15:
                    p.fifteenthArticle = 1

                elif p.selectedArticle == 16:
                    p.sixteenthArticle = 1

                elif p.selectedArticle == 17:
                    p.seventeenthArticle = 1

                elif p.selectedArticle == 18:
                    p.eighteenthArticle = 1

                elif p.selectedArticle == 19:
                    p.nineteenthArticle = 1

                elif p.selectedArticle == 20:
                    p.twentiethArticle = 1

                elif p.selectedArticle == 22:
                    p.twentyfirstArticle = 1

                elif p.selectedArticle == 22:
                    p.twentysecondArticle = 1

                elif p.selectedArticle == 23:
                    p.twentythirdArticle = 1

                else:
                    p.twentyforthArticle = 1


        # if not
        else:

            # but if two players have the same
            if p1.selectedArticle == p2.selectedArticle: # ------------ p1 = p2

                # safe which article was selected
                if self.articleSelectionRound == 1:
                    p3.minorityArticleNotSelectedR1 = p3.selectedArticle
                elif self.articleSelectionRound == 2:
                    p3.minorityArticleNotSelectedR2 = p3.selectedArticle
                elif self.articleSelectionRound == 3:
                    p3.minorityArticleNotSelectedR3 = p3.selectedArticle
                elif self.articleSelectionRound == 4:
                    p3.minorityArticleNotSelectedR4 = p3.selectedArticle
                elif self.articleSelectionRound == 5:
                    p3.minorityArticleNotSelectedR5 = p3.selectedArticle
                else:
                    p3.minorityArticleNotSelectedR6 = p3.selectedArticle


                for p in self.get_players():
                    # overwrite article values
                    p.selectedArticle = p1.selectedArticle
                    # save selected articles in selected articles list
                    p.participant.vars["selectedArticlesList"].append(p.selectedArticle)

                    if p.selectedArticle == 1:
                        p.firstArticle = 1
                        p.article1ChosenByMajority = 1
                    elif p.selectedArticle == 2:
                        p.secondArticle = 1
                        p.article2ChosenByMajority = 1
                    elif p.selectedArticle == 3:
                        p.thirdArticle = 1
                        p.article3ChosenByMajority = 1
                    elif p.selectedArticle == 4:
                        p.fourthArticle = 1
                        p.article4ChosenByMajority = 1
                    elif p.selectedArticle == 5:
                        p.fifthArticle = 1
                        p.article5ChosenByMajority = 1
                    elif p.selectedArticle == 6:
                        p.sixthArticle = 1
                        p.article6ChosenByMajority = 1
                    elif p.selectedArticle == 7:
                        p.seventhArticle = 1
                        p.article7ChosenByMajority = 1
                    elif p.selectedArticle == 8:
                        p.eigthArticle = 1
                        p.article8ChosenByMajority = 1
                    elif p.selectedArticle == 9:
                        p.ninethArticle = 1
                        p.article9ChosenByMajority = 1
                    elif p.selectedArticle == 10:
                        p.tenthArticle = 1
                        p.article10ChosenByMajority = 1
                    elif p.selectedArticle == 11:
                        p.eleventhArticle = 1
                        p.article11ChosenByMajority = 1
                    elif p.selectedArticle == 12:
                        p.twelvethArticle = 1
                        p.article12ChosenByMajority = 1
                    elif p.selectedArticle == 13:
                        p.thirteenthArticle = 1
                        p.article13ChosenByMajority = 1
                    elif p.selectedArticle == 14:
                        p.forteentethArticle = 1
                        p.article14ChosenByMajority = 1
                    elif p.selectedArticle == 15:
                        p.fifteenthArticle = 1
                        p.article15ChosenByMajority = 1
                    elif p.selectedArticle == 16:
                        p.sixteenthArticle = 1
                        p.article16ChosenByMajority = 1
                    elif p.selectedArticle == 17:
                        p.seventeenthArticle = 1
                        p.article17ChosenByMajority = 1
                    elif p.selectedArticle == 18:
                        p.eighteenthArticle = 1
                        p.article18ChosenByMajority = 1
                    elif p.selectedArticle == 19:
                        p.nineteenthArticle = 1
                        p.article19ChosenByMajority = 1
                    elif p.selectedArticle == 20:
                        p.twentiethArticle = 1
                        p.article20ChosenByMajority = 1
                    elif p.selectedArticle == 21:
                        p.twentyfirstArticle = 1
                        p.article21ChosenByMajority = 1
                    elif p.selectedArticle == 22:
                        p.twentysecondArticle = 1
                        p.article22ChosenByMajority = 1
                    elif p.selectedArticle == 23:
                        p.twentythirdArticle = 1
                        p.article23ChosenByMajority = 1
                    else:
                        p.twentyforthArticle = 1
                        p.article24ChosenByMajority = 1

            # -----------------------------------------------------------------

            if p1.selectedArticle == p3.selectedArticle: # ------------ p1 = p3

                # safe which article was selected
                if self.articleSelectionRound == 1:
                    p2.minorityArticleNotSelectedR1 = p2.selectedArticle
                elif self.articleSelectionRound == 2:
                    p2.minorityArticleNotSelectedR2 = p2.selectedArticle
                elif self.articleSelectionRound == 3:
                    p2.minorityArticleNotSelectedR3 = p2.selectedArticle
                elif self.articleSelectionRound == 4:
                    p2.minorityArticleNotSelectedR4 = p2.selectedArticle
                elif self.articleSelectionRound == 5:
                    p2.minorityArticleNotSelectedR5 = p2.selectedArticle
                else:
                    p2.minorityArticleNotSelectedR6 = p2.selectedArticle


                for p in self.get_players():
                    # overwrite article values
                    p.selectedArticle = p1.selectedArticle
                    # save selected articles in selected articles list
                    p.participant.vars["selectedArticlesList"].append(p.selectedArticle)

                    if p.selectedArticle == 1:
                        p.firstArticle = 1
                        p.article1ChosenByMajority = 1
                    elif p.selectedArticle == 2:
                        p.secondArticle = 1
                        p.article2ChosenByMajority = 1
                    elif p.selectedArticle == 3:
                        p.thirdArticle = 1
                        p.article3ChosenByMajority = 1
                    elif p.selectedArticle == 4:
                        p.fourthArticle = 1
                        p.article4ChosenByMajority = 1
                    elif p.selectedArticle == 5:
                        p.fifthArticle = 1
                        p.article5ChosenByMajority = 1
                    elif p.selectedArticle == 6:
                        p.sixthArticle = 1
                        p.article6ChosenByMajority = 1
                    elif p.selectedArticle == 7:
                        p.seventhArticle = 1
                        p.article7ChosenByMajority = 1
                    elif p.selectedArticle == 8:
                        p.eigthArticle = 1
                        p.article8ChosenByMajority = 1
                    elif p.selectedArticle == 9:
                        p.ninethArticle = 1
                        p.article9ChosenByMajority = 1
                    elif p.selectedArticle == 10:
                        p.tenthArticle = 1
                        p.article10ChosenByMajority = 1
                    elif p.selectedArticle == 11:
                        p.eleventhArticle = 1
                        p.article11ChosenByMajority = 1
                    elif p.selectedArticle == 12:
                        p.twelvethArticle = 1
                        p.article12ChosenByMajority = 1
                    elif p.selectedArticle == 13:
                        p.thirteenthArticle = 1
                        p.article13ChosenByMajority = 1
                    elif p.selectedArticle == 14:
                        p.forteentethArticle = 1
                        p.article14ChosenByMajority = 1
                    elif p.selectedArticle == 15:
                        p.fifteenthArticle = 1
                        p.article15ChosenByMajority = 1
                    elif p.selectedArticle == 16:
                        p.sixteenthArticle = 1
                        p.article16ChosenByMajority = 1
                    elif p.selectedArticle == 17:
                        p.seventeenthArticle = 1
                        p.article17ChosenByMajority = 1
                    elif p.selectedArticle == 18:
                        p.eighteenthArticle = 1
                        p.article18ChosenByMajority = 1
                    elif p.selectedArticle == 19:
                        p.nineteenthArticle = 1
                        p.article19ChosenByMajority = 1
                    elif p.selectedArticle == 20:
                        p.twentiethArticle = 1
                        p.article20ChosenByMajority = 1
                    elif p.selectedArticle == 21:
                        p.twentyfirstArticle = 1
                        p.article21ChosenByMajority = 1
                    elif p.selectedArticle == 22:
                        p.twentysecondArticle = 1
                        p.article22ChosenByMajority = 1
                    elif p.selectedArticle == 23:
                        p.twentythirdArticle = 1
                        p.article23ChosenByMajority = 1
                    else:
                        p.twentyforthArticle = 1
                        p.article24ChosenByMajority = 1

            # -----------------------------------------------------------------

            if p2.selectedArticle == p3.selectedArticle: # ------------ p2 = p3

                # safe which article was selected
                if self.articleSelectionRound == 1:
                    p1.minorityArticleNotSelectedR1 = p1.selectedArticle
                elif self.articleSelectionRound == 2:
                    p1.minorityArticleNotSelectedR2 = p1.selectedArticle
                elif self.articleSelectionRound == 3:
                    p1.minorityArticleNotSelectedR3 = p1.selectedArticle
                elif self.articleSelectionRound == 4:
                    p1.minorityArticleNotSelectedR4 = p1.selectedArticle
                elif self.articleSelectionRound == 5:
                    p1.minorityArticleNotSelectedR5 = p1.selectedArticle
                else:
                    p1.minorityArticleNotSelectedR6 = p1.selectedArticle


                for p in self.get_players():
                    # overwrite article values
                    p.selectedArticle = p2.selectedArticle
                    # save selected articles in selected articles list
                    p.participant.vars["selectedArticlesList"].append(p.selectedArticle)

                    if p.selectedArticle == 1:
                        p.firstArticle = 1
                        p.article1ChosenByMajority = 1
                    elif p.selectedArticle == 2:
                        p.secondArticle = 1
                        p.article2ChosenByMajority = 1
                    elif p.selectedArticle == 3:
                        p.thirdArticle = 1
                        p.article3ChosenByMajority = 1
                    elif p.selectedArticle == 4:
                        p.fourthArticle = 1
                        p.article4ChosenByMajority = 1
                    elif p.selectedArticle == 5:
                        p.fifthArticle = 1
                        p.article5ChosenByMajority = 1
                    elif p.selectedArticle == 6:
                        p.sixthArticle = 1
                        p.article6ChosenByMajority = 1
                    elif p.selectedArticle == 7:
                        p.seventhArticle = 1
                        p.article7ChosenByMajority = 1
                    elif p.selectedArticle == 8:
                        p.eigthArticle = 1
                        p.article8ChosenByMajority = 1
                    elif p.selectedArticle == 9:
                        p.ninethArticle = 1
                        p.article9ChosenByMajority = 1
                    elif p.selectedArticle == 10:
                        p.tenthArticle = 1
                        p.article10ChosenByMajority = 1
                    elif p.selectedArticle == 11:
                        p.eleventhArticle = 1
                        p.article11ChosenByMajority = 1
                    elif p.selectedArticle == 12:
                        p.twelvethArticle = 1
                        p.article12ChosenByMajority = 1
                    elif p.selectedArticle == 13:
                        p.thirteenthArticle = 1
                        p.article13ChosenByMajority = 1
                    elif p.selectedArticle == 14:
                        p.forteentethArticle = 1
                        p.article14ChosenByMajority = 1
                    elif p.selectedArticle == 15:
                        p.fifteenthArticle = 1
                        p.article15ChosenByMajority = 1
                    elif p.selectedArticle == 16:
                        p.sixteenthArticle = 1
                        p.article16ChosenByMajority = 1
                    elif p.selectedArticle == 17:
                        p.seventeenthArticle = 1
                        p.article17ChosenByMajority = 1
                    elif p.selectedArticle == 18:
                        p.eighteenthArticle = 1
                        p.article18ChosenByMajority = 1
                    elif p.selectedArticle == 19:
                        p.nineteenthArticle = 1
                        p.article19ChosenByMajority = 1
                    elif p.selectedArticle == 20:
                        p.twentiethArticle = 1
                        p.article20ChosenByMajority = 1
                    elif p.selectedArticle == 21:
                        p.twentyfirstArticle = 1
                        p.article21ChosenByMajority = 1
                    elif p.selectedArticle == 22:
                        p.twentysecondArticle = 1
                        p.article22ChosenByMajority = 1
                    elif p.selectedArticle == 23:
                        p.twentythirdArticle = 1
                        p.article23ChosenByMajority = 1
                    else:
                        p.twentyforthArticle = 1
                        p.article24ChosenByMajority = 1

            # -----------------------------------------------------------------


            else:
                # chose random player
                randInt = random.randint(1,3)
                pRandom = self.get_player_by_id(randInt)

                # save in which round which article has been chosen but was not selected due to chance
                if self.articleSelectionRound == 1:
                    p1.chanceArticleNotSelectedR1 = p1.selectedArticle
                    p2.chanceArticleNotSelectedR1 = p2.selectedArticle
                    p3.chanceArticleNotSelectedR1 = p3.selectedArticle
                    pRandom.chanceArticleNotSelectedR1 = 0
                elif self.articleSelectionRound == 2:
                    p1.chanceArticleNotSelectedR2 = p1.selectedArticle
                    p2.chanceArticleNotSelectedR2 = p2.selectedArticle
                    p3.chanceArticleNotSelectedR2 = p3.selectedArticle
                    pRandom.chanceArticleNotSelectedR2 = 0
                elif self.articleSelectionRound == 3:
                    p1.chanceArticleNotSelectedR3 = p1.selectedArticle
                    p2.chanceArticleNotSelectedR3 = p2.selectedArticle
                    p3.chanceArticleNotSelectedR3 = p3.selectedArticle
                    pRandom.chanceArticleNotSelectedR3 = 0
                elif self.articleSelectionRound == 4:
                    p1.chanceArticleNotSelectedR4 = p1.selectedArticle
                    p2.chanceArticleNotSelectedR4 = p2.selectedArticle
                    p3.chanceArticleNotSelectedR4 = p3.selectedArticle
                    pRandom.chanceArticleNotSelectedR4 = 0
                elif self.articleSelectionRound == 5:
                    p1.chanceArticleNotSelectedR5 = p1.selectedArticle
                    p2.chanceArticleNotSelectedR5 = p2.selectedArticle
                    p3.chanceArticleNotSelectedR5 = p3.selectedArticle
                    pRandom.chanceArticleNotSelectedR5 = 0
                else:
                    p1.chanceArticleNotSelectedR6 = p1.selectedArticle
                    p2.chanceArticleNotSelectedR6 = p2.selectedArticle
                    p3.chanceArticleNotSelectedR6 = p3.selectedArticle
                    pRandom.chanceArticleNotSelectedR6 = 0

                # and give everybody the article chosen by random player
                for p in self.get_players():
                    p.selectedArticle = pRandom.selectedArticle
                    p.participant.vars["selectedArticlesList"].append(pRandom.selectedArticle)

                    # if self.articleSelectionRound == 1:
                    if pRandom.selectedArticle == 1: # ------------------ 1
                        p.firstArticle = 1
                        # save which article was chosen by chance
                        p.article1ChosenByChance = 1
                    elif pRandom.selectedArticle == 2: # ---------------- 2
                        p.secondArticle = 1
                        # save which article was chosen by chance
                        p.article2ChosenByChance = 1
                    elif pRandom.selectedArticle == 3: # ---------------- 3
                        p.thirdArticle = 1
                        # save which article was chosen by chance
                        p.article3ChosenByChance = 1
                    elif pRandom.selectedArticle == 4: # ---------------- 4
                        p.fourthArticle = 1
                        # save which article was chosen by chance
                        p.article4ChosenByChance = 1
                    elif pRandom.selectedArticle == 5: # ---------------- 5
                        p.fifthArticle = 1
                        # save which article was chosen by chance
                        p.article5ChosenByChance = 1
                    elif pRandom.selectedArticle == 6: # ---------------- 6
                        p.sixthArticle = 1
                        # save which article was chosen by chance
                        p.article6ChosenByChance = 1
                    elif pRandom.selectedArticle == 7: # ---------------- 7
                        p.seventhArticle = 1
                        # save which article was chosen by chance
                        p.article7ChosenByChance = 1
                    elif pRandom.selectedArticle == 8: # ---------------- 8
                        p.eigthArticle = 1
                        # save which article was chosen by chance
                        p.article8ChosenByChance = 1
                    elif pRandom.selectedArticle == 9: # ---------------- 9
                        p.ninethArticle = 1
                        # save which article was chosen by chance
                        p.article9ChosenByChance = 1
                    elif pRandom.selectedArticle == 10: # -------------- 10
                        p.tenthArticle = 1
                        # save which article was chosen by chance
                        p.article10ChosenByChance = 1
                    elif pRandom.selectedArticle == 11: # -------------- 11
                        p.eleventhArticle = 1
                        # save which article was chosen by chance
                        p.article11ChosenByChance = 1
                    elif pRandom.selectedArticle == 12: # -------------- 12
                        p.twelvethArticle = 1
                        # save which article was chosen by chance
                        p.article12ChosenByChance = 1
                    elif pRandom.selectedArticle == 13: # -------------- 13
                        p.thirteenthArticle = 1
                        # save which article was chosen by chance
                        p.article13ChosenByChance = 1
                    elif pRandom.selectedArticle == 14: # -------------- 14
                        p.forteentethArticle = 1
                        # save which article was chosen by chance
                        p.article14ChosenByChance = 1
                    elif pRandom.selectedArticle == 15: # -------------- 15
                        p.fifteenthArticle = 1
                        # save which article was chosen by chance
                        p.article15ChosenByChance = 1
                    elif pRandom.selectedArticle == 16: # -------------- 16
                        p.sixteenthArticle = 1
                        # save which article was chosen by chance
                        p.article16ChosenByChance = 1
                    elif pRandom.selectedArticle == 17: # -------------- 17
                        p.seventeenthArticle = 1
                        # save which article was chosen by chance
                        p.article17ChosenByChance = 1
                    elif pRandom.selectedArticle == 18: # -------------- 18
                        p.eighteenthArticle = 1
                        # save which article was chosen by chance
                        p.article18ChosenByChance = 1
                    elif pRandom.selectedArticle == 19: # -------------- 19
                        p.nineteenthArticle = 1
                        # save which article was chosen by chance
                        p.article19ChosenByChance = 1
                    elif pRandom.selectedArticle == 20: # -------------- 20
                        p.twentiethArticle = 1
                        # save which article was chosen by chance
                        p.article20ChosenByChance = 1
                    elif pRandom.selectedArticle == 21: # -------------- 21
                        p.twentyfirstArticle = 1
                        # save which article was chosen by chance
                        p.article21ChosenByChance = 1
                    elif pRandom.selectedArticle == 22: # -------------- 22
                        p.twentysecondArticle = 1
                        # save which article was chosen by chance
                        p.article22ChosenByChance = 1
                    elif pRandom.selectedArticle == 23: # -------------- 23
                        p.twentythirdArticle = 1
                        # save which article was chosen by chance
                        p.article23ChosenByChance = 1
                    else: # -------------------------------------------- 24
                        p.twentyforthArticle = 1
                        # save which article was chosen by chance
                        p.article24ChosenByChance = 1

        # increase articleSelectionRound
        self.articleSelectionRound +=1
        p.disagreementArticle = 0

    # -------------------------------------------------------------------------



    # safe the singleplayer article selection
    def check_for_article_selection_singleplayer(self): # ---------------------
        for p in self.get_players():
            p.participant.vars["selectedArticlesList"].append(p.selectedArticle)
            # mark article as selected for
            if p.selectedArticle == 1:
                p.firstArticle = 1
            elif p.selectedArticle == 2:
                p.secondArticle = 1
            elif p.selectedArticle == 3:
                p.thirdArticle = 1
            elif p.selectedArticle == 4:
                p.fourthArticle = 1
            elif p.selectedArticle == 5:
                p.fifthArticle = 1
            elif p.selectedArticle == 6:
                p.sixthArticle = 1
            elif p.selectedArticle == 7:
                p.seventhArticle = 1
            elif p.selectedArticle == 8:
                p.eigthArticle = 1
            elif p.selectedArticle == 9:
                p.ninethArticle = 1
            elif p.selectedArticle == 10:
                p.tenthArticle = 1
            elif p.selectedArticle == 11:
                p.eleventhArticle = 1
            elif p.selectedArticle == 12:
                p.twelvethArticle = 1
            elif p.selectedArticle == 13:
                p.thirteenthArticle = 1
            elif p.selectedArticle == 14:
                p.forteentethArticle = 1
            elif p.selectedArticle == 15:
                p.fifteenthArticle = 1
            elif p.selectedArticle == 16:
                p.sixteenthArticle = 1
            elif p.selectedArticle == 17:
                p.seventeenthArticle = 1
            elif p.selectedArticle == 18:
                p.eighteenthArticle = 1
            elif p.selectedArticle == 19:
                p.nineteenthArticle = 1
            elif p.selectedArticle == 20:
                p.twentiethArticle = 1
            elif p.selectedArticle == 22:
                p.twentyfirstArticle = 1
            elif p.selectedArticle == 22:
                p.twentysecondArticle = 1
            elif p.selectedArticle == 23:
                p.twentythirdArticle = 1
            else:
                p.twentyforthArticle = 1
        # increase articleSelectionRound
        self.articleSelectionRound +=1

    # -------------------------------------------------------------------------

    def check_for_group_decision(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)
        players = self.get_players()

        if self.groupDecisionRound == 1:
            if p1.groupDecision == p2.groupDecision == p3.groupDecision:
                for p in players:
                    p.disagreementGroupDecision = 0
            else:
                for p in players:
                    p.disagreementGroupDecision = 1
                    p.groupDecision = 0
                self.groupDecisionRound = 2
        else:
            if p1.groupDecision == p2.groupDecision == p3.groupDecision:
                for p in players:
                    p.disagreementGroupDecision = 0
            else:
                if p1.groupDecision == p2.groupDecision:
                    p3.groupMinorityDecision = p3.groupDecision
                    p3.groupDecision = p1.groupDecision
                elif p1.groupDecision == p3.groupDecision:
                    p2.groupMinorityDecision = p2.groupDecision
                    p2.groupDecision = p1.groupDecision
                else:
                    p1.groupMinorityDecision = p1.groupDecision
                    p1.groupDecision = p2.groupDecision

    groupDecisionRound = models.IntegerField(initial=1)

    # -------------------------------------------------------------------------

    # prepare articles which should be displayed on the chat page
    articleSelectionRound = models.IntegerField(initial=1)

    # article headings for page
    head1 = models.StringField(initial=None)
    head2 = models.StringField(initial=None)
    head3 = models.StringField(initial=None)
    head4 = models.StringField(initial=None)

    def prepare_displayed_articles(self):
        from operator import itemgetter
        import random

        ##### possible sequences: #####
        #    | S1) S2) S3) S4) S5) S6)#
        # --------------------------- #
        # A1 | pB  pB  pB  lB  lB  lB #
        # A2 | pB  lB  lB  pB  lB  pB #
        # A3 | lB  pB  lB  lB  pB  pB #
        # A4 | lB  lB  pB  pB  pB  lB #
        ###############################

        p1 = self.get_player_by_id(1)

        # Round 1 ---------------------------------------------------------
        # check which round to not display articles twice
        if self.articleSelectionRound == 1:
            # get random number from sequence modifier
            sequenceChosen = random.randint(1,6)

            for p in self.get_players():
                p.lastArticleChosenByTimeout = 0

                p.shuffledArticlePolBrut1 = itemgetter(0)(p1.participant.vars["shuffledArticlesListPolBrut"])
                p.shuffledArticlePolBrut2 = itemgetter(1)(p1.participant.vars["shuffledArticlesListPolBrut"])
                # p.shuffledArticlePolBrut1 = p1.shuffledArticlePolBrut1
                # p.shuffledArticlePolBrut2 = p1.shuffledArticlePolBrut2

                p.shuffledArticleLegBrut1 = itemgetter(0)(p1.participant.vars["shuffledArticlesListLegBrut"])
                p.shuffledArticleLegBrut2 = itemgetter(1)(p1.participant.vars["shuffledArticlesListLegBrut"])
                # p.shuffledArticleLegBrut1 = p1.shuffledArticleLegBrut1
                # p.shuffledArticleLegBrut2 = p1.shuffledArticleLegBrut2

            # check which sequence should be shown
            if sequenceChosen == 1: # pB pB lB lB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticlePolBrut1 # pB
                self.head2 = p.shuffledArticlePolBrut2 # pB
                self.head3 = p.shuffledArticleLegBrut1 # lB
                self.head4 = p.shuffledArticleLegBrut2 # lB
            elif sequenceChosen == 2: # pB lB pB lB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticlePolBrut1 # pB
                self.head2 = p.shuffledArticleLegBrut1 # lB
                self.head3 = p.shuffledArticlePolBrut2 # pB
                self.head4 = p.shuffledArticleLegBrut2 # lB
            elif sequenceChosen == 3: # pB lB lB pB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticlePolBrut1 # pB
                self.head2 = p.shuffledArticleLegBrut1 # lB
                self.head3 = p.shuffledArticleLegBrut2 # lB
                self.head4 = p.shuffledArticlePolBrut2 # pB
            elif sequenceChosen == 4: # lB pB lB pB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticleLegBrut1 # lB
                self.head2 = p.shuffledArticlePolBrut1 # pB
                self.head3 = p.shuffledArticleLegBrut2 # lB
                self.head4 = p.shuffledArticlePolBrut2 # pB
            elif sequenceChosen == 5: # lB lB pB pB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticleLegBrut1 # lB
                self.head2 = p.shuffledArticleLegBrut2 # lB
                self.head3 = p.shuffledArticlePolBrut1 # pB
                self.head4 = p.shuffledArticlePolBrut2 # pB
            else: # lB pB pB lB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticleLegBrut1 # lB
                self.head2 = p.shuffledArticlePolBrut1 # pB
                self.head3 = p.shuffledArticlePolBrut2 # pB
                self.head4 = p.shuffledArticleLegBrut2 # lB

        # Round 2 ---------------------------------------------------------
        # check which round to not display articles twice
        elif self.articleSelectionRound == 2:
            # get random number from sequence modifier
            sequenceChosen = random.randint(1,6)

            for p in self.get_players():
                p.lastArticleChosenByTimeout = 0

                p.shuffledArticlePolBrut3 = itemgetter(2)(p.participant.vars["shuffledArticlesListPolBrut"])
                p.shuffledArticlePolBrut4 = itemgetter(3)(p.participant.vars["shuffledArticlesListPolBrut"])
                p.shuffledArticlePolBrut3 = p1.shuffledArticlePolBrut3
                p.shuffledArticlePolBrut4 = p1.shuffledArticlePolBrut4

                p.shuffledArticleLegBrut3 = itemgetter(2)(p.participant.vars["shuffledArticlesListLegBrut"])
                p.shuffledArticleLegBrut4 = itemgetter(3)(p.participant.vars["shuffledArticlesListLegBrut"])
                p.shuffledArticleLegBrut3 = p1.shuffledArticleLegBrut3
                p.shuffledArticleLegBrut4 = p1.shuffledArticleLegBrut4

            # check which sequence should be shown
            if sequenceChosen == 1: # pB pB lB lB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticlePolBrut3 # pB
                self.head2 = p.shuffledArticlePolBrut4 # pB
                self.head3 = p.shuffledArticleLegBrut3 # lB
                self.head4 = p.shuffledArticleLegBrut4 # lB
            elif sequenceChosen == 2: # pB lB pB lB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticlePolBrut3 # pB
                self.head2 = p.shuffledArticleLegBrut3 # lB
                self.head3 = p.shuffledArticlePolBrut4 # pB
                self.head4 = p.shuffledArticleLegBrut4 # lB
            elif sequenceChosen == 3: # pB lB lB pB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticlePolBrut3 # pB
                self.head2 = p.shuffledArticleLegBrut3 # lB
                self.head3 = p.shuffledArticleLegBrut4 # lB
                self.head4 = p.shuffledArticlePolBrut4 # pB
            elif sequenceChosen == 4: # lB pB lB pB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticleLegBrut3 # lB
                self.head2 = p.shuffledArticlePolBrut3 # pB
                self.head3 = p.shuffledArticleLegBrut4 # lB
                self.head4 = p.shuffledArticlePolBrut4 # pB
            elif sequenceChosen == 5: # lB lB pB pB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticleLegBrut3 # lB
                self.head2 = p.shuffledArticleLegBrut4 # lB
                self.head3 = p.shuffledArticlePolBrut3 # pB
                self.head4 = p.shuffledArticlePolBrut4 # pB
            else: # lB pB pB lB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticleLegBrut3 # lB
                self.head2 = p.shuffledArticlePolBrut3 # pB
                self.head3 = p.shuffledArticlePolBrut4 # pB
                self.head4 = p.shuffledArticleLegBrut4 # lB

        # Round 3 ---------------------------------------------------------
        # check which round to not display articles twice
        elif self.articleSelectionRound == 3:
            # get random number from sequence modifier
            sequenceChosen = random.randint(1,6)

            for p in self.get_players():
                p.lastArticleChosenByTimeout = 0

                p.shuffledArticlePolBrut5 = itemgetter(4)(p.participant.vars["shuffledArticlesListPolBrut"])
                p.shuffledArticlePolBrut6 = itemgetter(5)(p.participant.vars["shuffledArticlesListPolBrut"])
                p.shuffledArticlePolBrut5 = p1.shuffledArticlePolBrut5
                p.shuffledArticlePolBrut6 = p1.shuffledArticlePolBrut6

                p.shuffledArticleLegBrut5 = itemgetter(4)(p.participant.vars["shuffledArticlesListLegBrut"])
                p.shuffledArticleLegBrut6 = itemgetter(5)(p.participant.vars["shuffledArticlesListLegBrut"])
                p.shuffledArticleLegBrut5 = p1.shuffledArticleLegBrut5
                p.shuffledArticleLegBrut6 = p1.shuffledArticleLegBrut6

            # check which sequence should be shown
            if sequenceChosen == 1: # pB pB lB lB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticlePolBrut5 # pB
                self.head2 = p.shuffledArticlePolBrut6 # pB
                self.head3 = p.shuffledArticleLegBrut5 # lB
                self.head4 = p.shuffledArticleLegBrut6 # lB
            elif sequenceChosen == 2: # pB lB pB lB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticlePolBrut5 # pB
                self.head2 = p.shuffledArticleLegBrut5 # lB
                self.head3 = p.shuffledArticlePolBrut6 # pB
                self.head4 = p.shuffledArticleLegBrut6 # lB
            elif sequenceChosen == 3: # pB lB lB pB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticlePolBrut5 # pB
                self.head2 = p.shuffledArticleLegBrut5 # lB
                self.head3 = p.shuffledArticleLegBrut6 # lB
                self.head4 = p.shuffledArticlePolBrut6 # pB
            elif sequenceChosen == 4: # lB pB lB pB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticleLegBrut5 # lB
                self.head2 = p.shuffledArticlePolBrut5 # pB
                self.head3 = p.shuffledArticleLegBrut6 # lB
                self.head4 = p.shuffledArticlePolBrut6 # pB
            elif sequenceChosen == 5: # lB lB pB pB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticleLegBrut5 # lB
                self.head2 = p.shuffledArticleLegBrut6 # lB
                self.head3 = p.shuffledArticlePolBrut5 # pB
                self.head4 = p.shuffledArticlePolBrut6 # pB
            else: # lB pB pB lB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticleLegBrut5 # lB
                self.head2 = p.shuffledArticlePolBrut5 # pB
                self.head3 = p.shuffledArticlePolBrut6 # pB
                self.head4 = p.shuffledArticleLegBrut6 # lB

        # Round 4 ---------------------------------------------------------
        # check which round to not display articles twice
        elif self.articleSelectionRound == 4:
            # get random number from sequence modifier
            sequenceChosen = random.randint(1,6)

            for p in self.get_players():
                p.lastArticleChosenByTimeout = 0

                p.shuffledArticlePolBrut7 = itemgetter(6)(p.participant.vars["shuffledArticlesListPolBrut"])
                p.shuffledArticlePolBrut8 = itemgetter(7)(p.participant.vars["shuffledArticlesListPolBrut"])
                p.shuffledArticlePolBrut7 = p1.shuffledArticlePolBrut7
                p.shuffledArticlePolBrut8 = p1.shuffledArticlePolBrut8

                p.shuffledArticleLegBrut7 = itemgetter(6)(p.participant.vars["shuffledArticlesListLegBrut"])
                p.shuffledArticleLegBrut8 = itemgetter(7)(p.participant.vars["shuffledArticlesListLegBrut"])
                p.shuffledArticleLegBrut7 = p1.shuffledArticleLegBrut7
                p.shuffledArticleLegBrut8 = p1.shuffledArticleLegBrut8

            # check which sequence should be shown
            if sequenceChosen == 1: # pB pB lB lB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticlePolBrut7 # pB
                self.head2 = p.shuffledArticlePolBrut8 # pB
                self.head3 = p.shuffledArticleLegBrut7 # lB
                self.head4 = p.shuffledArticleLegBrut8 # lB
            elif sequenceChosen == 2: # pB lB pB lB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticlePolBrut7 # pB
                self.head2 = p.shuffledArticleLegBrut7 # lB
                self.head3 = p.shuffledArticlePolBrut8 # pB
                self.head4 = p.shuffledArticleLegBrut8 # lB
            elif sequenceChosen == 3: # pB lB lB pB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticlePolBrut7 # pB
                self.head2 = p.shuffledArticleLegBrut7 # lB
                self.head3 = p.shuffledArticleLegBrut8 # lB
                self.head4 = p.shuffledArticlePolBrut8 # pB
            elif sequenceChosen == 4: # lB pB lB pB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticleLegBrut7 # lB
                self.head2 = p.shuffledArticlePolBrut7 # pB
                self.head3 = p.shuffledArticleLegBrut8 # lB
                self.head4 = p.shuffledArticlePolBrut8 # pB
            elif sequenceChosen == 5: # lB lB pB pB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticleLegBrut7 # lB
                self.head2 = p.shuffledArticleLegBrut8 # lB
                self.head3 = p.shuffledArticlePolBrut7 # pB
                self.head4 = p.shuffledArticlePolBrut8 # pB
            else: # lB pB pB lB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticleLegBrut7 # lB
                self.head2 = p.shuffledArticlePolBrut7 # pB
                self.head3 = p.shuffledArticlePolBrut8 # pB
                self.head4 = p.shuffledArticleLegBrut8 # lB

        # Round 5 ---------------------------------------------------------
        # check which round to not display articles twice
        elif self.articleSelectionRound == 5:
            # get random number from sequence modifier
            sequenceChosen = random.randint(1,6)

            for p in self.get_players():
                p.lastArticleChosenByTimeout = 0

                p.shuffledArticlePolBrut9 = itemgetter(8)(p.participant.vars["shuffledArticlesListPolBrut"])
                p.shuffledArticlePolBrut10 = itemgetter(9)(p.participant.vars["shuffledArticlesListPolBrut"])
                p.shuffledArticlePolBrut9 = p1.shuffledArticlePolBrut9
                p.shuffledArticlePolBrut10 = p1.shuffledArticlePolBrut10

                p.shuffledArticleLegBrut9 = itemgetter(8)(p.participant.vars["shuffledArticlesListLegBrut"])
                p.shuffledArticleLegBrut10 = itemgetter(9)(p.participant.vars["shuffledArticlesListLegBrut"])
                p.shuffledArticleLegBrut9 = p1.shuffledArticleLegBrut9
                p.shuffledArticleLegBrut10 = p1.shuffledArticleLegBrut10

            # check which sequence should be shown
            if sequenceChosen == 1: # pB pB lB lB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticlePolBrut9 # pB
                self.head2 = p.shuffledArticlePolBrut10 # pB
                self.head3 = p.shuffledArticleLegBrut9 # lB
                self.head4 = p.shuffledArticleLegBrut10 # lB
            elif sequenceChosen == 2: # pB lB pB lB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticlePolBrut9 # pB
                self.head2 = p.shuffledArticleLegBrut9 # lB
                self.head3 = p.shuffledArticlePolBrut10 # pB
                self.head4 = p.shuffledArticleLegBrut10 # lB
            elif sequenceChosen == 3: # pB lB lB pB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticlePolBrut9 # pB
                self.head2 = p.shuffledArticleLegBrut9 # lB
                self.head3 = p.shuffledArticleLegBrut10 # lB
                self.head4 = p.shuffledArticlePolBrut10 # pB
            elif sequenceChosen == 4: # lB pB lB pB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticleLegBrut9 # lB
                self.head2 = p.shuffledArticlePolBrut9 # pB
                self.head3 = p.shuffledArticleLegBrut10 # lB
                self.head4 = p.shuffledArticlePolBrut10 # pB
            elif sequenceChosen == 5: # lB lB pB pB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticleLegBrut9 # lB
                self.head2 = p.shuffledArticleLegBrut10 # lB
                self.head3 = p.shuffledArticlePolBrut9 # pB
                self.head4 = p.shuffledArticlePolBrut10 # pB
            else: # lB pB pB lB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticleLegBrut9 # lB
                self.head2 = p.shuffledArticlePolBrut9 # pB
                self.head3 = p.shuffledArticlePolBrut10 # pB
                self.head4 = p.shuffledArticleLegBrut10 # lB

        # Round 6 ---------------------------------------------------------
        # check which round to not display articles twice
        else:
            # get random number from sequence modifier
            sequenceChosen = random.randint(1,6)

            for p in self.get_players():
                p.lastArticleChosenByTimeout = 0

                p.shuffledArticlePolBrut11 = itemgetter(10)(p.participant.vars["shuffledArticlesListPolBrut"])
                p.shuffledArticlePolBrut12 = itemgetter(11)(p.participant.vars["shuffledArticlesListPolBrut"])
                p.shuffledArticlePolBrut11 = p1.shuffledArticlePolBrut11
                p.shuffledArticlePolBrut12 = p1.shuffledArticlePolBrut12

                p.shuffledArticleLegBrut11 = itemgetter(10)(p.participant.vars["shuffledArticlesListLegBrut"])
                p.shuffledArticleLegBrut12 = itemgetter(11)(p.participant.vars["shuffledArticlesListLegBrut"])
                p.shuffledArticleLegBrut11 = p1.shuffledArticleLegBrut11
                p.shuffledArticleLegBrut12 = p1.shuffledArticleLegBrut12

            # check which sequence should be shown
            if sequenceChosen == 1: # pB pB lB lB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticlePolBrut11 # pB
                self.head2 = p.shuffledArticlePolBrut12 # pB
                self.head3 = p.shuffledArticleLegBrut11 # lB
                self.head4 = p.shuffledArticleLegBrut12 # lB
            elif sequenceChosen == 2: # pB lB pB lB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticlePolBrut11 # pB
                self.head2 = p.shuffledArticleLegBrut11 # lB
                self.head3 = p.shuffledArticlePolBrut12 # pB
                self.head4 = p.shuffledArticleLegBrut12 # lB
            elif sequenceChosen == 3: # pB lB lB pB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticlePolBrut11 # pB
                self.head2 = p.shuffledArticleLegBrut11 # lB
                self.head3 = p.shuffledArticleLegBrut12 # lB
                self.head4 = p.shuffledArticlePolBrut12 # pB
            elif sequenceChosen == 4: # lB pB lB pB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticleLegBrut11 # lB
                self.head2 = p.shuffledArticlePolBrut11 # pB
                self.head3 = p.shuffledArticleLegBrut12 # lB
                self.head4 = p.shuffledArticlePolBrut12 # pB
            elif sequenceChosen == 5: # lB lB pB pB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticleLegBrut11 # lB
                self.head2 = p.shuffledArticleLegBrut12 # lB
                self.head3 = p.shuffledArticlePolBrut11 # pB
                self.head4 = p.shuffledArticlePolBrut12 # pB
            else: # lB pB pB lB
                # get shuffled article headings from list
                self.head1 = p.shuffledArticleLegBrut11 # lB
                self.head2 = p.shuffledArticlePolBrut11 # pB
                self.head3 = p.shuffledArticlePolBrut12 # pB
                self.head4 = p.shuffledArticleLegBrut12 # lB

    # Group-variables ---------------------------------------------------------
    articleCounter = models.IntegerField(initial=0)



    # Live method ---------------
    def live_decision(self, data, x):
        if data == 1:
            print("Data erste Player abgegeben = ", data)
            return {0: "<i>Ein*e Teilnehmer*in hat sich bereits entschieden</i>"}
        elif data == 2:
            print("Data erste Player abgegeben = ", data)
            return {0: "<i>Beide Teilnehmer*in haben sich bereits entschieden</i>"}
        else:
            pass



class Player(BasePlayer):
    shuffledArticlePolBrut1 = models.StringField()
    shuffledArticlePolBrut2 = models.StringField()
    shuffledArticlePolBrut3 = models.StringField()
    shuffledArticlePolBrut4 = models.StringField()
    shuffledArticlePolBrut5 = models.StringField()
    shuffledArticlePolBrut6 = models.StringField()
    shuffledArticlePolBrut7 = models.StringField()
    shuffledArticlePolBrut8 = models.StringField()
    shuffledArticlePolBrut9 = models.StringField()
    shuffledArticlePolBrut10 = models.StringField()
    shuffledArticlePolBrut11 = models.StringField()
    shuffledArticlePolBrut12 = models.StringField()

    shuffledArticleLegBrut1 = models.StringField()
    shuffledArticleLegBrut2 = models.StringField()
    shuffledArticleLegBrut3 = models.StringField()
    shuffledArticleLegBrut4 = models.StringField()
    shuffledArticleLegBrut5 = models.StringField()
    shuffledArticleLegBrut6 = models.StringField()
    shuffledArticleLegBrut7 = models.StringField()
    shuffledArticleLegBrut8 = models.StringField()
    shuffledArticleLegBrut9 = models.StringField()
    shuffledArticleLegBrut10 = models.StringField()
    shuffledArticleLegBrut11 = models.StringField()
    shuffledArticleLegBrut12 = models.StringField()

    # nickname which appears in the chat
    nickname = models.StringField()

    # singleplayer-condition
    singleplayer = models.IntegerField(initial = 0)

    # hypothesis-condition
    conditionHypothesis = models.StringField()

    # article selection
    selectedArticle = models.IntegerField(initial=0)

    # track which articles get selected
    firstArticle = models.IntegerField(initial = 0)
    secondArticle = models.IntegerField(initial = 0)
    thirdArticle = models.IntegerField(initial = 0)
    fourthArticle = models.IntegerField(initial = 0)
    fifthArticle = models.IntegerField(initial = 0)
    sixthArticle = models.IntegerField(initial = 0)
    seventhArticle = models.IntegerField(initial = 0)
    eigthArticle = models.IntegerField(initial = 0)
    ninethArticle = models.IntegerField(initial = 0)
    tenthArticle = models.IntegerField(initial = 0)
    eleventhArticle = models.IntegerField(initial = 0)
    twelvethArticle = models.IntegerField(initial = 0)
    thirteenthArticle = models.IntegerField(initial = 0)
    forteentethArticle = models.IntegerField(initial = 0)
    fifteenthArticle = models.IntegerField(initial = 0)
    sixteenthArticle = models.IntegerField(initial = 0)
    seventeenthArticle = models.IntegerField(initial = 0)
    eighteenthArticle = models.IntegerField(initial = 0)
    nineteenthArticle = models.IntegerField(initial = 0)
    twentiethArticle = models.IntegerField(initial = 0)
    twentyfirstArticle = models.IntegerField(initial = 0)
    twentysecondArticle = models.IntegerField(initial = 0)
    twentythirdArticle = models.IntegerField(initial = 0)
    twentyforthArticle = models.IntegerField(initial = 0)

    # selected articles list
    selectedArticlesList = models.LongStringField()

    # disagreement in article selection
    disagreementArticle = models.IntegerField(initial = 0)

    # which articles have been chosen by chance
    article1ChosenByChance = models.IntegerField(initial = 0)
    article2ChosenByChance = models.IntegerField(initial = 0)
    article3ChosenByChance = models.IntegerField(initial = 0)
    article4ChosenByChance = models.IntegerField(initial = 0)
    article5ChosenByChance = models.IntegerField(initial = 0)
    article6ChosenByChance = models.IntegerField(initial = 0)
    article7ChosenByChance = models.IntegerField(initial = 0)
    article8ChosenByChance = models.IntegerField(initial = 0)
    article9ChosenByChance = models.IntegerField(initial = 0)
    article10ChosenByChance = models.IntegerField(initial = 0)
    article11ChosenByChance = models.IntegerField(initial = 0)
    article12ChosenByChance = models.IntegerField(initial = 0)
    article13ChosenByChance = models.IntegerField(initial = 0)
    article14ChosenByChance = models.IntegerField(initial = 0)
    article15ChosenByChance = models.IntegerField(initial = 0)
    article16ChosenByChance = models.IntegerField(initial = 0)
    article17ChosenByChance = models.IntegerField(initial = 0)
    article18ChosenByChance = models.IntegerField(initial = 0)
    article19ChosenByChance = models.IntegerField(initial = 0)
    article20ChosenByChance = models.IntegerField(initial = 0)
    article21ChosenByChance = models.IntegerField(initial = 0)
    article22ChosenByChance = models.IntegerField(initial = 0)
    article23ChosenByChance = models.IntegerField(initial = 0)
    article24ChosenByChance = models.IntegerField(initial = 0)

    # save articles which where not selected due to chance
    chanceArticleNotSelectedR1 = models.IntegerField(initial = 0)
    chanceArticleNotSelectedR2 = models.IntegerField(initial = 0)
    chanceArticleNotSelectedR3 = models.IntegerField(initial = 0)
    chanceArticleNotSelectedR4 = models.IntegerField(initial = 0)
    chanceArticleNotSelectedR5 = models.IntegerField(initial = 0)
    chanceArticleNotSelectedR6 = models.IntegerField(initial = 0)

    # which articles have been chosen by majority
    article1ChosenByMajority = models.IntegerField(initial = 0)
    article2ChosenByMajority = models.IntegerField(initial = 0)
    article3ChosenByMajority = models.IntegerField(initial = 0)
    article4ChosenByMajority = models.IntegerField(initial = 0)
    article5ChosenByMajority = models.IntegerField(initial = 0)
    article6ChosenByMajority = models.IntegerField(initial = 0)
    article7ChosenByMajority = models.IntegerField(initial = 0)
    article8ChosenByMajority = models.IntegerField(initial = 0)
    article9ChosenByMajority = models.IntegerField(initial = 0)
    article10ChosenByMajority = models.IntegerField(initial = 0)
    article11ChosenByMajority = models.IntegerField(initial = 0)
    article12ChosenByMajority = models.IntegerField(initial = 0)
    article13ChosenByMajority = models.IntegerField(initial = 0)
    article14ChosenByMajority = models.IntegerField(initial = 0)
    article15ChosenByMajority = models.IntegerField(initial = 0)
    article16ChosenByMajority = models.IntegerField(initial = 0)
    article17ChosenByMajority = models.IntegerField(initial = 0)
    article18ChosenByMajority = models.IntegerField(initial = 0)
    article19ChosenByMajority = models.IntegerField(initial = 0)
    article20ChosenByMajority = models.IntegerField(initial = 0)
    article21ChosenByMajority = models.IntegerField(initial = 0)
    article22ChosenByMajority = models.IntegerField(initial = 0)
    article23ChosenByMajority = models.IntegerField(initial = 0)
    article24ChosenByMajority = models.IntegerField(initial = 0)

    # minority tag: save article which was not selected due to minority
    minorityArticleNotSelectedR1 = models.IntegerField(initial = 0)
    minorityArticleNotSelectedR2 = models.IntegerField(initial = 0)
    minorityArticleNotSelectedR3 = models.IntegerField(initial = 0)
    minorityArticleNotSelectedR4 = models.IntegerField(initial = 0)
    minorityArticleNotSelectedR5 = models.IntegerField(initial = 0)
    minorityArticleNotSelectedR6 = models.IntegerField(initial = 0)

    # record which articles were chosen by timeout (and chance)
    articleChosenByTimeout1 = models.IntegerField(initial = 0)
    articleChosenByTimeout2 = models.IntegerField(initial = 0)
    articleChosenByTimeout3 = models.IntegerField(initial = 0)
    articleChosenByTimeout4 = models.IntegerField(initial = 0)
    articleChosenByTimeout5 = models.IntegerField(initial = 0)
    articleChosenByTimeout6 = models.IntegerField(initial = 0)
    # variable to check every round and to display the random selection as information on the SelectedArticlePage
    lastArticleChosenByTimeout = models.IntegerField(initial = 0)



    # have there been a timeout? 0 = no, 1 = first selection, 2 = first and second selection
    # timeoutRound1 = models.IntegerField(initial=0)
    # timeoutRound2 = models.IntegerField(initial=0)
    # timeoutRound3 = models.IntegerField(initial=0)
    # timeoutRound4 = models.IntegerField(initial=0)
    # timeoutRound5 = models.IntegerField(initial=0)
    # timeoutRound6 = models.IntegerField(initial=0)



    # groupDecision
    groupDecision = models.IntegerField()
    groupMinorityDecision = models.IntegerField(initial=0)

    # individual decision
    individualDecision = models.IntegerField()
    certaintyIndDec = models.IntegerField()

    # disagreement in group decision
    disagreementGroupDecision = models.IntegerField()


    # Dependent Variables -----------------------------------------------------
    # Inklusivität des Problems
    policeBrutalityProblem = models.IntegerField() # Polizeigewalt ist ein Problem in Deutschland. stimme überhaupt nicht zu --> stimme völlig zu
    frequencyPoliceBrutality = models.IntegerField() # 0 = nie, 1 = Tag, 2 = Woche, 3 = Monat, 4 = Jahr, 5 = 10 Jahre
    # Verhaltensebene
    actionsAgainstPoliceBrutality = models.IntegerField()
    moreBrutalityPolice = models.IntegerField() # Die Polizei in Deutschland sollte mehr Gewalt einsetzen dürfen.
                                                # 1 = Stimme überhaupt nicht zu, 7 = Stimme völlig zu
    # Konfidenz
    confidencePoliceBrutality = models.IntegerField()
    # Kompetenzen
    moreCompetencesPolice = models.IntegerField() # Besitzt die Polizei in Deutschland ausreichend Befugnisse Gewalt anzuwenden, um ihre Aufgaben zu erfüllen?
                                                  # -> 1 = zu wenige, 7 = zu viele
    # -------------------------------------------------------------------------


    # Fragen nach den Suchstrategien -----------------------------------------
    searchStrategy = models.IntegerField() # 1 = Sucherg. bestätigten PolGew, 2 = Sucherg. bestätigten PolGew nicht, 0 = weder noch
    equalitySearchResults = models.IntegerField() # Die Suchergebnisse empfand ich als einsitig zu gunsten von..., 0 = Polizei, 9 = Demonstranten
    frequencySearchResults = models.IntegerField() # Wie beurteilen Sie die Anzahl der zur Verfügung stehenden Suchergebnisse? 0 = mehr mit Polizeigewalt, 9 = mehr ohne Polizeigewalt
    # -------------------------------------------------------------------------


    # The Attitudes Towards Violence Scale (Funk et al., 1999) ----------------
    violenceAttitude1 = models.IntegerField() # Ich versuche mich von Orten an denen es warscheinlich zu Gewalt kommt, fern zu halten.
    violenceAttitude2 = models.IntegerField() # Menschen, die Gewalt einsetzen, werden respektiert.
    violenceAttitude3 = models.IntegerField() # Wenn dir eine Person wehtut, solltest Du zurückschlagen.
    # -------------------------------------------------------------------------


    # vertrauenswürdigkeit der Artikel ----------------------------------------
    trustArticles = models.IntegerField() #
    # -------------------------------------------------------------------------
