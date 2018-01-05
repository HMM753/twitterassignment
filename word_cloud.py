# %matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
import csv
import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
df = pd.read_csv('./swift.csv',header=None)
df.columns = ['time','name','text','reg_time','followers','friends','status','source','location','geo_en','lang','time_zone','retweet']
text = df.text

##save to a text file
with open('taylor_text.txt', 'w') as f:
    for t in text:
        f.write(t)
        f.write('\n')

text = open( 'taylor_text.txt').read()
## Set a picture as mask
alice_mask = np.array(Image.open( "alice_mask.png")) 
stopwords = set(STOPWORDS)
## add some stopwords
stopwords.add("said")
stopwords.add('youtube')
stopwords.add('https co')
stopwords.add('https')
stopwords.add('http')
wc = WordCloud(background_color="white",width=800, height=400, max_words=2000, mask=alice_mask,
               stopwords=stopwords, colormap='Set1')
# generate word cloud
wc.generate(text)
# store to file
wc.to_file("alice.png")
##Show
plt.figure(figsize=(20,12))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")