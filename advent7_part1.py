value_dict ={"A" : 12 , "K": 11 , "Q":10 , "J":9 , "T":8 , "9":7 , "8":6, "7":5 , "6":4 , "5":3, "4":2, "3":1 , "2":0}

def evaluate_hand(hand):
	i= 4
	total_value = 0
	for char in hand:
		total_value += value_dict[char]*(13**i)
		i-=1
	value = 0
	first_match = 0
	second_pair = 0
	while hand != "":
		char = hand[0]
		if first_match == 0 and hand.count(char) >=2:
			first_match = hand.count(char)
			hand = hand.replace(char, "")
		elif first_match == 0 and hand.count(char) == 1:
			hand = hand.replace(char, "")
		elif first_match != 0 and hand.count(char) == 1:
			hand = hand.replace(char, "")
		elif first_match !=0 and hand.count(char) >=2:
			second_pair = hand.count(char)
			hand = hand.replace(char, "")
		else:
			print("BIG PROBLEM Okayeg")
			print(hand)
	if second_pair > first_match:
		first_match = 3
		second_pair = 2		
	if first_match == 5:
		value = 7
	elif first_match == 4:		
		value = 6
	elif first_match ==3 and second_pair ==2:
		value = 5
	elif first_match ==3 and second_pair ==0:
		value =4
	elif first_match == 2 and second_pair == 2:
		value = 3
	elif first_match == 2 and second_pair == 0:
		value = 2	
	elif first_match == 0 and second_pair == 0:
		value = 1
	else:
		print("BIG PROBLEM Okayeg2222")
		print(hand)
	total_value += value*(13**5) 		 					
	return total_value		
						
				
sum = 0
with open('input7.txt') as fin: 
	total_hands = 0
	hands = {}
	values = []
	for line in fin:
		hand1 , bid1 = line.strip("\n").split(" ")
		val = evaluate_hand(hand1)
		values.append(val)
		hands[val] = [hand1 , int(bid1)]

for i, val1 in enumerate(sorted(values)):
	sum+= (i+1)*hands[val1][1]
						
print(sum)						
