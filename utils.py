import argparse
import os
import time
import shutil
import csv
import pandas as pd

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
	def __init__(self, user_name, kernel_name, result_dir):
		self.user_name = user_name
		self.kernel_name = kernel_name
		self.result_dir = result_dir
		self.temp_dir = "temp/"

		try:
			os.mkdir(self.temp_dir)
		except FileExistsError:
			shutil.rmtree("temp/")
		try:
			os.mkdir(self.result_dir)
		except FileExistsError:
			pass

	def getOutput(self):
		print("Fetching output from kaggle...")

		try:
			os.popen('kaggle kernels output ' + self.user_name + "/" + self.kernel_name + " --path " + self.temp_dir).read()
		except FileNotFoundError:
			print("Saving output failed because kaggle kernel stored output in subdirectory,so we are not able to download it.Please store outputs in current working directory only.")
			return None

		self.result_files = os.listdir(self.temp_dir)

		for file in self.result_files:
			shutil.move(self.temp_dir + "/" + file, self.result_dir + file)

		print("Done...")
		return self.result_files

def preProcessor():
	pass

def postProcessor(user_name, kernel_name, master_log, result_path, all_result_files, result_file):
	
	"""
	append result csv file to master csv file
	"""
	if all_result_files is not None and result_file is not None:
		data = pd.read_csv(result_path + result_file)
		print("post processing result")
		
		master = pd.read_csv(master_log)
		master = pd.concat([master, data], axis = 0)
		master.to_csv("master_log.csv")

		"""with open(master_log, "a") as f:
									f.write(data)"""
		"""with open(master_log, 'a') as f:
								    writer = csv.writer(f)
								    writer.writerow(data)"""



















































	











