#!/usr/bin/env python
# coding: utf-8

# In[70]:


from bs4 import BeautifulSoup
import requests, sys


# In[101]:


'''
爬虫练习 
笔趣网下载小说
'''

class downloader(object):
    def __init__(self):
        self.target = 'https://www.biqukan.com/0_790/'
        self.server = 'http://www.biqukan.com/'
        self.names = [] #章节名
        self.urls = [] #链接
        self.nums = 0 #章节数
        
        '''
        获取章节链接
        Parameters:
            None
        Returns:
            None
        '''
    
    def get_url(self):
        req = requests.get(url = self.target)
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]))
        a = a_bf.find_all('a')
        self.nums = len(a[15:])                                #剔除不必要的章节，并统计章节数
        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))
                
        '''
        获取章节内容
        Parameters:
            None
        Return:
            contenr - 章节内容
        '''
    def get_download_content(self, target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', class_ = 'showtxt')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts
        
        '''
        写入文件
        Parameters:
            name - 章节名
            path - 当前路径下，小说保存名称
            content - 章节内容
        '''
    def writer(self,name,path,content):
        writer_flag = True
        with open(path,'a',encoding = 'utf-8') as f:
            f.write(name + '\n')
            f.writelines(content)
            f.write('\n\n')


# In[102]:


if __name__ == '__main__':
    spider = downloader()
    spider.get_url()
    print('download start')
    for i in range(spider.nums):
        spider.writer(spider.names[i],'yuanzun.txt',spider.get_download_content(spider.urls[i]))
        sys.stdout.write('downloading:%.3f%%'% float(i/spider.nums)+'\r')
        sys.stdout.flush()
    print('download finish')


# In[ ]:





# In[ ]:




