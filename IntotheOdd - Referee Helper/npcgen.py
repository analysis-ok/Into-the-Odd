import random as r

forenames = ['Augost', 'Augosta', 'Benedict', 'Benedicta', 'Brin', 'Breen', 'Chumwan', 'Chumwel',
             'Calahed', 'Calit', 'Dorren', 'Dorret', 'Emmett', 'Emma', 'Felix', 'Felora', 'Fred', 'Freda', 'Grobin',
             'Grobina', 'Gizard', 'Giza', 'Helroff', 'Helriel', 'Istan', 'Isti', 'Ilmer', 'Ilda', 'Junas',
             'Julia', 'Katsun', 'Katsin', 'Lurpax', 'Lunda', 'Litton', 'Littona', 'Munfud', 'Munfi', 'Narmun',
             'Nadya', 'Orren', 'Orrena', 'Podder', 'Poddin', 'Peta', 'Pipp', 'Pippita', 'Quinn', 'Stellan', 'Stella',
             'Samford', 'Sambay', 'Tucker', 'Tuckis', 'Teevan', 'Teeva', 'Urntin', 'Urna', 'Varran', 'Varin', 'Vanis',
             'Vanisa', 'Volta', 'Volel', 'Weckster', 'Weckin', 'Yurnak', 'Yurna', 'Zarm']

surname = ['Allane', 'Bargroll', 'Brunfield', 'Chop', 'Creed', 'Dunbell', 'Eggler', 'Fox', 'Farsee', 'Gill', 'Gullwin',
           'Huckle', 'Horrican', 'Ingle', 'Jongler', 'Kross', 'Lix', 'Lowbile', 'Montane', 'Nutbush', 'Olifant',
           'Offenpot', 'Ouze', 'Phile', 'Parfait', 'Quigley', 'Regal', 'Stagger', 'Shark', 'Tumble', 'Terrine',
           'Underhog', 'Upperill', 'Volfhole', 'Vinifera', 'Wickerspin', 'Yarn', 'Zarrack']

npcname = r.choice(forenames) + " " + r.choice(surname)

occupation = ['Actor', 'Barge Pilot', 'Butler', 'Coffee House Host', 'Coal Miner', 'Dog Breeder', 'Engine Cleaner',
              'Fist Fighter', 'Fishmonger', 'Gull-Catcher', 'Glue Maker', 'Gunsmith', 'Gin-Maker', 'Hog-Slaughter',
              'Ivory Worker', 'Jeweler', 'Lower-Politician', 'Life Servant', 'Lamp-Lighter', 'Lesser-Noble',
              'Mercenary',
              'Newspaper Vendor', 'Octopus-Catcher', 'Oyster Seller', 'Perfumer', 'Professor', 'Prison Guard',
              'Pie-Smith', 'Road Sweeper', 'Salt Farmer', 'Sweet-Maker', 'Trinket-Merchant', 'Tax Collector',
              'Tunnel Digger', 'Whaler', 'Watchmaker', 'Watchman', 'Writer', 'Wig-maker']

capability = ['is an Anal-Retentive', 'is a Boringly Dependable', 'is the Best in the City', 'is a Cheap and Dirty',
              'is a Charming and Oily', 'is a Dabbler in ', 'is a Flashy and Expensive ', 'is a Fair and Down to Earth',
              'is a Very Cheap but Dirty', 'is a Great, but hated', 'is a Good but Annoying', 'is a Highly Artistic',
              'is a Hardly Trained', 'Inherited the Family Trade of', 'is an Unfulfilled', 'is an Imposter',
              'is a Jealous of Better Rival of the', 'is an Apprentice', 'Loves their Job as a', 'is Lazy and Greedy',
              'is a Money-Grabbing', 'is a Moral, but not that good', 'Only Serves Friends as a',
              'is an Old-Master-Trained', 'is a Perfectionist', 'is a Paragon of the Job',
              'is a Poor', 'is Retired from injury', 'is a Ruthless', 'is Sworn into the Profession of',
              'is a Silently dutiful', 'is a Trained from Birth', 'is Trapped in the Job of', 'is an Uncaring',
              'is an Unreliable Genius', 'is Wedded into Career of', 'has Wasted their Talent as a',
              'is a Warm and Friendly', 'is a Wealthy Successful']

manners = ['Attractive Dullard', 'Big Fat Glutton', 'Beaky Bore', 'Creaky Elder', 'Childlike', 'Dashing Young Gun',
           'Ethereal Beauty', 'Fails at Flirtastious', 'Flamboyant Charmer', 'Great Speaker', 'Greasy Toad',
           'Gentle Giant', 'Hulking Brute', 'Hunchback', 'Harmless Dope', 'Intensely Creepy', 'Ill-Coloured and Thin',
           'Jolly and Fat', 'Loads of Jewellery', 'Lots of Scars', 'No Nose', 'Nice but Dim', 'Naive Teenager',
           'Old Sleaze', 'Pig-Faced', 'Plucky Little Thing', 'Powdered Wig', 'Quite Ugly', 'Rough as a Dog',
           'Stocky Grunter', 'Stunted Growth', 'Straight-Laced', 'Towering Klutz', 'Unwashed Slob', 'Vapid Fashionista',
           'Very Long Hair', 'Well-Bred Snob', 'Waif', 'Weird Head']

connection = ['Aunt/Uncle', 'Sibling', 'Best Friend', 'Owes Money', 'Old Friend', 'Common Ancestry', 'Platonic Love',
              'Admiration', 'Parent', 'Owed Money', 'Acquaintance', 'Common Benefactor', 'Hatred', 'Irriation', 'Twin',
              'Spouse', 'Guardian', 'Lover', 'Mentor', 'Abuser', 'Lust', 'Distaste', 'House-Share', 'Former Colleagues',
              'School Friends', 'Adopted Parent', 'Unrequited Love', 'Planning Murder', 'Knows Secret',
              'One Night Stand', 'Rivals', 'Backhand Deal', 'Criminal Enterprise', 'Shared Trauma', 'Jealousy',
              'Voilent Hate', 'Engaged', 'Protector', 'Playful Rivalry']

event = ['was Arrested Wrongfully for Minor Crime.', 'was Arrested Rightfully for Major Crime.',
         'Became Addicted to an Exotic Drug.', 'Contracted a Terrible Disease.',
         'Debt Collectors are Applying Pressure.', 'Died in an Uprising.', 'Died in Industrial Accident.',
         'Found a Long-Lost Relative.', 'Found a (new) Love.', 'Found a Major Arcanum.', 'Found a Lesser Arcanum.',
         'Getting (Re)Married.', 'Joined a Star Cult.', 'Joined a New Revolutionary Group.', 'had their Home Collapse.',
         'was Lost at Sea.', 'was Lost Everything.', 'had a Lamp-Lighter Burnt Down their House.',
         'was Left Bastion for the Deep Country.', 'was Left Bastion for a Lesser City.', 'was Murdered in the Street.',
         'was Murdered in their Bed.', 'a Nice person has given them some juicy work.',
         'was Press-Ganged into Military.', 'heard Rumours of Criminal Activity.',
         'heard Rumours of personal Depravity.', 'Saw weird things in the sky.', 'Saw horrible beasts in the street.',
         'Saw a murder nearby.', 'has Taken up Military Service.', 'has Taken in an Orphan.',
         'The Watch are harassing them.', 'Underground Weirdos Abducted.', 'has Vanished in a Burst of Light.',
         'has Wandered into Underground, is now missing.', 'Won a fortune by gambling.',
         'Witnessed an Abduction into the night sky.', 'Went on a drinking binge.',
         'Recklessly leapt into a Doomed Romance.']


def genname():
    fname = r.choice(forenames) + " " + r.choice(surname)
    return fname


def genocc():
    jobtitle = r.choice(occupation)
    return jobtitle


def gencap():
    desc = r.choice(capability)
    return desc


def genmanner():
    mandes = r.choice(manners)
    return mandes


def genconnection():
    genconnect = r.choice(connection)
    return genconnect


def genevent():
    evt = r.choice(event)
    return evt

# print(doeswork(event))
