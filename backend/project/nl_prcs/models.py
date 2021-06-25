from django.db import models
from konlpy.corpus import kobill
from icecream import ic
from project.m_common.models import FileDTO, Reader
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc
import nltk
from konlpy.tag import Okt; t = Okt()


class Service(Reader):

    def __init__(self):
        self.f = FileDTO()
        self.r = Reader()

    def alice_plt_show(self):
        f = self.f
        r = self.r
        f.context = './data/'
        f.imgfile = '09. alice_mask.png'
        path = "c:/Windows/Fonts/Arial.ttf"
        alice_mask = r.img(f)
        if platform.system() == 'Darwin':
            rc('font', family='AppleGothic')
        elif platform.system() == 'Windows':
            font_name = font_manager.FontProperties(fname=path).get_name()
            rc('font', family=font_name)
        else:
            print('Unknown system... sorry~~~~')
        plt.figure(figsize=(8, 8))
        plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
        plt.axis('off')
        plt.show()

    def alice_wordcloud(self):
        f = self.f
        r = self.r
        f.context = './data/'
        f.textfile = '09. alice.txt'
        f.imgfile = '09. alice_mask.png'
        text = r.text(f)
        alice_mask = r.img(f)
        stopwords = set(STOPWORDS)
        stopwords.add("said")
        wc = WordCloud(background_color='white', max_words=2000, mask=alice_mask,
                       stopwords=stopwords)
        wc = wc.generate(text)
        # ic(wc.words_)
        plt.figure(figsize=(12, 12))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.show()

    def tokens_doc_ko(self):
        f = self.f
        r = self.r
        f.context = ''
        f.textfile = '1809890.txt'
        files_ko = kobill.fileids()
        doc_ko = r.doc_text(f)
        tokens_ko = t.nouns(doc_ko)
        ic(tokens_ko)

    def _doc_ko(self):
        pass



if __name__ == '__main__':
    s = Service()
    # s.alice_plt_show()
    # s.alice_wordcloud()
    s.tokens_doc_ko()


