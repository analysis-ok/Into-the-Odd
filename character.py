import random as r


# import sys

#  Uses random module in function to randomly generate item from list.
def get_random(y):
    x = r.choice(y)
    return x


# Quick 6 sided Dice Roll
def d6roll(value):
    i = 0
    stat = 0
    while i <= value:
        roll = r.randrange(1, 7)
        stat += roll
        i += 1
    return stat


d10 = r.randrange(1, 11)
d12 = r.randrange(1, 13)


# The Following generates a random stat for character creation.
def get_strength():
    stat = d6roll(2)
    return stat


def get_dexterity():
    stat = d6roll(2)
    return stat


def get_willpower():
    stat = d6roll(2)
    return stat


def get_hp():
    stat = d6roll(0)
    return stat


# Names assets for generating characters.
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

pname = r.choice(forenames) + " " + r.choice(surname)

# Variables created based on table in book to generate equipment.
HP1 = {"1": "Swords (d6), Pistol (d6), Modern Armour, Sense nearby unearthly beings",
       "10": "Rifle (d8 B), Bayonet (d6), Lighter Boy, Arcanum",
       "11": "Rifle (d8 B), Modern Armour, Hound, Arcanum",
       "12": "Club (d6), Throwing Knives, Arcanum",
       "13": "Pistol (d6), Ether, Poison, Arcanum",
       "14": "Cane (d6), Acid, Spyglass, Arcanum",
       "15": "Brace of Pistols (d8 B),Canary, Ether",
       "16": "Musket (d8 B),Pocket-watch, Bomb",
       "17": "Halberd (d8 B), Fake Pistol, Artificial Lung",
       "18": "Garotte (d6),Musket (d8 B), Mute"
       }

HP2 = {"1": "Musket (d8 B), Sword (d6), Flashbang, Sense nearby Arcana",
       "10": "Musket (d8 B), Hatchet (d6), Hawk, Arcanum",
       "11": "Hatchet (d6), Pistol (d6), BoltCutters, Arcanum",
       "12": "Musket (d8 B),Mule, Arcanum",
       "13": "Sword (d6), Pistol (d6), Crude Armour",
       "14": "Pistol (d6), Bell, Steel Wire, Smoke-bomb",
       "15": 'Longaxe (d8 B), Ferret, Fire Oil',
       "16": 'Staff (d6 B), Tongs, Glue',
       "17": "Pistol (d6), Net, Trumpet. Prosthetic Leg",
       "18": "GPistol (d6), Grease, Hacksaw. One Arm"
       }

HP3 = {"1": "Musket (d8 B), Club (d6). Immunity to extreme heat and cold",
       "10": "Musket (d8 B), Protective Gloves, Arcanum",
       "11": "Musket (d8 B), Mallet, Marbles, Fancy Hat, Arcanum",
       "12": "Pick-Axe (d6), Manacles, Arcanum",
       "13": "Pistol (d6), Smoke-bomb, Mutt, Shovel",
       "14": "Longaxe (d8 B), Throwing Axes, Fire Oil",
       "15": "Club (d6), Ether, Crowbar, Flute",
       "16": 'Hatchet (d6), Net, Fire Oil. Burnt Face',
       "17": "Club (d6), Paint, Crowbar. Loud Lungs",
       "18": "Pistol (d6), Cigars, Poison. Fugitive"
       }

HP4 = {"1": "Pistol (d6), Knife (d6). Telepathy if target fails WIL Save",
       "10": "Claymore (d8 B), Pistol (d6), 2 Acid Flasks, Arcanum",
       "11": "Musket (d8 B), Bayonet (d6), Mutt with telepathic link",
       "12": "Pistol (d6), Rocket. Toxin-Immune",
       "13": "Musket (d8 B), Portable Ram, Game Set",
       "14": "Pistol (d6), Saw, Animal Trap, Spyglass",
       "15": "Bow (d6 B), Knife (d6), Rocket, Fire Oil",
       "16": "Pistol (d6), Whip (d6), Cigars. Lost Eye",
       "17": "Musket (d8 B), Accordion. No Nose/Scent",
       "18": "Sword (d6), Shield. Illiterate"
       }

HP5 = {"1": "Blunderbuss (d8 B), Hatchet (d6), Mutt. Dreams show your undiscovered surroundings",
       "10": "Brace of Pistols (d8 B), Steel Wire, Grappling Hook, Arcanum",
       "11": "Machete (d6), Brace of Pistols (d8 B), Talking Parrot. Never Sleep",
       "12": "Harpoon Gun (d8 B),Baton (d6), Acid. Slightly Magnetic",
       "13": "Bolt-Cutters, Blunderbuss (d8 B), Fiddle",
       "14": "Pistol (d6), Grease, Hand Drill, Drum",
       "15": "Sword & Dagger(d8 B), Magnifying Glass. Lost Eye",
       "16": "Pistol (d6), Acid, Animal Repellent. Prosthetic Hand",
       "17": "Sword (d6), Steel Wire. Ugly Mutation",
       "18": "Sword (d6), Ferret, Tattered Clothes. Debt (3G)"
       }

HP6 = {"1": "Musket (d8 B), Hatchet (d6), Flashbang, Arcanum. Iron Limb",
       "10": "Rifle (d8 B), Mace (d6), Eagle, Poison",
       "11": "Club (d6), 3 Bombs, Rocket. Darkvision",
       "12": "Maul (d8 B), Dagger (d6), Chain",
       "13": "Longaxe (d8 B), Rum, Bomb",
       "14": "Dagger (d6), Fire Oil, Mirror",
       "15": "Pistol (d6), Knife (d6), Bomb, Saw",
       "16": "Pistol (d6), Bomb, Shovel. Glowing Eyes",
       "17": "Staff (d6 B), Throwing Knives (d6)",
       "18": "Mace (d6), Pigeon. Disfigured"
       }

# Alternative Starter Packages Lists

A1HP = {"1": "Hammer (d8 B), Mask, Arcanum",
        "10": "Femur (d6), Starmap, Arcanum",
        "11": "Stake (d6), Paint Can, Arcanum",
        "12": "Stiletto (d6), Monocle, Arcanum",
        "13": "Blunderbuss (d8 B), Miner's Helmet, Arcanum",
        "14": "Hook (d6), Pocket Lighter, Arcanum",
        "15": "Pistol (d6), Shield, Old Dog",
        "16": "Club (d6), Ventriloquist Dummy, Whistle",
        "17": "Poleaxe (d8 B), Wheelbarrow, Strong Magnet",
        "18": "Rake (d6 B), Jar of Worms, Foul Odour"
        }

A2HP = {"1": "Sabre (d6), Umbrella, Arcanum",
        "10": "Staff (d6 B), Skull, Arcanum",
        "11": "Billhook (d8 B), Fishing Net, Arcanum",
        "12": "Fist-Spike (d6), Rubber Ball, Arcanum",
        "13": "Morningstar (d6), Glitter Pouch, Arcanum",
        "14": "Cricket Bat (d6 B), Glue, Pig",
        "15": "Musket (d8 B), Bag of Screws, Squirrel",
        "16": "Pocket-Knife (d6), Joke Sweets, Net",
        "17": "Knife (d6), Cleaning Tools, Worthless Crystal",
        "18": "Fake Pistol, Poetry Book, Awful Hair"
        }

A3HP = {"1": "Jezzaii (d8 B), Perfume, Arcanum",
        "10": "Spear (d6), Arcanum, Minor Fame",
        "11": "Handcannon (d6 B), Holy Book, Arcanum",
        "12": "Crossbow (d6 B), Very Strong Coffee, Arcanum",
        "13": "Dagger (d6), Grappling Hook, Syringe",
        "14": "Greatsword (d8 B), Steel Wire, Fancy Cat",
        "15": "Glaive (d8 B), Barbed Wire, Preserved Fish",
        "16": "Snooker Cue (d6 B), Flash of Soup, Gum",
        "17": "Pitchfork (d6 B), Prickly Fruit, Toy Frog",
        "18": "Club (d6), Bag of Teeth"
        }

A4HP = {"1": "Spike Gun (d8 B), Absinthe, Arcanum",
        "10": "Longaxe (d8 B), Doll, Arcanum",
        "11": "Spike Chain (d6), Shield, Hyena-Dog",
        "12": "Sceptre (d6), Birdcall, Kookaburra",
        "13": "Halberd (d8 B), Deck of Cards, Double-Jointed",
        "14": "Trident (d6), Flashbang, Adoring Follower",
        "15": "Mallet (d6), Smoke-bomb, Mousetraps",
        "16": "Shovel (d6 B), Choking Powder, Treacle",
        "17": "Cane (d6), Fake Jewellery, Poison",
        "18": "Rod (d6), Jar of Pennies, Hate Sunlight"
        }

A5HP = {"1": "Rifle (d8 B), Modern Armour, Goat",
        "10": "Pike (d8 B), Herbs, Bug-Monkey",
        "11": "Rifle (d8 B), Chemistry Book, Small Fireworks",
        "12": "Stick (d6), Rat, Disguise Kit",
        "13": "Axe (d6), Shield, Jar of Honey",
        "14": "Big Stick (d6 B), Chain, Olive Oil",
        "15": "Pistol (d6)m Siren, Pesticide Can",
        "16": "Longbow (d6 B), Bottled Blood, Acid Flask",
        "17": "Sword (d6), Spyglass, Painting Set",
        "18": "Golf Club (d6 B), Gin, Bad Reputation"
        }

A6HP = {"1": "Twin Swords (d8 B), Chalk, Eye on Back of Head",
        "10": "Pistol (d6), Music Box, Unsettling Manner",
        "11": "Gun-Limb (d6), Crude Armour, Bell",
        "12": "Axe (d6), Bell, Poisonous Mushrooms",
        "13": "Flail (d8 B), Animal Feed, Brandy",
        "14": "Scythe (d6 B), Bones, Crystal Ball",
        "15": "Baton (d6), Periscope, Hot Peppers",
        "16": "Crowbar (d6), Snail, Scented Candle",
        "17": "Crossbow (d6 B), Bagpipes, Eye-patch",
        "18": "Spike (d6), Bomb, No Teeth"
        }


# Generates Equipment for Player Characters using HP & Highest Stat based on table in book.
# If the highest stat is less than 9 this function uses the first item in the list.
def get_kit(hpstat, histat):
    if hpstat == 1:
        if histat > 9:
            return HP1[str(histat)]
        else:
            return HP1["1"]
    if hpstat == 2:
        if histat > 9:
            return HP2[str(histat)]
        else:
            return HP2["1"]
    if hpstat == 3:
        if histat > 9:
            return HP3[str(histat)]
        else:
            return HP3["1"]
    if hpstat == 4:
        if histat > 9:
            return HP4[str(histat)]
        else:
            return HP4["1"]
    if hpstat == 5:
        if histat > 9:
            return HP5[str(histat)]
        else:
            return HP5["1"]
    if hpstat == 6:
        if histat > 9:
            return HP6[str(histat)]
        else:
            return HP6["1"]


def get_altkit(hpstat, histat):
    if hpstat == 1:
        if histat > 9:
            return A1HP[str(histat)]
        else:
            return A1HP["1"]
    if hpstat == 2:
        if histat > 9:
            return A2HP[str(histat)]
        else:
            return A2HP["1"]
    if hpstat == 3:
        if histat > 9:
            return A3HP[str(histat)]
        else:
            return A3HP["1"]
    if hpstat == 4:
        if histat > 9:
            return A4HP[str(histat)]
        else:
            return A4HP["1"]
    if hpstat == 5:
        if histat > 9:
            return A5HP[str(histat)]
        else:
            return A5HP["1"]
    if hpstat == 6:
        if histat > 9:
            return A6HP[str(histat)]
        else:
            return A6HP["1"]


# Alternative Character Options

# Mutants: Roll d20 for each Ability Score, Different Table.
mutations = ('Giant Head', 'Bone Claws (d6 Damage)', 'Bat Wings, Spit Acid (d8 Damage)',
             'Third Eye (sense clues about people)', 'Covered in Barnacles',
             'Nature Kinship (talk to animals and plants)', 'Illusionist (fool one person at a time)',
             'Chitinous Shell (Armour 1)', 'Venom (d6 STR Loss on Critical Damage)', 'Spider Climb', 'Boneless',
             'Bloodsucker (regain lost STR when you feed)', 'Compound Eyes (see all around you)', 'Bug Wings', 'Gills',
             'Toady Skin', 'Glorious Mane', 'Slug-Like', 'Cyclops', 'Constant Drooler', 'Red-Gaze (d8 Damage)',
             'Ruster (touch rusts metal)', 'Huge Jaws', 'Cocoon (sleep in an Armour 2 shell)',
             'Prehensile Tail, Echolocation', 'Heat Vision (see heat signatures)',
             'Devourer (eat anything for nourishment)', 'Living Hive (swarm of bugs live in you)',
             'Explosive (d12 Damage blast when you die)', 'Spray Ink', 'Morph (change face at will)',
             'Void (annihilate objects you grasp)', 'Spores (choke opponents)', 'Camouflage, Psychedelic Skin', 'Horns',
             'Hooves')


def get_mutation():
    m = r.choice(mutations)
    return m


MHP1 = {"1": "Crossbow (d6 B)",
        "11": "Mace (d6)",
        "12": "Mace (d6)",
        "13": "Mace (d6)",
        "14": "Longaxe (d8 B), Crude Armour",
        "15": "Longaxe (d8 B), Crude Armour",
        "16": "Bow (d6 B), Acid",
        "17": "Bow (d6 B), Acid",
        "18": "Club (d6), Wire",
        "19": "Club (d6), Wire",
        "20": "Brick (d6)"
        }

MHP2 = {"1": "Pistol (d6)",
        "11": "Knife (d6)",
        "12": "Knife (d6)",
        "13": "Knife (d6)",
        "14": "Club (d6), Shield",
        "15": "Club (d6), Shield",
        "16": "Knife (d6), Poison",
        "17": "Knife (d6), Poison",
        "18": "Staff (d6 B), Glue",
        "19": "Staff (d6 B), Glue",
        "20": "Spike (d6)"
        }

MHP3 = {"1": "Maul (d8 B)",
        "11": "Bow (d6 B)",
        "12": "Bow (d6 B)",
        "13": "Bow (d6 B)",
        "14": "Mace (d6), Shield",
        "15": "Mace (d6), Shield",
        "16": "Axe (d6), Hooch",
        "17": "Axe (d6), Hooch",
        "18": "Spear (d8 B), Lantern",
        "19": "Spear (d8 B), Lantern",
        "20": "Rope"
        }


def get_mstat():
    mstat = r.randrange(1, 21)
    return mstat


def get_mkit1(mhpstat, mhistat):
    if 1 <= mhpstat <= 2:
        if mhistat > 10:
            return MHP1[str(mhistat)]
        else:
            return MHP1["1"]
    if 3 <= mhpstat <= 4:
        if mhistat > 10:
            return MHP2[str(mhistat)]
        else:
            return MHP2["1"]
    if 5 <= mhpstat <= 6:
        if mhistat > 10:
            return MHP3[str(mhistat)]
        else:
            return MHP3["1"]


def get_mkit2(mhpstat, mhistat):
    if mhpstat <= 2 and mhistat <= 13:
        return "\n - " + get_mutation() + "\n - " + get_mutation() + "\n - " + get_mutation()
    if mhpstat <= 2 and mhistat <= 17:
        return "\n - " + get_mutation() + "\n - " + get_mutation()
    if mhpstat > 2 and mhistat <= 17:
        return "\n - " + get_mutation() + "\n - " + get_mutation()
    if mhistat >= 18:
        return "\n - " + get_mutation()


# Simple Folk: Roll d12 + 6 for STR and Dex, and 2d6 for WIL. Equipment on different table.
# Starts with Dagger (d6), torch, quaint clothes.

trinkets = ['Fighting Rooster (2d6hp)', 'Devil Mask', 'Eternally Smelly Hat', 'Horse Skull Helmet', 'Donkey',
            'Bag of Flour', 'Very Fat Dog', 'Bell on a Stick', "Explorer's Sabre (d6)",
            'An Actual Rifle! (d8 B, no ammo)', 'Potato Sack', 'Wagon Wheel', 'Dowsing Rods', 'Scythe (d6 B)',
            'Cage Full of Crickets', 'Unbreakable Conker', 'Ornate Shovel (d6)', 'Old Military Uniform',
            'Bag of Really Heavy Rocks', 'Wooden Locket', 'Brick on a Rope', 'Clothed Monkey', 'Huge Candle',
            'Bat on a String', 'Lucky Frog', 'Board with Nail (d6)', 'Noose', 'Fake Pistol', 'Rude Shaped Turnip',
            'Cannonball', 'Fire Oil', 'Gigantic Pumpkin', 'Bomb (no fuse)', 'Turnip Wine', 'Magic Beans (not magic)',
            'Prize Cow', 'Small', 'Blind', 'Old Dog', 'Pointy Star Hat', 'Arcanum']


def get_trinket():
    t = r.choice(trinkets)
    return t


FHP1 = {"7": "Bow (d6 B), Crude Armour, 3 Trinkets",
        "8": "Bow (d6 B), 2 Trinkets",
        "9": "Shield, Hammer (d6 B), 2 Trinkets",
        "10": "Flail (d6), 2 Trinkets",
        "11": "Crude Armour, 2 Trinkets",
        "12": "Hatchet (d6), 2 Trinkets",
        "13": "Club (d6), Crude Armour, 2 Trinkets",
        "14": "Crossbow (d6 B), 2 Trinkets",
        "15": "Sword (d6), Shield, 1 Trinket",
        "16": "Lantern, 1 Trinket",
        "17": "Wine, 1 Trinket",
        "18": "Broken Nose, 1 Trinket"
        }

FHP2 = {"7": "Rod (d6), Eye-patch, 3 Trinkets",
        "8": "Shield, 2 Trinkets",
        "9": "Hatchet (d6), One Ear, 1 Trinket",
        "10": "Shield, 1 Trinket",
        "11": "Bow (d6), 1 Trinket",
        "12": "Crude Armour, 1 Trinket",
        "13": "Machete (d6), No Nose, 1 Trinket",
        "14": "Greataxe, 1 Trinket",
        "15": "Axe (d6), Shield, 1 Trinket",
        "16": "Spear (d8 B), 1 Trinket",
        "17": "Mallet (d6), 1 Trinket",
        "18": "Hanging Jaw, 1 Trinket"
        }

FHP3 = {"7": "Sling (d6), One Leg, 3 Trinkets",
        "8": "Whistle, 2 Trinkets",
        "9": "Stick (d6), Extra Ear, 1 Trinket",
        "10": "Bow (d10 B), 1 Trinket",
        "11": "Shovel (d6), 1 Trinket",
        "12": "Drum, 1 Trinket",
        "13": "Spike (d6), Mute, 1 Trinket",
        "14": "Maul (d8 B), 1 Trinket",
        "15": "Bow (d6 B), Hawk, 1 Trinket",
        "16": "Axe (d6), 1 Trinket",
        "17": "Sling (d6), 1 Trinket",
        "18": "Flat Head, 1 Trinket"
        }


# Gets Simple Folks STR and DEX
def get_fstat():
    sfs = r.randrange(1, 13) + 6
    return sfs


# Gets Simple Folks WILL
def get_fwill():
    sfw = d6roll(1)
    return sfw


def get_fkit1(fhpstat, fhistat):
    if fhpstat <= 2:
        kit = FHP1[str(fhistat)]
        return kit
    if 3 <= fhpstat <= 4:
        kit = FHP2[str(fhistat)]
        return kit
    if 5 <= fhpstat <= 6:
        kit = FHP3[str(fhistat)]
        return kit


def get_fkit2(fhpstat, fhistat):
    if fhistat == 7:
        return "\n - " + get_trinket() + "\n - " + get_trinket() + "\n - " + get_trinket()
    if fhistat == 8:
        return "\n - " + get_trinket() + "\n - " + get_trinket()
    if 9 <= fhistat <= 14 and fhpstat <= 2:
        return "\n - " + get_trinket() + "\n - " + get_trinket()
    if fhistat >= 15 and fhpstat <= 2:
        return "\n - " + get_trinket()
    if fhistat >= 9 and fhpstat >= 3:
        return "\n - " + get_trinket()


# UNHUMANS: Roll d12 to get Type, Roll d10 + HP for Starter Items, Get stats from type.

unhuman_list = ["Stocky, beard, know everything about rocks. Immune to poison, d12+6 STR.",
                "Small and pudgy, hide in tiny places, 2d6 STR, 2d6+6 WIL.",
                "Slender, unaging, immortal. Pass a WIL Save to perform subtle trickery that may appear as magic. "
                "2d6+6 DEX.",
                "Ugly, animalistic features. d12+8 STR, d10 WIL.",
                "Tiny, green, sort of creepy looking. 2d6 STR and WIL, d12+6 DEX.",
                "Scales and immunity based on colour.",
                "Tiny, bald, know everything about machines, talk to burrowing animals. 2d6 STR.",
                "Made of living wood and stone. Immune to anything that would affect living tissue.",
                "Intelligent Ape. d12+6 DEX.",
                "Wings, beak, and talons. Fly quite well. d6+3 STR.",
                "Grey skin, white hair, talk to bugs, see perfectly in darkness.",
                "Twice normal size. d6+14 STR, d10 DEX. Weapons specially made for you are bumped up "
                "to the next size die. Hand Weapons cause d8, Field Weapons cause d10 etc."
                ]

unhuman_types = []

# d10 + HP
uhstarter_items = {"2": "Arcanum, Cult Symbol",
                   "3": "Arcanum, Poison",
                   "4": "Hound",
                   "5": "Arcanum, Ether",
                   "6": "Staff (d6 B), Raven",
                   "7": "Pistol Brace (d8)",
                   "8": "Arcanum, Shackles",
                   "9": "Fancy Sword (d8)",
                   "10": "Elaborate Clothes",
                   "11": "Fancy Pistol (d8)",
                   "12": "Pistol, Incredible Hat",
                   "13": "Blunderbuss (d8)",
                   "14": "Greatsword (d8)",
                   "15": "Shield, Sword (d6)",
                   "16": "Cult Symbol",
                   }

uh_social = {"1": "No idea you exist.",
             "2": "You're just a rumour.",
             "3": "Word is starting to spread.",
             "4": "One bad example is publicly known.",
             "5": "One good example is publicly known.",
             "6": "Lots of stories, but you're still hidden.",
             "7": "You went into hiding a few years ago.",
             "8": "They think you’re from the Golden Lands (you’re not).",
             "9": "They think you’re a mutant from the Underground (you're not).",
             "10": "They think you’re from space (you’re not).",
             "11": "They want you dead!",
             "12": "Incredibly stereotyped, generally bad.",
             "13": "Incredibly stereotyped, generally good.",
             "14": "Generally a good reputation.",
             "15": "Generally a bad reputation.",
             "16": "Good history, but things are turning sour.",
             "17": "Bad history, but things are generally okay now.",
             "18": "You work closely with them.",
             "19": "They don't care.",
             "20": "They think you're great."
             }


def get_type():
    t = r.choice(unhuman_list)
    return t


unHP = get_hp()


def get_unstart(un_hp):
    roll = un_hp + d10
    starter = uhstarter_items[str(roll)]
    return starter


def get_unreaction():
    roll = r.randrange(1, 21)
    react = uh_social[str(roll)]
    return react

# unhuman_type = r.choice(unhuman_list)
