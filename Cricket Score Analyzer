 #Cricket Score Analyzer 🏏
import numpy as np
score=np.array([
    [45,67,89,90,12,32],
    [45,67,87,21,34,43],
    [12,34,78,65,43,90],
    [14,2,6,8,90,99],
    [120,120,90,87,97,78]
])
print("The scores of players are:",score )

#step 2
total_score_perplayer=np.sum(score,axis=1)
print("The total score per player is:",total_score_perplayer)

#step 3
average_score_pp=np.mean(score,axis=1)
print("Average score per player is:",average_score_pp)

#step 4
highest_score_permatch=np.max(score,axis=0)
print("The highest score per match is:",highest_score_permatch)

#step 5
#all players are included
#only first 3 matches
slicing=score[:,0:3]
print("Values after sicing:",slicing)

#step 6
filter_score=score[score>80]
print("The scores greater than 80 are:",filter_score)

#step 7
sorted=np.argsort(total_score_perplayer)
#now top 2 players are at end so
top_two_players=sorted[-2:]
print("Top two players index:",top_two_players)
print("Top two players score:",total_score_perplayer[top_two_players])

#step 8
flaten_array=score.flatten()
print("ARray after 1d conversion is:",flaten_array)
