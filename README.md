# DutchGame
Dutch Card Game Is Python Project for Polish-Japanese Academy of Information Technology

## How to Start Game?

Go to Game directory and run command (This Game needs to be run terminal or cmd):

### mac/linux (using Termainal):
```bash
$ python3 main.py
```

### Windows (using Cmd):
If you use windows you need to install 
[window curses](https://pypi.org/project/windows-curses/) library!

```commandline
python main.py 
```

## Rules
### Start of game
1. On start every player gets 4 cards to it's deck.
2. Every player needs to check two of it's own cards

### Player Moves
1. Look at own card - Player can look at card in his deck
2. Look at any card - Player can look at any player card
3. Dutch - It sets Last round and after whole circle it players cards values are counted and player with the lowest card value wins
4. Jump In - Player can jump with card that is in his deck to used stack and if card rank is same as in card on used stack player looses one card from he's deck but if Card rank is different Player gets additional card to he's deck from stack.
5. Take Card From Stack - Player can take card from stack to he's placeholder.
6. Take Card From Used Stack - Player can take card from used stack to he's placeholde.
7. Replace Card From Own Deck - Player can take card from Placeholder and replace he's own card with it.
8. Put Card On Used Stack - Player can Put card from Placeholder to the used stack 

### How To Win
There are two possible ways to win a game
1. Jump Ins - if player does not have any cards after jumpin Player Wins
2. Dutch - if any player Dutched the Game and after one more round that player wins which have the lowest cards Value in deck

