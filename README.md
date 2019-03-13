Real-time vehicle identification system using image processing

Reqirements:
	WebCamera or Android phone with IPCamera installed
	install Python modules to run the program

Pre-Run
	Make a MySql server in on MySql Workbench
	Connect server with the program as shown in ModelDataEntering.py
	Copy the IPCamera url to Tables.py
	Create Tables on the serer by running SQL commands on the Tables.py

After you creating the tables, you can input data by running DataInput.py ---> the gui pops up

then you can retrieve data by givin input image to the database after executing DataOutput.py 

Focus your mobile phone camera to the vehicle number plate.The database will capture the photo
and process the image and identifies the vehicle
 


