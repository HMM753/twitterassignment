# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn
import csv
import pandas as pd
import numpy as np
from collections import Counter

df = pd.read_csv('./swift.csv',header=None)

with open('./swift.csv') as f:
    line = f.readline()

df.columns = ['time','name','text','reg_time','followers','friends','status','source','location','geo_en','lang','time_zone','retweet']

df.sort_values(['retweet'],ascending=False).head(10)
#top tweeters
a = df.name
a.unique()
c = Counter(a)
top_twitter = c.most_common()[:10]
print(top_twitter)
#geo_engaged
g=df.geo_en
g.unique()
gg=Counter(b)
ggg=gg.most_common()
print(ggg)
# local distributon
lo=df.location
lo.unique()
loc=Counter(lo)
loca=loc.most_common()[:100]
print(loca)