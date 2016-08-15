'''
0 - Main Menu
1 - Show all lists. (show all keys)
2 - Show a specific list. (show the value of a specific key)
3 - Add a new shopping list. (add a new key with value to dic)
4 - Add an item to a shopping list. (change the value of a key)
5 - Remove an item from a shopping list. (update a value of a key)
6 - Remove a list by nickname. (delete key/value from dictionary)
7 - Exit when you done are. (break away from loop) 

- sorted
- lower
- no dupes
- print out content of list when anything changes
- after updating list/key, prompt user for more items.
'''

shopping_dict = {"Target":["shoes","socks","diapers","soap"], 
"Safeway":["milk""eggs","apples", "oranges"], 
"Farmers_Market":["kale","peaches","honey","cheese"], 
"Macys":["skirt","belt","dress","tie"]}

def menu_prompt():
	#todo: add menu, print, while loop, include break
	# continuosly prompt to add/remove items until user says 'EXIT' to break loop
	print """
	Shopping List Options:
	0 - Main Menu
	1 - Show all lists.		
	2 - Show a specific list.
	3 - Add a new shopping list.
	4 - Add an item to a shopping list.
	5 - Remove an item from a shopping list.
	6 - Remove a list by nickname.
	7 - Type exit when you are done. 
	"""
	option = raw_input("Please enter your selection: ")
	return option


def show_all_lists():
	# print out all lists and sort alphabetically
	global shopping_dict
	lists = []
	for key in shopping_dict.keys():
		lists.append(key)
		return lists.sort()
	

def show_specific_list(specific_list):
	#todo: print out specific key with it's values from dictionary
	# make sure it's sorted/lowercase
	global shopping_dict
	specific_list = []
	for value in shopping_dict.values():
		specific_list.append(value)
		return specific_list

	
def add_list(make_list):
# 	#todo: add a key and value to dictionary
# 	# make sure key name is unique and item is not repeated in list (2 while loops)
# 	# lowercase/sorted
# 	# print out list, prompt user for more updates
# 	pass
	global shopping_dict
	if make_list in shopping_dict:
		print "This list %s already exists!" % (make_list)
	else:
		shopping_dict.append(make_list)
	return shopping_dict.sort()

def add_item(make_item):
# 	# todo: change key value in dictionary
# 	# no dupes (check if value already exists in key)
# 	# lower/sorted
# 	# print out list, prompt user for more updates
	global shopping_dict
	if make_item in shopping_dict.values():
		print "This item %s already exists!" % (make_item)
	else:
		shopping_dict.append(make_item)
		return shopping_dict

def remove_item(rid_item):
# 	# todo: update value of key
# 	# lower/sorted
# 	# print out list, prompt user for more updates
	global shopping_dict
	if rid_item.lower() not in shopping_dict.values():
		print "This item %s not in list!" % (rid_item)
	else:
		shopping_dict.remove(rid_item)
		return shopping_dict


def remove_list(rid_list):
# 	# todo: remove key and value from dictionary
# 	#lower/sorted
# 	# print out list, prompt user for more updates
# 	global shopping_dict
	if rid_list.lower() in shopping_dict.keys():
		del shopping_dict[rid_list]
		return shopping_dict
	else:
		if rid_list.lower() not in shopping_dict.keys():
			print "This list %s not in list!" % (rid_list)
	

def continue_menu():
	done = raw_input("Do you want to continue?").lower()
	if done == 'yes':
		return False
	else:
		return True


def main():
	
	while (True):
		option = menu_prompt()
		if option.lower() == "exit":
			break
		elif option == "0":
			pass
		elif option == "1":
			print show_all_lists()
		elif option == "2":
			print show_all_lists()
			selection = raw_input("Which list would you like to see?").lower()
			print show_specific_list(selection)
		elif option == "3":
			add_shop_list = raw_input("What list would you like to add?").lower()
			print add_list(add_shop_list)
			print continue_menu
		elif option == "4":
			add_shop_item = raw_input("What item would you like to add?").lower()
			print add_item(add_shop_item)
			print continue_menu
		elif option == 5:
			remove_item()
		elif option == 6:
			remove_list()
		else:
			break


# 	# specific_list = raw_input("")
# 	# make_list = raw_input(" ")
# 	# make_item = raw_input(" ")
# 	# rid_item = raw_input(" ")
# 	# rid_list = raw_input(" ")

if __name__ == '__main__':
	main()