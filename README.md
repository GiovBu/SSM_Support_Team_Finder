# SSM_Support_Team_Finder
SAP Solution Manager Support Team Finder Python App

This app is developed in Python and allows you to query the Watson Natural Language Classifier (NLC) service in the IBM Cloud.
App tested on: Windows 7 Professional Service Pack 1, macOs High Sierra 10.13.3, Ubuntu 14.04 and 17.10. 

The app has also been tested in the Android environment but using the Python Kivy library for the management of the graphical interface. Kivy is an open source software library for the rapid development of applications with new user interfaces, such as multi-touch apps.

Run the app required to enter the text of an SAP ticket/incident and press the "Find" button.
The app contacts the Watson NLC service, checking first that it is in "Available" status. The query will return a class whose name is the reference SAP module for the ticket (eg MM CO, FI, BW and so on).
It is shown the message "We recommend contacting the Support Team >>" followed by the name of the reference SAP module

The "Clear" button allows you to clear the text box for a new text.
The "Exit" button ends the execution of the app.