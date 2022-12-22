import numpy as np
import pandas as pd

#  generatePreferences(values) - generates a preference list for each agent by argsort and creating a dictionary
#  parameters - values: a set of worksheet values as described in the problem (I treat it as an numpy array)
#  returns a preferenceProfile dictionary
def generatePreferences(values):
    numberOfAgents = len(values)
    preferenceProfile = {}  # Empty dict
    for i in range(numberOfAgents):
        preferenceProfile[i+1] = list(values[i].argsort(kind = 'stable')[::-1]+1)  # reverse argsort for descending order and 'stable' picks a stable sorting algorithm (for equal values).

    return preferenceProfile


#  dictatorship(preferenceProfile, agent) - implements the dictatorship election method
#  parameters - preferenceProfile: dictionary from generatePreferences function, agent: Integer indicating whose preference we follow
#  returns the winner (first priority of the agent)
def dictatorship(preferenceProfile, agent):
    try:
        return preferenceProfile[agent][0]  # Return the first priority of the agent
    except KeyError:
        print("Agent doesn't exist, What kinda cronyistic dictatorship is this?")


#  scoringRule(preferences, scoreVector, tieBreak) - implements a scoring rule by summing a score for each candidate from each agent
#  parameters - preferences: dictionary from generatePreferences, scoreVector: vector of float numbers indicating preferences, tieBreak: tiebreak parameter for dealing with ties
#  returns the winner (candidate with the highest overall score)
def scoringRule(preferences, scoreVector, tieBreak):
    try:
        if(len(scoreVector) != len(next(iter(preferenceProfile.values())))):
               raise IndexError
        scoreVector.sort()  # Sort the score scoreVector for consistency
        scoredPreferences = preferences.copy()

        for agent in preferences.keys():
            scoredPreferences[agent] = [scoreVector[i-1] for i in preferences[agent]]  # assign scores to corresponding priority

        for


        if tieBreak == "max":
            pass
        elif tieBreak == "min":
            pass
        else:
            dictatorship(preferences, tieBreak)
        return scoredPreferences
    except IndexError:
        print("Incorrect input")
        return


#  plurality (preferences, tieBreak) - implements the plurality election method
#  parameters - preferences: dictionary from generatePreferences, tieBreak: tiebreak parameter for dealing with ties
#  return the winner (candidate who was top priority for majority of the agents)
def plurality (preferences, tieBreak):
    alternatives =  [x[0] for x in list(preferences.values())]
    alternatives.sort()
    if tieBreak == "max":
        winner = max(alternatives[::-1], key = alternatives.count)
    elif tieBreak == "min":
        winner = max(alternatives, key = alternatives.count)
    else:
        winner = dictatorship(preferences, tieBreak)
    return winner


#  veto(preferences, tieBreak) - implements the veto election method
#  parameters - preferences: dictionary from generatePreferences, tieBreak: tiebreak parameter for dealing with ties
#  returns the winner (similar to scoringRule but scores are 1(favorite) and rest 0(least fav))
def veto (preferences, tieBreak):
    if tieBreak == "max":
        pass
    elif tieBreak == "min":
        pass
    else:
        pass
    return


#  borda (preferences, tieBreak) - implements the borda election method
#  parameters - preferences: dictionary from generatePreferences, tieBreak: tiebreak parameter for dealing with ties
#  returns the winner (similar to scoringRule but the scores are integers from 0(least fav) to m-1(fav))
def borda (preferences, tieBreak):
    if tieBreak == "max":
        pass
    elif tieBreak == "min":
        pass
    else:
        pass
    return


#  harmonic(preferences, tieBreak) - implements the harmonic election method
#  parameters - preferences: dictionary from generatePreferences, tieBreak: tiebreak parameter for dealing with ties
#  returns the winner (similar to scoringRule but the scores are float from 1/m(least fav) to 1(favorite))
def harmonic (preferences, tieBreak):
    if tieBreak == "max":
        pass
    elif tieBreak == "min":
        pass
    else:
        pass
    return


#  STV(preferences, tieBreak) - implements the single transferable vote election method
#  parameters - preferences: dictionary from generatePreferences, tieBreak: tiebreak parameter for dealing with ties
#  returns the winner (multiple rounds that eliminate candidates iteratively based on how often they come in first)
def STV (preferences, tieBreak):
    if tieBreak == "max":
        pass
    elif tieBreak == "min":
        pass
    else:
        pass
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
