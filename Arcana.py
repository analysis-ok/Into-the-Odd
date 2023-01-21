import random as r

gateKeepersSigil = "Gatekeeper’s Sigil: Create a gate between two flat surfaces that you can see. " \
                   "The gates close if you pass through or break line of sight."
piercedHeart = 'Pierced Heart: State an object you desire. The heart indicates its direction and vague distance.'
paleFlame = 'Pale Flame: An object you touch glows with white light. Contact with ' \
            'the glowing object causes a chilling pain. The effect wears off when the Arcanum is used again.'
soulChain = 'Soul Chain: Target must pass a DEX Save to avoid your touch, or they lose d6 WIL ' \
            'and you get a glimpse of their current desire.'
gavelUnbreakableSeal = 'Gavel of the Unbreakable Seal: One door, window, etc. is sealed until you open it.'
foulCenser = 'Foul Censer: Green smoke surrounds you and everyone within 20ft. Missiles cannot pass through the smoke.'
bleedingStave = 'Bleeding Stave: Spews blood-like oil onto a 10ft area. Anyone moving or ' \
                'standing on the oil must make a DEX Save to avoid falling and being unable to move on their turn. ' \
                'Disappears in a harmless flash if ignited.'
painIdol = 'Pain Idol: Roll a die of your choice. If the result is odd, you lose that much STR, ' \
           'if it’s even your target loses that much STR.'
webbedHands = 'Webbed Hands: Climb sheer surfaces as if you were a spider.'
sunblessedBands = 'Sun-blessed Bands: Glow and hum lightly. Anybody attacking you suffers Damage equal to that ' \
                  'they cause to you. If you attack a target yourself then the effect ends until you Rest.'
fleshTomeBabble = 'Flesh-Tome of Babble: Speak in a strange sounding language. Every living thing ' \
                  'is able to understand and reply in the same tongue if they wish.'
tyrantsRod = 'Tyrant’s Rod: Order a target to drop, fall, flee or halt unless they pass a WIL Save.'
blackVeil = 'Black Veil: Target must pass a WIL Save or is blinded until you lift the curse or they Rest. ' \
            'Blinded individuals may require a DEX Save to carry out ' \
            'other actions that rely on sight, and their attacks are Impaired.'
strandsSuffering = 'Strands of Suffering: Strands spread between two surfaces up to 20ft apart. ' \
                   'Those within only move very slowly and painfully unless they pass a DEX Save.'
heatRay = 'Heat Ray: One metal object becomes too hot to touch. If it cannot be quickly dropped ' \
          'or removed the wielder suffers d8 Damage, ignoring armour.'
miniaturisationCoil = 'Miniaturisation Coil: Touch an object to shrink it into a tiny miniature. ' \
                      'Restore the object to original size at will. The original object can be up to your size, ' \
                      'but living beings must be willing.'
frozenCloud = 'Frozen Cloud: Floats at your will. Anybody within takes d6 Damage and cannot move ' \
              'unless they pass a STR Save.'
manyPhaseKey = 'Many Phase Key: Phase through a wall or floor with any objects you are carrying.'
skullMagnet = 'Skull Magnet: You may attract or repel a single target that has a boney skull, ' \
              'unless they pass a WIL Save.'
transrealMirror = 'Transreal Mirror: A perfect duplicate of you is formed. It acts independently, ' \
                  'and just like the original. It cannot interact physically with anything. ' \
                  'The double lasts until dismissed or a new double is created.'
gorgersMask = 'Gorger’s Mask: The wearer can consume anything safely.'
tombBox = 'Tomb Box: Contains three tiny skeletons that obey whoever holds the box. ' \
          'They are too small to do any real damage, but are quite agile and clever.'
howlingLantern = 'Howling Lantern: Blowing into the lantern causes a roar that terrifies prey animals, ' \
                 'but attracts predators.'
rainbowBlade = 'Rainbow Blade: This sword (d6) can fire a beam of harmless light in any colour the wielder wishes.'
hawkProsperity = 'Hawk of Prosperity: A mechanical bird (3hp, d6 claws) that will only help you' \
                 ' to accumulate wealth. Requires a Shilling each day as food.'
inquisitorsHood = 'Inquisitor’s Hood: Speak a question with two possible answers. The target must pass a WIL Save ' \
                  'or answer as honestly as they can. If they pass their Save you blurt out an inconvenient truth.'
wintersSickle = 'Winter’s Sickle: Anybody taking Damage from this Sickle (d6) is Deprived ' \
                'and feels cold to their bones until they spend at least an hour warming ' \
                'themselves by a fire or other heat source.'
griefCup = 'Grief Cup: Anybody drinking from this cup has upsetting visions showing ' \
           'the consequences of their past actions.'
victoryGlobe = 'Victory Globe: Swear an oath aloud. The globe gently guides you in the direction that would help you' \
               ' achieve the oath, but if you fail to complete it before the end of the day' \
               ' it lashes your mind for d12 WIL loss.'
moonLens = 'Moon Lens: Look at two objects and ask a question. The lens highlights the one object ' \
           'that best answers the question. It cannot predict the future.'
foolsCoin = 'Fool’s Coin: Anybody that values money will crave this coin the first time they see it. ' \
            'The effect wears off after an hour.'
chanceRose = 'Chance Rose: Crush this ceramic rose to change the odds of success for a single action to 50%. ' \
             'This cannot make the impossible possible. The rose reforms at the start of each day.'
homingStick = 'Homing Stick: A staff that can be called to return to you, flying by the best route possible.'
falsePlatter = 'False Platter: Anybody viewing this platter sees an illusion of luxury that they are craving right now.'
goldVisor = 'Gold Visor: While wearing this you visualise a general sense of somebody’s honesty ' \
            'and sincerity while they speak.'
infinityIcon = 'Infinity Icon: You can stop time, but you can do nothing but observe and think during this time.'

basic_arcana = [gateKeepersSigil, piercedHeart, paleFlame, soulChain, gavelUnbreakableSeal, foulCenser, bleedingStave,
                painIdol, webbedHands, sunblessedBands, fleshTomeBabble, tyrantsRod, blackVeil, strandsSuffering,
                heatRay, miniaturisationCoil, frozenCloud, manyPhaseKey, skullMagnet, transrealMirror, gorgersMask,
                tombBox, howlingLantern, rainbowBlade, hawkProsperity, inquisitorsHood, wintersSickle, griefCup,
                victoryGlobe, moonLens, foolsCoin, chanceRose, homingStick, falsePlatter, goldVisor, infinityIcon]

hypnoTorch = 'Hypno-Torch: Target repeats their current action until you say stop, or they pass the Save on their turn.'
infernoDevice = 'Inferno Device: Cause a source of fire to explode, causing d10 Damage to all within 20ft.'
powerLeech = 'Power Leech: Target must pass a WIL Save, or else you swap STR scores with them. ' \
             'Either side returns their STR to its original value when they Rest.'
fireBloodedScroll = 'Fire Blooded Scroll: Target feels their blood begin to boil. They take d6 Damage, ' \
                    'ignoring armour, each round, until they pass the Save.'
mindProbe = 'Mind Probe: You are able to dig into the innermost thoughts of the target. ' \
            'They may pass a WIL Save to resist.'
bookDespair = 'Book of Despair: Summon a 20ft area of tentacles that lash out and grab. Anyone within must pass a ' \
              'STR Save to break free. The mass of tentacles has 10hp and is destroyed at 0hp .'
primalFlute = 'Primal Flute: All within 15ft must pass a WIL Save or turn feral. They do nothing but attack ' \
              'the nearest living thing until they pass a WIL Save on their turn.'
windowBeyond = 'Window to Beyond: Summon a flying beast (STR 14, 10hp, d8 Damage) to fight for you ' \
               'until no enemies remain. After this, you must pass a WIL Save or the beast turns on you. ' \
               'If you pass the Save, it flies for freedom. Only one beast can be summoned at once.'
blackOrb = 'Black Orb: Obliterate a man-sized or smaller object you touch. No effect on living tissue.'
snakebiteParasite = 'Snakebite Parasite: Bite a target, for d6 Damage. You both lose d12 DEX ' \
                    'as the venom flows through you.'
hornedMask = 'Horned Mask: You take on a bestial form (Armour 1, d10 Damage claws, retain Ability Scores and hp), ' \
             'but lose the ability to speak. Return to normal form when you sleep.'
doomHive = 'Doom Hive: 20ft buzzing cloud moves 10ft away from you each round. ' \
           'Anyone within loses d6 STR every round.'
witheringGlove = 'Withering Glove: Target must pass a STR Save or shrink to a husk. ' \
                 'They halve their STR score (rounding up) and have all attacks Impaired. ' \
                 'A Long Rest restores them to full size.'
spiritCup = 'Spirit Cup: Swap bodies with another that drinks from the cup. They can resist with a WIL Save. ' \
            'Retain WIL scores only.'
entropyCrystal = 'Entropy Crystal: Fires an unerring beam. Target must pass a STR Save or lose d12 DEX. ' \
                 'If this reduces their DEX to zero they are turned to blue crystal.'
guardiansShield = 'Guardian’s Shield: A shield of light appears between you and a single target. ' \
                  'The shield absorbs 10 points of Damage before vanishing. Each turn it pushes the target 10ft away ' \
                  'from you unless they pass a STR Save.'
earthStone = 'Earth Stone: Over an hour you shift sand, soil or earth to your will, creating ditches ' \
             'up to 10ft deep. This may destabilise structures, redirect rivers and fell trees ' \
             'but does not affect rock, create tunnels, or move fast enough to bury mobile opponents.'
roaringLion = 'Roaring Lion: Glass, crystal or ceramic objects within 5ft are shattered. In addition, ' \
              'one object you are touching (wielder may avoid with a WIL Save) is shattered. ' \
              'This object must be light enough for you to lift.'
pressureNeedle = 'Pressure Needle: If the target takes Critical Damage today they explode in a bloody mess.'
orbBox = 'Orb Box: Summon two orbs of light that obey your commands. They can be flung at a target for d12 Damage, ' \
         'destroying the orb. No more than two orbs can be summoned each day'

greater_arcana = [hypnoTorch, infernoDevice, powerLeech, fireBloodedScroll, mindProbe, bookDespair, primalFlute,
                  windowBeyond, blackOrb, snakebiteParasite, hornedMask, doomHive, witheringGlove, spiritCup,
                  entropyCrystal, guardiansShield, earthStone, roaringLion, pressureNeedle, orbBox]

weatherAltar = 'Weather Altar: Cause the weather within a mile radius to change for the rest of the day. ' \
               'In the case of dangerous weather, you cannot target specific individuals or locations, ' \
               'or cause extremes that are inescapably lethal.'
obliterationPrism = 'Obliteration Prism: Choose a target and roll d12. If this is equal or higher than their ' \
                    'current hp they are completely destroyed in a blast of fire.'
rebirthCoffin = 'Rebirth Coffin: A corpse is miraculously restored to life if they pass a WIL Save. ' \
                'If they fail the Save, the remains are utterly destroyed.'
spaceCube = 'Space Cube: You and up to one companion are teleported to a location you have been to before.'
maliceGong = 'Malice Gong: All enemies within 20ft lose d6 STR.'
essenceProjector = 'Essence Projector: Conjures a ghostly image of a dead target, which speaks with you clearly ' \
                   'and willingly, regardless of language or intelligence. The image remains until dismissed.'
sealMadness = 'Seal of Madness: Creates symbols on any object. Anyone trying to decode them loses d12 WIL.'
quakeSpire = 'Quake Spire: Targets a 100ft area. All structures take d20 Damage and caves or tunnels collapse, ' \
             'causing d6 Damage per round to anyone within, until they escape.'
tabletMaster = 'Tablet of the Master: A large object is animated and serves you. The object has 10hp, Armour 2, ' \
               'and attacks for d10 Damage. No more than one object can serve you at once.'
forcefieldGenerator = 'Forcefield Generator: Create a semi-transparent, shimmering surface that only you ' \
                      'may pass through. Any enemy approaching the wall is blasted with light for d12 Damage. ' \
                      'The field lasts until dismissed or another field is created.'
ironSuit = 'Iron Suit: You have Armour 3 and ignore fire and poison based Damage. You can no longer swim ' \
           'but also do not need to breathe, eat or drink. The effect lasts until dismissed.'
deadOak = 'Dead Oak: Creates a permanent one-mile zone where any living things lose d6 STR each hour, ' \
          'starting at the end of this hour. Living things within this zone are instantly aware of this ' \
          'and try to leave. Even plants wither and die.'
forgeReconstruction = 'Forge of Reconstruction: Over an hour one damaged or ruined structure, ship or similar target' \
                      ' is repaired to peak condition without need for materials.'
statueGoldenChariot = 'Statue of the Golden Chariot: You and your allies fight to the death, ' \
                      'even after taking Critical Damage.'
divinePool = 'Divine Pool: You take on the appearance of a huge, godlike entity. You can conjure purely cosmetic, ' \
             'but impressive, visual effects.'
stormThrone = 'Storm Throne: You turn into a bolt of lightning, moving at impossible speed to a specified location ' \
              'you can see. Anyone you pass through takes d10 Damage, ignoring armour.'
transformationCave = 'Transformation Cave: You shift to take the form of your chosen enemy, retaining only your WIL ' \
                     'score and level of intelligence. This lasts until dismissed.'
blackHoleCollider = 'Black Hole Collider: Create a five-foot, black sphere. Anything entering it is ' \
                    'utterly destroyed. Cannot be moved or placed on top of an object or opponent.'
mindWiper = 'Mind Wiper: Target must pass a WIL Save or become a mindless automaton.'
starbeamPanel = 'Starbeam Panel: As long as you have line of sight to the sky, you call down ' \
                'a column of light for d20 Damage'

legend_arcana = [weatherAltar, obliterationPrism, rebirthCoffin, spaceCube, maliceGong, essenceProjector,
                 sealMadness, quakeSpire, tabletMaster, forcefieldGenerator, ironSuit, deadOak,
                 forgeReconstruction, statueGoldenChariot, divinePool, stormThrone, transformationCave,
                 blackHoleCollider, mindWiper, starbeamPanel]

all_arcana = [weatherAltar, obliterationPrism, rebirthCoffin, spaceCube, maliceGong, essenceProjector,
              sealMadness, quakeSpire, tabletMaster, forcefieldGenerator, ironSuit, deadOak,
              forgeReconstruction, statueGoldenChariot, divinePool, stormThrone, transformationCave,
              blackHoleCollider, mindWiper, starbeamPanel, hypnoTorch, infernoDevice, powerLeech,
              fireBloodedScroll, mindProbe, bookDespair, primalFlute,
              windowBeyond, blackOrb, snakebiteParasite, hornedMask, doomHive, witheringGlove, spiritCup,
              entropyCrystal, guardiansShield, earthStone, roaringLion, pressureNeedle, orbBox, gateKeepersSigil,
              piercedHeart, paleFlame, soulChain, gavelUnbreakableSeal, foulCenser, bleedingStave,
              painIdol, webbedHands, sunblessedBands, fleshTomeBabble, tyrantsRod, blackVeil, strandsSuffering,
              heatRay, miniaturisationCoil, frozenCloud, manyPhaseKey, skullMagnet, transrealMirror, gorgersMask,
              tombBox, howlingLantern, rainbowBlade, hawkProsperity, inquisitorsHood, wintersSickle, griefCup,
              victoryGlobe, moonLens, foolsCoin, chanceRose, homingStick, falsePlatter, goldVisor, infinityIcon]

# Assets for Creating Arcana
form = ['Throne', 'Chest', 'Rod', 'Wand', 'Ring', 'Cube', 'Bell', 'Lantern', 'Brooch', 'Gem', 'Telescope', 'Lens',
        'Dagger', 'Pistol', 'Musket', 'Sphere', 'Hammer', 'Headband', 'Bracers', 'Flute', 'Drum', 'Huge Machine',
        'Mirror', 'Painting', 'Staff', 'Helmet', 'Breastplate', 'Rock', 'Boulder', 'Horn', 'Tusk', 'Sword', 'Tablet',
        'Engine', 'Anvil', 'Dice', 'Chains', 'Cannon']

power = ['Cosmic Travel', 'Time Distortion', 'Cosmic Summoning', 'Astral-Transcendence', 'Telekinesis',
         'Elemental Blast', 'Slow Painful Death', 'Disintegration', 'Flight', 'Size Distortion', 'Plant Control',
         'Mass-Creation', 'Energy-Creation', 'Thing go BOOM!', 'Unlock Primal Rage', 'Persuasion', 'Auditory Illusions',
         'Visual Illusions', 'Liquify Matter', 'Blast Minds', 'Read Thoughts', 'Create Deadly Traps', 'Summon the Dead',
         'Hypnotic Music', 'Dull Senses', 'Venom Ray', 'Great Knowledge', 'Communicate Great Distances',
         'Arm the Masses', 'Destroy Structures', 'Unnatural Slumber', 'Spread Insanity', 'Possession',
         'Create Servants',
         'Release Unstoppable Creature', 'Release Benevolent Spirit', 'Swap Materials', 'Sensory Overload']


def get_arcana():
    print("\nPrepare to Receive a gift of Odd")
    print("1: Basic Arcana \n2: Greater Arcana \n3: Legendary Arcana \n4: Any Type")
    sel = input("ENTER SELECTION: ")
    print("." * 100)
    if sel == "1":
        arc0 = r.choice(basic_arcana)
        return arc0
    if sel == "2":
        arc1 = r.choice(greater_arcana)
        return arc1
    if sel == "3":
        arc2 = r.choice(legend_arcana)
        return arc2
    if sel == "4":
        arcall = r.choices(all_arcana)
        return arcall


# print(get_arcana())
