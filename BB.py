from console import clear
from time import sleep

TM=[]
tape=[0]
head=0
states=[]
state='0' #prob have to change often

with open('BB(18)record.txt','r') as table:
	rules=[l[:-1].split(' ') for l in table.readlines()]
	for i in range(0,len(rules),2):
		states+=[rules[i][0]]
		stuff=[rules[i][2:],rules[i+1][2:]]
		if rules[i][1]=='1':
			stuff=[stuff[1],stuff[0]]
		TM+=[stuff]

while state!='halt':
	clear()
	for cell in range(len(tape)):
		print('%s %s'%(['0 ',' 1'][tape[cell]],('< %d'%states.index(state))*(cell==head)))
	sleep(.04)
	actions=TM[states.index(state)][tape[head]]
	tape[head]=int(actions[0]=='1')
	head+=2*(actions[1]=='r')-1
	if head<0:
		tape=[0]+tape
		head+=1
	elif head>=len(tape):
		tape+=[0]
	state=actions[2]
