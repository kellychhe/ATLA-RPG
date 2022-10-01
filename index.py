#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def gameIntro():
    # set up the storyline for the game with the intro from the show
    print('''
    Water.
    Earth.
    Fire.
    Air

    Long ago, the four nations lived together in harmony. Then everything changed when the Fire Nation attacked.

    Only the Avatar, master of all four elements, could stop them. But when the world needed him most, he vanished.

    A hundred years passed and my brother and I discovered the new avatar:

    An airbender named Aang, 
    and although his airbending skills are great he still has a lot to learn before he's ready to save anyone.
    
    But I believe Aang can save the world.
    
    ''')

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    How to play:
    ============
    Commands:      
        go [direction]
        yipyip [city]
        meet [character]
        learn [element]

    As Katara, you must find Aang and explore the four kingdoms to help him master all the elements before the Fire Nation destroys the world!
    
    Avoid Fire Nation spies posing as bending masters throughout the kingdom.
    Find Fire Lord Ozai to stop him from carrying out his sinister plans!

    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentCity)
    # print Aang's bending skills
    print('Aang\'s skills:', skills)
    # print the player's friends 
    print('Friends:', friends)
    # check if there's an item in the room, if so print it
    if "character" in city[currentCity]:
        print('You see ' + city[currentCity]['character'])
    if "skill" in city[currentCity]:
        print('Hmmmm... are there any skills to learn here?')
    print("---------------------------")


# skills needed to win the game, which is initially empty
skills = ['air']

# friends you find along the way 
friends = ['Sokka']

# fire nation enemies
enemies = ['Man In Green Shirt', 'Man In Blue Shirt', 'Man In Red Shirt']
boss = 'Fire Lord Ozai'

## A dictionary linking cities
city = {
    'Southern Water Tribe' : {
        'north'     : 'Southern Air Temple',
        'country'   : 'Water Tribe',
        'character' : 'Aang',
    },
    'Southern Air Temple' : {
        'south'     : 'Southern Water Tribe',
        'east'      : 'Kyoshi Island',
        'country'   : 'Air Nomads',
        'character' : 'Appa',
    },
    'Kyoshi Island' : {
        'north'     : 'Omashu',
        'east'      : 'Gaoling',
        'west'      : 'Southern Air Temple',
        'country'   : 'Earth Kingdom',
        'character' : 'Suki',
    },
    'Omashu' : {
        'north'     : 'Fire Nation Colony',
        'south'     : 'Kyoshi Island',
        'east'      : 'Wan Shi Tong\'s Library',
        'west'      : 'Roku\'s Island',
        'country'   : 'Earth Kingdom',
    },
    'Gaoling' : {
        'north'     : 'Wan Shi Tong\'s Library',
        'east'      : 'Eastern Air Temple',
        'west'      : 'Kyoshi Island',
        'country'   : 'Earth Kingdom',
        'character' : 'Toph',
        'skill'     : 'earth',
    },
    'Wan Shi Tong\'s Library' : {
        'north'     : 'Ba Sing Se',
        'south'     : 'Gaoling',
        'west'      : 'Wan Shi Tong\'s Library',
        'country'   : 'Earth Kingdom',
    },
    'Eastern Air Temple' : {
        'west'      : 'Gaoling',
        'country'   : 'Air Nomads',
        'character' : 'Momo',
    },
    'Fire Nation Colony' : {
        'north'     : 'Northern Water Tribe',
        'south'     : 'Omashu',
        'east'      : 'Ba Sing Se',
        'west'      : 'Western Air Temple',
        'country'   : 'Earth Kingdom',
        'character' : 'Man In Red Shirt',
    },
    'Ba Sing Se' : {
        'south'     : 'Wan Shi Tong\'s Library',
        'west'      : 'Fire Nation Colony',
        'country'   : 'Earth Kingdom',
        'character' : 'Man In Green Shirt',
    },
    'Northern Water Tribe' : {
        'south'     : 'Fire Nation Colony',
        'country'   : 'Water Tribe',
        'skill'     : 'water',
    },
    'Western Air Temple' : {
        'south'     : 'Fire Nation Capital',
        'east'      : 'Fire Nation Colony',
        'country'   : 'Air Nomads',
        'character' : 'Man In Blue Shirt',
    },
    'Fire Nation Capital' : {
        'north'     : 'Western Air Temple',
        'east'      : 'Roku\'s Island',
        'country'   : 'Fire Nation',
        'character' : 'Fire Lord Ozai'
    },
    'Roku\'s Island' : {
        'east'      : 'Omashu',
        'west'      : 'Fire Nation Capital',
        'country'   : 'Fire Nation',
        'character' : 'Zuko',
        'skill'     : 'fire',
    },
}

# start the player in the Southern Water Tribe   
currentCity = 'Southern Water Tribe'

def main():
    
    global currentCity

    gameIntro()

    showInstructions()

    # breaking this while loop means the game is over
    while True:
        showStatus()

        # the player MUST type something in otherwise input will keep asking for a move
        move = ''
        while move == '':
            move = input('>')

        # normalizing input into lower case and a list
        move = move.lower().split(" ", 1)

        #if they type 'go' first
        if move[0] == 'go':
            #check that they are allowed wherever they want to go
            if move[1] in city[currentCity]:
                #set the current city to the new city
                currentCity = city[currentCity][move[1]]
            # if they aren't allowed to go that way:
            else:
                print('You can\'t go that way!')
        
        #if they type 'yipyip' first
        # they can choose any city if they have appa as a friend
        if move[0] == 'yipyip':
            if 'Appa' in friends:
            #check that they are allowed wherever they want to go
                if move[1].title() in city:
                  #set the current city to the new city
                    currentCity = move[1].title()
                # if they aren't allowed to go that way:
                else:
                    print('Not a valid city!')
            else: 
                print("You can't fly anywhere without Appa!")

        #if they type 'meet' first
        if move[0] == 'meet' :
            if move[1].title() in friends:
                print(move[1].title() + " is already in your friend group!")
            # does the current city contains a character
            if "character" in city[currentCity] and move[1].title() == city[currentCity]['character']:
                # is the character a spy
                if move[1].title() in enemies:
                    print("OH NO!! You just met a fire nation spy!")
                    # did aang learn all the skills. if yes then he beats henchmen if no he loses
                    if len(skills) != 4:
                        print("Aang and the gang don't have the skills to fight Fire Lord Ozai\'s henchmen.")
                        print(move[1].title() + " has defeated Aang and all of your friends. Now there is no one left to stop Fire Lord Ozai... GAME OVER")
                        break
                    else: 
                        # remove henchman from game
                        print("Wow!! Aang and the gang defeated " + move[1].title() + " with impeccable teamwork and the skills from all the nations!")
                        del city[currentCity]['character']
                # did aang learn all the skills. if yes then he beats the entire game if no he loses
                elif move[1].title() == boss:
                    print("""It is now time for the ultimate battle, what Aang has been training for all his life. 
                    This is his one and only chance at defeating Fire Lord Ozai and foil is heinous plans!""")
                    if len(skills) == 4:
                        print("AANG HAS MASTERED ALL OF THE ELEMENTS AND DEFEATED FIRE LORD OZAI. THE WORLD IS IN PEACE ONCE AGAIN")
                        print("GOOD WORK TEAM! YOU WIN!!!!")
                        break
                    else: 
                        print("Aang and the gang don't have the skills to fight Fire Lord Ozai\'s.")
                        print(move[1].title() + " has defeated Aang and all of your friends.")
                        print("Fire Lord Ozai has colonized the entire world and erradicated all other benders from existance... GAME OVER")
                        break
                # if the character is a friend and not and enemy or the boss then add them to friend group
                else:
                    print("The gang meets " + move[1].title() + ". They're super cool and would love to join the fight against Fire Lord Ozai\'s agenda!")
                    friends.append(city[currentCity]['character'])
                    del city[currentCity]['character']
            # if there's no character in the city
            else:
                #tell them the person is not there
                print(move[1] + ' is not here!')

        ## if they type 'learn'
        if move[0] == 'learn':
            # make sure aang is a part of the gang
            if "Aang" in friends:
                # learn and remove skill from dictionary
                if 'skill' in city[currentCity]:
                    if move[1] == city[currentCity]['skill']:
                        print("Aang has mastered " + city[currentCity]['skill'] + " bending!")
                        skills.append(city[currentCity]['skill'])
                        del city[currentCity]['skill']
                    else:
                        print("You cannot learn that skill here.")
                else:
                    print("There seems to be no skills to learn here right now...")
            else: 
                "Find Aang to learn new skills!"

if __name__ == "__main__":
    main()