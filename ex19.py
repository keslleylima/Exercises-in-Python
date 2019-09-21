import  random
l1 = input('type a name of first learner:')
l2 = input('type a name of second learner:')
l3 = input('type a name of third learner:')
l4 = input('type a name of fourth learner:')

list = [l1,l2,l3,l4]

chosenLearner = random.choice(list)
print("the chosen learner is: ", chosenLearner)
