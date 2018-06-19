############################################
# SAP Solution Manager Support Team Finder #
############################################
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import os
import json
import watson_developer_cloud

#---- Global variables
classifier_id = '8fc87cx***-nlc-2919'
service_username = '5ab8138e-199a-41**-8ca5-6372cdc86541'
service_password = 'sWQ8p**fk1ge'
input_string = ""

def clicked():
        global classifier_id
        global input_string
        global service_username
        global service_password
        eText = st.get('1.0', END)
        input_string = eText.replace("\n"," ")

        if input_string and input_string.strip():

          if os.getenv("natural_language_classifier_classifier_id") is not None:
             classifier_id = os.getenv("natural_language_classifier_classifier_id")
             
          
          natural_language_classifier = watson_developer_cloud.NaturalLanguageClassifierV1(username=service_username,
                                                                                           password=service_password)
          classifiers = natural_language_classifier.list_classifiers()
          status = natural_language_classifier.get_classifier(classifier_id)
          if status['status'] == 'Available':
             classes = natural_language_classifier.classify(classifier_id, input_string)

          W_answer="We recommend contacting the Support Team >>> "+json.dumps(classes["top_class"], indent=2)
          Label(mainwin, text=W_answer).grid(row=2, column=1)

def cleared():
       global mainwin
       Label(mainwin, text="Answer: ").grid(row=2, column=0)
       Label(mainwin, text=" "[:1]*100).grid(row=2, column=1)
       st.delete('1.0', END)

if __name__ == '__main__':
  mainwin = Tk()
  Label(mainwin, text="Watson - Natural Language Classifier - Find SAP Support Team").grid(row=0, column=1)
  Label(mainwin, text="Incident description").grid(row=1, column=0)
  st = ScrolledText(mainwin, height=5); st.grid(row=1, column=1)
  Button(mainwin, text="Find", command=clicked).grid(row=1, column=2, sticky="EW")
  Button(mainwin, text="Clear", command=cleared).grid(row=2, column=2, sticky="EW")
  Button(mainwin, text="Exit", command=sys.exit).grid(row=3, column=0, columnspan=3, sticky="EW")
  Label(mainwin, text="Answer:  ").grid(row=2, column=0)
 
mainwin.mainloop()