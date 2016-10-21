"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments. 
#

#List of lists.
BREVET_TABLE = [[200, 15, 34],[400, 15, 32],[600, 15, 30],\
[1000, 11.428, 28],[1300, 13.333, 26]]



def open_time( control_dist_km, brevet_dist_km, brevet_start_time ):
	"""
	Args:
	   control_dist_km:  number, the control distance in kilometers
	   brevet_dist_km: number, the nominal distance of the brevet in kilometers,
		   which must be one of 200, 300, 400, 600, or 1000 (the only official
		   ACP brevet distances)
	   brevet_start_time:  An ISO 8601 format date-time string indicating
		   the official start time of the brevet
	Returns:
	   An ISO 8601 format date string indicating the control open time.
	   This will be in the same time zone as the brevet start time.
	"""
	brevet_list = [(200,15,34),(400,15,32),(600,15,30),(1000,11.428,28),(1300,13.333,26)]
	done = False
	
	dt = 0
	i = 0
	time = 0
	prev = 0
	control = control_dist_km
	
	while(not done):
	
		if (dt + control) <= brevet_list[i][0]:
			time += control / brevet_list[i][1]
			done = True
		else:
			prev = brevet_list[i][0] - prev
			time += prev/brevet_list[i][1]
			i += 1
			control -+ prev
			dt += prev

	print('time in hours:', time)
	min = time % 1
	hr = time - min
	min = round(min * 60) 
	
	brevet_start_time = brevet_start_time.replace(hours =+ hr)
	brevet_start_time = brevet_start_time.replace(minutes =+ min)
	
	return brevet_start_time.isoformat()

def close_time( control_dist_km, brevet_dist_km, brevet_start_time ):
	"""
	Args:
	   control_dist_km:  number, the control distance in kilometers
	   brevet_dist_km: number, the nominal distance of the brevet in kilometers,
		   which must be one of 200, 300, 400, 600, or 1000 (the only official
		   ACP brevet distances)
	   brevet_start_time:  An ISO 8601 format date-time string indicating
		   the official start time of the brevet
	Returns:
	   An ISO 8601 format date string indicating the control close time.
	   This will be in the same time zone as the brevet start time.
	"""
	return arrow.now().isoformat()


