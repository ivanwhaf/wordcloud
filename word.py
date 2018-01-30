import jieba
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
import itchat
import re

text_path='text.txt'
image_path='3.jpg'

def get_wechat_signature_text():
    itchat.auto_login()
    friends = itchat.get_friends(update=True)
    siglist = []
    for i in friends:
        signature = i["NickName"].strip().replace('span','').replace('class','').replace('emoji','').replace('\n','')
        rep = re.compile("1f\d+\w*|[<>/=]")
        signature = rep.sub("", signature)
        if(signature!=""):
            siglist.append(signature)
    text = "".join(siglist)
    print(text)
    return text
    
def get_file_text():
    text=open(text_path).read()
    return text

def make_wordcloud(text):
    wordlist=jieba.cut(text)
    list_split=" ".join(wordlist)
    print(list_split)
    pic=np.array(Image.open(image_path))
    wd=WordCloud(mask=pic,background_color='white', max_font_size=52,max_words=150,font_path = 'yy.TTF',random_state = 150).generate(list_split)
    #image_colors = ImageColorGenerator(pic)
    #plt.imshow(wd.recolor(color_func=image_colors))
    plt.imshow(wd,interpolation='bilinear')
    plt.axis("off")
    plt.show()

def main():
    #text=get_wechat_sigature_text()
    text=get_file_text()
    make_wordcloud(text)

if __name__=='__main__':
    main()
