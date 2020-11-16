
def DictComparisonAll(dict_1, dict_2):

	if test_dict_1 == test_dict_2:
		comp_ret = True
	else:
		comp_ret = False
	
	return comp_ret


def DictComparisonSelectKey(dict_1, dict_2, wanted_keys):

	dictfilter = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])

	dictfilter_1 = dictfilter(dict_1, wanted_keys)
	dictfilter_2 = dictfilter(dict_2, wanted_keys)
	
	if dictfilter_1 == dictfilter_2:
		comp_ret = True
	else:
		comp_ret = False
	
	return comp_ret



if __name__ == '__main__':

	test_dict_1 = {
		'key1': 1,
		'key2': 2,
		'key3': 3
	}

	test_dict_2 = {
		'key1': 1,
		'key2': 2,
		'key3': 4
	}

	comp_ret_1 = DictComparisonAll(test_dict_1, test_dict_2)
	print(comp_ret_1)

	wanted_keys = ('key1', 'key2')
	comp_ret_2 = DictComparisonSelectKey(test_dict_1, test_dict_2, wanted_keys)
	print(comp_ret_2)