import argparse
import os
import time


class Submit():
	def __init__(self, path, message, competition):
		self.path = path
		self.message = message
		self.competition = competition

	def submit_to_competition(self):
		res = os.popen("kaggle competitions submit" + " -f " + self.path +  " -m hey " + self.competition)
	
	def upload(self):
		res = os.popen("kaggle kernel upload")

class CheckStatus():
	def __init__(self,user_name ,kernel_name, frequency):
		self.kernel_name = kernel_name
		self.user_name = user_name
		self.frequency = frequency

	def getStatus(self):
		#expecting "kaggle kernel status -> complete / running"

		if(not self.frequency):
			res = os.popen('kaggle kernels status ' + self.user_name + "/" + self.kernel_name).read()
			print(res)

		elif(self.frequency > 0):
			while(True):
				res = os.popen('kaggle kernels status ' + self.user_name + "/" + self.kernel_name).read()
				print(res)
				status = res.split(" ")[-1].strip("\n")
				if((status == "\"complete\"") or (status == "cancel.\"")):
					print("exiting")
					return
				print(res)
				time.sleep(self.frequency)


class GetOutput():
	def __init__(self, user_name, kernel_name, dire):
		self.user_name = user_name
		self.kernel_name = kernel_name
		self.dir = dire

	def getOutput(self):
		os.popen('kaggle kernels output ' + self.user_name + "/" + self.kernel_name + " --path " + self.dir).read()























































	











