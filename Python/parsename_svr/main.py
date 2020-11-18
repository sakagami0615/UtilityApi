import numpy
from parsename import ParseFirstLastNameSVR


def RunTrain(dataset_file):
	parse = ParseFirstLastNameSVR()
	parse.Train(dataset_file)
	parse.Save()


def RunTest():
	parse = ParseFirstLastNameSVR()
	parse.Load()
	
	test_datas = numpy.array([
		['大蜘蛛英紀', '大蜘蛛', '英紀'],
		['四手井淑子', '四手井', '淑子'],
		['大豆生田啓友', '大豆生田', '啓友'],
		['吉弘統幸', '吉弘', '統幸'],
		['聞間彩', '聞間', '彩'],
		['関水武', '関水', '武'],
		['野呂恭一', '野呂', '恭一'],
		['橋本甜歌', '橋本', '甜歌'],
		['深山亀三郎', '深山', '亀三郎'],
		['國井善弥', '國井', '善弥']
	])


	separate_indexs = parse.Predict(test_datas[:,0])
	
	correct_count = 0
	for (test_data, separate_index) in zip(test_datas, separate_indexs):
		lastname = test_data[0][:int(separate_index)]
		firstname = test_data[0][int(separate_index):]

		if (lastname == test_data[1]) and (firstname == test_data[2]):
			correct_flg = True
			correct_count = correct_count + 1
		else:
			correct_flg = False

		print((test_data[0], (lastname, firstname), (test_data[1], test_data[2]), correct_flg))
	
	print('Accuracy: {}'.format(float(correct_count)/len(test_datas)))


if __name__ == '__main__':

	TEST_DATA = 'Dataset_NameOriginNet(SameNameRanking).csv'

	RunTrain(TEST_DATA)
	RunTest()
	