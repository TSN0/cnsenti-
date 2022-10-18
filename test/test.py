import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)
from cnsenti import Sentiment

senti = Sentiment(pos='test/pos.txt',  #正面词典txt文件相对路径
                  neg='test/pos.txt',  #负面词典txt文件相对路径
                  merge=True,  #merge=True融合自定义词典和cnsenti自带词典；merge=False只使用自定义词典
                  encoding='utf-8')      #两txt均为utf-8编码

test_text = '这家公司是行业的引领者，是中流砥柱。'
result1 = senti.sentiment_count(test_text)
result2 = senti.sentiment_calculate(test_text)
print('sentiment_count',result1)
print('sentiment_calculate',result2)