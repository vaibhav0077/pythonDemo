# # assert condition, error_message(optional)    

# def avg(score):
#     assert len(score) != 0, "The list is empty"
#     return sum(score)/ len(score)


# score1 = []
# print("score1 : " +  str(avg(score1)))

# score2 = [1, 2, 3, 4]
# print("Score2 : " +  str(avg(score2)))


def avg(scores):    
    assert len(scores) != 0,"The List is empty."    
    return sum(scores)/len(scores)    
    
scores2 = [67,59,86,75,92]    
print("The Average of scores2:",avg(scores2))    
    
scores1 = []    
print("The Average of scores1:",avg(scores1))  