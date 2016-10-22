"""
Nose Tests for project 4
"""

from acp_times import *
import arrow
import os

#ISO format: YYYY-MM-DD HH:mm:ss
ISO_START = '2017-01-01 00:00:00'
#year is 2016 by default. this is a problem if leap year or not
YEAR = '2016'
'''
TEST_DICT =  {filename:{dist: 200, \
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
	
	USE: Go to: https://rusa.org/octime_acp.html
	Use the brevet calculator to calculate and opening and closing time text file.
	Save file in the tests folder
	In the command line type 'make test' (only for unix machines)
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
					checkpoints['opens'].append(YEAR + '/' + line[2] + ' ' + line[3])
				else:
					#add the closing time
					checkpoints['closes'].append(YEAR + '/' + line[1] + ' ' + line[2])
			
		#save in the global dict
		TEST_DICT[filename] = checkpoints
		
		
def test_web_example1():
	#Example 1
	#just in case
	'''
	assert open_time(60, 200, ISO_START) == '2017-01-01 01:46:00'
	assert open_time(120, 200, ISO_START) == '2017-01-01 03:32:00'
	assert open_time(175, 200, ISO_START) == '2017-01-01 05:09:00'
	assert open_time(205, 200, ISO_START) == '2017-01-01 05:53:00'
	
	assert close_time(60, 200, ISO_START) == '2017-01-01 04:00:00'
	assert close_time(120, 200, ISO_START) == '2017-01-01 08:00:00'
	assert close_time(175, 200, ISO_START) == '2017-01-01 011:40:00'
	assert close_time(205, 200, ISO_START) == '2017-01-01 013:30:00'
	'''
	
def test_web_files():
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
			open = arrow.get(opens[i], 'YYYY/MM/DD HH:mm').isoformat()
			print('open')
			print(open_time(int(controls[i]), int(dist), start_time), '==', open)
			#assert open_time(int(dist), int(controls[i]), start_time) == open
			print(open_time(dist, controls[i], start_time) == open)
			
			close = arrow.get(closes[i], 'YYYY/MM/DD HH:mm').isoformat()
			print('close')
			print(close_time(int(controls[i]), int(dist), start_time), '==', close)
			#assert close_time(int(dist), int(controls[i]), start_time) == close
			print(close_time(dist, controls[i], start_time) == close)

#run file from command line to print checkpoints			
test_web_files()