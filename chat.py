import csv
import re
import random
from collections import defaultdict
import numpy as np

training=2
conv_dict=defaultdict(list)
reward_dict=defaultdict(list)
with open('conversation.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=';')
    line_count=0
    for row in csv_reader:
            conv_dict[int(row[0])].append(row[1])
            reward_dict[int(row[0])].append(int(row[2]))

Y_feedback=re.compile('y',re.I)
### index of set of questions
session_index=1
### set of questions and their rewards
questions=conv_dict.get(session_index)
rewards=reward_dict.get(session_index)
print(rewards)
#q_index=random.randint(1,2)
def getQuestionWithMaxReward(max_reward):
    max_list=[]
    for i in rewards:
        if(i==max_reward):
            max_list.append(rewards.index(i))
    print('list of max rewards ',max_list)
    return random.randrange(0,len(max_list)-1)


def updateQtable():
    print(reward_dict.items())
    q_index=getQuestionWithMaxReward(max(rewards))
    print('question with max reward ',questions[q_index])
    feedback=input()
    if(Y_feedback.match(feedback)):
        rewards[q_index]+=1

for i in range(training):
    updateQtable()