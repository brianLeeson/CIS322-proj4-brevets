"""
Nose Tests for project 4
"""

from acp_times import *
import arrow
import os

# data_base [dist(km), 
# [[control(km), oTime(min), cTime(min)],...], 
# ISO_START]

#ISO format: YYYY-MM-DD HH:mm:ss
ISO_START = '2017-01-01 00:00:00'
#year is 2016 by default
YEAR = 2016
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
	processes everything in the test folder into value dictionary
	stores value in global TEST_DICT. key is filename.
	'''
	for filename in os.listdir(". /tests"):
		value = {}
		
		with open(filename, 'r') as f:
			for i in range(6):
				f.readline()
			read_data = f.readlines()

		#Get the brevet dist. Stores in dict.
		value['dis'] = read_data[0].split('>')[6].split('km')[0]
		value['controls'] = []
		value['opens'] = []
		value['closes'] = []
		
		for i in range(3, len(read_data)):
			line = len(read_data[i].strip())
			#if it has a length
			if (len(line) and (line[0] != '<')):
				line.split()
				if isinstance(line[0][0], int):
					value['controls'].append(line[0].split('km')[0])
					value['opens'].append(YEAR + '/' + line[2] + ' ' + line[3]
				else:
					value['closes'].append(YEAR + '/' + line[1] + ' ' + line[2]
			
		TEST_DICT[fileneame] = value
		
		
def test_web_example1(data_base):
	#Example 1
	#just in case
	assert open_time(60, 200, ISO_START) == '2017-01-01 01:46:00'
	assert open_time(120, 200, ISO_START) == '2017-01-01 03:32:00'
	assert open_time(175, 200, ISO_START) == '2017-01-01 05:09:00'
	assert open_time(205, 200, ISO_START) == '2017-01-01 05:53:00'
	
	assert close_time(60, 200, ISO_START) == '2017-01-01 04:00:00'
	assert close_time(120, 200, ISO_START) == '2017-01-01 08:00:00'
	assert close_time(175, 200, ISO_START) == '2017-01-01 011:40:00'
	assert close_time(205, 200, ISO_START) == '2017-01-01 013:30:00'

	
def test_web_files():
	process()
	
	for filename in TEST_DICT:
		value = TEST_DICT[filename]
		
		dist = value['dist']
		controls = value['controls']
		opens = value['opens']
		closes = value['closes']
		
		start_time = opens[0]
		
		for i in range(1, len(controls)):
			open = arrow.get(opens[i], 'YYYY/MM/DD HH:mm').isoformat()
			assert open_time(dist[i], control[i], start_time) == open
			
			close = arrow.get(closes[i], 'YYYY/MM/DD HH:mm').isoformat()
			assert open_time(dist[i], control[i], start_time) == close
		