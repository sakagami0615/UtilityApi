import numpy
import pandas
import pickle
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer


class ParseFirstLastNameSVR:

	def __init__(self):
		pass
	

	def __CreateTrainData(self, filepath):

		dataframe = pandas.read_csv(filepath)

		fit_datas = []
		train_datas = []
		correct_datas = []

		for (full, last, first) in zip(dataframe['Fullname'], dataframe['Lastname'], dataframe['Firstname']):
			
			name_size = len(full)
			separate_index = len(last)

			train_value = float(separate_index)/float(name_size)
			
			fit_datas.extend(list(full))
			train_datas.append(full)
			correct_datas.append(train_value)
		
		# 重複文字を削除
		fit_datas = list(set(fit_datas))

		# convert list -> numpy
		fit_datas = numpy.array(fit_datas)
		train_datas = numpy.array(train_datas)
		correct_datas = numpy.array(correct_datas)
		
		return fit_datas, train_datas, correct_datas
	

	def __CreateTfidfVectorizer(self, fit_datas):
		
		# 参考資料
		# https://analytics-note.xyz/machine-learning/bow-tfidf-one-character/
		tfidf_vectorizer = TfidfVectorizer(token_pattern='(?u)\\b\\w+\\b')
		tfidf_vectorizer.fit(fit_datas)

		return tfidf_vectorizer
	
	
	def Load(self, svr_model_name='svr_model.pkl', vectorizer_name='vectorizer.pkl'):

		self.svr_model = pickle.load(open(svr_model_name, 'rb'))
		self.vectorizer = pickle.load(open(vectorizer_name, 'rb'))

	
	def Save(self, svr_model_name='svr_model.pkl', vectorizer_name='vectorizer.pkl'):
		
		pickle.dump(self.svr_model, open(svr_model_name, 'wb'))
		pickle.dump(self.vectorizer, open(vectorizer_name, 'wb'))
	

	def Train(self, filepath):

		# パラメータ読み込み
		fit_datas, train_datas, correct_datas = self.__CreateTrainData(filepath)
		# 文字列ベクトル化クラスを作成
		self.vectorizer = self.__CreateTfidfVectorizer(fit_datas)
		# 学習文字列をベクトル化
		train_vec_datas = self.vectorizer.transform(train_datas).toarray()
		# 苗字/名前分割位置取得用SVRモデルを学習
		self.svr_model = svm.SVR(C=1.0, kernel='linear', epsilon=0.1)
		self.svr_model.fit(train_vec_datas, correct_datas)
	
	
	def Predict(self, test_datas):

		test_vec_datas = self.vectorizer.transform(test_datas).toarray()
		regression_values = self.svr_model.predict(test_vec_datas)

		test_data_lens = numpy.array([len(data) for data in test_datas])

		separate_indexs = numpy.round(test_data_lens*regression_values)

		return separate_indexs
