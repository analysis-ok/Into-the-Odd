import random as r

nature = ['Solid-Smoke', 'Skeletal', 'Decaying', 'Luxurious', 'Bio-Machine', 'Living Construct', 'Reptilian',
          'Slime Covered', 'Glassy', 'Liquid Metal', 'Ceramic', 'Living Rock', 'Scabs and Sores', 'Hyper-Robotic',
          'Spiny', 'Stinking Filth', 'Shadow-Cloaked', 'Eerily Beautiful', 'Mechanical Suit', 'Sapient and Armoured',
          'Baroque Excess', 'Leathery', 'Pale and Bald', 'Ghostly, Holographic', 'Hard-light', 'Acid Dripping',
          'Shaggy Hair', 'Mirrored Metal', 'Damp Clay', 'Colossal', 'Bare Musculature', 'All-brain', 'Plasmic',
          'Chitin', 'Rusted Shell', 'Bionic Parts']

form = ['Cube', 'Tripod', 'Swarm', 'Disembodied Hand', 'Worm', 'Sphere', 'Hound', 'Great Cat', 'Snake', 'Crustacean',
        'Squat Biped', 'Slender Biped', 'Insect', 'Obese Biped', 'Towering Biped', 'Baby Bird', 'Slug', 'Snail', 'Hawk',
        'Terror-Bird', 'Bull', 'Shark', 'Spider', 'Blob', 'Spiral', 'Pyramid', 'Sheet', 'Wasp', 'Maggot', 'Tadpole',
        'Jellyfish', 'Bat', 'Octopus', 'Pike', 'Sea Urchin', 'Cannon', 'Fly', 'Fetal']

twist = ['Mastery of Magnetism', 'Grasps with Extra Limbs', 'Phases Through Matter', 'Chimera (roll additional Form)',
         'Reads Minds', 'Colossal Size', 'Drains Life', 'Sprays Acid', 'Creates Black-Holes', 'Teleports Self',
         'Teleports Others', 'Shifts Shape', 'Breathes Smoke', 'Creates Electric Charge', 'Sees Future',
         'Controls Others', 'Cloaking Device', 'Conjures Illusions', 'Infects with Disease', 'Kills with Venom',
         'Hunts Arcana', 'Fires Bullets', 'Freeze Matter', 'Heat/Melt Matter', 'Implants with Egg/Parasite',
         'Paralyzes with Touch', 'Fires Death Rays', 'Manipulates Living Tissue Telekinetically',
         'Manipulates Objects Telekinetically', 'Sees Distant Places', 'Regenerates from any harm',
         'Reflects harm onto attacker', 'Absorbs victims into Body', 'Turns victims into non-living matter',
         'Launch explosives', 'Cause intense pain at touch', 'Heal any harm with a touch', 'Sense distant objects']

drive = ["to protect itself.", "to hunt worthy prey.", "to feed in monthly gorges.", "to trick the foolish.",
         "to guard an Arcanum.", "to implant host.", "torment a victim.", "by desire.", "by desire to be left alone.",
         "by cruelty to the weak.", "to trap victims.", "by hunger.", "by lost.", "by fear.", "by fear of people.",
         "by fear of loud sounds.", "by anger.", "by revenge.", "by desire to depress victims.",
         "by desire to cause self pity.", "to repel intruders.", "to feed master.", "by lust.", "to banish intruders.",
         "to deliver messages.", "to find sense of purpose.", "to cause mass death.", "by loneliness.", "by curiosity.",
         "mad with power.", "to find weird things.", "to find shiny things.", "to cheap others.", "to find it's body.",
         "to escape.", "feed on the helpless.", "to create darkness and silence.", "by greed."]


def d6roll(value):
    i = 0
    stat = 0
    while i <= value:
        roll = r.randrange(1, 7)
        stat += roll
        i += 1
    return stat


def get_strength():
    stat = d6roll(2)
    return stat


def get_dexterity():
    stat = d6roll(2)
    return stat


def get_willpower():
    stat = d6roll(2)
    return stat


def get_mon_hp():
    stat = r.randrange(1, 30)
    return stat


def get_nature():
    nat = r.choice(nature)
    return nat


def get_form():
    frm = r.choice(form)
    return frm


def get_drive():
    drve = r.choice(drive)
    return drve


def get_twist():
    twst = r.choice(twist)
    return twst


amonster_hp = get_mon_hp()
