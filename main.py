import const, os, random, time, threading, json, sys

### DYNAMIC STATS
money = 0
toBuy = const.ItemsToBuy
pp = 0 # persuasion points. every roll adds or subtract from the persuation point: rollNum - 10 = persuation + or persuation -
total_score = 0

# will be used by the timer
sec_elapsed = 0
min_elapsed = 0
za_warudo = False

# main dynamic dics
stores = { # will contain all available stores at the start of the game 
          # 'store 1':{
          #     'cat':{
          #         'item':[min, max],...
          #     },...
          # },
          # ...
}

bought = { # bought items will be updated here
        # cat:{
          #  'item': quantity
          # }
}

shopList = { # shopping list will be appended and removed here
        # item: quantity
}

leaderboard = {} # placeholder leaderboard if leaderboard.json is yet to be loaded

HighScore = 0
TopPlayer = None


### PRE-PROCESSING FUNCTIONS

# DEF A FUNCTION that loads leaderboard.json and creates a new leaderboard dicitonary
def loadLeaderboard():
    global leaderboard, HighScore, TopPlayer
    try:
        with open('leaderboard.json', 'r') as file:
            leaderboard = json.load(file)
        HighScore = max(leaderboard.items(), key=lambda look: look[1])[1]
        TopPlayer = max(leaderboard.items(), key=lambda look: look[1])[0]
    except:
        pass


# DEF A FUNCTION that sorts and updates leaderboard.json (at the start of the game and at the end of the game)
def updateLeaderboard(new_entry=None): # new_entry format: {'player': score}
    global leaderboard
    if new_entry != None:
        leaderboard.update(new_entry)

    leaderboard = {name: score for name, score in sorted(leaderboard.items(), key=lambda look: look[1], reverse=True)}
    with open('leaderboard.json', 'w') as file:
        json.dump(leaderboard, file, indent=4)

# DEF A FUNCTION that gets the maximum length of characters in a list or dictionary
def max_char_length_in(iterable):
    max = 0
    for item in iterable:
        if len(item) > max:
            max = len(item)
    return max

# PRIO: DEF A FUNCTION that gets the maximum length of store names and item names (child inclusive)
def max_name_length():
    max = 0
    for type in const.items:
        if len(type) > max:
            max = len(type)
        for item in const.items[type]:
            if len(item) > max:
                max = len(item)
    return max
maxStrLn = max_name_length() + len('[x] ') # '[x] ' is added to an item at its head when printing in an oredered list

# PRIO: DEF A FUNCTION that runs a stopwatch in a threaded process
def stopwatch():
    global sec_elapsed, min_elapsed

    while za_warudo  == False:
        if sec_elapsed < 59:
            sec_elapsed += 1
            time.sleep(1)
        else:
            sec_elapsed = 0
            min_elapsed += 1
            time.sleep(1)
doStopwatch = threading.Thread(target=stopwatch) # call this to start stopwatch


### DEBUGGING FUNCTIONS
def viewStoresR():
    for s in stores:
        print(s)
        for cat in stores[s]:
            print(f'\t{cat} | n items from: {len(const.items[cat])} | n items got: {len(stores[s][cat])}')
            for item in stores[s][cat]:
                print(f'\t\t{item}: {stores[s][cat][item]}')

### GRAPHIC FUNCTIONS

def clear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        print('Clear error')

def header():
    print('''

-------------------------------------------------------------

    ''')

# DEF A FUNCTION that prints the start game menu and the game ascii title
def mainMenu(HighScore):
    while True:
        clear()
        header()
        print(r'''
    ___                  ___                           ___  
    (   )                (   )                         (   ) 
    | |.-.    ___  ___   | |.-.     .--.    ___  ___   | |  
    | /   \  (   )(   )  | /   \   /    \  (   )(   )  | |  
    |  .-. |  | |  | |   |  .-. | |  .-. ;  | |  | |   | |  
    | |  | |  | |  | |   | |  | | | |  | |  | |  | |   | |  
    | |  | |  | |  | |   | |  | | | |  | |  | '  | |   | |  
    | |  | |  | |  | |   | |  | | | |  | |  '  `-' |   | |  
    | '  | |  | |  ; '   | '  | | | '  | |   `.__. |   |_|  
    ' `-' ;   ' `-'  /   ' `-' ;  '  `-' /   ___ | |   .-.  
    `.__.     '.__.'     `.__.    `.__.'   (   )' |  (   ) 
                                            ; `-' '   '-'  
                                            .__.'         
        ''')
        if TopPlayer != None:
            print(f"\tHIGH SCORE: {HighScore}\t\tTOP PLAYER: {TopPlayer}")
        header()
        menu_select = selection(['Start Game', 'View Leaderboard'], 'H')
        if menu_select == 'Start Game':
            loading_screen(random.choice(const.gameTips))
            gameGreeter()
            storeMenu()
            return
        elif menu_select == 'View Leaderboard':
            viewLeaderboard(mainMenu, HighScore)
        else:
            continue


# PRIO: DEF A FUNCTION that prints stats and header()
def stats():
    clear()
    header()
    print(f'\tItems left to buy:{toBuy}\t\tTime elapsed: {min_elapsed}:{sec_elapsed:02d}\n\tMoney: {money}\t\t\tPP:{pp}')
    print()

# DEF A FUNCTION that presents a loading screen with random loading texts
def loading_screen(quote=random.choice(const.gameTips)):
    loadingSpd = random.randint(6, 11)

    loadingDots = ''
    for n in range(1, loadingSpd + 1):
        clear()
        header()
        print(f"\tLoading{loadingDots}\n")
        print(f" {quote}")
        header()
        loadingDots += '.'
        time.sleep(0.5)

# DEF A FUNCTION that prints the leaderboard
def viewLeaderboard(called_from, args=None):
    try:
        maxStrLn = max(len(name) for name in leaderboard) + 3
    except:
        maxStrLn = 0

    clear()
    header()
    print('\tLEADERBOARD\n')
    print(f"\t\t{just(' | NAME |', custom=maxStrLn)} | SCORE |")
    if len(leaderboard) == 0:
        print('\n\tThe leaderboard is empty. Start playing!')
    else:
        for i, player in enumerate(leaderboard):
            print(f'\t\t{i+1}  {just(player, custom=maxStrLn)}  {leaderboard[player]}')
    header()

    menu_select = selection(['go back'], 'H')
    called_from(args)

# PRIO: DEF A FUNCTION that dynamically justifies a singular string's tail depending on their character length
def just(string, sep=' ', custom=None):
    if custom == None:
        new_str = string.ljust(maxStrLn + 1, sep)
    else:
        new_str = string.ljust(custom + 1, sep)
    return new_str


### PRE GAME FUNCTIONS

# PRIO: DEF A FUNCTION that prints selection and returns choice
def selection(options, format=None, special=None): # options must be list
    global za_warudo
    maxStrLn = max_char_length_in(options)

    if format == 'H': # horizontal print
        for i, op in enumerate(options):
            if i == 2:
                print(f"\n{f'[{i+1}] {op}'.ljust(maxStrLn)}", end='\t\t')
            else:
                print(f"[{i+1}] {op}".ljust(maxStrLn), end='\t\t')
        print()
    elif format == 'V': # vertical print
        for i, op in enumerate(options):
            print(f'[{i+1} {op}]')
    # else: don't print the options
    
    while True:
        selected = input('>>> ')
        if selected == 'b':
            return selected
        if selected == special:
            return special
        if selected == 'go home':
            za_warudo = False
            goHome()
            return

        try:
            selected = int(selected)
        except:
            print('Invalid input.')
            continue
        if selected not in range(1, len(options) + 1):
            print('Invalid input.')
            continue
        else:
            break

    for i, op in enumerate(options):
        if selected == i + 1:
            return op

# PRIO: DEF A FUNCTION that rolls for a dice, modifies the persu, and returns a roll result
def roll(): # 1,   2, 3, 4,     5, 6, 7, 8, 9, 10,      11, 12, 13, 14, 15, 16      ,17, 18, 19,    20
    global pp
    if pp > 5:
        pp = 0
    if pp < -3:
        pp = 0

    rollVal = random.randint(1, 20) + pp
    if rollVal > 20:
        rollVal = 20

    if rollVal <= 1:
        result = 'catastrophic'
        pp -= 2
    elif rollVal in range(2, 5):
        result = 'very bad'
        pp -= 1
    elif rollVal in range(5, 11):
        result = 'bad'
    elif rollVal in range(11, 17):
        result = 'good'
        pp += 1
    elif rollVal in range (17, 20):
        result = 'great'
        pp += 2
    else:# rollVal == 20
        result = 'perfect'
        pp += 3

    return {'value': rollVal, 'result': result}

# PRIO: DEF A FUNCTION that gets random store names and append them to stores{}
def getStores():
    stores.update(dict.fromkeys(random.sample(const.StoreNames, const.StoreNum)))
    for s in stores:
        stores[s] = {}

# PRIO: DEF A FUNCTION that gets atleast X amount of items from const.Items[type] and appends them to a single store
def getItemsForStores():
    for s in stores:
        for cat in const.items: # get categories and items
            nItemsToGet = round(const.ItemsObtainable * len(const.items[cat]))
            stores[s].update({cat: dict(random.sample(list(const.items[cat].items()), nItemsToGet))})
            for item in stores[s][cat]:
                stores[s][cat][item] = random.randint(*stores[s][cat][item])

# PRIO: DEF A FUNCTION that gets random X items from const.shoppable and appends them to shopList
def getItemsForShopList():
    global toBuy
    blacklist = []
    while True:
        for item in const.shoppable:
            if item in blacklist:
                continue
            if isinstance(const.shoppable[item], dict) and random.choice(list(const.shoppable)) == item:
                if random.choice([True, False]):
                    if len(shopList) < toBuy:
                        item_qty = random.randint(*const.shoppable[item]['any'])
                        shopList.update({item:{'to buy': item_qty, 'bought': 0}})
                    else:
                        break
                else:
                    pickFrom = list(const.shoppable[item].keys())
                    pickFrom.remove('any')
                    sub_itemsGot = 0

                    for sub_item in pickFrom:
                        if random.choice([True, False]):
                            if len(shopList) < toBuy:
                                item_qty = random.randint(*const.shoppable[item][sub_item])
                                shopList.update({sub_item:{'to buy': item_qty, 'bought': 0}})
                                sub_itemsGot += 1
                            else:
                                break

                            if random.choice([True, False]):
                                break
                        if sub_itemsGot >= 2:
                            break
                blacklist.append(item)

            elif isinstance(const.shoppable[item], list) and random.choice(list(const.shoppable)) == item:
                if len(shopList) < toBuy:
                    item_qty = random.randint(*const.shoppable[item])
                    shopList.update({item:{'to buy': item_qty, 'bought': 0}})
        if len(shopList) >= toBuy:
            break
    toBuy = len(shopList)

# PRIO: DEF A FUNCTION that picks a random dialogue from the relevant category
def getSay(cat):
    return random.choice(const.Dialogues[cat])

### MID GAME FUNCTIONS

# DEF A FUNCTION where Buboy's mother will tell him to buy specific items + give buboy money
def gameGreeter():
    global money
    dialogue = 'Buboy! Bili ka muna dyan sa labas. Ito listahan oh.'
    printed = ''
    for i, c in enumerate(dialogue):
        clear()
        header()
        if i == 0:
            print("\t", end='')
        printed += c
        print(printed, end='')
        print()
        time.sleep(0.02)
    
    print(f"\n\t{just('| ITEM |')}| QTY |")
    for item in shopList:
        print(f"\t{just(item, '-')}  {str(shopList[item]['to buy']).ljust(3)}")
    header()

    # give buboy money
    choice_list = []
    for listed in shopList:
        already_found = False
        for cat in const.items:
            if already_found == True:
                break
            if listed in cat:
                money += const.items[cat][random.choice(const.items[cat])][0] * shopList[listed]['to buy'] + const.moneyModifier
                already_found = True
                continue
            else:
                for child in const.items[cat]:
                    if listed in child:
                        choice_list.append(child)
    for cat in const.items:
        try:
            money += const.items[cat][str(random.choice(choice_list))][0] * shopList[listed]['to buy'] + const.moneyModifier
        except:
            pass

                #for child in const.items[cat]:
                 #   if listed in child:
                  #      money += const.items[cat][child][0] * shopList[listed]['to buy']

    time.sleep(3)
    input('>>> ')
    print("\nOkay po ma!")
    time.sleep(1)
    doStopwatch.start()

# PRIO: DEF A FUNCTION that prints shopping list that can go back to the previous menu it was called from
def viewShopList(called_from, args=None): # args should be a list
    stats()
    print(f'\tSHOPPING LIST')
    print(f"\t{just('| ITEM |')}| QTY | BOUGHT")
    for item in shopList:
        print(f"\t{just(item, '-')}  {str(shopList[item]['to buy']).ljust(3)} |   {shopList[item]['bought']}")
    header()

    menu_select = selection(['back'], 'H')
    if args == None:
        called_from()
        return
    else:
        if isinstance(args, (list, tuple)):
            called_from(*args)
        else:
            called_from(args)

# PRIO: DEF A FUNCTION for a store menu
last_visited_store = None
def storeMenu():
    global last_visited_store
    stats()
    print('\tSTORES')
    if last_visited_store != None:
        print(f'\tLast visited: {last_visited_store}\n')
    print('\t\t[V] VIEW SHOPPING LIST')
    for i, s in enumerate(stores):
        print(f'\t\t[{i+1}] {s}')
    header()

    while True:
        store_select = selection(stores, special='V')
        if store_select == 'b':
            storeMenu()
            return
        elif store_select == 'V':
            viewShopList(storeMenu)
        else:
            break

    last_visited_store = store_select
    itemMenu(store_select)

# PRIO: DEF A FUNCCTION for an item menu, which navigates through item types
def itemMenu(store, startpage=0):
    if len(shopList) == 0:
        allItemsBought(itemMenu, store)

    current_cat = ''
    last_page = len(stores[store]) - 1
    current_page = startpage # 3, powdered drinks
    message = None

    # 0 - chichirya
    # 1 - condiments
    # 2 - inumin
    # 3 - powdered drinks

    while True:
        stats()
        print(f'\t{store}\n')

        for i, cat in enumerate(stores[store]):
            current_cat = cat
            if i == current_page:
                break

        print(f'\t{current_cat.upper()}')
        print(f"\t\t{just('| # | ITEM |')}| COST |")
        for i, item in enumerate(stores[store][current_cat]):
            item_cost = stores[store][current_cat][item]
            print(f"\t\t{just(f'[{i+1}] {item} ', '-')}  {item_cost}")
        header()
        if message != None:
            print(f'''"{message}"''')
        
        menu_select = selection(['prev page', 'next page', 'buy an item', 'view shopping list'], 'H')
        
        if menu_select == 'b':
            storeMenu()
            return

        if menu_select == 'prev page':
            if current_page == 0:
                current_page = last_page
                continue
            else:
                current_page -= 1
                continue
        elif menu_select == 'next page':
            if current_page == last_page:
                current_page = 0
                continue
            else:
                current_page += 1
                continue
        elif menu_select == 'view shopping list':
            viewShopList(itemMenu, (store, current_page))
        else: # buy an item
            print(f'''\n"{getSay('what')}"''')
            item_select = selection(stores[store][current_cat])
            if item_select == 'b':
                continue

            item_cost = stores[store][current_cat][item_select]
            if money < item_cost:
                message = getSay('notEnough')
                continue
            
            print(f'''\n"{getSay('howMany')}"''')
            
            while True:
                qty = input('>>> ')
                
                if qty == 'b':
                    break

                try:
                    qty = int(qty)
                except:
                    print('Invalid input')
                    continue
                
                if money < qty * item_cost:
                    message = getSay('notEnough')
                    break
                break
            if qty == 'b':
                continue
            
            total_cost = qty * item_cost

            purchase(item_select, current_cat, qty, total_cost, store, current_page)
            break

# PRIO: DEF A FUNCTION that prints purchase summary, gives an option to tawad, and passes the item to boughtItem()
def purchase(item, cat, qty, cost, store, page):
    global pp
    nakatawad_na = False

    message = None
    while True:
        stats()
        print('\tPURCHASE SUMMARY\n')
        print(f"\t\t[{item.upper()}]\n\t\t{'cost: '.ljust(18)} {cost}\n\t\t{'money after buy: '.ljust(18)} {money - cost}")
        header()
        if message != None:
            print(f'''"{message}"''')

        if nakatawad_na == False:
            menu_select = selection(['confirm', 'ask for tawad'], 'H')
        else:
            menu_select = selection(['confirm'], 'H')


        if menu_select == 'confirm':
            if cost > money:
                print(getSay('notEnough'))
                time.sleep(1)
                continue
            if cat not in bought:
                bought[cat] = {item: qty}
                boughtItem(item, qty, cost)
            else:
                if item not in bought[cat]:
                    bought[cat].update({item: qty})
                    boughtItem(item, qty, cost)
                else:
                    bought[cat][item] += qty
                    boughtItem(item, qty, cost)
            break
        elif menu_select == 'ask for tawad':
            nRoll = roll()
            cost -= const.rollCon[nRoll['result']]
            if cost < 0:
                cost = 0
            message = getSay(nRoll['result'])
            nakatawad_na = True
        else: # if 'b'
            break
    itemMenu(store, page)
    return

# PRIO: DEF A FUNCTION that adds a specified item to shoplist[item][bought] and subtracts that item from shop list; also subtracts money depending on cost
def boughtItem(item_to_buy, qty, total_cost):
    def proceed(listedItem, qty, total_cost):
        global money, toBuy
        shopList[listedItem]['bought'] += qty
        shopList[listedItem]['to buy'] -= qty
        if shopList[listedItem]['to buy'] <= 0:
            del shopList[listedItem]
        money -= total_cost
        toBuy -= 1

    for listedItem in shopList:
        if listedItem in item_to_buy:
            proceed(listedItem, qty, total_cost)
            return
        else:
            parent = None
            for item in const.items:
                if item_to_buy in const.items[item]:
                    parent = item
                    break
            if listedItem in parent:
                proceed(listedItem, qty, total_cost)
                return

def allItemsBought(called_from, args=None):
    global za_warudo, doStopwatch
    za_warudo = True
    stats()
    print(f"\tYou've ticked off all items in the shopping list!")
    header()

    menu_select = selection(['go home', 'continue shopping'], 'H')
    
    if menu_select == 'go home':
        goHome()
    else:
        za_warudo = False

        doStopwatch = threading.Thread(target=stopwatch)
        doStopwatch.start()
        clear()
        return

def goHome():
    global total_score
    global leaderboard
    loading_screen('\tWalking back home.')
    clear()
    header()
    print('\tOh Buboy nakauwi ka na. Nabili mo ba lahat?')
    header()
    input('>>> ')

    # CALCULATE SCORE
    loading_screen('\tYou see nanay check your eco bag.')
    message = None
    while True:
        clear()
        header()
        if message != None:
            print(f'\t{message}\n')
        playerName = input('\tPlease enter your name: ')
        if playerName in leaderboard:
            message = f"Name, '{playerName}' already exists."
            continue
        else:
            break
    clear()
    header()
    time_bonus = const.flatTimeBonus - min_elapsed
    if time_bonus < 0:
        time_bonus = 0
    bought_score = const.ItemsToBuy - len(shopList)
    total_score = time_bonus + bought_score + pp
    if total_score < 0:
        total_score = 0

    print('\tSCORE SUMMARY')
    print(f"\t\t{just('items bought:')}{bought_score}\n\t\t{just('PP bonus:')}{pp}\n\t\t{just('time bonus:')}{time_bonus}")
    print(f"\t\t{just('TOTAL SCORE:')}{total_score}")

    # append to leaderboard
    updateLeaderboard({playerName: total_score})

    print(f'\n\tCongratulations! You placed {list(leaderboard.keys()).index(playerName) + 1} in the leaderboard!')
    header()
    input('>>> ')
    clear()
    header()
    print('\tThank you for playing :)')
    header()
    sys.exit()
    

    print(f"")

def main():
    # pre processing
    getStores()
    getItemsForStores()
    getItemsForShopList()
    loadLeaderboard()
    updateLeaderboard()
    
    mainMenu(HighScore)

main()
