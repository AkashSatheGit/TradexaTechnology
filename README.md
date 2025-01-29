# TradexaTechnology
Hello . This is a Guide to run this assignment.

First , Set up django project then do following steps.

1 . Run command :
	
 	python manage.py runserver

You can see there is a no data in tables by clicking options there.

2 . Then come to command prompt and fire command :

	python manage.py insert_data

   This command add all data at once

3. Then run command : python manage.py runserver
	
	And check data will be added in tables.


NOTE: If you try to insert the same data again, you will facenan error due to primary key.

	To avoid this, use the Delete button provided in the Systam . This will remove all existing data from tables. 

	After deleting the data, repeat Step 2 and Step 3 to insert fresh data again.
