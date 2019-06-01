import requests

class LineNotifyAPI:

	url = "https://notify-api.line.me/api/notify"

	def __init__(self, access_token):
		self.__headers = {'Authorization': 'Bearer ' + access_token}

	def send(self, message, image=None, stickerPackageId=None, stickerId=None):
		payload = {
		'message': message,
		"stickerPackageId": stickerId,
		"stickerId": stickerPackageId,
		}
		files={}
		if image != None:
			files = {"imageFile": open(image, "rb")}
		r = requests.post(
			url=LineNotifyAPI.url,
			headers=self.__headers,
			data=payload,
			files=files,
			)
