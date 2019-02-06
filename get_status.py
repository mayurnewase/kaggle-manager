import argparse
import os
import time

"""
usage:
	take compettiion-kernel name
	output status

arguments:
	kernel name
	output directory
	check frequency
"""

class CheckStatus():
	def __init__(self,user_name ,kernel_name, frequency):
		self.kernel_name = kernel_name
		self.user_name = user_name
		self.frequency = frequency

	def getStatus(self):
		#expecting "kaggle kernel status -> complete / running"

		if(self.frequency == 0):
			res = os.popen('kaggle kernels status ' + self.user_name + "/" + self.kernel_name).read()
			print(res)

		if(self.frequency > 0):
			while(True):
				res = os.popen('kaggle kernels status ' + self.user_name + "/" + self.kernel_name).read()
				print(res)
				status = res.split(" ")[-1].strip("\n")
				if((status == "\"complete\"") or (status == "cancel.\"")):
					print("exiting")
					return
				print(res)
				time.sleep(self.frequency)


def main():
	parser = argparse.ArgumentParser(description = "default parser")
	parser.add_argument("--user_name")
	parser.add_argument("--kernel_name")
	parser.add_argument("--frequency")
	args = parser.parse_args()

	cs = checkStatus(args.user_name, args.kernel_name, args.frequency)
	print(cs.getStatus())



if __name__ == "__main__":
	main()















if __name__ == "__main__":main()
























	











