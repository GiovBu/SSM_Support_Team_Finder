# SSM_Support_Team_Finder
SAP Solution Manager Support Team Finder Python App

This app is developed in Python and allows you to query the Watson Natural Language Classifier (NLC) service in the IBM Cloud.
App tested on: Windows 7 Professional Service Pack 1, macOs High Sierra 10.13.3, Ubuntu 14.04 and 17.10. 

The app has also been tested on Android environment but using the Python Kivy library for the management of the graphical interface. Kivy is an open source software library for the rapid development of applications with new user interfaces, such as multi-touch apps.

Run the app required to enter the text of an SAP ticket/incident and press the "Find" button.
The app contacts the Watson NLC service, checking first that it is in "Available" status. The query will return a class whose name is the reference SAP module for the ticket (eg MM CO, FI, BW and so on).
It is shown the message "We recommend contacting the Support Team >>" followed by the name of the reference SAP module

The "Clear" button allows you to clear the text box for a new text.
The "Exit" button ends the execution of the app.

REQUIREMENTS

A) Watson Requirements

1) Create an instance of the NLC Watson service:

   * Log in to IBM Cloud.
   * Create an instance of the service:
   * Click on Create Resource.
   * In the IBM Cloud Catalog, select the Watson service you want to use. For example, select the Conversation service.
   * Type a unique name for the service instance in the Service name field. For example, type my-service-name. Leave the default
        values for the other options.
   * Click Create.
2) Copy your credentials from the Manage page. On the "Manage" page, you will see a Credentials pane.
3) create and train a classifier. Prepare your data to train a classifier (suggested upload a csv file)

B) Python Requirements (OS: Windows 7 Service Pack 1 and Python 3.4.4)
   Install in your laptop Python version 2.7, 3.4 or 3.5 and the Python client library "watson-developer-cloud"

   Dependencies:   
   *    asn1crypto==0.24.0
   *    certifi==2018.1.18
   *    cffi==1.11.4
   *    chardet==3.0.4
   *    cookies==2.2.1
   *    cryptography==2.1.4
   *    Cython==0.28.2
   *    Django==2.0.3
   *    docutils==0.14
   *    idna==2.6
   *    image==1.5.19
   *    Kivy==1.10.1.dev0
   *    Kivy-examples==1.10.1.dev0
   *    Kivy-Garden==0.1.4
   *    kivy.deps.angle==0.1.6
   *    kivy.deps.gstreamer==0.1.12
   *    kivy.deps.sdl2==0.1.17
   *    Pillow==5.0.0
   *    pycparser==2.18
   *    pygame==1.9.3
   *    Pygments==2.2.0
   *    pyOpenSSL==17.5.0
   *    pysolr==3.7.0
   *    python-dateutil==2.6.1
   *    pytz==2018.3
   *    requests==2.18.4
   *    responses==0.8.1
   *    six==1.11.0
   *    urllib3==1.22
   *    watson-developer-cloud==1.0.2
   
C) Run the Python App

   * Run a Python script under Windows with the Command Prompt
     - C:\Python27\python.exe C:\Users\Username\Desktop\my_python_script.py
   
   * Run a Python Script Under Mac, Linux, BSD, Unix, etc
     - You must then make the script executable, using the following command
       
       chmod +x my_python_script.py
     
     - You can then run a program by invoking the Python interpreter manually as follows
       
       python firstprogram.py


   




