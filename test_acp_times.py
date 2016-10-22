"""
Nose Tests for project 4
"""

from acp_times import *
import arrow
import os

# year is 2016 by default. This is a problem if leap year or not
# FIXME: Automate querying https://rusa.org/octime_acp.html 
# and processing test from web. Year would then be correct.
YEAR = '2016'

'''
In the form of:
TEST_DICT =  {filename:{dist: 200,
						controls: [1,2, i]
						opens: [1,2, i]
						closes: [1,2,i]}}
'''
TEST_DICT =  {}
						
def process():
	'''
	arg: none
	return: None
	processes everything in the test folder into checkpoints dictionary
	stores checkpoints in global TEST_DICT. key is filename.
	
	NOTES: This function is highly dependent on rusa 
	not changing their output format.
	'''
	
	for filename in os.listdir("tests"):

		checkpoints = {}
		checkpoints['controls'] = []
		checkpoints['opens'] = []
		checkpoints['closes'] = []
		filename = 'tests/' + filename
		
		with open(filename, 'r') as f:
			#skip first 6 lines.
			for i in range(6):
				f.readline()
			read_data = f.readlines()

		#Get the brevet dist. Stores in checkpoints dict.
		checkpoints['dist'] = read_data[0].split('>')[6].split('km')[0]
		
		#Skip first 2 lines
		for i in range(3, len(read_data)):
			line = read_data[i].strip()
			#if it has a length and it doesn't start with '<'
			if (len(line) and (line[0] != '<')):
				line = line.split()
				#if the first position is a number
				if (line[0][0].isdigit()):
					#add the control distance
					checkpoints['controls'].append(line[0].split('km')[0])
					#add the opening time
					mmdd = line[2].split('/')
					mmdd_slash = mmdd[0] + '-' + mmdd[1]
					checkpoints['opens'].append(YEAR + '-' + mmdd_slash + ' ' + line[3])
				else:
					#add the closing time
					mmdd = line[1].split('/')
					mmdd_slash = mmdd[0] + '-' + mmdd[1]
					checkpoints['closes'].append(YEAR + '-' + mmdd_slash + ' ' + line[2])
			
		#save in the global dict
		TEST_DICT[filename] = checkpoints
		
		
def test_web_files():
	'''
	arg: none
	return None
	
	Function calls process(), which parses files in 'tests' folder into TEST_DICT.
	Then runs asserts on all entries in TEST_DICT. 
	
	USE: Go to: https://rusa.org/octime_acp.html
	Use the brevet calculator to calculate an opening and closing time text file.
	Save file as a complete webpage in the tests folder

	In the command line type 'make test' (only for unix machines)
	'''
	
	#process all files in 'test' folder
	process()
	
	for filename in TEST_DICT:		
		checkpoints = TEST_DICT[filename]
		
		#for testing
		print(checkpoints)
		
		dist = checkpoints['dist']
		controls = checkpoints['controls']
		opens = checkpoints['opens']
		closes = checkpoints['closes']
		
		start_time = opens[0]
		
		for i in range(1, len(controls)):
			open = arrow.get(opens[i], 'YYYY-MM-DD HH:mm').isoformat()
			print('open results:')
			print(open_time(int(controls[i]), int(dist), start_time), '==', open)
			assert open_time(int(controls[i]), int(dist), start_time) == open
			
			close = arrow.get(closes[i], 'YYYY-MM-DD HH:mm').isoformat()
			print('close results:')
			print(close_time(int(controls[i]), int(dist), start_time), '==', close)
			assert close_time(int(controls[i]), int(dist), start_time) == close

#run file from command line to print checkpoints 
#and print the conditional statement for debugging.			
test_web_files()