# Project 4:  Brevet time calculator with Ajax
Reimplement the RUSA ACP control time calculator with flask and ajax
AUTHOR: Brian Leeson, bel@cs.uoregon.edu

## Overview ACP controle times

Controls are points where a rider must obtain proof of passage,
and control times are the minimum and maximum times by which the 
rider must arrive at the location.   

The algorithm for calculating controle times is described at
https://rusa.org/octime_alg.html.

We are essentially replacing the calculator at
https://rusa.org/octime_acp.html.

## RUNNING THE APPLICATION
Do NOT enter the virtual enviroment.

Deployment should work "out of the box" with this command sequence:
sudo apt-get install python3-venv  
git clone <gitURL>  
cd to the cloned repository  
make configure  
make run  

The default port is 5000. If your are on your own machine connect at localhost:5000. 
If the server is running another machine connect at <OtherMachineIP>:5000.
 
## TESTING THE APPLICAITON
Test this server by following the RUNNING instructions and attempt to connect to the server.
From there you may enter values in the Km or Miles fields to calulate the controls.

To run automated tests:
	make test

To add your own test cases:
	Go to: https://rusa.org/octime_acp.html
	Use the brevet calculator to calculate an opening and closing time text file.
	Save file as a complete webpage in the tests folder


