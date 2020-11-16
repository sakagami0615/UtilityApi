
from outlook import OutlookWrapper
import TEST_PARAM


if __name__ == '__main__':

	outlook = OutlookWrapper(TEST_PARAM.MAIL_ADDRESS)

	# メールの検索
	mail = outlook.FindMail(TEST_PARAM.FOLDER_NAME, TEST_PARAM.MAIL_TITLE)
	if not mail:
		print(mail)
	else:
		print("件名: " ,mail.subject)
		print("差出人: %s [%s]" % (mail.sendername, mail.senderEmailAddress))
		print("受信日時: ", mail.receivedtime)
		print("未読: ", mail.Unread)
		print("本文: ", mail.body)

	# 下書きメールを作成
	ret = outlook.CreateDraftMail('a', 'b', 'TEST', 'TEST MESSAGE')
