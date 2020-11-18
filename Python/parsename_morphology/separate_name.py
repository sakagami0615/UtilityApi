# coding: utf-8
import sys
import os
import pickle
import numpy as np
from janome.tokenizer import Tokenizer

# 形態素解析による苗字/名前の分割処理
def SeparateNameByMorphologicalAnalysis(name):

	t = Tokenizer()
	tokens = [token for token in t.tokenize(name, wakati=True)]
	
	if len(tokens) == 2:
		return tokens[0], tokens[1]
	
	return name, None


if __name__ == '__main__':

	# 下記サイトの情報を使用 (取得日：2020/11/18)
	# https://myoji-yurai.net/myojiData.htm
	# ■本日の有名人アクセスランキング
	# ■同姓同名アクセスランキング
	TEST_DATAS = [
		['美広彩花',	'美広 彩花'],
		['堂珍嘉邦',	'堂珍 嘉邦'],
		['頼朝隆',		'頼朝 隆'],
		['到津公誼',	'到津 公誼'],
		['魚澄惣五郎',	'魚澄 惣五郎'],
		['民秋貴也',	'民秋 貴也'],
		['萬鉄五郎',	'萬 鉄五郎'],
		['納谷悟朗',	'納谷 悟朗'],
		['上郎清助',	'上郎 清助'],
		['目賀田綱美',	'目賀田 綱美'],
		['鬼頭敏夫',	'鬼頭 敏夫'],
		['木村忍',		'木村 忍'],
		['半沢直樹',	'半沢 直樹'],
		['山田太郎',	'山田 太郎'],
		['水野米治',	'水野 米治'],
		['日浦智',		'日浦 智'],
		['堂本剛',		'堂本 剛'],
		['豊島宏之',	'豊島 宏之'],
		['伊藤誠',		'伊藤 誠'],
		['秋山智英',	'秋山 智英'],
	]

	for TEST_DATA in TEST_DATAS:
		tokens = TEST_DATA[1].split(' ')
		corr_lastname = tokens[0]
		corr_firstname = tokens[1]
		
		lastname, firstname = SeparateNameByMorphologicalAnalysis(TEST_DATA[0])
		
		if (corr_lastname == lastname) and (corr_firstname == firstname):
			is_success = True
		else:
			is_success = False
		
		print((lastname, firstname, is_success))
