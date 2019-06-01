from Notify_bot import LineNotifyAPI

tome_token = 'eemHbY4riW0drjOwx9x2drcjszNEWM2mrbtWWXiIICs' 
taku_tatsuya = 'OyXUd9ZOYM2xEJaUHuVOKq0RAs5Exo2BKyIQ5AS2I3n'

bot = LineNotifyAPI(access_token=tome)

bot.send(
	message="簡単に作れるよ",
	image="/Users/yamadaikuya/pics_of_quintuplet/itsuki.png",
	stickerPackageId=None, 
	stickerId=None,
	)
