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
	players_per_group = 2
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
			if time.time() - p.participant.vars["arrivalTime"] > 6*60: # adjust time?
				# if it does make them singleplayer
				p.singleplayer = 1
				# and move them foreward
				return [p]
			else:
				pass
	# -------------------------------------------------------------------------


class Group(BaseGroup):
	# Group variables ---------------------------------------------------------
	# article headings for page
	head1 = models.StringField(initial=None)
	head2 = models.StringField(initial=None)
	head3 = models.StringField(initial=None)
	head4 = models.StringField(initial=None)

	# prepare articles which should be displayed on the chat page
	articleSelectionRound = models.IntegerField(initial = 1)

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




	# check for disagreement in SE selection 1 -----------------------------
	def check_for_article_selection1(self):

		# get variables to work with
		players = self.get_players()
		p1 = self.get_player_by_id(1)
		p2 = self.get_player_by_id(2)

		round = self.articleSelectionRound


		for p in players:

			p.disagreement1 = 0 # reset disagreement-variables from last round

		# when all players produce timeout
		if p1.selectedSR == 99 and p2.selectedSR == 99:
			print("Round " + str(self.articleSelectionRound) + ", 1st Selection: All players produced a timeout\n")
			print("Selection P1: " + str(p1.selectedSR) + "\n")
			print("Selection P2: " + str(p2.selectedSR) + "\n")


			for p in players:

				p.disagreement1 = 1 # internal disagreement-variable

				p.selectedSR = 0 # reset selected SE

				if round == 1: # check which round
					p.timeoutSel1R1 = 1
				elif round == 2: # check which round
					p.timeoutSel1R2 = 1
				elif round == 3: # check which round
					p.timeoutSel1R3 = 1
				elif round == 4: # check which round
					p.timeoutSel1R4 = 1
				elif round == 5: # check which round
					p.timeoutSel1R5 = 1
				else:
					p.timeoutSel1R6 = 1

		# when all players select same article
		elif p1.selectedSR == p2.selectedSR:
			print("Round " + str(self.articleSelectionRound) + ", 1st Selection: All players agree\n")
			print("Selection P1: " + str(p1.selectedSR) + "\n")
			print("Selection P2: " + str(p2.selectedSR) + "\n")


			# increase articleSelectionRound
			#self.articleSelectionRound += 1
			#self.player.articleSelectionRoundInd += 1

			for p in players:

				if round == 1:
					p.SRseenR1 = p.selectedSR # save which SR was seen
					p.SRindSelR1 = p.selectedSR # save which SR has been selected
				elif round == 2:
					p.SRseenR2 = p.selectedSR # save which SR was seen
					p.SRindSelR2 = p.selectedSR # save which SR has been selected
				elif round == 3:
					p.SRseenR3 = p.selectedSR # save which SR was seen
					p.SRindSelR3 = p.selectedSR # save which SR has been selected
				elif round == 4:
					p.SRseenR4 = p.selectedSR # save which SR was seen
					p.SRindSelR4 = p.selectedSR # save which SR has been selected
				elif round == 5:
					p.SRseenR5 = p.selectedSR # save which SR was seen
					p.SRindSelR5 = p.selectedSR # save which SR has been selected
				else:
					p.SRseenR6 = p.selectedSR # save which SR was seen
					p.SRindSelR6 = p.selectedSR # save which SR has been selected

		# when somone has not chosen the same as the others
		else:
			print("Round " + str(self.articleSelectionRound) + ", 1st Selection: Not all players agree\n")
			print("Selection P1: " + str(p1.selectedSR) + "\n")
			print("Selection P2: " + str(p2.selectedSR) + "\n")


			for p in players:
				p.disagreement1 = 1 # increase disagreement-help-var

				# save disagreement
				if round == 1:
					p.disagreementSel1R1 = 1

					# if participant produced timeout
					if p.selectedSR == 99: 	# get timeout
						p.timeoutSel1R1 = 1 # save timeout

				elif round == 2:
					p.disagreementSel1R2 = 1

					# if participant produced timeout
					if p.selectedSR == 99: 	# get timeout
						p.timeoutSel1R2 = 1 # save timeout

				elif round == 3:
					p.disagreementSel1R3 = 1

					# if participant produced timeout
					if p.selectedSR == 99: 	# get timeout
						p.timeoutSel1R3 = 1 # save timeout

				elif round == 4:
					p.disagreementSel1R4 = 1

					# if participant produced timeout
					if p.selectedSR == 99: 	# get timeout
						p.timeoutSel1R4 = 1 # save timeout

				elif round == 5:
					p.disagreementSel1R5 = 1

					# if participant produced timeout
					if p.selectedSR == 99: 	# get timeout
						p.timeoutSel1R5 = 1 # save timeout

				else:
					p.disagreementSel1R6 = 1

					# if participant produced timeout
					if p.selectedSR == 99: 	# get timeout
						p.timeoutSel1R6 = 1 # save timeout

				p.selectedSR = 0 	# reset selected SR





	# check for disagreement in SE selection two
	def check_for_article_selection2(self): # ---------------------------------
		import random

		# get variables
		players = self.get_players()
		p1 = self.get_player_by_id(1)
		p2 = self.get_player_by_id(2)

		round = self.articleSelectionRound




		# check if selections match

		# if timeout by all ----------------------
		if p1.SRbyTimeout == 1 and p2.SRbyTimeout == 1:
			print("Round " + str(self.articleSelectionRound) + ", 2nd Selection: All players produced timeout\n")
			print("Timeout P1: " + str(p1.SRbyTimeout) + "\n")
			print("Timeout P2: " + str(p2.SRbyTimeout) + "\n")

			#self.articleSelectionRound += 1
			#self.player.articleSelectionRoundInd += 1

			for p in players:
				# timeoutRoundX += 1

				# randomSEfromTimeoutRoundX = 1
				if round == 1:
					p.randomByTimeoutR1 = 1 # overall selection by timeout?
					p.SRseenR1 = p.selectedSR # save which SR was seen
					# -> this works bc on ChatPage I select one random article for
					# 	 all players if certain time is over. So this is specified
					#	 on the page
					p.timeoutSel2R1 = 1 # save that timeout haopend
				elif round == 2:
					p.randomByTimeoutR2 = 1 # overall selection by timeout?
					p.SRseenR2 = p.selectedSR # save which SR was seen
					p.timeoutSel2R2 = 1
				elif round == 3:
					p.randomByTimeoutR3 = 1 # overall selection by timeout?
					p.SRseenR3 = p.selectedSR # save which SR was seen
					p.timeoutSel2R3 = 1
				elif round == 4:
					p.randomByTimeoutR4 = 1 # overall selection by timeout?
					p.SRseenR4 = p.selectedSR # save which SR was seen
					p.timeoutSel2R4 = 1
				elif round == 5:
					p.randomByTimeoutR5 = 1 # overall selection by timeout?
					p.SRseenR5 = p.selectedSR # save which SR was seen
					p.timeoutSel2R5 = 1
				else:
					p.randomByTimeoutR6 = 1 # overall selection by timeout?
					p.SRseenR6 = p.selectedSR # save which SR was seen
					p.timeoutSel2R6 = 1


		# elif all agree ---------------------
		elif p1.selectedSR == p2.selectedSR:
			# do not need to check for timeout that happend because first if-statement
			#	is evaluated false if this gets executed. First if-statement is automatically
			#	true if all produce timeout and timeout production is evaluated on html-Page

			print("Round " + str(self.articleSelectionRound) + ", 2nd Selection: All players agree\n")
			print("Selection P1: " + str(p1.selectedSR) + "\n")
			print("Selection P2: " + str(p2.selectedSR) + "\n")


			#self.articleSelectionRound += 1
			#self.player.articleSelectionRoundInd += 1

			# for all palyers
			for p in players:

				# check round
				if round == 1:
					p.SRindSelR1 = p.selectedSR # save individual selection
					p.SRseenR1 = p.selectedSR	# save which article hase been seen
				elif round == 2:
					p.SRindSelR2 = p.selectedSR
					p.SRseenR2 = p.selectedSR
				elif round == 3:
					p.SRindSelR3 = p.selectedSR
					p.SRseenR3 = p.selectedSR
				elif round == 4:
					p.SRindSelR4 = p.selectedSR
					p.SRseenR4 = p.selectedSR
				elif round == 5:
					p.SRindSelR5 = p.selectedSR
					p.SRseenR5 = p.selectedSR
				else:
					p.SRindSelR6 = p.selectedSR
					p.SRseenR6 = p.selectedSR


			# save ind selection
			# save group selection
			# save round

		# # elif two agree
		# elif p1.selectedSR == p2.selectedSR and p1.SRbyTimeout == 0: # 1 and two agree
		# 	print("Round " + str(self.articleSelectionRound) + ", 2nd Selection: Two players agree\n")
		# 	print("Selection P1: " + str(p1.selectedSR) + "\n")
		# 	print("Selection P2: " + str(p2.selectedSR) + "\n")
		# 	print("Selection P3: " + str(p3.selectedSR) + "\n")
		#
		#
		# 	#self.articleSelectionRound += 1
		# 	#self.player.articleSelectionRoundInd += 1
		#
		# 	if round == 1:
		#
		# 		# save majority and minority
		# 		p1.majorityR1 = 1
		# 		p2.majorityR1 = 1
		# 		p3.minorityR1 = 1
		#
		# 		for p in players:
		#
		# 			p.SRindSelR1 = p.selectedSR  # save every individual selection
		# 			p.SRseenR1 = p1.selectedSR	 # save for all players which article will be displayed
		# 			p.selectedSR = p1.selectedSR # give all players the same SR
		# 			p.disagreementSel2R1 = 1	 # save that there was disagreement
		#
		# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
		# 				p.timeoutSel2R1 = 1
		# 			else:
		# 				pass
		#
		# 	elif round == 2:
		#
		# 		# save majority and minority
		# 		p1.majorityR2 = 1
		# 		p2.majorityR2 = 1
		# 		p3.minorityR2 = 1
		#
		# 		for p in players:
		#
		# 			p.SRindSelR2 = p.selectedSR  # save every individual selection
		# 			p.SRseenR2 = p1.selectedSR	 # save for all players which article will be displayed
		# 			p.selectedSR = p1.selectedSR # give all players the same SR
		# 			p.disagreementSel2R2 = 1	 # save that there was disagreement
		#
		# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
		# 				p.timeoutSel2R2 = 1
		# 			else:
		# 				pass
		#
		# 	elif round == 3:
		#
		# 		# save majority and minority
		# 		p1.majorityR3 = 1
		# 		p2.majorityR3 = 1
		# 		p3.minorityR3 = 1
		#
		# 		for p in players:
		#
		# 			p.SRindSelR3 = p.selectedSR  # save every individual selection
		# 			p.SRseenR3 = p1.selectedSR	 # save for all players which article will be displayed
		# 			p.selectedSR = p1.selectedSR # give all players the same SR
		# 			p.disagreementSel2R3 = 1	 # save that there was disagreement
		#
		# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
		# 				p.timeoutSel2R3 = 1
		# 			else:
		# 				pass
		#
		# 	elif round == 4:
		#
		# 		# save majority and minority
		# 		p1.majorityR4 = 1
		# 		p2.majorityR4 = 1
		# 		p3.minorityR4 = 1
		#
		# 		for p in players:
		#
		# 			p.SRindSelR4 = p.selectedSR  # save every individual selection
		# 			p.SRseenR4 = p1.selectedSR	 # save for all players which article will be displayed
		# 			p.selectedSR = p1.selectedSR # give all players the same SR
		# 			p.disagreementSel2R4 = 1	 # save that there was disagreement
		#
		# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
		# 				p.timeoutSel2R4 = 1
		# 			else:
		# 				pass
		#
		# 	elif round == 5:
		#
		# 		# save majority and minority
		# 		p1.majorityR5 = 1
		# 		p2.majorityR5 = 1
		# 		p3.minorityR5 = 1
		#
		# 		for p in players:
		#
		# 			p.SRindSelR5 = p.selectedSR  # save every individual selection
		# 			p.SRseenR5 = p1.selectedSR	 # save for all players which article will be displayed
		# 			p.selectedSR = p1.selectedSR # give all players the same SR
		# 			p.disagreementSel2R5 = 1	 # save that there was disagreement
		#
		# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
		# 				p.timeoutSel2R5 = 1
		# 			else:
		# 				pass
		#
		# 	else:
		#
		# 		# save majority and minority
		# 		p1.majorityR6 = 1
		# 		p2.majorityR6 = 1
		# 		p3.minorityR6 = 1
		#
		# 		for p in players:
		#
		# 			p.SRindSelR6 = p.selectedSR  # save every individual selection
		# 			p.SRseenR6 = p1.selectedSR	 # save for all players which article will be displayed
		# 			p.selectedSR = p1.selectedSR # give all players the same SR
		# 			p.disagreementSel2R6 = 1	 # save that there was disagreement
		#
		# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
		# 				p.timeoutSel2R6 = 1
		# 			else:
		# 				pass
		#

		# elif two agree
		# elif p1.selectedSR == p3.selectedSR and p1.SRbyTimeout == 0: # 1 and two agree
		# 	print("Round " + str(self.articleSelectionRound) + ", 2nd Selection: Two players agree\n")
		# 	print("Selection P1: " + str(p1.selectedSR) + "\n")
		# 	print("Selection P2: " + str(p2.selectedSR) + "\n")
		# 	print("Selection P3: " + str(p3.selectedSR) + "\n")
		#
		#
		# 	#self.articleSelectionRound += 1
		# 	#self.player.articleSelectionRoundInd += 1
		#
		# 	if round == 1:
		#
		# 		# save majority and minority
		# 		p1.majorityR1 = 1
		# 		p3.majorityR1 = 1
		# 		p2.minorityR1 = 1
		#
		# 		for p in players:
		#
		# 			p.SRindSelR1 = p.selectedSR  # save every individual selection
		# 			p.SRseenR1 = p1.selectedSR	 # save for all players which article will be displayed
		# 			p.selectedSR = p1.selectedSR # give all players the same SR
		# 			p.disagreementSel2R1 = 1	 # save that there was disagreement
		#
		# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
		# 				p.timeoutSel2R1 = 1
		# 			else:
		# 				pass
		#
		# 	elif round == 2:
		#
		# 		# save majority and minority
		# 		p1.majorityR2 = 1
		# 		p3.majorityR2 = 1
		# 		p2.minorityR2 = 1
		#
		# 		for p in players:
		#
		# 			p.SRindSelR2 = p.selectedSR  # save every individual selection
		# 			p.SRseenR2 = p1.selectedSR	 # save for all players which article will be displayed
		# 			p.selectedSR = p1.selectedSR # give all players the same SR
		# 			p.disagreementSel2R2 = 1	 # save that there was disagreement
		#
		# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
		# 				p.timeoutSel2R2 = 1
		# 			else:
		# 				pass
		#
		# 	elif round == 3:
		#
		# 		# save majority and minority
		# 		p1.majorityR3 = 1
		# 		p3.majorityR3 = 1
		# 		p2.minorityR3 = 1
		#
		# 		for p in players:
		#
		# 			p.SRindSelR3 = p.selectedSR  # save every individual selection
		# 			p.SRseenR3 = p1.selectedSR	 # save for all players which article will be displayed
		# 			p.selectedSR = p1.selectedSR # give all players the same SR
		# 			p.disagreementSel2R3 = 1	 # save that there was disagreement
		#
		# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
		# 				p.timeoutSel2R3 = 1
		# 			else:
		# 				pass
		#
		# 	elif round == 4:
		#
		# 		# save majority and minority
		# 		p1.majorityR4 = 1
		# 		p3.majorityR4 = 1
		# 		p2.minorityR4 = 1
		#
		# 		for p in players:
		#
		# 			p.SRindSelR4 = p.selectedSR  # save every individual selection
		# 			p.SRseenR4 = p1.selectedSR	 # save for all players which article will be displayed
		# 			p.selectedSR = p1.selectedSR # give all players the same SR
		# 			p.disagreementSel2R4 = 1	 # save that there was disagreement
		#
		# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
		# 				p.timeoutSel2R4 = 1
		# 			else:
		# 				pass
		#
		# 	elif round == 5:
		#
		# 		# save majority and minority
		# 		p1.majorityR5 = 1
		# 		p3.majorityR5 = 1
		# 		p2.minorityR5 = 1
		#
		# 		for p in players:
		#
		# 			p.SRindSelR5 = p.selectedSR  # save every individual selection
		# 			p.SRseenR5 = p1.selectedSR	 # save for all players which article will be displayed
		# 			p.selectedSR = p1.selectedSR # give all players the same SR
		# 			p.disagreementSel2R5 = 1	 # save that there was disagreement
		#
		# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
		# 				p.timeoutSel2R5 = 1
		# 			else:
		# 				pass
		#
		# 	else:
		#
		# 		# save majority and minority
		# 		p1.majorityR6 = 1
		# 		p3.majorityR6 = 1
		# 		p2.minorityR6 = 1
		#
		# 		for p in players:
		#
		# 			p.SRindSelR6 = p.selectedSR  # save every individual selection
		# 			p.SRseenR6 = p1.selectedSR	 # save for all players which article will be displayed
		# 			p.selectedSR = p1.selectedSR # give all players the same SR
		# 			p.disagreementSel2R6 = 1	 # save that there was disagreement
		#
		# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
		# 				p.timeoutSel2R6 = 1
		# 			else:
		# 				pass
		#
		#
		# # elif two agree
		# elif p2.selectedSR == p3.selectedSR and p2.SRbyTimeout == 0: # 1 and two agree
		# 	print("Round " + str(self.articleSelectionRound) + ", 2nd Selection: Two players agree\n")
		# 	print("Selection P1: " + str(p1.selectedSR) + "\n")
		# 	print("Selection P2: " + str(p2.selectedSR) + "\n")
		# 	print("Selection P3: " + str(p3.selectedSR) + "\n")
		#
		#
		# 	#self.articleSelectionRound += 1
		# 	#self.player.articleSelectionRoundInd += 1
		#
		# 	if round == 1:
		#
		# 		# save majority and minority
		# 		p2.majorityR1 = 1
		# 		p3.majorityR1 = 1
		# 		p1.minorityR1 = 1
		#
		# 		for p in players:
		#
		# 			p.SRindSelR1 = p.selectedSR  # save every individual selection
		# 			p.SRseenR1 = p2.selectedSR	 # save for all players which article will be displayed
		# 			p.selectedSR = p2.selectedSR # give all players the same SR
		# 			p.disagreementSel2R1 = 1	 # save that there was disagreement
		#
		# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
		# 				p.timeoutSel2R1 = 1
		# 			else:
		# 				pass
		#
		# 	elif round == 2:
		#
		# 		# save majority and minority
		# 		p2.majorityR2 = 1
		# 		p3.majorityR2 = 1
		# 		p1.minorityR2 = 1
		#
		# 		for p in players:
		#
		# 			p.SRindSelR2 = p.selectedSR  # save every individual selection
		# 			p.SRseenR2 = p2.selectedSR	 # save for all players which article will be displayed
		# 			p.selectedSR = p2.selectedSR # give all players the same SR
		# 			p.disagreementSel2R2 = 1	 # save that there was disagreement
		#
		# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
		# 				p.timeoutSel2R2 = 1
		# 			else:
		# 				pass
		#
		# 	elif round == 3:
		#
		# 		# save majority and minority
		# 		p2.majorityR3 = 1
		# 		p3.majorityR3 = 1
		# 		p1.minorityR3 = 1
		#
		# 		for p in players:
		#
		# 			p.SRindSelR3 = p.selectedSR  # save every individual selection
		# 			p.SRseenR3 = p2.selectedSR	 # save for all players which article will be displayed
		# 			p.selectedSR = p2.selectedSR # give all players the same SR
		# 			p.disagreementSel2R3 = 1	 # save that there was disagreement
		#
		# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
		# 				p.timeoutSel2R3 = 1
		# 			else:
		# 				pass
		#
		# 	elif round == 4:
		#
		# 		# save majority and minority
		# 		p2.majorityR4 = 1
		# 		p3.majorityR4 = 1
		# 		p1.minorityR4 = 1
		#
		# 		for p in players:
		#
		# 			p.SRindSelR4 = p.selectedSR  # save every individual selection
		# 			p.SRseenR4 = p2.selectedSR	 # save for all players which article will be displayed
		# 			p.selectedSR = p2.selectedSR # give all players the same SR
		# 			p.disagreementSel2R4 = 1	 # save that there was disagreement
		#
		# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
		# 				p.timeoutSel2R4 = 1
		# 			else:
		# 				pass
		#
		# 	elif round == 5:
		#
		# 		# save majority and minority
		# 		p2.majorityR5 = 1
		# 		p3.majorityR5 = 1
		# 		p1.minorityR5 = 1
		#
		# 		for p in players:
		#
		# 			p.SRindSelR5 = p.selectedSR  # save every individual selection
		# 			p.SRseenR5 = p2.selectedSR	 # save for all players which article will be displayed
		# 			p.selectedSR = p2.selectedSR # give all players the same SR
		# 			p.disagreementSel2R5 = 1	 # save that there was disagreement
		#
		# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
		# 				p.timeoutSel2R5 = 1
		# 			else:
		# 				pass
		#
		# 	else:
		#
		# 		# save majority and minority
		# 		p2.majorityR6 = 1
		# 		p3.majorityR6 = 1
		# 		p1.minorityR6 = 1
		#
		# 		for p in players:
		#
		# 			p.SRindSelR6 = p.selectedSR  # save every individual selection
		# 			p.SRseenR6 = p2.selectedSR	 # save for all players which article will be displayed
		# 			p.selectedSR = p2.selectedSR # give all players the same SR
		# 			p.disagreementSel2R6 = 1	 # save that there was disagreement
		#
		# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
		# 				p.timeoutSel2R6 = 1
		# 			else:
		# 				pass
		#
		#

		# if nobody agrees and there is no timeout
		elif p1.selectedSR != p2.selectedSR:
			print("Round " + str(self.articleSelectionRound) + ", 2nd Selection: All players disagree\n")
			print("Selection P1: " + str(p1.selectedSR) + "\n")
			print("Selection P2: " + str(p2.selectedSR) + "\n")

			# checking var for
			check = 0

			#self.articleSelectionRound += 1
			#self.get_players().player.articleSelectionRoundInd += 1

			# iterate through this loop as long as pR has not produced a timeout
			#	-> otherwise I would choose the randomly selected search-result of
			#	   that participant, who has produced a timeout
			while check == 0:

				# choose a random player
				randInt = random.randint(1,2)
				pR = self.get_player_by_id(randInt)

				if round == 1 and pR.SRbyTimeout == 0:

					check = 1

					for p in players:

						p.SRindSelR1 = p.selectedSR  # save every individual selection
						p.SRseenR1 = pR.selectedSR   # save for all players which article will be displayed
						p.selectedSR = pR.selectedSR # give all players the same SR
						p.disagreementSel2R1 = 1 	 # save that there was disagreement
						p.randomByDisagreementR1 = 1 # save if random selection was due to disagreement

						if p.SRbyTimeout == 1:		 # if player produced timeout than save it
							p.timeoutSel2R1 = 1
						else:
							pass

				elif round == 2 and pR.SRbyTimeout == 0:

					check = 1

					for p in players:

						p.SRindSelR2 = p.selectedSR  # save every individual selection
						p.SRseenR2 = pR.selectedSR   # save for all players which article will be displayed
						p.selectedSR = pR.selectedSR # give all players the same SR
						p.disagreementSel2R2 = 1 	 # save that there was disagreement
						p.randomByDisagreementR2 = 1 # save if random selection was du to disagreement

						if p.SRbyTimeout == 1:		 # if player produced timeout than save it
							p.timeoutSel2R2 = 1
						else:
							pass

				elif round == 3 and pR.SRbyTimeout == 0:

					check = 1

					for p in players:

						p.SRindSelR3 = p.selectedSR  # save every individual selection
						p.SRseenR3 = pR.selectedSR   # save for all players which article will be displayed
						p.selectedSR = pR.selectedSR # give all players the same SR
						p.disagreementSel2R3 = 1 	 # save that there was disagreement
						p.randomByDisagreementR3 = 1 # save if random selection was du to disagreement

						if p.SRbyTimeout == 1:		 # if player produced timeout than save it
							p.timeoutSel2R3 = 1
						else:
							pass

				elif round == 4 and pR.SRbyTimeout == 0:

					check = 1

					for p in players:

						p.SRindSelR4 = p.selectedSR  # save every individual selection
						p.SRseenR4 = pR.selectedSR   # save for all players which article will be displayed
						p.selectedSR = pR.selectedSR # give all players the same SR
						p.disagreementSel2R4 = 1 	 # save that there was disagreement
						p.randomByDisagreementR4 = 1 # save if random selection was du to disagreement

						if p.SRbyTimeout == 1:		 # if player produced timeout than save it
							p.timeoutSel2R4 = 1
						else:
							pass

				elif round == 5 and pR.SRbyTimeout == 0:

					check = 1

					for p in players:

						p.SRindSelR5 = p.selectedSR  # save every individual selection
						p.SRseenR5 = pR.selectedSR   # save for all players which article will be displayed
						p.selectedSR = pR.selectedSR # give all players the same SR
						p.disagreementSel2R5 = 1 	 # save that there was disagreement
						p.randomByDisagreementR5 = 1 # save if random selection was du to disagreement

						if p.SRbyTimeout == 1:		 # if player produced timeout than save it
							p.timeoutSel2R5 = 1
						else:
							pass

				elif round == 6 and pR.SRbyTimeout == 0:

					check = 1

					for p in players:

						p.SRindSelR6 = p.selectedSR  # save every individual selection
						p.SRseenR6 = pR.selectedSR   # save for all players which article will be displayed
						p.selectedSR = pR.selectedSR # give all players the same SR
						p.disagreementSel2R6 = 1 	 # save that there was disagreement
						p.randomByDisagreementR6 = 1 # save if random selection was du to disagreement

						if p.SRbyTimeout == 1:		 # if player produced timeout than save it
							p.timeoutSel2R6 = 1
						else:
							pass

				else:
					pass

		else: # e.g. two players time out and one selects article
			print("Irgendwas läuft hier, was ich nicht antizipiert habe")

			# # checking var for
			# noTimeoutPlayer = 0
			#
			#
			# while noTimeoutPlayer == 0:
			#
			# 	# choose a random player
			# 	randInt = random.randint(1,3)
			# 	pR = self.get_player_by_id(randInt)
			#
			# 	if round == 1 and pR.SRbyTimeout == 0:
			# 		for p in players:
			#
			# 			p.SRindSelR1 = p.selectedSR  # save every individual selection
			# 			p.SRseenR1 = pR.selectedSR   # save for all players which article will be displayed
			# 			p.selectedSR = pR.selectedSR # give all players the same SR
			# 			p.disagreementSel2R1 = 1 	 # save that there was disagreement
			#
			# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
			# 				p.timeoutSel2R1 = 1
			# 			else:
			# 				pass
			#
			# 		noTimeoutPlayer = 1
			#
			# 	elif round == 2 and pR.SRbyTimeout == 0:
			# 		for p in players:
			#
			# 			p.SRindSelR2 = p.selectedSR  # save every individual selection
			# 			p.SRseenR2 = pR.selectedSR   # save for all players which article will be displayed
			# 			p.selectedSR = pR.selectedSR # give all players the same SR
			# 			p.disagreementSel2R2 = 1 	 # save that there was disagreement
			#
			# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
			# 				p.timeoutSel2R2 = 1
			# 			else:
			# 				pass
			#
			# 		noTimeoutPlayer = 1
			#
			# 	elif round == 3 and pR.SRbyTimeout == 0:
			# 		for p in players:
			#
			# 			p.SRindSelR3 = p.selectedSR  # save every individual selection
			# 			p.SRseenR3 = pR.selectedSR   # save for all players which article will be displayed
			# 			p.selectedSR = pR.selectedSR # give all players the same SR
			# 			p.disagreementSel2R3 = 1 	 # save that there was disagreement
			#
			# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
			# 				p.timeoutSel2R3 = 1
			# 			else:
			# 				pass
			#
			# 		noTimeoutPlayer = 1
			#
			# 	elif round == 4 and pR.SRbyTimeout == 0:
			# 		for p in players:
			#
			# 			p.SRindSelR4 = p.selectedSR  # save every individual selection
			# 			p.SRseenR4 = pR.selectedSR   # save for all players which article will be displayed
			# 			p.selectedSR = pR.selectedSR # give all players the same SR
			# 			p.disagreementSel2R4 = 1 	 # save that there was disagreement
			#
			# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
			# 				p.timeoutSel2R4 = 1
			# 			else:
			# 				pass
			#
			# 		noTimeoutPlayer = 1
			#
			# 	elif round == 5 and pR.SRbyTimeout == 0:
			# 		for p in players:
			#
			# 			p.SRindSelR5 = p.selectedSR  # save every individual selection
			# 			p.SRseenR5 = pR.selectedSR   # save for all players which article will be displayed
			# 			p.selectedSR = pR.selectedSR # give all players the same SR
			# 			p.disagreementSel2R5 = 1 	 # save that there was disagreement
			#
			# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
			# 				p.timeoutSel2R5 = 1
			# 			else:
			# 				pass
			#
			# 		noTimeoutPlayer = 1
			#
			# 	elif round == 6 and pR.SRbyTimeout == 0:
			# 		for p in players:
			#
			# 			p.SRindSelR6 = p.selectedSR  # save every individual selection
			# 			p.SRseenR6 = pR.selectedSR   # save for all players which article will be displayed
			# 			p.selectedSR = pR.selectedSR # give all players the same SR
			# 			p.disagreementSel2R6 = 1 	 # save that there was disagreement
			#
			# 			if p.SRbyTimeout == 1:		 # if player produced timeout than save it
			# 				p.timeoutSel2R6 = 1
			# 			else:
			# 				pass
			#
			# 		noTimeoutPlayer = 1
			#
			# 	else:
			# 		print("first try to select right player")




	def prepare_displayed_articles(self):
		from operator import itemgetter
		import random

		p1 = self.get_player_by_id(1)
		# p2 = self.get_player_by_id(2)
		# p3 = self.get_player_by_id(3)

        ##### possible sequences: #####
        #    | S1) S2) S3) S4) S5) S6)#
        # --------------------------- #
        # A1 | pB  pB  pB  lB  lB  lB #
        # A2 | pB  lB  lB  pB  lB  pB #
        # A3 | lB  pB  lB  lB  pB  pB #
        # A4 | lB  lB  pB  pB  pB  lB #
        ###############################

		round = self.articleSelectionRound
		players = self.get_players()

        # Round 1 ---------------------------------------------------------
        # check which round to not display articles twice
		if round == 1:
            # get random number from sequence modifier
			sequenceChosen = random.randint(1,6)

			for p in players:

				p.articleByTimeout = 0
				p.SRbyTimeout = 0

				p.shuffledArticlePolBrut1 = itemgetter(0)(p1.participant.vars["shuffledArticlesListPolBrut"])
				p.shuffledArticlePolBrut2 = itemgetter(1)(p1.participant.vars["shuffledArticlesListPolBrut"])

				p.shuffledArticleLegBrut1 = itemgetter(0)(p1.participant.vars["shuffledArticlesListLegBrut"])
				p.shuffledArticleLegBrut2 = itemgetter(1)(p1.participant.vars["shuffledArticlesListLegBrut"])

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
		elif round == 2:
            # get random number from sequence modifier
			sequenceChosen = random.randint(1,6)

			for p in players:

				p.SRbyTimeout = 0
				p.articleByTimeout = 0

				p.shuffledArticlePolBrut3 = itemgetter(2)(p1.participant.vars["shuffledArticlesListPolBrut"])
				p.shuffledArticlePolBrut4 = itemgetter(3)(p1.participant.vars["shuffledArticlesListPolBrut"])
				# p.shuffledArticlePolBrut3 = p1.shuffledArticlePolBrut3
				# p.shuffledArticlePolBrut4 = p1.shuffledArticlePolBrut4

				p.shuffledArticleLegBrut3 = itemgetter(2)(p1.participant.vars["shuffledArticlesListLegBrut"])
				p.shuffledArticleLegBrut4 = itemgetter(3)(p1.participant.vars["shuffledArticlesListLegBrut"])
				# p.shuffledArticleLegBrut3 = p1.shuffledArticleLegBrut3
				# p.shuffledArticleLegBrut4 = p1.shuffledArticleLegBrut4

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
		elif round == 3:
            # get random number from sequence modifier
			sequenceChosen = random.randint(1,6)

			for p in players:

				p.SRbyTimeout = 0
				p.articleByTimeout = 0

				p.shuffledArticlePolBrut5 = itemgetter(4)(p1.participant.vars["shuffledArticlesListPolBrut"])
				p.shuffledArticlePolBrut6 = itemgetter(5)(p1.participant.vars["shuffledArticlesListPolBrut"])
				# p.shuffledArticlePolBrut5 = p1.shuffledArticlePolBrut5
				# p.shuffledArticlePolBrut6 = p1.shuffledArticlePolBrut6

				p.shuffledArticleLegBrut5 = itemgetter(4)(p1.participant.vars["shuffledArticlesListLegBrut"])
				p.shuffledArticleLegBrut6 = itemgetter(5)(p1.participant.vars["shuffledArticlesListLegBrut"])
				# p.shuffledArticleLegBrut5 = p1.shuffledArticleLegBrut5
				# p.shuffledArticleLegBrut6 = p1.shuffledArticleLegBrut6

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
		elif round == 4:
            # get random number from sequence modifier
			sequenceChosen = random.randint(1,6)

			for p in players:

				p.SRbyTimeout = 0
				p.articleByTimeout = 0

				p.shuffledArticlePolBrut7 = itemgetter(6)(p1.participant.vars["shuffledArticlesListPolBrut"])
				p.shuffledArticlePolBrut8 = itemgetter(7)(p1.participant.vars["shuffledArticlesListPolBrut"])

				p.shuffledArticleLegBrut7 = itemgetter(6)(p1.participant.vars["shuffledArticlesListLegBrut"])
				p.shuffledArticleLegBrut8 = itemgetter(7)(p1.participant.vars["shuffledArticlesListLegBrut"])

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
		elif round == 5:
            # get random number from sequence modifier
			sequenceChosen = random.randint(1,6)

			for p in players:

				p.SRbyTimeout = 0
				p.articleByTimeout = 0

				p.shuffledArticlePolBrut9 = itemgetter(8)(p1.participant.vars["shuffledArticlesListPolBrut"])
				p.shuffledArticlePolBrut10 = itemgetter(9)(p1.participant.vars["shuffledArticlesListPolBrut"])

				p.shuffledArticleLegBrut9 = itemgetter(8)(p1.participant.vars["shuffledArticlesListLegBrut"])
				p.shuffledArticleLegBrut10 = itemgetter(9)(p1.participant.vars["shuffledArticlesListLegBrut"])

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

			for p in players:

				p.SRbyTimeout = 0
				p.articleByTimeout = 0

				p.shuffledArticlePolBrut11 = itemgetter(10)(p1.participant.vars["shuffledArticlesListPolBrut"])
				p.shuffledArticlePolBrut12 = itemgetter(11)(p1.participant.vars["shuffledArticlesListPolBrut"])

				p.shuffledArticleLegBrut11 = itemgetter(10)(p1.participant.vars["shuffledArticlesListLegBrut"])
				p.shuffledArticleLegBrut12 = itemgetter(11)(p1.participant.vars["shuffledArticlesListLegBrut"])

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
				self.head4 = p.shuffledArticlePolBrut12 # p
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



	def check_for_article_selection_singleplayer(self):

		p1 = self.get_player_by_id(1)
		players = self.get_players()
		round = self.articleSelectionRound

		if p1.articleByTimeout == 1:
			for p in players:
				if round == 1: # check which round
					p.timeoutSel1R1 = 1
					p.randomByTimeoutR1 = 1
					p.SRseenR1 = p.selectedSR
				elif round == 2: # check which round
					p.timeoutSel1R2 = 1
					p.randomByTimeoutR2 = 1
					p.SRseenR2 = p.selectedSR
				elif round == 3: # check which round
					p.timeoutSel1R3 = 1
					p.randomByTimeoutR3 = 1
					p.SRseenR3 = p.selectedSR
				elif round == 4: # check which round
					p.timeoutSel1R4 = 1
					p.randomByTimeoutR4 = 1
					p.SRseenR4 = p.selectedSR
				elif round == 5: # check which round
					p.timeoutSel1R5 = 1
					p.randomByTimeoutR5 = 1
					p.SRseenR5 = p.selectedSR
				else:
					p.timeoutSel1R6 = 1
					p.randomByTimeoutR6 = 1
					p.SRseenR6 = p.selectedSR

		else:
			for p in players:
				if round == 1: # check which round
					p.SRseenR1 = p.selectedSR
					p.SRindSelR1 = p.selectedSR
				elif round == 2: # check which round
					p.SRseenR2 = p.selectedSR
					p.SRindSelR2 = p.selectedSR
				elif round == 3: # check which round
					p.SRseenR3 = p.selectedSR
					p.SRindSelR3 = p.selectedSR
				elif round == 4: # check which round
					p.SRseenR4 = p.selectedSR
					p.SRindSelR4 = p.selectedSR
				elif round == 5: # check which round
					p.SRseenR5 = p.selectedSR
					p.SRindSelR5 = p.selectedSR
				else:
					p.SRseenR6 = p.selectedSR
					p.SRindSelR6 = p.selectedSR




    # Live method ---------------
	def live_decision(self, data, x):
		if data == 1:
			print("Data erste Player abgegeben = ", data)
			return {0: "<i>Ihr Gruppenmitglied hat sich bereits entschieden</i>"}
		# elif data == 2:
		# 	print("Data erste Player abgegeben = ", data)
		# 	return {0: "<i>Beide Teilnehmer*innen haben sich bereits entschieden</i>"}
		else:
			pass




class Player(BasePlayer):
	selectedSR=models.IntegerField(initial=0)

    # Dependent Variables -----------------------------------------------------
    # Inklusivität des Problems

	policeBrutalityProblem=models.IntegerField()# Polizeigewalt ist ein Problem in Deutschland. stimme überhaupt nicht zu --> stimme völlig zu
	frequencyPoliceBrutality = models.IntegerField() # 0 = nie, 1 = Tag, 2 = Woche, 3 = Monat, 4 = Jahr, 5 = 10 Jahre
    # Verhaltensebene
	actionsAgainstPoliceBrutality = models.IntegerField()
	moreBrutalityPolice = models.IntegerField() # Die Polizei in Deutschland sollte mehr Gewalt einsetzen dürfen.
                                                # 1 = Stimme überhaupt nicht zu, 9 = Stimme völlig zu
    # Konfidenz
	confidencePoliceBrutality = models.IntegerField()
    # Kompetenzen
	moreCompetencesPolice = models.IntegerField() # Besitzt die Polizei in Deutschland ausreichend Befugnisse Gewalt anzuwenden, um ihre Aufgaben zu erfüllen?
                                                  # -> 1 = zu wenige, 9 = zu viele
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

    # individual decision
	individualDecision = models.IntegerField()
	certaintyIndDec = models.IntegerField()

    # nickname which appears in the chat
	nickname = models.StringField()

    # singleplayer-condition
	singleplayer = models.IntegerField(initial = 0)

    # hypothesis-condition
	conditionHypothesis = models.StringField()


	# drop_out-variable
	timeOut = models.IntegerField(initial = 0) # 0 = no time out, 1 = time out


	####################### SR selection ######################################
	#
	# helping variables (will not be analyzed) --------------------------------

	articleByTimeout = models.IntegerField(initial = 0)

	#selectedSR=models.IntegerField(initial=0)
	articleSelectionRoundInd = models.IntegerField(initial = 1)

	disagreement1 = models.IntegerField(initial = 0)

	SRbyTimeout = models.IntegerField(initial = 0) # second article selection round

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

	# -------------------------------------------------------------------------
	#
	#
	# timeout variables -------------------------------------------------------
	# was article selected by timeout?
	# round 1
	timeoutSel1R1 = models.IntegerField(initial = 0) # 0 = no, 1 = timeout
	timeoutSel2R1 = models.IntegerField(initial = 0) # 0 = no, 1 = timeout
	# round 2
	timeoutSel1R2 = models.IntegerField(initial = 0) # 0 = no, 1 = timeout
	timeoutSel2R2 = models.IntegerField(initial = 0) # 0 = no, 1 = timeout
	# round 3
	timeoutSel1R3 = models.IntegerField(initial = 0) # 0 = no, 1 = timeout
	timeoutSel2R3 = models.IntegerField(initial = 0) # 0 = no, 1 = timeout
	# round 4
	timeoutSel1R4 = models.IntegerField(initial = 0) # 0 = no, 1 = timeout
	timeoutSel2R4 = models.IntegerField(initial = 0) # 0 = no, 1 = timeout
	# round 5
	timeoutSel1R5 = models.IntegerField(initial = 0) # 0 = no, 1 = timeout
	timeoutSel2R5 = models.IntegerField(initial = 0) # 0 = no, 1 = timeout
	# round 6
	timeoutSel1R6 = models.IntegerField(initial = 0) # 0 = no, 1 = timeout
	timeoutSel2R6 = models.IntegerField(initial = 0) # 0 = no, 1 = timeout
	#
	#
	randomByTimeoutR1 = models.IntegerField(initial = 0) # final decision is made by timeout = 1
	randomByTimeoutR2 = models.IntegerField(initial = 0) # final decision is made by timeout = 1
	randomByTimeoutR3 = models.IntegerField(initial = 0) # final decision is made by timeout = 1
	randomByTimeoutR4 = models.IntegerField(initial = 0) # final decision is made by timeout = 1
	randomByTimeoutR5 = models.IntegerField(initial = 0) # final decision is made by timeout = 1
	randomByTimeoutR6 = models.IntegerField(initial = 0) # final decision is made by timeout = 1
	# -------------------------------------------------------------------------
	#
	#
	# search results selection and seen = group selection ---------------------
	# 		-> can be analyzed as the group selection if at least two agree
	SRseenR1 = models.IntegerField(initial = 0) # number of SR which has been seen
	SRseenR2 = models.IntegerField(initial = 0) # number of SR which has been seen
	SRseenR3 = models.IntegerField(initial = 0) # number of SR which has been seen
	SRseenR4 = models.IntegerField(initial = 0) # number of SR which has been seen
	SRseenR5 = models.IntegerField(initial = 0) # number of SR which has been seen
	SRseenR6 = models.IntegerField(initial = 0) # number of SR which has been seen
	#
	SRindSelR1 = models.IntegerField(initial = 0) # number of SR which has been selected individually
	SRindSelR2 = models.IntegerField(initial = 0) # number of SR which has been selected individually
	SRindSelR3 = models.IntegerField(initial = 0) # number of SR which has been selected individually
	SRindSelR4 = models.IntegerField(initial = 0) # number of SR which has been selected individually
	SRindSelR5 = models.IntegerField(initial = 0) # number of SR which has been selected individually
	SRindSelR6 = models.IntegerField(initial = 0) # number of SR which has been selected individually
	# -> if 0 = timeout and no selection
	# -------------------------------------------------------------------------
	#
	#
	# disagreements -----------------------------------------------------------
	# round 1
	disagreementSel1R1 = models.IntegerField(initial = 0) # 0 = no, 1 = disagreement in this round and selection
	disagreementSel2R1 = models.IntegerField(initial = 0) # 0 = no, 1 = disagreement in this round and selection
	# round 2
	disagreementSel1R2 = models.IntegerField(initial = 0) # 0 = no, 1 = disagreement in this round and selection
	disagreementSel2R2 = models.IntegerField(initial = 0) # 0 = no, 1 = disagreement in this round and selection
	# round 3
	disagreementSel1R3 = models.IntegerField(initial = 0) # 0 = no, 1 = disagreement in this round and selection
	disagreementSel2R3 = models.IntegerField(initial = 0) # 0 = no, 1 = disagreement in this round and selection
	# round 4
	disagreementSel1R4 = models.IntegerField(initial = 0) # 0 = no, 1 = disagreement in this round and selection
	disagreementSel2R4 = models.IntegerField(initial = 0) # 0 = no, 1 = disagreement in this round and selection
	# round 5
	disagreementSel1R5 = models.IntegerField(initial = 0) # 0 = no, 1 = disagreement in this round and selection
	disagreementSel2R5 = models.IntegerField(initial = 0) # 0 = no, 1 = disagreement in this round and selection
	# round 6
	disagreementSel1R6 = models.IntegerField(initial = 0) # 0 = no, 1 = disagreement in this round and selection
	disagreementSel2R6 = models.IntegerField(initial = 0) # 0 = no, 1 = disagreement in this round and selection
	#
	#
	# check wether random selection of article was due to disagreement
	randomByDisagreementR1 = models.IntegerField(initial = 0) # 0 = no, 1 = yes
	randomByDisagreementR2 = models.IntegerField(initial = 0) # 0 = no, 1 = yes
	randomByDisagreementR3 = models.IntegerField(initial = 0) # 0 = no, 1 = yes
	randomByDisagreementR4 = models.IntegerField(initial = 0) # 0 = no, 1 = yes
	randomByDisagreementR5 = models.IntegerField(initial = 0) # 0 = no, 1 = yes
	randomByDisagreementR6 = models.IntegerField(initial = 0) # 0 = no, 1 = yes
	#
	#
	# -------------------------------------------------------------------------
	#
	#
	# majority and minortiy vote ----------------------------------------------
	# majorityR1 = models.IntegerField(initial = 0) # 0 = no, 1 = yes
	# majorityR2 = models.IntegerField(initial = 0) # 0 = no, 1 = yes
	# majorityR3 = models.IntegerField(initial = 0) # 0 = no, 1 = yes
	# majorityR4 = models.IntegerField(initial = 0) # 0 = no, 1 = yes
	# majorityR5 = models.IntegerField(initial = 0) # 0 = no, 1 = yes
	# majorityR6 = models.IntegerField(initial = 0) # 0 = no, 1 = yes
	# #
	# minorityR1 = models.IntegerField(initial = 0) # 0 = no, 1 = yes
	# minorityR2 = models.IntegerField(initial = 0) # 0 = no, 1 = yes
	# minorityR3 = models.IntegerField(initial = 0) # 0 = no, 1 = yes
	# minorityR4 = models.IntegerField(initial = 0) # 0 = no, 1 = yes
	# minorityR5 = models.IntegerField(initial = 0) # 0 = no, 1 = yes
	# minorityR6 = models.IntegerField(initial = 0) # 0 = no, 1 = yes
	#
	#
	###########################################################################
