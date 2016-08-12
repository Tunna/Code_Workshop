'''
0 - Main Menu
1 - Show all lists. (show all keys)
2 - Show a specific list. (show the value of a specific key)
3 - Add a new shopping list. (add a new key with value to dic)
4 - Add an item to a shopping list. (change the value of a key)
5 - Remove an item from a shopping list. (update a value of a key)
6 - Remove a list by nickname. (delete key/value from dictionary)
7 - Exit when you are done. (break away from loop) 

- sorted
- lower
- no dupes
- print out content of list when anything changes
- after updating list/key, prompt user for more items.
'''

master_shopping_list = {}

def menu_prompt():
	#todo: add menu, print, while loop, include break
	# continuosly prompt to add/remove items until user says 'EXIT' to break loop
	print """
	Here are your options:
	0 - Main Menu"
	1 - Show all lists.
	2 - Show a specific list.
	3 - Add a new shopping list.
	4 - Add an item to a shopping list.
	5 - Remove an item from a shopping list.
	6 - Remove a list by nickname.
	7 - Exit when you are done.  
	"""
	menu_select = int(raw_input("Please enter your selection: ")))
	return menu_select


def show_all_lists(master_shopping_list):
	# print out lists
	global master_shopping_list
	print master_shopping_list.keys()
	mini_menu = raw_input("Are you done?" ).lower()
		if mini_menu == "yes"
			return
		else:
			menu_prompt()

def show_specific_list(master_shopping_list, specific_list):
	#todo: print out specific key with it's values from dictionary
	# make sure it's sorted/lowercase
	global master_shopping_list
	print master_shopping_list.items()
	mini_menu = raw_input("Are you done?" ).lower()
		if mini_menu == "yes"
			return
		else:
			menu_prompt()
	return
	

def add_list(master_shopping_list, make_list):
	#todo: add a key and value to dictionary
	# make sure key name is unique and item is not repeated in list (2 while loops)
	# lowercase/sorted
	# print out list, prompt user for more updates
	pass

def add_item(master_shopping_list, make_item):
	# todo: change key value in dictionary
	# no dupes (check if value already exists in key)
	# lower/sorted
	# print out list, prompt user for more updates
	pass

def remove_item(master_shopping_list, rid_item):
	# todo: update value of key
	# lower/sorted
	# print out list, prompt user for more updates
	pass

def remove_list( master_shopping_list, rid_list):
	# todo: remove key and value from dictionary
	#lower/sorted
	# print out list, prompt user for more updates
	pass

def sorted_items():
	# sort items in list alphabetically
	pass


def main():
	menu_select = menu_prompt()
	while (True):
		if menu_select == 0:
			menu_prompt()
		elif menu_select == 1:
			show_all_lists()
		elif menu_select == 2:
			show_specific_list()
		elif menu_select == 3:
			add_list()
		elif menu_select == 4:
			add_item()
		elif menu_select == 5:
			remove_item()
		elif menu_select == 6:
			remove_list()
		else:
			break


	specific_list = raw_input("")
	make_list = raw_input(" ")
	make_item = raw_input(" ")
	rid_item = raw_input(" ")
	rid_list = raw_input(" ")

	