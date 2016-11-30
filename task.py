import sys
# from utils.envs import API_KEY, USER_NAME

def main(slug):
	fname = '{}.py'.format(slug.replace('-', '_'))
	sys.stdout = open(fname, 'w')
	sys.stdout = open('test_' + fname, 'w')


if __name__ == "__main__":
	main(sys.argv[1])