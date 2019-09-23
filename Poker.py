#  File: Poker.py

#  Description:

#  Student's Name: Mitchel Walker

#  Student's UT EID: mlw3852

#  Course Name: CS 313E 

#  Unique Number: 50725

#  Date Created: 2/17/19

#  Date Last Modified:

import random



class Card(object):
    ranks = (2,3,4,5,6,7,8,9,10,11,12,13,14)
    suits = ('C','D','H','S')

    #constructor
    def __init__(self, rank = 14, suit = 'S'):
        if rank in Card.ranks:
            self.rank = rank
        else:
            self.rank = 14

        if suit in Card.suits:
            self.suit = suit
        else:
            self.suit = 'S'

    #string representation
    def __str__(self):
        if self.rank == 14:
            rank = 'A'
        elif self.rank == 13:
            rank = 'K'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 11:
            rank = 'J'
        else:
            rank = str(self.rank)
        return rank + self.suit

    #equality tests
    def __eq__(self,other):
        return self.rank == other.rank

    def __ne__(self,other):
        return self.rank != other.rank

    def __lt__(self,other):
        return self.rank < other.rank

    def __le__(self,other):
        return self.rank <= other.rank

    def __gt__(self,other):
        return self.rank > other.rank

    def __ge__(self,other):
        return self.rank >= other.rank
    


class Deck(object):
    #constructor
    def __init__(self, num_decks = 1):
        self.deck = []
        for i in range(num_decks):
            for suit in Card.suits:
                for rank in Card.ranks:
                    card = Card(rank, suit)
                    self.deck.append(card)

    #shuffle the deck
    def shuffle(self):
        random.shuffle(self.deck)

    #dealing a card
    def deal(self):
    #removes and returns the 'top' card (position 0)
        if len(self.deck) == 0:
            return None
        else:
            return self.deck.pop(0)




class Poker(object):
    
    #constructor
    def __init__(self, num_players = 2, num_cards = 5):
        self.deck = Deck()
        self.deck.shuffle()
        self.all_hands = []
        self.num_cards = num_cards
        self.num_players = num_players


        #setup empty array of all hands
        for i in range(self.num_players):
            hand = [0]*num_cards
            self.all_hands.append(hand)
            
        #deal cards to all players
        for j in range(num_cards):
            for i in range(self.num_players):
                self.all_hands[i][j] = self.deck.deal()


    #play the game of poker
    def play(self):
        #sort and print the hands of each player
        print("\n")
        for c, hand in enumerate(self.all_hands):
            sorted_hand = sorted(hand,reverse = True)
            #sorted_hand = hand
            self.all_hands[c] = sorted_hand
            #print the sorted hand
            hand_str = ''
            for card in self.all_hands[c]:
                hand_str += str(card) + ' '
            print('Player ' + str(c+1) + ':' + hand_str)

        #Create two lists, one for player's points, the other for the player's hands
        print("\n")
        hand_type = []
        hand_points = []
        for c,hand in enumerate(self.all_hands):
            pts, h_type = self.check_all_hands(hand)
            hand_type.append(h_type)
            hand_points.append(pts)
        #print each player's hand
        for i in range(len(hand_type)):
            print("Player " + str(i+1) + ": " + hand_type[i])
        print("\n")
        #determine the player with the highest number of points
        winner = hand_points.index(max(hand_points))
        #determine if any players tie
        tied_players = [winner]
        for i in range(len(hand_type)):
            if (hand_type[i] == hand_type[winner]) and (i != winner):
                tied_players.append(i)
        if tied_players != [winner]:
            #create dictionairy of points of tying players
            tied = {}
            for num in tied_players:
                tied[hand_points[num]] = num
            #print in order of most points
            while tied != {}:
                next_player = tied[max(tied)]
                print("Player %s ties." % (str(next_player + 1)))
                del tied[max(tied)]
        else:
            print("Player %s wins." % str(winner + 1))
                



    def check_all_hands(self,hand):
        #this function runs through all the possible hands and returns
        #the highest matching hand and its points (points, hand name)
        #the if statement is necessary because some lower hands return non-null when higher hands are valid
        if self.is_royal(hand) is not None:
            return self.is_royal(hand)
        if self.is_straight_flush(hand) is not None:
            return self.is_straight_flush(hand)
        if self.is_four_kind(hand) is not None:
            return self.is_four_kind(hand)
        if self.is_full_house(hand) is not None:
            return self.is_full_house(hand)
        if self.is_flush(hand) is not None:
            return self.is_flush(hand)
        if self.is_straight(hand) is not None:
            return self.is_straight(hand)
        if self.is_three_kind(hand) is not None:
            return self.is_three_kind(hand)
        if self.is_two_pair(hand) is not None:
            return self.is_two_pair(hand)
        if self.is_one_pair(hand) is not None:
            return self.is_one_pair(hand)
        if self.is_high_card(hand) is not None:
            return self.is_high_card(hand)
    


    #functions to determine the type of hand
    #returns total number of points for a given hand and a string of the type of hand
    def is_royal(self, hand):
        #check for flush
        same_suit = True
        for i in range(len(hand)-1):
            if hand[i].suit != hand[i+1].suit:
                return
            
        #check for straight of 5 highest cards
        order = True
        for i in range(len(hand)):
            if hand[i].rank != 14-i:
                return
        
        #award points
        points = 10*15**5 + hand[0].rank*15**4 + hand[1].rank*15**3 + hand[2].rank*15**2
        points += hand[3].rank*15 + hand[4].rank

        return points, 'Royal Flush'


    def is_straight_flush(self,hand):
        #check for flush
        same_suit = True
        for i in range(len(hand)-1):
            if hand[i].suit != hand[i+1].suit:
                return

        #check for straight
        order = True
        for i in range(len(hand)-1):
            if hand[i].rank != hand[i+1].rank + 1:
                return

        #award points
        points = 9*15**5 + hand[0].rank*15**4 + hand[1].rank*15**3 + hand[2].rank*15**2
        points += hand[3].rank*15 + hand[4].rank
        
        return points, 'Straight Flush'


    def is_four_kind(self,hand):
        #check for 4 of a kind
        #make a list of every rank
        ranks_list = []
        for card in hand:
            ranks_list.append(card.rank)
        #delete the unlike card
        if ranks_list[0] == ranks_list[1]:
            #set the position of the unlike card
            unlike_card = -1
            del ranks_list[-1]
        else:
            unlike_card = 0
            del ranks_list[0]
        #create a set of ranks list and make sure it only has one value
        if len(set(ranks_list)) != 1:
            return
        
        
            
        #award points
        points = 8*15**5 + ranks_list[0]*(15**4 + 15**3 + 15**2 + 15)
        points += hand[unlike_card].rank

        return points, 'Four of a Kind'


    def is_full_house(self,hand):
        #make a list of every rank
        ranks_list = []
        for card in hand:
            ranks_list.append(card.rank)
        #split the two rank types into two lists
        if ranks_list[1] != ranks_list[2]:
            two_kind = ranks_list[:2]
            three_kind = ranks_list[2:]
        else:
            three_kind = ranks_list[:3]
            two_kind = ranks_list[3:]
        #check that each list only makes a set with 1 element
        if len(set(two_kind)) != 1 or len(set(three_kind)) != 1:
            return

            
        #award points
        points = 7*15**5 + three_kind[0]*(15**4 + 15**3 + 15**2)
        points += two_kind[0]*(15 + 1)

        return points, 'Full House'


    def is_flush(self,hand):
        #check for all cards being the same suit
        for i in range(len(hand)-1):
            if hand[i].suit != hand[i+1].suit:
                return
        
        #award points
        points = 6*15**5 + hand[0].rank*15**4 + hand[1].rank*15**3 + hand[2].rank*15**2
        points += hand[3].rank*15 + hand[4].rank

        return points, 'Flush'

    def is_straight(self,hand):
        #check for all cards in order
        for i in range(len(hand) -1):
            if hand[i].rank != hand[i+1].rank + 1:
                return
            
        #award points
        points = 5*15**5 + hand[0].rank*15**4 + hand[1].rank*15**3 + hand[2].rank*15**2
        points += hand[3].rank*15 + hand[4].rank

        return points, 'Straight'


    def is_three_kind(self,hand):
        #check for three of a kind
        #create list of ranks
        rank_list = []
        for card in hand:
            rank_list.append(card.rank)
        #check that there are three in a row, and no more than three of a kind
        for i in range(3):
            if rank_list[i] == rank_list[i + 2]:  
                check_set = set(rank_list[i:i+3])
                del rank_list[i:i+3]
                if len(check_set) ==1 and len(set(rank_list))!= 1:
                    #award points
                    points = 4*15**5 + check_set.pop()*(15**4 + 15**3 + 15**2)
                    points += rank_list[0]*15 + rank_list[1]

                    return points, 'Three of a Kind'
                else:
                    return
        
        

    def is_two_pair(self,hand):
        #create list of ranks
        ranks_list = []
        for card in hand:
            ranks_list.append(card.rank)
        #remove two pairs and add their rank to a list of pair ranks
        pair_ranks = []
        for i in range(len(ranks_list)-1):
            if ranks_list[i] == ranks_list[i+1]:
                pair_ranks.append(ranks_list[i])
            elif ranks_list[i] not in pair_ranks:
                no_pair = ranks_list[i]
            elif ranks_list[i+1] not in pair_ranks:
                no_pair = ranks_list[i+1]
        #check that there are only two values and no duplicating values
        if len(set(pair_ranks)) == 2:
            #award points
            points = 3*15**5 + pair_ranks[0]*(15**4 + 15**3) + pair_ranks[1]*(15**2 + 15)
            points += no_pair

            return points, 'Two Pair'

        else:
            return
        

        
        


    def is_one_pair(self,hand):
        #make a set of ranks and ensure that it has four values
        card_ranks = set()
        for card in hand:
            card_ranks.add(card.rank)
        if len(card_ranks) != 4:
            return
        #determine the repeating card
        for i in range(len(hand)):
            for j in range(len(hand[i:])):
                if hand[i].rank == hand[j].rank:
                    pair_rank = hand[i].rank
                    pair_position = (i,j)
        #create a list of ranks that are not the pair
        no_pair_ranks = []
        for c in range(len(hand)):
            if c != i and c != j:
                no_pair_ranks.append(hand[c].rank)
            
        
        #award points
        points = 2*15**5 + pair_rank*(15**4 + 15**3) + no_pair_ranks[0]*15**2
        points += no_pair_ranks[1]*15 + no_pair_ranks[2]

        return points, 'One Pair'


    def is_high_card(self,hand):
        #because it is the last method, no checking is needed
        #award points
        points = 1*15**5 + hand[0].rank*15**4 + hand[1].rank*15**3 + hand[2].rank*15**2
        points += hand[3].rank*15 + hand[4].rank

        return points, 'High Card'



        
def main():
    deck = Deck()
    deck.shuffle()
    num_players = eval(input("Enter Number of Players: "))
    game = Poker(num_players)
    game.play()



main()




    
