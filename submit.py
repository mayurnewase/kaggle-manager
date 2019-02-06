import kaggle
import os


class Submit():
	def __init__(self, path, message, competition):
		self.path = path
		self.message = message
		self.competition = competition

	def upload(self):
		res = os.popen("kaggle competitions submit" + " -f " + self.path +  " -m hey " + self.competition)

def main():
	parser = argparse.ArgumentParser(description = "default parser")
	parser.add_argument("--path")
	parser.add_argument("--message")
	parser.add_argument("--competition")
	args = parser.parse_args()

	s = Submit(args.path, args.message, args.competition)
	s.upload()


if "__name__" == "__main__":
	main()



































