import random
civilizations = ['Morocco','Greece','Assyria','Songhai','Huns','Rome','Germany','Celts','Poland','Russia',
                 'Persia','Carthage', 'England','Venice', 'Indonesia','India','Mongolia', 'Sweden', 'Ethiopia',
                 'Denmark','Arabia', 'Iroquois', 'Spain', 'Polynesia', 'Portugal', 'Austria', 'Aztecs',
                 'France', 'Babylon', 'Japan', 'Maya', 'Inca', 'Brazil', 'Shoshone', 'Egypt', 'Siam',
                 'Korea', 'Zulus', 'Ottomans', 'Byzantium', 'America', 'Netherlands', 'China']

playerNumber = int(input('Enter number of players: '))
#Debug value error of playerNumber
playerName = ['' for i in range(playerNumber)]
for name in range(playerNumber):
    playerName[name] = input(f'Enter player {name+1} name:')

while True:
    banned = input('Enter the correct name of civ you wish to ban beforehand (Type "end" to finish banning phase): ')

    if banned.lower() == 'end':
        break

    if banned.capitalize() not in civilizations:
        print('You typed it incorrectly, please try again')
        continue
    if banned.capitalize() in civilizations:
        civilizations.remove(banned.capitalize())
        print(f'{banned.capitalize()} has been removed from the pool')

displayNewCivs = input(f'Game is going to be played with {len(civilizations)} number of civilizations.'
                       f'\nDo you wish to see available pool of civilizations(type Yes to see): ')
if displayNewCivs.lower() == 'yes':
    print(civilizations)

initiallyBanned = ''

civPerPlayer = int(len(civilizations) / playerNumber)
initiallyBannedCivs = len(civilizations) - playerNumber*civPerPlayer
print(f'{initiallyBannedCivs} civilizations required to be banned beforehand to even the numbers')
for x in range(initiallyBannedCivs):
    ban = random.randint(0,len(civilizations)-1)
    initiallyBanned += civilizations[ban] + ', '
    civilizations.pop(ban)

initiallyBanned = initiallyBanned[:-2]
initiallyBanned += ' are initially banned'
print(initiallyBanned+ '\n Each player will now have a pool of '+ str(civPerPlayer)+' civilizations')
random.shuffle(civilizations)
player = [['' for j in range(civPerPlayer)] for i in range(playerNumber)]

for k in range(playerNumber):
    for m in range(civPerPlayer):
        player[k][m] = civilizations[0]
        civilizations.pop(0)
civMsg = ''
for i in range(playerNumber):
    availCivMsg = f'Available civilizations for "{playerName[i]}" are '
    for j in range(civPerPlayer):
        civMsg += player[i][j] + ', '
    civMsg = civMsg[:-2]
    print(availCivMsg + civMsg)
    civMsg = ''
for j in range(civPerPlayer):

    for i in range(playerNumber):
        if len(player[i]) == 1:
            print(f'The civilization for "{playerName[i]}" is {player[i][0]}')
            continue
        while True:
            removeMsg = input(f'Civs for {playerName[i]} are {player[i]} '
                              f'\n{playerName[i]} remove a civ: ')
            if removeMsg.capitalize() in player[i]:
                break
            else:
                print('You typed it wrong. Please write again ')
        player[i].remove(removeMsg.capitalize())
        if len(player[i]) == 1:
            print(f'The civilization for "{playerName[i]}" is {player[i][0]}')
            continue
        banP = random.randint(0,len(player[i])-1)
        removedCivMsg = player[i][banP]
        player[i].remove(removedCivMsg)
        print(f'The computer removed {removedCivMsg} for {playerName[i]}')
        if len(player[i]) == 1:
            print(f'The civilization for "{playerName[i]}" is {player[i][0]}')
            continue
    if len(player[playerNumber-1]) == 1:
        break
print("Have a nice game!")