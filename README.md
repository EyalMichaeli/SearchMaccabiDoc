# SearchMaccabiDoc
An API to search for, and set a reminder (once the doctor has an earlier appointment then is available now) to a Maccabi (healthcare insurance, Israel) Doctor. 
* It doesn't support orders because it assumes there is already an appointment booked, and Maccabi doesn't let you order 2 appointments at a time(and we won't cancel because we need to make sure you're available at this date).
* The reminder will be sent via telegram/slack
* I'll might extend this with more multiple cities for a single doctor, multiple doctors, etc.

## Environment 
* Currently, tested only on Mac - for self use only
* Need to have python installed
* And, install requirements, as usual, by: pip install -r requirements.txt

## What you need to do: 
1. Open config.json
2. Insert your Maccabi online ID & password 
3. Insert your doc last, first name and his city
4. Insert the earliest appointment with the doctor (that I assume you already booked)
5. Run the program
