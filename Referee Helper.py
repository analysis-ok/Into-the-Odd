import tkinter as tk
import webbrowser
from Arcana import *
from character import *
from enemygen import *
from npcgen import *
from misc import *

root = tk.Tk()
root.title("Into the Odd")
canvas = tk.Canvas(root, width=550, height=100)
canvas.grid(columnspan=4, rowspan=5)

instructions = tk.Label(root, text="~Into the Odd~\n", font=("Times", "16"))
instructions.grid(columnspan=4, row=0, column=0)


def open_npc():
    page_content = f"{genname()} {gencap()} {genocc()}, who {genevent()}"
    text_box = tk.Text(root, height=12, width=70, wrap="word")
    text_box.insert(1.0, page_content)
    text_box.tag_configure("center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(row=5, columnspan=4, padx=5, pady=30)


def open_arcana():
    page_content = f'A {get_random(form)} that has a power of {get_random(power)}.'
    text_box = tk.Text(root, height=12, width=70, wrap="word")
    text_box.insert(1.0, page_content)
    text_box.tag_configure("center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(row=5, columnspan=4, padx=5, pady=30)


def open_decree():
    page_content = f"The Magistrate declares {get_random(decree)}.\n\nThe people are saying {get_random(pub_reaction)}."
    text_box = tk.Text(root, height=12, width=70, wrap="word")
    text_box.insert(1.0, page_content)
    text_box.tag_configure("center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(row=5, columnspan=4, padx=5, pady=30)


def open_monster():
    page_content = f'Type: {get_nature()} {get_form()} \nHit Protection: {get_mon_hp()} \nStrength:\t  {get_strength()}' \
                   f'\nDexterity:\t {get_dexterity()} \nWillpower:\t {get_willpower()}  \nPower:\n - {get_twist()} ' \
                   f'\nMotivation:\n - It is Driven {get_drive()}'
    text_box = tk.Text(root, height=12, width=70, wrap="word")
    text_box.insert(1.0, page_content)
    text_box.tag_configure("center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(row=5, columnspan=4, padx=5, pady=30)


# Needs to be worked on.
def open_character():
    reg_name = f"{get_random(forenames)} {get_random(surname)}"
    reg_hp = get_hp()
    reg_str = get_strength()
    reg_dex = get_dexterity()
    reg_will = get_willpower()
    reg_hi = max(reg_str, reg_dex, reg_will)
    hpstat = reg_hp
    histat = reg_hi
    page_content = f"Name: {reg_name} \nHit Protection: {reg_hp}" \
                   f" \nStrength:\t  {reg_str} \nDexterity:\t {reg_dex} \nWillpower:\t {reg_will}" \
                   f"\nInventory & Characteristics:\n - {get_kit(hpstat, histat)} " \
                   f"\n\nAlternative Starter Items:\n - {get_altkit(hpstat, histat)}"
    text_box = tk.Text(root, height=12, width=70, wrap="word")
    text_box.insert(1.0, page_content)
    text_box.tag_configure("center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(row=5, columnspan=4, padx=5, pady=30)


# Needs to be fixed.
def open_mutant():
    mu_hp = get_hp()
    mu_str = get_mstat()
    mu_dex = get_mstat()
    mu_will = get_mstat()
    mhpstat = mu_hp
    mhistat = max(mu_str, mu_dex, mu_will)

    page_content = f"Mutant \nHit Protection: {mu_hp} \nStrength:\t  {mu_str} \nDexterity:\t {mu_dex} " \
                   f"\nWillpower:\t {mu_will} \nInventory & Characteristics:\n - {get_mkit1(mhpstat, mhistat)} " \
                   f"\nMutations: {get_mkit2(mhpstat, mhistat)}"
    text_box = tk.Text(root, height=12, width=70, wrap="word")
    text_box.insert(1.0, page_content)
    text_box.tag_configure("center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(row=5, columnspan=4, padx=5, pady=30)


def open_folk():
    fo_hp = get_hp()
    fo_str = get_fstat()
    fo_dex = get_fstat()
    fo_will = get_fwill()
    fhpstat = fo_hp
    fhistat = max(fo_str, fo_dex, fo_will)

    page_content = f"Simple Folk \nHit Protection: {fo_hp} \nStrength:\t  {fo_str} \nDexterity:\t {fo_dex}" \
                   f"\nWillpower:\t {fo_will} \nInventory & Characteristics:\n - Dagger (d6), Torch, Quaint Clothes\n" \
                   f" - {get_fkit1(fhpstat, fhistat)} \nTrinkets:{get_fkit2(fhpstat, fhistat)}"
    text_box = tk.Text(root, height=12, width=70, wrap="word")
    text_box.insert(1.0, page_content)
    text_box.tag_configure("center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(row=5, columnspan=4, padx=5, pady=30)


def open_unhuman():
    unequip = []
    un_hp = get_hp()
    un_str = get_strength()
    un_dex = get_dexterity()
    un_will = get_willpower()
    un_type = get_random(unhuman_list)
    unhuman_type = r.choice(unhuman_list)

    if unhuman_type == unhuman_list[0]:
        un_str = r.randrange(1, 13) + 6
        unequip.append('Axe (d6)')

    if unhuman_type == unhuman_list[1]:
        un_str = d6roll(1)
        un_will = d6roll(1)
        unequip.append('Dagger (d6)')

    if unhuman_type == unhuman_list[2]:
        un_dex = d6roll(1) + 6
        unequip.append('Sword (d6), Bow (d6 B)')

    if unhuman_type == unhuman_list[3]:
        un_str = r.randrange(1, 13) + 8
        un_will = r.randrange(1, 11)
        unequip.append("Heavy Two-Handed Chopper (d8 B)")

    if unhuman_type == unhuman_list[4]:
        un_str = d6roll(1)
        un_dex = r.randrange(1, 13) + 6
        un_will = d6roll(1)
        unequip.append('Dagger (d6)')

    if unhuman_type == unhuman_list[5]:
        color = ["Red Dragonkin: Fire Immunity, Breath Weapon (d8)",
                 "Black Dragonkin: Acid Immunity, Breath Weapon (d8)",
                 "Blue Dragonkin: Lighting Immunity, Breath Weapon (d8)",
                 "White Dragonkin: Cold Immunity, Breath Weapon (d8)",
                 "Green Dragonkin: Acid Immunity, Breath Weapon (d8)"]
        get_color = r.choice(color) + ", Sword (d6)"
        unequip.append(get_color)

    if unhuman_type == unhuman_list[6]:
        un_str = d6roll(1)
        unequip.append('Musket (d8 B)')

    if unhuman_type == unhuman_list[7]:
        unequip.append('Rifle (d8 B)')

    if unhuman_type == unhuman_list[8]:
        un_dex = r.randrange(1, 13) + 6
        unequip.append('Musket (d8 B)')

    if unhuman_type == unhuman_list[9]:
        un_str = d6roll(0) + 3
        unequip.append('Musket (d8 B)')

    if unhuman_type == unhuman_list[10]:
        unequip.append('Sword (d6), Poison*')

    if unhuman_type == unhuman_list[11]:
        un_str = d6roll(0) + 14
        un_dex = r.randrange(1, 11)
        unequip.append("Maul (d10)")

    page_content = f"UnHuman \nHit Protection: {un_hp} \nStrength:\t  {un_str} \nDexterity:\t {un_dex}" \
                   f"\nWillpower:\t {un_will} \nInventory & Characteristics:\n - {un_type} \n - {unequip[0]} " \
                   f"\nAdditional Items: \n - {get_unstart(un_hp)}"
    text_box = tk.Text(root, height=12, width=70, wrap="word")
    text_box.insert(1.0, page_content)
    text_box.tag_configure("center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(row=5, columnspan=4, padx=5, pady=30)


def open_cult():
    page_content = f"The {get_random(standing)} {get_random(cult_type)} named the {get_random(descriptions)} " \
                   f"{get_random(collective)}. \nWhose symbol is {get_random(symbol)} in/on {get_random(symbol)}."
    text_box = tk.Text(root, height=12, width=70, wrap="word")
    text_box.insert(1.0, page_content)
    text_box.tag_configure("center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(row=5, columnspan=4, padx=5, pady=30)


def open_bizz():
    page_content = f"Business Name:\n - {get_random(businesses)}\nQuickest Route:\n - {get_random(quick_route)}" \
                   f"\nLink Underground?\t\n - {get_random(link_underground)}"
    text_box = tk.Text(root, height=12, width=70, wrap="word")
    text_box.insert(1.0, page_content)
    text_box.tag_configure("center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(row=5, columnspan=4, padx=5, pady=30)


def open_danger():
    page_content = f"Setting:\t {get_random(atmosphere)} {get_random(locations)}\n***Choose the Difficulty***" \
                   f"\nSimple:\n - {get_random(hazards)}" \
                   f"\nChallenging:\n - {get_random(hazards)}, {get_random(hazards)}\n" \
                   f"Dangerous:\n - {get_random(hazards)}, {get_random(hazards)}, {get_random(hazards)}"
    text_box = tk.Text(root, height=12, width=70, wrap="word")
    text_box.insert(1.0, page_content)
    text_box.tag_configure("center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(row=5, columnspan=4, padx=5, pady=30)


def open_setting():
    page_content = f"Landmark/Scenery:\n - {get_random(landmarks)} \nDanger/Challenge:\n - {get_random(dangers)}."
    text_box = tk.Text(root, height=12, width=70, wrap="word")
    text_box.insert(1.0, page_content)
    text_box.tag_configure("center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(row=5, columnspan=4, padx=5, pady=30)


npc_text = tk.StringVar()
arcana_text = tk.StringVar()
decree_text = tk.StringVar()
monster_text = tk.StringVar()
character_text = tk.StringVar()
mutant_text = tk.StringVar()
simpleFolk_text = tk.StringVar()
unhuman_text = tk.StringVar()
cult_text = tk.StringVar()
bizz_text = tk.StringVar()
danger_text = tk.StringVar()
setting_text = tk.StringVar()

npc_btn = tk.Button(root, textvariable=npc_text, command=lambda: open_npc(), bg="teal", fg="white", height=1,
                    width=15)
npc_text.set("Get NPC")
npc_btn.grid(column=0, row=1)

arcana_btn = tk.Button(root, textvariable=arcana_text, command=lambda: open_arcana(), bg="teal", fg="white",
                       height=1,
                       width=15)
arcana_text.set("Get Arcana")
arcana_btn.grid(column=1, row=1)

decree_btn = tk.Button(root, textvariable=decree_text, command=lambda: open_decree(), bg="teal", fg="white",
                       height=1,
                       width=15)
decree_text.set("Get Decree")
decree_btn.grid(column=2, row=1)

monster_btn = tk.Button(root, textvariable=monster_text, command=lambda: open_monster(), bg="teal", fg="white",
                        height=1,
                        width=15)
monster_text.set("Get Monster")
monster_btn.grid(column=3, row=1)

character_btn = tk.Button(root, textvariable=character_text, command=lambda: open_character(), bg="orange", fg="white",
                          height=1,
                          width=15)
character_text.set("Get Character")
character_btn.grid(column=0, row=2)

mutant_btn = tk.Button(root, textvariable=mutant_text, command=lambda: open_mutant(), bg="orange", fg="white",
                       height=1,
                       width=15)
mutant_text.set("Get Mutant")
mutant_btn.grid(column=1, row=2)

simpleFolk_btn = tk.Button(root, textvariable=simpleFolk_text, command=lambda: open_folk(), bg="orange", fg="white",
                           height=1,
                           width=15)
simpleFolk_text.set("Get Simple Folk")
simpleFolk_btn.grid(column=2, row=2)

unhuman_btn = tk.Button(root, textvariable=unhuman_text, command=lambda: open_unhuman(), bg="orange", fg="white",
                        height=1,
                        width=15)
unhuman_text.set("Get Unhuman")
unhuman_btn.grid(column=3, row=2)

cult_btn = tk.Button(root, textvariable=cult_text, command=lambda: open_cult(), bg="teal", fg="white",
                     height=1,
                     width=15)
cult_text.set("Get Cult/Group")
cult_btn.grid(column=0, row=3)

bizz_btn = tk.Button(root, textvariable=bizz_text, command=lambda: open_bizz(), bg="teal", fg="white",
                     height=1,
                     width=15)
bizz_text.set("Get Business")
bizz_btn.grid(column=1, row=3)

danger_btn = tk.Button(root, textvariable=danger_text, command=lambda: open_danger(), bg="teal", fg="white",
                       height=1,
                       width=15)
danger_text.set("Get Room")
danger_btn.grid(column=2, row=3)

setting_btn = tk.Button(root, textvariable=setting_text, command=lambda: open_setting(), bg="teal", fg="white",
                        height=1,
                        width=15)
setting_text.set("Get Setting")
setting_btn.grid(column=3, row=3)

canvas = tk.Canvas(root, width=150, height=30)
canvas.grid(columnspan=4)


def callback(url):
    webbrowser.open_new_tab(url)


# Create a Label to display the link
link = tk.Label(root, text="Buy the Book", font=('Helveticabold', 9), fg="blue", cursor="hand2")
link.grid(columnspan=4)
link.bind("<Button-1>", lambda e:

callback("https://freeleaguepublishing.com/en/games/into-the-odd/"))

root.mainloop()
