import win32com.client


class OutlookWrapper:

	def __init__(self, address):

		self.__outlook_app = win32com.client.Dispatch('Outlook.Application')
		self.__outlook_mapi = self.__outlook_app.GetNamespace('MAPI')
		self.__account_datas = next(filter(lambda x: str(x) == address, self.__outlook_mapi.Folders), None)

	
	def __FindFolder(self, folder_datas, folder_name):

		infolder_data = next(filter(lambda x: str(x) == folder_name, folder_datas), None)
		return infolder_data


	def FindMail(self, folder_list, title):

		def FindFolder(folder_tokens):
			folder_datas = self.__account_datas
			for folder_token in folder_tokens:
				folder_datas = self.__FindFolder(folder_datas.Folders, folder_token)
				if not folder_datas:
					return False, None
			return True, folder_datas
		
		get_folder_datas = None
		
		# フォルダ探索
		for folder in folder_list:
			folder_tokens = folder.split('/')
			is_find_folder, folder_datas = FindFolder(folder_tokens)
			
			if is_find_folder:
				get_folder_datas = folder_datas
				break
		
		# 探索ファイルが無い場合はNoneを返却
		if not get_folder_datas:
			return None
		
		# 探索フォルダからメールを取得
		# メールが無い場合はNoneを返却
		mail = next(filter(lambda x: x.subject == title, folder_datas.Items), None)
		return mail
	
	
	def CreateDraftMail(self, to, cc, subject, body):

		draft_folder = next(filter(lambda x: '下書き' in str(x), self.__account_datas.Folders), None)
		
		if not draft_folder:
			return False
		
		mail = self.__outlook_app.CreateItem(0)
		mail.to = to
		mail.cc = cc
		mail.subject = subject
		mail.body = body
		mail.Move(draft_folder)

		return True
