import argparse
import os
import time


class Submit():
	def __init__(self, path, competition):
		self.path = path
		self.competition = competition

	def submit_to_competition(self):
		res = os.popen("kaggle competitions submit" + " -f " + self.path + self.competition)
	
	def upload(self):
		res = os.popen("kaggle kernel push -p " + self.path)

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
					return 0
				print(res)
				time.sleep(self.frequency)

class GetOutput():
	def __init__(self, user_name, kernel_name, dire):
		self.user_name = user_name
		self.kernel_name = kernel_name
		self.dir = dire

	def getOutput(self):
		print("Fetching output from kaggle...")
		if not os.path.isdir(self.dir):
			os.mkdir(self.dir)
		os.popen('kaggle kernels output ' + self.user_name + "/" + self.kernel_name + " --path " + self.dir).read()
		print("Done...")

class PostProcessor():
	def __init__(self, user_name, kernel_name, result_dir):
		self.user_name = user_name
		self.kernel_name = kernel_name
		self.result_dir = result_dir

	def postProcess():
			





















































	











