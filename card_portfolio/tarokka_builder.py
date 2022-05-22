from deck_builder import deck_builder
from card_constructor import Card, Low_Card
import random


tarokka_suits = ["Coins", "Glyphs", "Stars", "Swords"]
tarokka_lows = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Master"]
tarokka_highs = ["Artifact", "Beast", "Broken One", "Darklord", "Donjon", "Seer", "Ghost", "Executioner", "Horseman", "Innocent", "Marionette", "Mists", "Raven", "Tempter"]

tarokka = deck_builder(tarokka_suits, tarokka_lows, 0, tarokka_highs)

tarokka_dictionary = {}


for card in tarokka:
    tarokka_dictionary[card] = Card(card)


tarokka_class_object_list = list(tarokka_dictionary.values())


tarokka_class_object_list[0].description = "I see the skeleton of a deadly warrior, lying on a bed of stone flanked by gargoyles."
tarokka_class_object_list[1].description = "Look to a place where sickness and madness are bred. Where children once cried, the treasure lies still."
tarokka_class_object_list[2].description = "Look to the wizard of wines! In wood and sand the treasure hides."
tarokka_class_object_list[3].description = "Seek a cask that once contained the finest wine, of which not a drop remains."
tarokka_class_object_list[4].description = "I see a dark room full of bottles. It is the tomb of a guild member."
tarokka_class_object_list[5].description = "A wounded elf has what you seek. He will part with the treasure to see his dark dreams fulfilled."
tarokka_class_object_list[6].description = "What you seek lies at the crossroads of life and death, among the buried dead."
tarokka_class_object_list[7].description = "The Vistani have what you seek. A missing child holds the key to the treasure's release."
tarokka_class_object_list[8].description = "Look for a fortress inside a fortress, in a place hidden behind fire."
tarokka_class_object_list[9].description = "I see a nest of ravens. There you will find the prize."
tarokka_class_object_list[10].description = "The treasure you seek is hidden behind the sun, in the house of a saint."
tarokka_class_object_list[11].description = "I see a garden dusted with snow, watched over by a scarecrow with a sackcloth grin. Look not to the garden, but to the guardian."
tarokka_class_object_list[12].description = "Look to the west. Find a pool blessed by the light of the white sun."
tarokka_class_object_list[13].description = "Find the mother - she who gave birth to evil."
tarokka_class_object_list[14].description = "An evil tree grows atop a hill of graves where the ancient dead sleep. The ravens can help you find it. Look for the treasure there."
tarokka_class_object_list[15].description = "I see walls of bones, a chandelier of bones, and a table of bones - all that remains of enemies long forgotten."
tarokka_class_object_list[16].description = "I see a lonely mill on a precipice. The treasure lies within."
tarokka_class_object_list[17].description = "What you seek lies in a pile of treasure, beyond a set of amber doors."
tarokka_class_object_list[18].description = "Look for a wealthy woman. A staunch ally of the devil, she keeps the treasure under lock and key, with the bones of an ancient enemy."
tarokka_class_object_list[19].description = "You will find what you seek in the castle, amid the ruins of a place of supplication."
tarokka_class_object_list[20].description = "Go to a place of dizzying heights, where the stone itself is alive!"
tarokka_class_object_list[21].description = "Look to the one who sees all. The treasure is hidden in her camp."
tarokka_class_object_list[22].description = "I see a kneeling woman - a rose of great beauty plucked too soon. The master of the marsh knows of whom I speak."
tarokka_class_object_list[23].description = "I see a fallen house guarded by a great stone dragon. Look to the highest peak."
tarokka_class_object_list[24].description = "The treasure is hidden in a small castle beneath a mountain, guarded by amber giants."
tarokka_class_object_list[25].description = "Search for the crypt of a wizard ordinaire. His staff is the key."
tarokka_class_object_list[26].description = "A man is not what he seems. He comes here in a carnival wagon. Therein lies what you seek."
tarokka_class_object_list[27].description = "A woman hangs above a roaring fire. Find her, and you will find treasure."
tarokka_class_object_list[28].description = "I see a dead village, drowned by a river, ruled by one who has brought great evil into the world."
tarokka_class_object_list[29].description = "Look for a wizard's tower on a lake. Let the wizard's name and servant guide you to that which you seek."
tarokka_class_object_list[30].description = "The treasure lies in a dragon's house, in hands once clean and now corrupted."
tarokka_class_object_list[31].description = "I see a sleeping prince, a servant of light and the brother of darkness. The treasure lies with him."
tarokka_class_object_list[32].description = "Go to the mountains. Climb the white tower guarded by golden knights."
tarokka_class_object_list[33].description = "The thing you seek lies with the dead, under mountains of gold coins."
tarokka_class_object_list[34].description = "Look for a den of wolves in the hills overlooking a mountain lake. the treasure belongs to Mother Night."
tarokka_class_object_list[35].description = "Find the Mad Dog's crypt. The treasure lies within, beneath blackened bones."
tarokka_class_object_list[36].description = "I see a faceless god. He awaits you at the end of a long and winding road, deep in the mountains."
tarokka_class_object_list[37].description = "I see a throne fit for a king."
tarokka_class_object_list[38].description = "There is a town where all is not well. There you will find a house of corruption, and within, a dark room full of still ghosts."
tarokka_class_object_list[39].description = "That which you seek lies in the womb of darkness, the devil's lair: the one place to which he must return."

tarokka_class_object_list[0].namealt = "Swashbuckler"
tarokka_class_object_list[1].namealt = "Philanthropist"
tarokka_class_object_list[2].namealt = "Trader"
tarokka_class_object_list[3].namealt = "Merchant"
tarokka_class_object_list[4].namealt = "Guild Member"
tarokka_class_object_list[5].namealt = "Beggar"
tarokka_class_object_list[6].namealt = "Thief"
tarokka_class_object_list[7].namealt = "Tax Collector"
tarokka_class_object_list[8].namealt = "Miser"
tarokka_class_object_list[9].namealt = "Rogue"
tarokka_class_object_list[10].namealt = "Monk"
tarokka_class_object_list[11].namealt = "Missionary"
tarokka_class_object_list[12].namealt = "Healer"
tarokka_class_object_list[13].namealt = "Shepherd"
tarokka_class_object_list[14].namealt = "Druid"
tarokka_class_object_list[15].namealt = "Anarchist"
tarokka_class_object_list[16].namealt = "Charlatan"
tarokka_class_object_list[17].namealt = "Bishop"
tarokka_class_object_list[18].namealt = "Traitor"
tarokka_class_object_list[19].namealt = "Priest"
tarokka_class_object_list[20].namealt = "Transmuter"
tarokka_class_object_list[21].namealt = "Diviner"
tarokka_class_object_list[22].namealt = "Enchanter"
tarokka_class_object_list[23].namealt = "Abjurer"
tarokka_class_object_list[24].namealt = "Elementalist"
tarokka_class_object_list[25].namealt = "Evoker"
tarokka_class_object_list[26].namealt = "Illusionist"
tarokka_class_object_list[27].namealt = "Necromancer"
tarokka_class_object_list[28].namealt = "Conjurer"
tarokka_class_object_list[29].namealt = "Wizard"
tarokka_class_object_list[30].namealt = "Avenger"
tarokka_class_object_list[31].namealt = "Paladin"
tarokka_class_object_list[32].namealt = "Soldier"
tarokka_class_object_list[33].namealt = "Mercenary"
tarokka_class_object_list[34].namealt = "Myrmidon"
tarokka_class_object_list[35].namealt = "Berserker"
tarokka_class_object_list[36].namealt = "Hooded One"
tarokka_class_object_list[37].namealt = "Dictator"
tarokka_class_object_list[38].namealt = "Torturer"
tarokka_class_object_list[39].namealt = "Warrior"
tarokka_class_object_list[40].namealt = "Artifact"
tarokka_class_object_list[41].namealt = "Beast"
tarokka_class_object_list[42].namealt = "Broken One"
tarokka_class_object_list[43].namealt = "Darklord"
tarokka_class_object_list[44].namealt = "Donjon"
tarokka_class_object_list[45].namealt = "Seer"
tarokka_class_object_list[46].namealt = "Ghost"
tarokka_class_object_list[47].namealt = "Executioner"
tarokka_class_object_list[48].namealt = "Horseman"
tarokka_class_object_list[49].namealt = "Innocent"
tarokka_class_object_list[50].namealt = "Marionette"
tarokka_class_object_list[51].namealt = "Mists"
tarokka_class_object_list[52].namealt = "Raven"
tarokka_class_object_list[53].namealt = "Tempter"

# Tarokka Enemy Deck descriptions: either a single description, or a choice of descriptions to be chosen randomly.

tarokka_enemy_deck = tarokka_class_object_list[-14:]

tarokka_enemy_deck[0].description = "Look for an entertaining man with a monkey. This man is more than he seems."
tarokka_enemy_deck[1].description = "A werewolf holds a secret hatred for your enemy. Use her hatred to your advantage."
tarokka_enemy_deck[2].desca = "Your greatest ally will be a wizard. His mind is broken, but his spells are strong."
tarokka_enemy_deck[2].descb = "I see a man of faith whose sanity hangs by a thread. He has lost someone close to him."
tarokka_enemy_deck[3].description = "Ah, the worst of all truths: You must face this evil land alone!"
tarokka_enemy_deck[4].desca = "Search for a troubled young man surrounded by wealth and madness. His home is his prison."
tarokka_enemy_deck[4].descb = "Find a girl driven to insanity, locked in the heart of her dead father's house. Curing her madness is key to your success."
tarokka_enemy_deck[5].description = "Look for a dusk elf living among the Vistani. He has suffered a great loss and is haunted by dark dreams. Help him, and he will help you in return."
tarokka_enemy_deck[6].desca = "I see a fallen paladin of a fallen order of knights. He lingers like a ghost in a dead dragon's lair."
tarokka_enemy_deck[6].descb = "Stir the spirit of the clumsy knight whose crypt lies deep within the castle."
tarokka_enemy_deck[7].description = "Seek out the brother of the devil's bride. They call him 'the lesser,' but he has a powerful soul."
tarokka_enemy_deck[8].desca = "I see a dead man of noble birth, guarded by his widow. Return life to the dead man's corpse, and he will be your staunch ally."
tarokka_enemy_deck[8].descb = "A man of death named Arrigal will forsake his dark lord to serve your cause. Beware! He has a rotten soul."
tarokka_enemy_deck[9].desca = "I see a young man with a kind heart. A mother's boy! He is strong in body, but weak of mind. Seek him out in the village of Barovia."
tarokka_enemy_deck[9].descb = "Evil's bride is the one you seek!"
tarokka_enemy_deck[10].desca = "What horror is this? I see a man made by a man. Ageless and alone, it haunts the towers of the castle."
tarokka_enemy_deck[10].descb = "Look for a man of music, a man with two heads. He lives in a place of great hunger and sorrow."
tarokka_enemy_deck[11].description = "A Vistania wanders this land alone, searching for her mentor. She does not stay in one place for long. Seek her out at Saint Markovia's abbey, near the mists."
tarokka_enemy_deck[12].description = "Find the leader of the feathered ones who live among the vines. Though old, he has one more fight left in him."
tarokka_enemy_deck[13].desca = "I see a child - a Vistana. You must hurry, for her fate hangs in the balance. Find her at the lake!"
tarokka_enemy_deck[13].descb = "I hear a wedding bell, or perhaps a death knell. It calls thee to a mountainside abbey, wherein you will find a woman who is more than the sum of her parts."

for card in tarokka_enemy_deck:
    if len(card.desca) > 1:
        choices = [card.desca, card.descb]
        card.description = random.choice(choices)

# Check Confirmed
# print(tarokka_enemy_deck[6].description)


# Tarokka Location Deck desciptions: either a description, or a choice of descriptions to be chosen randomly.

tarokka_location_deck = tarokka_class_object_list[-14:]

tarokka_location_deck[0].description = "He lurks in the darkness where the morning light once shone - a sacred place."
tarokka_location_deck[1].description = "The beast sits on his dark throne."
tarokka_location_deck[2].description = "He haunts the tomb of the man he envied above all."
tarokka_location_deck[3].description = "He lurks in the depths of darkness, in the one place to which he must return."
tarokka_location_deck[4].description = "He lurks in a hall of bones, in the dark pits of his castle."
tarokka_location_deck[5].description = "He waits for you in a place of wisdom, warmth, and despair. Great secrets are there."
tarokka_location_deck[6].description = "Look to the father's tomb."
tarokka_location_deck[7].description = "I see a dark figure on a balcony, looking down upon this tortured land with a twisted smile."
tarokka_location_deck[8].description = "He lurks in the one place to which he must return - a place of death."
tarokka_location_deck[9].description = "He dwells with the one whose blood sealed his doom, a brother of light snuffed out too soon."
tarokka_location_deck[10].description = "Look to great heights. Find the beating heart of the castle. He waits nearby."
tarokka_location_deck[11].description = "The cards can't see where the evil lurks. The mists obscure all!"
tarokka_location_deck[12].description = "Look to the mother's tomb."
tarokka_location_deck[13].description = "I see a secret place - a vault of temptation hidden behind a woman of great beauty. The evil waits atop his tower of treasure."












