# Shreeharsha Satish, 201665390
import numpy as np
import pandas as pd
import pdb

#  generatePreferences(values) - generates a preferences list for each agent by argsort and creating a dictionary
#  parameters - values: a set of worksheet values as described in the problem (I treat it as an numpy array)
#  returns a preferenceProfile dictionary
def generatePreferences(values):
    numberOfAgents = len(values)
    preferenceProfile = {}  # Empty dict
    for i in range(numberOfAgents):
        preferenceProfile[i+1] = list(values[i].argsort(kind = 'stable')[::-1]+1)  # reverse argsort for descending order and 'stable' picks a stable sorting algorithm (for sorting equal values)

    return preferenceProfile


#  dictatorship(preferenceProfile, agent) - implements the dictatorship election method
#  parameters - preferenceProfile: dictionary from generatePreferences function, agent: Integer indicating whose preferences we follow
#  returns the winner (first priority of the agent)
def dictatorship(preferenceProfile, agent):
    try:
        return preferenceProfile[agent][0]  # Return the first priority of the agent
    except KeyError:
        print("Agent doesn't exist, what kinda cronyistic dictatorship is this?")


#  tieBreaker(alternatives, tieBreak, preferenceProfile) - the tiebreak function that picks the tie winner from alternatives
#  parameters - alternatives: drawn candidates, tieBreak: option to settle the tie, preferenceProfile: dictionary from generatePreferences function
#  returns the winner based on the tieBreak rule
def tieBreaker(alternatives, tieBreak, preferenceProfile):
    alternatives.sort()
    if tieBreak == "max":
        return max(alternatives[::-1], key = alternatives.count)
    elif tieBreak == "min":
        return max(alternatives, key = alternatives.count)
    else:
        try:
            winner = list(set(preferenceProfile[tieBreak]).intersection(alternatives))  # This is all the alternatives for agent tieBreak
            winner.sort()
            return winner[-1]  # Getting the fav from the alternatives
        except KeyError:
            print("Incorrect input")
            return False


#  scoringRule(preferences, scoreVector, tieBreak) - implements a scoring rule by summing a score for each candidate from each agent
#  parameters - preferences: dictionary from generatePreferences, scoreVector: vector of float numbers indicating preferences, tieBreak: tiebreak parameter for dealing with ties
#  returns the winner (candidate with the highest overall score)
def scoringRule(preferences, scoreVector, tieBreak):
    try:
        if(len(scoreVector) != len(next(iter(preferences.values())))):  # Checking length consistency
               raise IndexError
        scoreVector.sort()  # Sort the score scoreVector for consistency
        scoredPreferences = preferences.copy()

        for agent in preferences.keys():
            scoredPreferences[agent] = [scoreVector[i-1] for i in preferences[agent]]  # assign scores to corresponding priority

        finalScores = [sum(candidate) for candidate in zip(*scoredPreferences.values())]  # Sum the scores row wise for each candidate
        highScore = max(finalScores)

        alternatives = []
        for candidateIndex,candidateScore in enumerate(finalScores):
            if(candidateScore == highScore):
                alternatives += [candidateIndex+1]  # Getting the canidates who all have the same high score

        return tieBreaker(alternatives, tieBreak, preferences)
    except IndexError:
        print("Incorrect input")
        return False


#  plurality (preferences, tieBreak) - implements the plurality election method
#  parameters - preferences: dictionary from generatePreferences, tieBreak: tiebreak parameter for dealing with ties
#  return the winner (candidate who was top priority for majority of the agents)
def plurality(preferences, tieBreak):
    alternatives =  [x[0] for x in list(preferences.values())]
    return tieBreaker(alternatives, tieBreak, preferences)

#  veto(preferences, tieBreak) - implements the veto election method
#  parameters - preferences: dictionary from generatePreferences, tieBreak: tiebreak parameter for dealing with ties
#  returns the winner (similar to scoringRule but scores are 0(least fav) and rest 1(non-least fav))
def veto(preferences, tieBreak):
    vetoScoreVector = [0]+[1]*(len(next(iter(preferences.values())))-1)  # Creating a Veto scoreVector, now we just call scoringRule
    return scoringRule(preferences, vetoScoreVector, tieBreak)

#  borda (preferences, tieBreak) - implements the borda election method
#  parameters - preferences: dictionary from generatePreferences, tieBreak: tiebreak parameter for dealing with ties
#  returns the winner (similar to scoringRule but the scores are integers from 0(least fav) to m-1(fav))
def borda(preferences, tieBreak):
    bordaScoreVector = list(range(0, len(next(iter(preferences.values())))))  # Creating a borda scoreVector, now we just call scoringRule
    return scoringRule(preferences, bordaScoreVector, tieBreak)


#  harmonic(preferences, tieBreak) - implements the harmonic election method
#  parameters - preferences: dictionary from generatePreferences, tieBreak: tiebreak parameter for dealing with ties
#  returns the winner (similar to scoringRule but the scores are float from 1/m(least fav) to 1(favorite))
def harmonic(preferences, tieBreak):
    harmonicScoreVector = list(range(1, len(next(iter(preferences.values())))+1))
    harmonicScoreVector = [1/x for x in harmonicScoreVector]  # Creating a harmonic scoreVector, now we just call scoringRule
    return scoringRule(preferences, harmonicScoreVector, tieBreak)


#  STV(preferences, tieBreak) - implements the single transferable vote election method
#  parameters - preferences: dictionary from generatePreferences, tieBreak: tiebreak parameter for dealing with ties
#  returns the winner (multiple rounds that eliminate candidates iteratively based on how often they come in first)
def STV (preferences, tieBreak):

    return


#  rangeVoting(preferences, tieBreak) - implements the range voting election method
#  parameters - values: worksheet values, tieBreak: tiebreak parameter for dealing with ties
#  returns the winner (similar to scoringRule but with predefined values from the worksheet)
def rangeVoting (values, tieBreak):
    if tieBreak == "max":
        pass
    elif tieBreak == "min":
        pass
    else:
        pass
    return

if __name__ == '__main__':
    #print("Test all")
    values = np.array(pd.read_excel('voting.xlsx', header=None))
    preferenceProfile = generatePreferences(values)
