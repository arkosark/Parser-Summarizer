
# coding: utf-8

# In[4]:

import bs4 as bs
import nltk
import urllib.request
import pandas as pd
import random
import re

import summarizer

#list_article_text = []
article = ''


# In[5]:

source = urllib.request.urlopen('http://www.wikihow.com/Play-Soccer')
#source = urllib.request.urlopen('http://www.wikihow.com/Play-Tennis')
soup = bs.BeautifulSoup(source,'lxml')
length= len(soup.find_all('li')) 
print(length)
article += (soup.find_all('p')[1].text + '')
for i in range(14,length-55):
    article += (soup.find_all('li')[i].text + '')
    i+=1
    

# In[6]:

bad_words = ['document.getElementById','defer.add','WH.performance.clearMarks','image1','img','var', 'rendered', 'WH.performance.mark', 'image1' 'rendered' ]
#all_words = re.findall(r"[\w']+", article)
all_words = re.findall(r"[a-zA-Z0-9,;.-:?']+", article)
article = ' '.join(filter(lambda x: x not in bad_words,  all_words))
#article
with open("Article.txt", "w") as text_file:
    print(article, file=text_file)


# In[ ]:

fs = summarizer.FrequencySummarizer()
summary = fs.summarize(article, 5)

with open("Summary.txt", "w") as text_file:
    print(summary, file=text_file)



# In[ ]:



