CSC495 (Programming Languages) - Project 3
Group Q - Wenting Zheng (wzheng8), Garrett Watts (gcwatts), Raymond Woods (rjwoods3)

To Run Game:
1. Run the Game.py file
2. Console will prompt the user to choose between the two games by typing the associated number, Bartok (0) or King's Corner (1)
3. Console will prompt the user to choose number of players (1-4). 2-4 players allows multiple humans to play the game, while choosing 1 player will allow a human to play against a computer player.
4. Once the game starts, the player can play the game according to the rules outlined below.
5. Game will end when a player is declared the winner




-------------------
Kings Corner Rules:

1. Everyone is dealt a hand of 7 cards
2. The deck is then placed face down on the table
3. One card each is dealt face up directly next to the deck in each North East West South (NEWS) position
4. This creates 8 playable position on the field, the NEWS positions, and the empty corner positions.
5. On a player’s turn a player draws a card from the center deck. 
6. They can then play a card from their hand on top of a face up card, provided that the card is one value below and the opposite color suit.
   -> For example, a 4 of spades or 4 of clubs can be played on top of a 5 of hearts or a 5 of diamonds.
7. A king can only be played on one of the four empty corner spaces, and no other cards can be played on to a corner position
8. If a stack can be moved and placed on top of another stack so that the rule from step 6 is maintained for the whole new stack, the player may also do this
9. When a player decides to end their turn, they declare so and the turn moves to the next player
10. When a player has no cards left in their hand, they are declared the winner

Play commands:

	"end" 										to end your turn;
	"play: card_index, destination field" 		to play the card in your hand to destination field. Card index is after #;
		-> Example: "play: 3, n"				--- Will play the card at index 3 of your hand to the north stack, if valid
	"move: source field, destination field"		to move cards from source field to destination field.
		-> Example: "move: e, c3"				--- Will move the stack at E on top of stack C3, if valid

		
		
		
Bartok Rules:

1. Everyone is dealt a hand of 7 cards
2. One card is dealt face up on the table
3. The remaining cards are placed face down on the table as the deck
4. On a player’s turn, they can play any card of the same rank or suit by placing it on top of the face-up stack in the middle, which will end your turn
5. If you can’t play any cards, you must draw a card and your turn ends
6. Whoever runs out of cards in the hand first is declared the winner
E1: If at any point you hold all 4 cards of the same rank in your hand, you immediately win the game
E2: An ace can be played on top of any card, and the next player must play the suit chosen by the previous player. This is effectively a “wild card”

Play commands:

	"draw"						to draw a card from the desk and end your turn;
	"play card_index"			to play the card in your hand to destination field. Card index is after #;
		-> Example: "play 3"    --- Will play the card at index 3 in your hand to the stack, if valid
