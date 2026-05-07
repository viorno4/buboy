# contains constant variables. Read only

# note: if a variable contains a value of [x, x], it defines a range


StoreNum = 4 # number of stores available
ItemsObtainable = 0.5 # defines how many items (in percentage) will be obtained from the item list per category
ItemsToBuy = 3 # number of items na inutos ng nanay ni buboy na bilhin nya

flatTimeBonus = 50
moneyModifier = 100

StoreNames = [
        "Tindahan ni Aling Nena",
        "Bossing store",
        "Tindahan ni Kapitan Tago",
        "Aling Miray store",
        "Manong Badang's sari-sari",
        "Inday Batutay store",
        "Sierra Baddie store",
        "Marites store",
        "Zild zari-zari",
        "Tindahan ni Ryan Gosling",
        "Keanu 'J' Reeves sari-sari",
        "Aling Tess sari-sari",
        "Best Dean Rodrigo store",
        "Steven Super Store"
]

Dialogues = {
    # buy dialogues
    'what':[
        "Anong bibilhin mo?",
        "Alin?",
        "Pili ka nalang dyan.",
        "Aba'y pili, di yan magkukusa!",
        "What do you need bes?"
    ],
    'howMany':[
        "Ilan?",
        "Ilan ba?",
        "Ilan nito?",
        "How much do you want ba?"
    ],
    'notEnough':[
        "Kulang pera mo utoy.",
        "Ano? Mangungutang nanaman ba?",
        "Kulang arep mo my G.",
        "Aww Buboy your money not enough tho skrrt skrrt :(("
    ],
    # roll dialogues
    'catastrophic':[
        "Angkapal naman ng mukha mo!",
        "Sabihin mo sa nanay mo maghaharap kami sa lunes!",
        "Baka gusto mong i-fireball kita G?",
        "Aba aba aba may utang ka pa nung nakaraan ah!"
    ],
    'very bad':[
        "Really? Right in front of my pancit canton?",
        "Tawad nanaman?",
        "Kung gusto mo ng tawad, sabihin mo sa nanay mo sya bumili.",
        "Aba tanghaling tapat tatawad ka?"
    ],
    'bad':[
        "Sorry G pass muna.",
        "Mahina ang benta ngayong linggo, wag muna.",
        "Next time nalang Buboy.",
        "Baka mapagalitan ako ni mama eh, wag muna."
    ],
    'good':[
        "Ay nako sige na nga!",
        "Alright G you're one of the hood naman sheesh!",
        "Geh bes wag ka nalang maingay kay mama ha...",
        "Pasalamat ka good mood ako ngayon :)"
    ],
    'great':[
        "Syempre! Malakas ka sakin eh!",
        "No problem G! Anything for my homiez!",
        "Okay bestie!",
        "Sige sige, anak ka naman ni ano."
    ],
    'perfect':[
        "Aba syempre naman! Iniintay lang kita magtanong eh!",
        "Fo'sho fo'sho my absolute G!",
        "Actually balak nga kitang tawaran e kasi ang cute cute cute mo!",
        "Walang problema! Kiss pa kita eh :)"
    ]
}

rollCon = {
    'catastrophic': -5,
    'very bad': -1,
    'bad': 0,
    'good': 2,
    'great': 5,
    'perfect': 10
}

items = { # item: [x, x] range of item price
    'chichirya':{
        'piattos':[16, 21],
        'nova':[16, 21],
        'v-cut':[16, 21],
        'mr. chips':[14, 18],
        'tortillos':[16, 21],
        'clover':[16, 21],
        'mang juan':[14, 18],
        'bangus':[1, 3],
        'bits':[1, 3],
        'kiss':[1, 3],
        'mang inasal':[1, 3]
    },
    'condiments':{
        'vetsin':[4, 6],
        'paminta durog':[4, 6],
        'paminta buo':[4, 8],
        'asukal':[10, 16],
        'asin':[4, 8],
        'kamatis':[8, 11],
        'sibuyas':[6, 11],
        'bawang':[6, 11],
        'luya':[8, 12],
        'crispy fry breading':[18, 22],
        'tasty boy breading':[16, 21],
        'evaporada':[22, 30],
        'kremdensada':[69, 75],
        'coco mama gata':[34, 38],
        'condensada':[46, 51],
        'knor cubes':[7, 10],
        'knor sinigang mix':[9, 13],
        'mang tomas':[41, 51],
        'silver swan toyo':[9, 12],
        'marca pina toyo':[9, 13],
        'datu puti toyo':[8, 13],
        'silver swan suka':[7, 11],
        'datu puti suka':[8, 12],
        'rose suka':[7, 12]
    },
    'inumin':{
        'fruit soda':[10, 13],
        'root beer':[10, 13],
        'cobra':[15, 19],
        'coke':[10, 14],
        'royal':[10, 14],
        'sprite':[10, 14],
        'c2':[10, 14],
        'yakult':[12, 16],
        'zest-o':[11, 14],
        'natures spring water':[12, 21],
        'absolute water':[13, 22]
    },
    'powdered drinks':{
        'bear brand':[15, 21],
        'milo':[11, 15],
        'birch tree':[12, 17],
        'kopiko barako':[14, 17],
        'kopiko 3 in 1':[14, 17],
        'kopiko blanca':[14,17],
        'coffee mate':[2, 4]
    },
    'tinapay':{
        'doowee donut':[10, 14],
        'fudgee bar':[10, 13],
        'lemon square':[8, 12],
        'skyflakes':[8, 11],
        'presto':[8, 11],
        'combi':[8, 11],
        'bingo':[8, 11],
        'cream-o':[8, 11],
        'choco mucho':[9, 15],
        'magic chips':[9, 12]
    },
    'instant foods':{
        'pancit canton calamansi':[16, 19],
        'pancit canton sweet & spicy':[16, 19],
        'pancit canton hot & spicy':[16, 19],
        'pancit canton chilimansi':[16, 19],
        'lucky me chicken mami':[12, 15],
        'lucky me beef mami':[12, 15],
        'lucky me beef labuyo mami':[12, 15]
    },
    'delata':{
        '555 tuna':[35, 41],
        'argentina corned beef':[44, 47],
        'CDO corned beef':[35, 38],
        'san marino tuna':[35, 38],
        'mega sardines':[26, 30],
        'ligo sardines':[29, 32]
    },
    'raw goods':{
        'itlog':[8, 15],
        '1kg manok':[120, 191],
        '1kg isda':[90, 191]
    },
    'household':{
        'ariel laundry powder':[12, 15],
        'tide laundry powder':[12, 15,],
        'champion laundry powder':[12, 15],
        'downy':[8, 12],
        'joy dishwashing liquid':[7, 11],
        'maxglow dishwashing liquid':[7, 11],
        'katol':[2, 6],
        'kandila':[4, 9],
        'close up toothpaste':[12, 16],
        'happee toothpaste':[12, 16],
        'colgate toothpaste':[12, 16],
        'creamsilk conditioner':[9, 12],
        'keratin conditioner':[8, 11],
        'dove shampoo':[8, 11],
        'head & shoulder shampoo':[8, 11],
        'panteen shampoo':[8, 11],
        'perla bath soap':[17, 21],
        'safeguard bath soap':[17, 21],
        'cetaphil bath soap':[21, 30],
        'effecascent oil':[35, 42],
        'posporo':[3, 6],
        'diaper':[11, 15],
        'tissue':[13, 17]
    }
}

shoppable = { # contains all the possible items that Buboy's mom's shopping list will have; format: 'item':[x, y] range of how many of that item mom will ask buboy to buy
    'chichirya':{
        'any':[1, 4],
        'piattos':[1, 2],
        'nova':[1, 2],
        'v-cut':[1, 2],
        'mr. chips':[1, 2],
        'tortillos':[1, 2],
        'clover':[1, 2],
        'mang juan':[1, 2],
        'bangus':[1, 5],
        'bits':[1, 5],
        'kiss':[1, 5],
        'mang inasal':[1, 5]
        },
# condiments
    'vetsin':[1, 3],
    'paminta':[1, 5],
    'asukal':[1, 2],
    'asin':[1, 3],
    'kamatis':[3, 10],
    'sibuyas':[3, 10],
    'bawang':[3, 10],
    'luya':[2, 4],
    'breading':[1, 3],
    'evaporada':[1, 2],
    'kremdensada':[1, 2],
    'gata':[1, 3],
    'condensada':[1, 3],
    'knor cubes':[1, 3],
    'sinigang mix':[1, 2],
    'mang tomas':[1, 1],
    'toyo':[1, 1],
    'suka':[1, 1],

# inumin
    'inumin':{
        'any':[1, 3],
        'fruit soda':[1, 2],
        'root beer':[1, 1],
        'cobra':[1, 1],
        'coke':[1, 1],
        'royal':[1, 1],
        'sprite':[1, 1],
        'c2':[1, 1],
        'yakult':[1, 2],
        'zest-o':[1, 2],
        'water':[1, 1]
        },

# powdered drinks
    'bear brand':[1, 3],
    'milo':[1, 3],
    'birch tree':[1, 3],
    'kopiko barako':[1, 2],
    'kopiko 3 in 1':[1, 2],
    'kopiko blanca':[1, 2],
    'coffee mate':[1, 4],

# tinapay
    'tinapay':{
        'any':{1, 4},
        'doowee donut':[1, 2],
        'fudgee bar':[1, 2],
        'lemon square':[1, 2],
        'skyflakes':[1, 2],
        'presto':[1, 2],
        'combi':[1, 2],
        'bingo':[1, 2],
        'cream-o':[1, 2],
        'choco mucho':[1, 2],
        'magic chips':[1, 3]
        },

# instant foods
    'pancit canton':[2, 4],
    'lucky me':[2, 4],

# delata
    'tuna':[1, 3],
    'corned beef':[1, 3],
    'sardines':[1, 3],

# raw goods
    'itlog':[3, 6],
    'manok':[1, 2],
    'isda':[1, 2],

# household
    'laundry powder':[2, 5],
    'downy':[1, 3],
    'dishwashing liquid':[2, 4],
    'katol':[1, 2],
    'kandila':[2, 4],
    'toothpaste':[1, 3],
    'conditioner':[1, 3],
    'shampoo':[2, 4],
    'soap':[1, 2],
    'effecascent oil':[1, 1],
    'posporo':[1, 1],
    'diaper':[2, 5],
    'tissue':[1, 3]
}
itemChance = 100 / len(shoppable)

gameTips = [
    'You can always press [b] to go back.',
    "'PP' points stand for 'persuasion points'",
    "You gain points depending on your performance!",
    "There's a timer! You gain extra points when u finish FAST!",
    'Dean Rodrigo is the best teacher ever :)'
]











