from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv(".env")

class Notify():

	def __init__(self, kernel_name, notify_message = None, tone_path = None):
		self.account_sid = os.environ.get("account_sid")
		self.auth_token = os.environ.get("auth_token")
		self.twillio_number = os.environ.get("number")
		self.personal_number = os.environ.get("personal_number")

		self.kernel_name = kernel_name
		self.notify_message = notify_message

		self.tone_path = tone_path

	def notifyMessage(self):
		client = Client(self.account_sid, self.auth_token)

		try:
			message = client.messages \
			                .create(
			                     body = self.kernel_name + " " + self.notify_message,
			                     from_= self.twillio_number,
			                     to = self.personal_number
			                 )
		except:
			print("Error occured while sending twillio message")

		print("sms sent successfully with id "+message.sid)

	def notifyDesktop(self):
		if(os.name == "posix"):
			os.popen("notify-send {self.kernel_name} {self.notify_message}")
		elif(os.name == "nt"):
			from win10toast import ToastNotifier
			toaster = ToastNotifier()
			toaster.show_toast("{self.kernel_name}","{self.notify_message}")
		else:
			print("Only linux and windows notifications are supported")

	def notifyTone(self):
		os.system("ffplay {self.tone_path} -nodisp")


#to='+917020846176'
#to='+919423514849'