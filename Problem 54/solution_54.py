import time
import itertools

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def isSameSuitPlayer(x):
    return x[0][-1] == x[1][-1] and x[0][-1] == x[2][-1] and x[0][-1] == x[3][-1] and x[0][-1] == x[4][-1]

def parseInputs(x):
    total_count = 0
    total_hand = ""
    hand = " ".join(x)
    pair = {}
        
    for index in range(0, 5):
        card_number = x[index][0]
        count = hand.count(card_number)
        pair[card_number] = count
        total_count += count
        total_hand += card_number

    pair['same_suit'] = isSameSuitPlayer(x)

    if total_count == 17:
        pair['type'] = four_kind
        pair['type_value'] = 8
    elif total_count == 13:
        pair['type'] = full_house
        pair['type_value'] = 7
    elif total_count == 11:
        if pair['same_suit']:
            pair['type'] = flush
            pair['type_value'] = 6
        else:
            pair['type'] = three_kind
            pair['type_value'] = 4
    elif total_count == 9:
        if pair['same_suit']:
            pair['type'] = flush
            pair['type_value'] = 6
        else:
            pair['type'] = two_pair
            pair['type_value'] = 3
    elif total_count == 7:
        if pair['same_suit']:
            pair['type'] = flush
            pair['type_value'] = 6
        else:
            pair['type'] = one_pair
            pair['type_value'] = 2
    elif total_count == 5:
        for permutation in itertools.permutations(total_hand):
            if ''.join(permutation) in consecutive_hands:
                pair['consecutive'] = True
                break
            else:
                pair['consecutive'] = False

        if pair['consecutive'] and pair['same_suit']:
            if 'A' in total_hand and 'K' in total_hand and 'Q' in total_hand and 'J' in total_hand and 'T' in total_hand:
                pair['type'] = royal_flush
                pair['type_value'] = 10
            else:
                pair['type'] = straight_flush
                pair['type_value'] = 9
        elif pair['same_suit']:
            pair['type'] = flush
            pair['type_value'] = 6
        elif pair['consecutive']:
            pair['type'] = straight
            pair['type_value'] = 5 
        else: 
            pair['type'] = high_card
            pair['type_value'] = 1
    
    return pair

def getMaxCardAndCount(p):
    count = 0
    card = ""
    for key, value in p.items():
        if  key != "type_value" and type(value) == int and value > count:
            count = value
            card = key
    return card, count

# Generate Consecutive Hands
def generateConsectiveHands():
    consecutive_hands = []
    for i  in range(len(cards) - 4):
        temp = ""
        for j in range(i, i + 5):
            temp += cards[j]
        consecutive_hands.append(temp)
    return consecutive_hands

timer = timing()

poker_file = open('poker.txt', 'r').readlines()

royal_flush = "royal_flush"
straight_flush = "straight_flush"
four_kind = "four_a_kind"
full_house = "full_house"
flush = "flush"
straight = "straight"
three_kind = "three_a_kind"
two_pair = "two_pair"
one_pair = "one_pair"
high_card = "high_card"

player_1_win_counter = 0
player_2_win_counter = 0

cards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

cards_dict = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
consecutive_hands = set(generateConsectiveHands())

DEBUG = False

for line in poker_file:
    line = line.replace("\n", "")
    input_hand = line.split(" ")
    p1 = parseInputs(input_hand[0:5])
    p2 = parseInputs(input_hand[5:10])

    if DEBUG:
        print(input_hand)
        print('p1 hand', p1)
        print('p2 hand', p2)

    if p1['type_value'] > p2['type_value']:
        player_1_win_counter += 1
    
        if DEBUG:
            print('p1 won')
            print()
    elif p1['type_value'] == p2['type_value']:
        p1_max_card, p1_max_count = getMaxCardAndCount(p1)
        p2_max_card, p2_max_count = getMaxCardAndCount(p2)

        # If pX_max_count = 0, i.e, its a high card -> go to else
        if p1_max_count > 1 and p2_max_count > 1 and p1_max_count == p2_max_count:
            if cards_dict.get(p1_max_card) > cards_dict.get(p2_max_card):
                player_1_win_counter += 1

                if DEBUG:
                    print('p1 won : higher hand card value')
                    print()
            elif cards_dict.get(p1_max_card) == cards_dict.get(p2_max_card):
                for card in cards:
                    if card != p1_max_card:
                        if card in p1 and card not in p2:
                            player_1_win_counter += 1

                            if DEBUG:
                                print('p1 won : same hand but highcard')
                                print()
                            break       
                        elif card in p2 and card not in p1:
                            break
        else:
            # Check who has the highest high card
            for card in cards:
                if card in p1 and card not in p2:
                    player_1_win_counter += 1
                    break       
                elif card in p2 and card not in p1:
                    break

timer("Player 1 win's {} hands out of {}".format(player_1_win_counter, len(poker_file)))