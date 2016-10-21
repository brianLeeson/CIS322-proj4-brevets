"""
Nose Tests for project 4
"""

from acp_times import *

import arrow
#ISO format: YYYY-MM-DD HH:mm:ss
ISO_START = '2017-01-01 00:00:00'

# data_base [dist(km), 
# [[control(km), oTime(min), cTime(min)],...], 
# ISO_START]
data_base = [200, /
[[60, 106, 240], [120, 212, 480], [175, 309, 700], [205, 353, 800]], /
ISO_START]

def test_web_example1(data_base):
	#Example 1
	dist = data_base[0]
	pairs = data_base[1]
	start = data_base[2]
	
	for pair in pairs:
		control = pair[0]
		oTime = pair[1]
		open = arrow.get(start).replace('hour' =+ (round(oTime/60))).isoformat()
		assert open_time(control, control) == open
	
	for pair in pairs:
		control = pair[0]
		cTime = pair[2]
		close = arrow.get(start).replace('hour' =+ (round(cTime/60))).isoformat()
		assert open_time(control, control) == close
	
	
	assert open_time(60, 200, ISO_START) == '2017-01-01 01:46:00'
	assert open_time(120, 200, ISO_START) == '2017-01-01 03:32:00'
	assert open_time(175, 200, ISO_START) == '2017-01-01 05:09:00'
	assert open_time(205, 200, ISO_START) == '2017-01-01 05:53:00'
	
	assert close_time(60, 200, ISO_START) == '2017-01-01 04:00:00'
	assert close_time(120, 200, ISO_START) == '2017-01-01 08:00:00'
	assert close_time(175, 200, ISO_START) == '2017-01-01 011:40:00'
	assert close_time(205, 200, ISO_START) == '2017-01-01 013:30:00'
	
def test_web_example2():
	#Example 2
	
	
	
	#Example 3