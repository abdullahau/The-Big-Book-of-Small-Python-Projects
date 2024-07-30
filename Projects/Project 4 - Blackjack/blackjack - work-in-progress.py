import sys
from random import shuffle

def getBet(maxBet):
    while True:
        print(f'How much do you bet? (1-{maxBet}, or QUIT)')
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue 

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def getDec(deckNum=1):
    suits = ['♥', '♦', '♠', '♣']
    ranks = list(map(str,range(2,11))) + ['J', 'Q', 'K', 'A']
    deck = [(rank, suit) for suit in suits for rank in ranks for _ in range(deckNum)]
    shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        displayCards(['BACKSIDE'] + dealerHand[1:])

    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)

def displayCards(cards):
    rows = ['', '', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += ' ___  '
        if card == 'BACKSIDE':
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += f'|{rank.ljust(2)} | '
            rows[2] += f'| {suit} | '
            rows[3] += f'|_{rank.rjust(2, '_')}| '

    for row in rows:
        print(row)

def getHandValue(cards):
    value = 0 
    numAces = 0
    
    for card in cards:
        if card[0] == 'A':
            numAces += 1
        elif card[0] in {'J', 'Q', 'K'}:
            value += 10
        else:
            value += int(card[0])
    
    value += numAces
    for i in range(numAces):
        if value + 10 <= 21:
            value += 10
    
    return value