"""    DOC~STRING

This program is designed to generate a random character.
Each character has 6 unqieu features.
There is a given set of data stored on excel and it can always be edited to
specific character building needs.

-No known Bugs

    """


#Import packages
import pandas as pd
import random


#Instantiate a file in a variable
file = "./card_image.xlsx"
#loading in the file 
card_image = pd.read_excel(io = file, sheet_name = 0, header = 0)


#saving the size of y axis in df as a variable
all_rows =card_image.shape[0]

#saving a random range between 0 and all_rows
row_star = random.randrange(0,all_rows)
#saving the random row selected from the specific feature
card_star_rand = card_image.loc[(row_star),"card_power_level"]


#saving a random range between 0 and all_rows
row_name = random.randrange(0,all_rows)
#saving the random row selected from the specific feature
card_name_rand = card_image.loc[(row_name),"card_name"]


#saving a random range between 0 and all_rows
row_type = random.randrange(0,all_rows)
#saving the random row selected from the specific feature
card_type_rand = card_image.loc[(row_type),"card_type"]


#saving a random range between 0 and all_rows
row = random.randrange(0,all_rows)
#saving the random row selected from the specific feature
card_image_rand = card_image.loc[(row),"image"]



#Saving an attack between a range of values
card_attck = random.randrange(300,2300)
#Saving an Defence between a range of values
card_def = random.randrange(100,1850)



#a function that prints all the core card information out
def card_summary():
	print(f"""
	Power Level:{card_star_rand}
	Card Name:{card_name_rand}
	Card Type:{card_type_rand}
	{card_image_rand}
	ATK/{card_attck}
	DEF/{card_def}
	""")

#a function that designs a boarder
def boarder_x():
	b = "_.-="
	b_2 = "-_-"
	b_3 = "o0o"
	print(f"{b_2*15}")
	

#calling all the functions to display the card
boarder_x()
card_summary()
boarder_x()

