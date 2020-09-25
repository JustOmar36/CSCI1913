# CSCI 1913, Spring 2020, Lab 4
# Student Names:
# Omar Masri!
# Brandon Weinstein!
# MASRI013@umn.edu
# WEINS127@umn.edu

def lin_contains(lin_dict, key):
	for v,k in lin_dict:
		if k == key:
			return True
	return False

def lin_get(lin_dict, key):
	for v,k in lin_dict:
		if k == key:
			return v
	return None

def lin_put(lin_dict, key, value):
	new_pair = (value, key)
	does_contain = lin_contain_key(lin_dict, key)
	if does_contain == -1:
		lin_dict.append(new_pair)
	else:
		lin_dict[does_contain] = new_pair

def lin_contain_key(lin_dict, key):
	for i in range(len(lin_dict)):
		v,k = lin_dict[i]
		if k == key:
			return i
	return -1


def bin_contains(bin_dict, key):
	low = 0
	high = len(bin_dict) - 1

	while high >= low:
		mid = high + low // 2
		if bin_dict[mid][1] < key:
			low = mid + 1
		elif bin_dict[mid][1] > key:
			high = mid - 1
		else:
			return True
	return False

def bin_get(bin_dict, key):
	low = 0
	high = len(bin_dict) - 1 

	while high >= low:
		mid = high + low // 2
		if bin_dict[mid][1] < key:
			low = mid + 1
		elif bin_dict[mid][1] > key:
			high = mid - 1
		else:
			return bin_dict[mid][0] 
	return None


def bin_put(bin_dict, key, value):
	new_pair = (value, key)
	does_contain = lin_contain_key(bin_dict, key)
	if does_contain == -1:
		if bin_dict == []:
			bin_dict.append(new_pair)
		elif key < bin_dict[0][1]:
			bin_dict.insert(0, new_pair)
		elif key > bin_dict[len(bin_dict) - 1][1]:
			bin_dict.append(new_pair)
		else:
			for i in range(len(bin_dict)):
				if bin_dict[i][1] < key < bin_dict[i+1][1]:
					bin_dict.insert(i+1, new_pair)
					return
	else:
		bin_dict[does_contain] = new_pair
		