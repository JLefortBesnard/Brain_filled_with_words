from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud, STOPWORDS

# most of this code was copied from https://amueller.github.io/word_cloud/

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'test_wordcloud.txt')).read()
brain_mask = np.array(Image.open(path.join(d, "brain_mask.png")))
stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=170, max_font_size=50, mask=brain_mask,
               stopwords=stopwords, contour_width=3, contour_color='#0099b8', random_state=0) 

# geneate word cloud
wc.generate(text)

# save 
wc.to_file(path.join(d, "brain.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
