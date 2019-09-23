# poker
This is a simple OOP, which contains 3 object classes to 'deal' 5 cards to a given number of players and compare the hands, in accordance with the rules of poker.

The three classes are:

**Card** , **Deck** , and **Poker**

The general purposes of their methods and attributes are as follows:

***Card***

- Hold the value of a card's rank and suit
- Override comparison operators

***Deck***

- Create all 52 cards (jokers not included)
- Allow for multiple decks to be added together
- Shuffle the deck

***Poker***

- Create a Deck instance, shuffle, and deal a given number of cards (default 5) to each player (number of players is given from user input
- Assign a number of points to each hand based on its poker hand, and the card values that make it up to that, for example, a straight will beat a three of a kind, but an A,K,Q,J,10 straight will beat a 6,5,4,3,2 straight.
-Print the hands of each player, and the winner(s) of each round.
