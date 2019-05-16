##################################################################################
#
#  CSE 231 Project #6
#   Samuel Isken CSE 231 - 730 
#
#
#  Algorithm
#   Display hand and community cards and winner of hand
#   ask if player wants to play again
#   deal new hand and check all possible combos to determine winning hand
#    display winning hand 
#    repeat until player prompts to stop or less than 9 cards remain
#    end the program
#
#################################################################################
#GIVEN DONT CHANGE 
##########################################################################
import cards

def less_than(c1,c2):
    '''Return 
           True if c1 is smaller in rank, 
           True if ranks are equal and c1 has a 'smaller' suit
           False otherwise'''
    if c1.rank() < c2.rank():
        return True
    elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
        return True
    return False

def min_in_list(L):
    '''Return the index of the mininmum card in L'''
    min_card = L[0]  # first card
    min_index = 0
    for i,c in enumerate(L):
        if less_than(c,min_card):  # found a smaller card, c
            min_card = c
            min_index = i
    return min_index
        
def cannonical(H):
    #Sorts method - essentially a rewritten sort function 
    ''' Selection Sort: find smallest and swap with first in H,
        then find second smallest (smallest of rest) and swap with second in H,
        and so on...'''
    for i,c in enumerate(H):
        # get smallest of rest; +i to account for indexing within slice
        min_index = min_in_list(H[i:]) + i 
        H[i], H[min_index] = H[min_index], c  # swap
    return H
################################################################################
#GIVEN DONT CHANGE 
################################################################################
def flush_7(H):
    '''Return a list of 5 cards forming a flush,
       if at least 5 of 7 cards form a flush in H, a list of 7 cards, 
       False otherwise.'''
    #Initializes lists of suit
    suit1 = []
    suit2 = []
    suit3 = []
    suit4 = []
    #Appends to suit lists 
    for c in H:
        if c.suit() == 1:
            suit1.append(c)
            suit1 = cannonical(suit1)
        if c.suit() == 2:
            suit2.append(c)
            suit2 = cannonical(suit2)
        if c.suit() == 3:
            suit3.append(c)
            suit3 = cannonical(suit3)
        if c.suit() == 4:
            suit4.append(c)
            suit4 = cannonical(suit4)
    #Checks for flush 
    if len(suit1) >=5:
        return suit1[:5]
    if len(suit2) >=5:
        return suit2[:5]
    if len(suit3) >=5:
        return suit3[:5]
    if len(suit4) >=5:
        return suit4[:5]
    return False
#################################################################################
def straight_7(H):
    #5 cards in a sequence 
    '''Return a list of 5 cards forming a straight,
       if at least 5 of 7 cards form a straight in H, a list of 7 cards, 
       False otherwise.'''
       
    #Initializes rank lists 
    rank1 = []
    rank2 = []
    rank3 = []
    rank4 = []
    rank5 = []
    rank6 = []
    rank7 = []
    rank8 = []
    rank9 = []
    rank10 = []
    rank11 = []
    rank12 = []
    rank13 = []
    rank14 = []
    straight_list = []
    hand_list = []


    
    for c in H:

        if c.rank() == 1:
            rank1.append(c)
        if c.rank() == 2:
            rank2.append(c)
        if c.rank() == 3:
            rank3.append(c)
        if c.rank() == 4:
            rank4.append(c)
        if c.rank() == 5:
            rank5.append(c)
        if c.rank() == 6:
            rank6.append(c)
        if c.rank() == 7:
            rank7.append(c)
        if c.rank() == 8:
            rank8.append(c)
        if c.rank() == 9:
            rank9.append(c)
        if c.rank() == 10:
            rank10.append(c)
        if c.rank() == 11:
            rank11.append(c)
        if c.rank() == 12:
            rank12.append(c)
        if c.rank() == 13:
            rank13.append(c)
        if c.rank() == 14:
            rank14.append(c)
    
    
    
    if len(rank1) >=1:
        hand_list += rank1[0:]
        straight_list += "1" * len(rank1)
    if len(rank2) >=1:
        hand_list += rank2[0:]
        straight_list += "2" * len(rank2)
    if len(rank3) >=1:
        hand_list += rank3[0:]
        straight_list += "3" * len(rank3)
    if len(rank4) >=1:
        hand_list += rank4[0:]
        straight_list += "4" * len(rank4)
    if len(rank5) >=1:
        hand_list += rank5[0:]
        straight_list += "5" * len(rank5)
    if len(rank6) >=1:
        hand_list += rank6[0:]
        straight_list += "6" * len(rank6)
    if len(rank7) >=1:
        hand_list += rank7[0:]
        straight_list += "7" * len(rank7)
    if len(rank8) >=1:
        hand_list += rank8[0:]
        straight_list += "8" * len(rank8)
    if len(rank9) >=1:
        hand_list += rank9[0:]
        straight_list += "9" * len(rank9)
    if len(rank10) >=1:
        hand_list += rank10[0:] 
        straight_list += "10" * len(rank10)
    if len(rank11) >=1:
        hand_list += rank11[0:]
        straight_list += "11" * len(rank11)
    if len(rank12) >=1:
        hand_list += rank12[0:]
        straight_list += "12" * len(rank12)
    if len(rank13) >=1:
        hand_list += rank13[0:]
        straight_list += "13" * len(rank13)
    if len(rank14) >=1:
        hand_list += rank14[0:]
        straight_list += "14" * len(rank14)


    #Straight_list is the full hand of cards 
    #Checks for straight 
    if int(straight_list[1]) - int(straight_list[0]) == 1 and int(straight_list[2]) - int(straight_list[1]) == 1 and int(straight_list[3]) - int(straight_list[2]) == 1 and int(straight_list[4]) - int(straight_list[3]) == 1:
        hand_list = hand_list[0:5]
        return hand_list
    
    if int(straight_list[2]) - int(straight_list[1]) == 1 and int(straight_list[3]) - int(straight_list[2]) == 1 and int(straight_list[4]) - int(straight_list[3]) == 1 and int(straight_list[5]) - int(straight_list[4]) == 1:
        hand_list = hand_list[1:6]
        return hand_list
    if int(straight_list[3]) - int(straight_list[2]) == 1 and int(straight_list[4]) - int(straight_list[3]) == 1 and int(straight_list[5]) - int(straight_list[4]) == 1 and int(straight_list[6]) - int(straight_list[5]) == 1:
        hand_list = hand_list[2:]
        return hand_list
        
            

    return False
###############################################################################################################   
def straight_flush_7(H):
    '''Return a list of 5 cards forming a straight flush,
       if at least 5 of 7 cards form a straight flush in H, a list of 7 cards, 
       False otherwise.'''
    checker_one = straight_7(H)
    if checker_one == False:
        checker_one = []
    else:
        checker_one=checker_one
    answer = flush_7(checker_one)
    
    #Simply combines straight and flush functions 
    
    return answer
######################################################################################################

def four_7(H):
    '''Return a list of 4 cards with the same rank,
       if 4 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.'''
    rank1 = []
    rank2 = []
    rank3 = []
    rank4 = []
    rank5 = []
    rank6 = []
    rank7 = []
    rank8 = []
    rank9 = []
    rank10 = []
    rank11 = []
    rank12 = []
    rank13 = []
    rank14 = []
    
    for c in H:
        if c.rank() == 1:
            rank1.append(c)
        if c.rank() == 2:
            rank2.append(c)
        if c.rank() == 3:
            rank3.append(c)
        if c.rank() == 4:
            rank4.append(c)
        if c.rank() == 5:
            rank5.append(c)
        if c.rank() == 6:
            rank6.append(c)
        if c.rank() == 7:
            rank7.append(c)
        if c.rank() == 8:
            rank8.append(c)
        if c.rank() == 9:
            rank9.append(c)
        if c.rank() == 10:
            rank10.append(c)
        if c.rank() == 11:
            rank11.append(c)
        if c.rank() == 12:
            rank12.append(c)
        if c.rank() == 13:
            rank13.append(c)
        if c.rank() == 14:
            rank14.append(c)
        
        #Checks for 4 of a kind 
    if len(rank1) >=4:
        return rank1[:4]
    if len(rank2) >=4:
        return rank2[:4]
    if len(rank3) >=4:
        return rank3[:4]
    if len(rank4) >=4:
        return rank4[:4]
    if len(rank5) >=4:
        return rank5[:4]
    if len(rank6) >=4:
        return rank6[:4]
    if len(rank7) >=4:
        return rank7[:4]
    if len(rank8) >=4:
        return rank8[:4]
    if len(rank9) >=4:
        return rank9[:4]
    if len(rank10) >=4:
        return rank10[:4]
    if len(rank11) >=4:
        return rank11[:4]
    if len(rank12) >=4:
        return rank12[:4]
    if len(rank13) >=4:
        return rank13[:4]
    if len(rank14) >=4:
        return rank14[:4]
    return False

def three_7(H):
    #ASSUME NOT 4 of a kind from prior function 
    '''Return a list of 3 cards with the same rank,
       if 3 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''
    rank1 = []
    rank2 = []
    rank3 = []
    rank4 = []
    rank5 = []
    rank6 = []
    rank7 = []
    rank8 = []
    rank9 = []
    rank10 = []
    rank11 = []
    rank12 = []
    rank13 = []
    rank14 = []
    
    for c in H:
        if c.rank() == 1:
            rank1.append(c)
        if c.rank() == 2:
            rank2.append(c)
        if c.rank() == 3:
            rank3.append(c)
        if c.rank() == 4:
            rank4.append(c)
        if c.rank() == 5:
            rank5.append(c)
        if c.rank() == 6:
            rank6.append(c)
        if c.rank() == 7:
            rank7.append(c)
        if c.rank() == 8:
            rank8.append(c)
        if c.rank() == 9:
            rank9.append(c)
        if c.rank() == 10:
            rank10.append(c)
        if c.rank() == 11:
            rank11.append(c)
        if c.rank() == 12:
            rank12.append(c)
        if c.rank() == 13:
            rank13.append(c)
        if c.rank() == 14:
            rank14.append(c)
        
            
            
    #Checks for three of a kind 
    if len(rank1) >=3:
        return rank1[:3]
    if len(rank2) >=3:
        return rank2[:3]
    if len(rank3) >=3:
        return rank3[:3]
    if len(rank4) >=3:
        return rank4[:3]
    if len(rank5) >=3:
        return rank5[:3]
    if len(rank6) >=3:
        return rank6[:3]
    if len(rank7) >=3:
        return rank7[:3]
    if len(rank8) >=3:
        return rank8[:3]
    if len(rank9) >=3:
        return rank9[:3]
    if len(rank10) >=3:
        return rank10[:3]
    if len(rank11) >=3:
        return rank11[:3]
    if len(rank12) >=3:
        return rank12[:3]
    if len(rank13) >=3:
        return rank13[:3]
    if len(rank14) >=3:
        return rank14[:3]
    return False

#######################################################################################################    
    
        
def two_pair_7(H):
    '''Return a list of 4 cards that form 2 pairs,
       if there exist two pairs in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H) and three_7(H) are both False.'''
    rank1 = []
    rank2 = []
    rank3 = []
    rank4 = []
    rank5 = []
    rank6 = []
    rank7 = []
    rank8 = []
    rank9 = []
    rank10 = []
    rank11 = []
    rank12 = []
    rank13 = []
    rank14 = []
    pair_list = []
    for c in H:
        if c.rank() == 1:
            rank1.append(c)
            rank1 = cannonical(rank1)
        if c.rank() == 2:
            rank2.append(c)
            rank2 = cannonical(rank2)
        if c.rank() == 3:
            rank3.append(c)
            rank3 = cannonical(rank3)
        if c.rank() == 4:
            rank4.append(c)
            rank4 = cannonical(rank4)
        if c.rank() == 5:
            rank5.append(c)
            rank5 = cannonical(rank5)
        if c.rank() == 6:
            rank6.append(c)
            rank6 = cannonical(rank6)
        if c.rank() == 7:
            rank7.append(c)
            rank7 = cannonical(rank7)
        if c.rank() == 8:
            rank8.append(c)
            rank8 = cannonical(rank8)
        if c.rank() == 9:
            rank9.append(c)
            rank9 = cannonical(rank9)
        if c.rank() == 10:
            rank10.append(c)
            rank10 = cannonical(rank10)
        if c.rank() == 11:
            rank11 = cannonical(rank11)
        if c.rank() == 12:
            rank12 = cannonical(rank12)
        if c.rank() == 13:
            rank13 = cannonical(rank13)
        if c.rank() == 14:
            rank14.append(c)
            rank14 = cannonical(rank14)
            
    
    if len(rank1) >=2:
        pair_list.append(rank1[:2])
    if len(rank2) >=2:
        pair_list.append(rank2[:2])
    if len(rank3) >=2:
        pair_list.append(rank3[:2])
    if len(rank4) >=2:
        pair_list.append(rank4[:2])
    if len(rank5) >=2:
        pair_list.append(rank5[:2])
    if len(rank6) >=2:
        pair_list.append(rank6[:2])
    if len(rank7) >=2:
        pair_list.append(rank7[:2])
    if len(rank8) >=2:
        pair_list.append(rank8[:2])
    if len(rank9) >=2:
        pair_list.append(rank9[:2])
    if len(rank10) >=2:
        pair_list.append(rank10[:2])
    if len(rank11) >=2:
        pair_list.append(rank11[:2])
    if len(rank12) >=2:
        pair_list.append(rank12[:2])
    if len(rank13) >=2:
        pair_list.append(rank13[:2])
    if len(rank14) >=2:
        pair_list.append(rank14[:2])
    if len(pair_list) >= 2:
        return pair_list[0]+pair_list[1]

    return False



def one_pair_7(H):
    '''Return a list of 2 cards that form a pair,
       if there exists exactly one pair in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H), three_7(H) and two_pair(H) are False.'''
    rank1 = []
    rank2 = []
    rank3 = []
    rank4 = []
    rank5 = []
    rank6 = []
    rank7 = []
    rank8 = []
    rank9 = []
    rank10 = []
    rank11 = []
    rank12 = []
    rank13 = []
    rank14 = []
    
    for c in H:
        if c.rank() == 1:
            rank1.append(c)
        if c.rank() == 2:
            rank2.append(c)
        if c.rank() == 3:
            rank3.append(c)
        if c.rank() == 4:
            rank4.append(c)
        if c.rank() == 5:
            rank5.append(c)
        if c.rank() == 6:
            rank6.append(c)
        if c.rank() == 7:
            rank7.append(c)
        if c.rank() == 8:
            rank8.append(c)
        if c.rank() == 9:
            rank9.append(c)
        if c.rank() == 10:
            rank10.append(c)
        if c.rank() == 11:
            rank11.append(c)
        if c.rank() == 12:
            rank12.append(c)
        if c.rank() == 13:
            rank13.append(c)
        if c.rank() == 14:
            rank14.append(c)
        
            

    
    if len(rank1) >=2:
        return rank1[:2]
    if len(rank2) >=2:
        return rank2[:2]
    if len(rank3) >=2:
        return rank3[:2]
    if len(rank4) >=2:
        return rank4[:2]
    if len(rank5) >=2:
        return rank5[:2]
    if len(rank6) >=2:
        return rank6[:2]
    if len(rank7) >=2:
        return rank7[:2]
    if len(rank8) >=2:
        return rank8[:2]
    if len(rank9) >=2:
        return rank9[:2]
    if len(rank10) >=2:
        return rank10[:2]
    if len(rank11) >=2:
        return rank11[:2]
    if len(rank12) >=2:
        return rank12[:2]
    if len(rank13) >=2:
        return rank13[:2]
    if len(rank14) >=2:
        return rank14[:2]
    return False
    
    
    

def two_for_full_house(H):
    rank1 = []
    rank2 = []
    rank3 = []
    rank4 = []
    rank5 = []
    rank6 = []
    rank7 = []
    rank8 = []
    rank9 = []
    rank10 = []
    rank11 = []
    rank12 = []
    rank13 = []
    rank14 = []
    
    for c in H:
        if c.rank() == 1:
            rank1.append(c)
        if c.rank() == 2:
            rank2.append(c)
        if c.rank() == 3:
            rank3.append(c)
        if c.rank() == 4:
            rank4.append(c)
        if c.rank() == 5:
            rank5.append(c)
        if c.rank() == 6:
            rank6.append(c)
        if c.rank() == 7:
            rank7.append(c)
        if c.rank() == 8:
            rank8.append(c)
        if c.rank() == 9:
            rank9.append(c)
        if c.rank() == 10:
            rank10.append(c)
        if c.rank() == 11:
            rank11.append(c)
        if c.rank() == 12:
            rank12.append(c)
        if c.rank() == 13:
            rank13.append(c)
        if c.rank() == 14:
            rank14.append(c)
        
    
    if len(rank1) ==2:
        return rank1[:2]
    if len(rank2) ==2:
        return rank2[:2]
    if len(rank3) ==2:
        return rank3[:2]
    if len(rank4) ==2:
        return rank4[:2]
    if len(rank5) ==2:
        return rank5[:2]
    if len(rank6) ==2:
        return rank6[:2]
    if len(rank7) ==2:
        return rank7[:2]
    if len(rank8) ==2:
        return rank8[:2]
    if len(rank9) ==2:
        return rank9[:2]
    if len(rank10) ==2:
        return rank10[:2]
    if len(rank11) ==2:
        return rank11[:2]
    if len(rank12) ==2:
        return rank12[:2]
    if len(rank13) ==2:
        return rank13[:2]
    if len(rank14) ==2:
        return rank14[:2]
    #Returns empty list if fails as to not cause an error
    return []
    
 ##############################################################################################################   
def three_in_house_7(H):
    result = three_7(H)
    if result == False:
        return []
    return result
    
##############################################################################################################
def full_house_7(H):
    '''Return a list of 5 cards forming a full house,
       if 5 of the 7 cards form a full house in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''    
    two_in_house = two_for_full_house(H)
    three_in_house = three_in_house_7(H)
    two_in_house = cannonical(two_in_house)
    three_in_house = cannonical(three_in_house)
    full_house_set = two_in_house + three_in_house
    if len(full_house_set) == 5:
        return full_house_set
    return False
##############################################################################################################    

def main():
    D = cards.Deck()
    D.shuffle()
    
    my_deck = cards.Deck()
    my_deck.shuffle()
    community_list = []
    hand_1_list = []
    hand_2_list = []

    x = "y"
    while x == "y":
         community_list = []
         hand_1_list = []
         hand_2_list = []
        

        #Creates hands and community cards
         for i in range(5):
             community_list.append(my_deck.deal())
         for i in range(1):
             hand_1_list.append(my_deck.deal())
             hand_1_list.append(my_deck.deal())

             hand_2_list.append(my_deck.deal())
             hand_2_list.append(my_deck.deal())
         #Prints prompt and card data
         print("-"*40)
         print("Let's play poker!\n")
         print("Community cards:",community_list)


         print("Player 1:",hand_1_list)
         print("Player 2:",hand_2_list)
         print()

         player_1_hand = hand_1_list + community_list
         player_2_hand = hand_2_list + community_list         
        
         SF1 = straight_flush_7(player_1_hand)
         SF2 = straight_flush_7(player_2_hand)
         four_k1 = four_7(player_1_hand)
         four_k2 = four_7(player_2_hand)
         full_house1 = full_house_7(player_1_hand)
         full_house2 = full_house_7(player_2_hand)
         flush1 = flush_7(player_1_hand)
         flush2 = flush_7(player_2_hand)
         straight1 = straight_7(player_1_hand)
         straight2 = straight_7(player_2_hand)
         three_k1 = three_7(player_1_hand)
         three_k2 = three_7(player_2_hand)
         two_pair1 = two_pair_7(player_1_hand)
         two_pair2 = two_pair_7(player_2_hand)
         pair1 = one_pair_7(player_1_hand)
         pair2 = one_pair_7(player_2_hand)
         

#The section below checks in order strongest to weakest hands and returns the tie or winner and prompts for next hand
#==============================================================================
         if SF1 != False and SF2 != False:
             print("TIE with two straight flushes: " , SF1)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False


         if SF1 != False:
             print("Player 1 wins with a straight flush: " , SF1)
             community_list = []
             hand_1_list = []
             hand_2_list = []
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False

         if SF2 != False:
             print("Player 2 wins with a straight flush: " , SF1)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False

         
         if four_k1 != False and four_k2 != False:
             print("TIE with two four of a kind: " , four_k1)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False

         if four_k1 != False:
             four_k1 = cannonical(four_k1)
             print("Player 1 wins with four of a kind:" , four_k1)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False

         if four_k2 != False:
             print("Player 2 wins with four of a kind:" , four_k2)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False


         
         if full_house1 != False and full_house2 != False:
             print("TIE with two full houses: " , full_house1)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False   

         if full_house1 != False:
             print("Player 1 wins with a full house: " , full_house1)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False     

         if full_house2 != False:
             print("Player 2 wins with a full house: " , full_house2)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False                  

             
         if flush1 != False and flush2 != False:
             flush1 = cannonical(flush1)
             print("TIE with a flush:" , flush1)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False                   
 

         if flush1 != False:
             print("Player 1 wins with a flush: " , flush1)
             
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False

         if flush2 != False:
             print("Player 2 wins with a flush: " , flush2)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False

             
         if straight1 != False and straight2 != False:
             print("TIE with two straights: " , straight1)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False          
 
         if straight1 != False: 
             print("Player 1 wins with a straight: " , straight1)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False

         if straight2 != False:
             print("Player 2 wins with a straight: " , straight2)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False
        
         if three_k1 != False and three_k2 != False:
             print("TIE with two three of a kind: " , three_k1)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False


         if three_k1 != False: 
             print("Player 1 wins with three of a kind: " , three_k1)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False

         if three_k2 != False:
             print("Player 2 wins with three of a kind: " , three_k2)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False
             
             
         if two_pair1 != False and two_pair2 != False:
             print("TIE with two pairs:", two_pair1)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False
            
         if two_pair1 != False: 
             print("Player 1 wins with two pairs: " , two_pair1)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False

         if two_pair2 != False:
             print("Player 2 wins with a two pairs: " , two_pair2)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False
             
         if pair1 != False and pair2 != False:
             print("TIE with two pairs:", pair1)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False

         if pair1 != False: 
             print("Player 1 wins with a pair: " , pair1)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False


         if pair2 != False:
             print("Player 2 wins with a pair: " , pair2)
             SF1 = False
             SF2 = False
             four_k1 = False
             four_k2 = False
             full_house1 = False
             full_house2 = False
             flush1 = False
             flush2 = False
             straight1 = False
             straight2 = False
             three_k1 = False
             three_k2 = False
             two_pair1 = False
             two_pair2 = False
             pair1 = False
             pair2 = False

############################################################################
#Checks number of cards left after each hand 
         if len(my_deck) < 9:
             print("Deck has too few cards so game is done.")
             break
         x = input("Do you wish to play another hand?(Y or N) ")
         if x != "y":
             break             

##################################################
if __name__ == "__main__": #LEAVE ALONE 
#################################################    
    main()