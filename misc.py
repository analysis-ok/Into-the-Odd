import random as r


#  Uses random module in function to randomly generate item from list.
def get_random(y):
    x = r.choice(y)
    return x


# Government Actions

decree = ['All Arcana must be registered', 'War with all other cities', 'Major cult is outlawed',
          'Entire borough to be flattened', 'Army conscription', 'New council-sanctioned cult', 'Animal census',
          'All prisoners to be executed', 'All prisoners to be released', 'Launching a cosmic rocket', 'Double taxes',
          'Random mass eviction', 'Total lockdown', 'Inquisition into possible rebellion',
          'Entire council executed and replaced', 'Exodus to the Golden Lands', 'Underground crusade', 'Guns outlawed',
          'Alcohol prohibited', 'Martial law']

pub_reaction = ['"Riots!"', '"Tomorrow we launch an uprising!"', '"Someone should do something!"', '"They don’t care"',
                '"They probably have a good reason..."', '"Well it’s about time!"']

# Places
locations = ['Brewery', 'Meeting Fountain', 'Restaurant', 'Sunken Pit', 'Bar', 'Fighting Den', 'Castle', 'City Wall',
             'Huge Factory', 'Coal Heep', 'Poorhouse', 'Public Baths', 'Observatory', 'University', 'Building Site',
             'Winding Alleyways', 'Show Row', 'Residential Terrace', 'Botanical Garden', 'Cult Temple', 'Docks',
             'Warehouse', 'Underground Shelter', 'School', 'Ironworks', 'Canal Docks', 'Amusement Complex',
             'Specialist Shops', 'Bridge', 'Manor', 'Guild House', 'Army Barracks', 'Shopping Arcade', 'Watchtower',
             'City Watch Station', 'Hospital', 'Cult Cathedral', 'Shrine']

atmosphere = ['Welcoming', 'Dark', 'Smoggy', 'Abandoned', 'Bustling', 'Brightly Lit', 'Creepy', 'Drafty', 'Sinister',
              'Comforting', 'Rat-infested', 'Expensive', 'In Poverty', 'Dusty', 'Freshly Built', 'Ruined',
              'Burnt', 'On Fire!', 'Overran by Rioters', 'Bird Infested', 'Falling Down', 'Ancient', 'Artistic',
              'Eccentric', 'Physics-Defying', 'Underground', 'Overground', 'Hidden', 'Criminal', 'Council-Sanctioned',
              'Rebellious', 'Protesting', 'Cult-Linked', 'Dangerous', 'Filthy', 'Overrun by Orphans', 'Fearful',
              'Nonsensical']

link_underground = ["No", "Probably in the next road down", "No, and why are you so interested?",
                    "No, we don't want Weirdos coming up", "No, it's too dangerous to leave them open",
                    "Sure! Oh, wait, it's gone", "Yes, but the tunnels are too hot to survive",
                    "No, soldiers came and sealed it up", "Yes, but it leads straight into an acid pool",
                    "Nobody wants to talk about the Underground", "We dug this one quite recently",
                    "An escape tunnel out of town", "Yeah, an old trapdoor", "A wine cellar leads somewhere horrible",
                    "This tunnel goes right across town", "A particularly disgusting sewer", "An old bank vault",
                    "Smugglers have set up tunnels around here", "They all got sealed up years ago",
                    "There's a tunnel in plain sight", "Hidden stairway indoors", "A hole opened up last week",
                    "Nasty things burst from the ground here", "An old vault entrance", "Emergency shelter nearby",
                    "Just a chute straight down", "Spiral staircase ornately decorated", "An overgrown natural cave",
                    "Tunnel at the bottom of a pond", "Open sewer", "An old well", "Rusty ladder down a chute",
                    "It caved in recently", "An old elevator", "A newly fitted elevator",
                    "The hole where they throw their rubbish", "Huge pit into the darkness",
                    "Tunnel at the bottom of the river", "Natural cave in somebody's cellar"]

quick_route = ['Crawl-Tunnel', 'Funicular', 'Horse Carriage', 'Underground Carriageway', 'Canal Boat',
               'Underground Canal', 'Shady Alleyways', 'Straight Through the Park', 'Along the Docks',
               'Rooftop Walkway,', 'Down the High Street', 'Through a Riot', 'Underground Tramway',
               'Tunnel with Toll Booth', 'Hired Carriage', 'Through an Abandoned Warehouse',
               'Through a Working Factory', 'Through the Slums', 'Through the Rich Neighbourhoods',
               'Along the City Walls', 'Steamboat Down the River', 'Rickshaw', 'Underground Tunnels',
               'Through the Market', 'The Wine Cellar Network', 'Catacombs', 'Through the Old Town', 'Ugh, Sewers',
               'Through the Bad End of Town', 'Across University Campus', 'Through the Botanical Gardens',
               'Along the Canals', 'Over a Ruined Castle', 'Through the Graveyard Quarter',
               'Up the Hill, then back down', 'Right Through the Crazy Part of Town', 'Through a Cult Temple',
               'Past the Army Barracks', 'Through the Smuggler Tunnels']

businesses = ["Cage-Brand Steam Generators", "Pickem's Enterprise Loans", "Anise Sisters Security Wire",
              "Gasman Spice & Soap", "Prospective Telecoms", "The Lady's Sugar and Coffeehouse",
              "Yesser's Wool and Meat", "Secure Properties and Jails", "Consolidated Bookmakers",
              "Commercial Voice Printed Press", "Gallow, Sniff, & Pine Medical Research",
              "Claymore Bank & Private Military", "Broken Compass Offshore Acquisitions", "Baker Arms & Munitions",
              "Cohen Mass Nutrition Solutions", "Footman Stills Spirits & Tonics", "Braker's Streetlamp and Halberd",
              "Black Horse Hospitals and Asylums", "Bastio-Goldish Coal, Oil, and Ore",
              "Confectioner's Village Foods & Homes", "Red Ghost Roads & Carriages", "Freeman Brewers & Bakers",
              "Drake Ships & Sails", "Shooman Boots & Tonics", "Bates' Smoke Farms",
              "Great Underground Disposal Company", "Clock's Shippage & Canals", "Hightower Hats & Canes",
              "Territorial Tea & Wine", "Outlander's Exotic Down & Fur", "Furrupp's Brick & Mortar",
              "Bitter & Snatch Jewellery", "Werner's Industrial Machinery", "Silvermountain Private Security",
              "Aria Mines", "Miracle Factory Ice & Salt", "Metropolitan Tramway", "Sunfair Gold Holdings"]

rooms_places = ['Weird Generator', 'Corpse Pit', 'Abyssal Chasm', 'Labyrinth', 'Murder Shrine', 'Flowing Filth',
                'Sealed Vault', 'Bunker', 'Dirt Hole', 'Crumbling Chapel', 'Art Gallery', 'Forge', 'Office',
                'Torture Chamber', 'Feast Hall', 'Military Tomb', 'Ancient Barrow', 'Cult Catacomb', 'Fighting Pit',
                'Well', 'Drinking Hole', 'Crystal Cave', 'Prison', 'Natural Spring', 'Open Vault', 'Flooded Sewer',
                'Abandoned Tramway', 'Gun Workshop', 'Gunpowder Store', 'Dog Pit', 'Alchemy Lab', 'Printing Press',
                'Metal Sphere', 'Underground Lake', 'Throne Room', 'Armoury', 'Swimming Pool', 'Observatory']

hazards = ['Bell Alarm', 'Searing Hot Walls', 'Glass Snakes', 'Crawling Eyes', 'Acid Puddles', 'Tunnel Shark',
           'Crushing Walls', 'Taunting Voices', 'Hidden Spikes', 'Slime Drones', 'Carnivorous Birds', 'Insane Soldiers',
           'Deafening Siren', 'Devouring Maw', 'Grasping Tentacles', 'Questioning Brain', 'Huge Beast',
           'Collapsing Floor', 'Shifting Illusions', 'Stone Automatons', 'Incineration Pit', 'Living Chains',
           'Cursing Hag', 'Frightened Cat', 'Holographic Spiders', 'Gust of Wind', 'Ghostly Hands', 'Dust Tornadoes',
           'Acidic Ooze', 'Freeze-Rays', 'Shifting Blocks', 'All-Seeing Eye', 'Mechanical Judge', 'Angry Mutants',
           'Rival Explorers', 'Impenetrable Shadow', 'Blinding Lights']

situation = f"At {get_random(atmosphere)} {get_random(locations)} holds a room containing " \
            f"{get_random(rooms_places)} with {get_random(hazards)}"

# print(situation)


landmarks = ['Smoking Volcano', 'Huge Waterfall', 'Ice-Capped Peak', 'Glittering Lake', 'Colorful Lights',
             'Red Forests', 'Rock Fortress', 'Abandoned Fleet', 'Salt Beach', 'Crystal Shard Cave',
             'Absolutely Flat', 'Thorny Jungle', 'Ice All Over', 'Blasted Waste', 'Long and Thin Path',
             'Creeping Moss', 'Steel Spires', 'Blooded Bushes', 'Spiral Mountains', "Hot and Dry",
             'Misty, Grand Canyon', 'Delicious Fruit', 'Ruined Temple', 'High Walls that are', 'Glass Towers',
             'Lone Mountains', 'Blue Grass', 'Yellow Rock', 'Piles of Skulls', 'Over-sized Fungus',
             'Dense Cacti', 'Chocking Fog', 'Gusts of Wind', 'Tiny Trees', 'Elephant Herds', 'Underwater']

dangers = ['Island is Intelligent', 'Sweltering Heat', 'Covered by Metal Dome', 'Nobody Can Die Here', 'Sinking',
           'Recently Resurfaced', 'Toxic Air', 'Utterly Silent', 'Plants Grows Visibly', 'Eternal Night',
           'Completely Abandoned', 'Expedition Gone Native', 'Giant Killer Frogs', 'Whispering Wind',
           'Monkeys with Guns', 'Shipwrecked Explorers', 'Metal Skeletons', 'Sand Wraiths', 'Huge Spiders',
           'Harmless, Cute Piggies', 'Advanced Fish-People', 'Terrible Lizard Eggs', 'Silver Statues',
           'Meteor Armour', 'Doomsday Device', 'Time Machine', 'Crashed Sky-Boat', 'New Energy Source',
           'Fountain of Immortality', 'Ghost Army', 'Ruby-Growing Tree', 'Astral Vessel',
           'Island is a Giant Turtle', "Always Growing", "All a Hologram",
           'No Time Passes Here', 'Steel Dinosaurs', 'Slime Volcano']

# Cults and Groups

collective = ['Library', 'Children', 'Fortress', 'Heralds', 'Keepers', 'Temple', 'Betrayers', 'Hunters', 'Union',
              'School', 'Seekers', 'Knights', 'Order', 'Drinkers', 'Choir', 'Sons', 'Daughters', 'Servants', 'Society',
              'Army', 'Wanderers', 'Pilgrims', 'Comtemplators', 'Movement', 'Preachers', 'Revolution', 'Mercy-Givers',
              'Council', 'Tower', 'Worshipers', 'Observers', 'Beggars', 'Witnesses', 'Centre', 'Garrison', 'Engineers',
              'Family', 'Chanters']

descriptions = ['Devouring', 'Kindly', 'Dreaming', 'Infinite', 'Glowing', 'Dead', 'Rotting', 'Raging', 'Golden',
                'Unborn', 'Blessed', 'Chained', 'Sunken', 'Broken', 'Stirring', 'Newborn', 'Golden', 'Bloodied', 'Half',
                'Forgotten', 'Underground', 'Twisted', 'Glorious', 'Vengeful', 'Laughing', 'Elder', 'Loving',
                'Undefeatable', 'Timeless', 'Striking', 'Roaring', 'Inevitable', 'Bright', 'Jade', 'Iron', 'Bone',
                'Silent', 'Pure']

symbol = ['a Sword', 'a Snake', 'a Child', 'an Egg', 'a Cloud', 'a Light', 'a Star', 'a Father', 'a Maw', 'a Song',
          'a Color', 'a Gate', 'a Ship', 'Death', 'the Sea', 'a Shadow', 'a Giants', 'a General', 'a Truth', 'a Lie',
          'a King', 'a Queen', 'a Force', 'a Swarm', 'a Fleet', 'a Horror', 'a Beauty', 'a Spire', 'a Crystals',
          'a Pantheon', 'a Throne', 'a Web', 'a Eye', 'a Hand', 'a Shield', 'a Skull', 'a Weed', 'Mist']

standing = ['Hated', 'Hidden', 'Disgraced', 'Bankrupt', 'Disqusting', 'Outlawed', 'Enemies of another', 'Tiny',
            'Weak', 'Fake', 'Forgotten', 'Nobody Cares', 'Mocked, Discouraged', 'Hunted', 'Weakened', 'Underground',
            'Unknown', 'Hardly Known', 'Feared', 'Taboo', 'Too Old to Criticise', 'Too Big to Fall', 'Somewhat Liked',
            'Charitable', 'Tolerated', 'Wealthy', 'Allies of another', 'Respected', 'Front as a Business',
            'Actively Recruiting', 'Fashionable', 'Strong', 'Powerful', 'Legendary', 'Beloved', 'Council-Sanctioned']

cult_type = 'cult', 'club', 'collective', 'organization'

# Food Effects, Smelling give hint to effect.

eating_things = ['Delici...argh! STR Save or your guts explode.', 'Delicious! Fruity. Quite satisfying.',
                 'Tastes meaty. You regain any lost STR.',
                 'Your insides feel cold, and liquid metal coats your bones. You always have Armour 1.',
                 'Tastes pickled. You get real drunk.', 'Woah. Hallucinations for d6 hours.',
                 'Blech! Vomit now and for d6 hours.',
                 'Tastes inky. You can read books instantly by waving your hand over them.',
                 "Urgh... so salty. It's gross.", 'Literally liquid gold. Lose d6 STR.',
                 'Hot! Breathe Fire (d10) at "whoever is right in front of you.', 'Roll a Mutation (see p137).',
                 'Turn Invisible for d6 minutes.', 'Horrible pain for d6 minutes.',
                 'Bready. You need never eat or drink again.', 'Like liquid fish. Quite stirring.',
                 'Blind for d6 hours!', 'Awful poison. Lose 2d6 STR.', 'Lose 2d6 DEX. Turn to stone at DEX 0.',
                 'Lose 2d6 WIL. Turn into an insane monster at WIL 0.', "It's okay I guess, for slime.",
                 'Gain an evil voice in your head forever.', 'Gain a helpful voice in your head forever.',
                 "It's the best! You crave more. Lose 1 WIL each day until you eat some more.",
                 "Invigorating! Gain 1d6 STR for d6 hours.", 'Mind-Opening. Gain 1d6 WIL for d6 hours.',
                 'Zippy! Move at double pace for d6 hours.', 'First taste is gross. Second is delicious.',
                 'Your mouth seals shut for d6 hours.', 'Go on a rampage for d6 turns.', 'Your voice now echoes.',
                 'Your voice is permanently higher pitched.', 'Rapid hair growth, permanently.',
                 'Like Honey! Heals any ailment.']

public_policy = f"The Magistrate declares {get_random(decree)}. The people are saying {get_random(pub_reaction)}."

setting = f"Landmark/Scenery:\t {get_random(landmarks)} \nDanger/Challenge: \t {get_random(dangers)}."

cult_gen = f"The {get_random(standing)} {get_random(cult_type)} named the {get_random(descriptions)} " \
           f"{get_random(collective)}. Whose symbol is {get_random(symbol)} in/on {get_random(symbol)}."
danger_room = f"\nSetting:\t\t {get_random(atmosphere)} {get_random(locations)}\n" \
              f"\nSimple:\t\t\t {get_random(hazards)}\nChallenging:\t {get_random(hazards)}, {get_random(hazards)}\n" \
              f"Dangerous:\t\t {get_random(hazards)}, {get_random(hazards)}, {get_random(hazards)}"

business = f"Business Name:\t\t {get_random(businesses)}\nQuickest Route:\t\t {get_random(quick_route)}" \
           f"\nLink Underground?\t {get_random(link_underground)}"

# print(cult_gen)
# print(business)
# print(danger_room)
# print(setting)
