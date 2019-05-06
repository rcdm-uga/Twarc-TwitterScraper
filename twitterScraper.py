from twarc import Twarc
import os

'''
@author Caleb Crumley

THIS PYTHON SCRIPT WILL CREATE A NEW DIRECTORY OF TXT FILES 
THAT CONTAIN TWEETS PERTAINING TO THE TOPICS OF YOUR CHOICE.
THE ONLY NEEDED TO USE THIS, IS MAKING SURE YOU HAVE THE TWO 
LIBRARIES ABOVE (twarc and os) INSTALLED ON YOUR MACHINE.


ONCE YOU'VE MADE YOUR DEVELOPMENT APP WITH TWITTER (http://dev.twitter.com) 
AND PLACE THESE KEYS PROVIDED TO YOU BELOW TO GET ACCESS TO TWITTER'S API.
'''
consumer_key = ''              
consumer_secret = ''           
access_token = ''              
access_token_secret = ''       

'''
YOU ARE ALLOWED TO SPECIFY THE LANGUAGE OF THE TWEETS AS WELL. 
en: ENGLISH
es: Spanish
ja: Japanese
de: German
https://developer.twitter.com/en/docs/developer-utilities/supported-languages/api-reference/get-help-languages.html
'''

language = 'en'            


'''
THE LIST BELOW, topic_list, IS WHERE YOU WILL PLACE ALL OF THE TOPICS
YOU WOULD LIKE TO SEARCH, INCLUDING HASHTAGS.

=============================================================
=====================SUGGESTION==============================
=============================================================

I WILL ADD THAT TWITTER ONLY ALLOWS 180 REQUEST PER 15 MINUTES, SO 
BIG TOPICS WILL TAKE A WHILE. SO I SUGGEST ONLY DOING 2 OR 3 TOPICS 
AT A TIME THAT WAY IF ONE IS TAKING A WHILE, YOU CAN STOP THE PROGRAM 
AND START WITH THE NEXT ONE. IF YOU WANT ALL, YOURE JUST GONNA HAVE TO 
WAIT UNTIL IT STOPS. 
'''

topic_list = ['replace with one', 'or more topics all separated by commas', 'and with qoutations']

'''
NAME THE TWEET DOCUMEsNTS THAT YOU 
WOULD LIKE THE TWEETS TO BE DUMPED IN
'''

file_dir = 'tweet_files'
if not os.path.isdir(file_dir):
    os.mkdir(file_dir)

'''
HERE IS WHERE THE TWITTER SCRAPING STARTS. PLEASE DO NOT TOUCH 
ANTHING BELOW. IF YOU WANT TO CHANGE THE TWARC FUNCTION, YOU MAY DO SO AS
LONG AS YOU MAKE SURE THE CORRESPONDING PARAMETERS ARE CHANGED.
'''
t = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)

for topic in topic_list:
    
            
    #Removing and spaces and hashtags to name output file
    temp_str = topic.replace('#','')
    temp_str = temp_str.replace(' ','_')
    file_name = temp_str + '.txt'
    file_write = os.path.join(file_dir,file_name)
    print('Started scraping tweets for the topic {0}'.format(topic))
    
    #writing to output file
    with open(file_write,'w') as writefile:    
        for tweet in t.search(topic ,lang = language):
            line = tweet['full_text']
            
            #writing tweet to file
            writefile.write(line)
        print('Just finished scraping tweets for the topic {0}'.format(topic))