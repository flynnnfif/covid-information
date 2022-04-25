#coding=utf-8
import re
import requests
from bs4 import BeautifulSoup


#re
re_con = ("(?P<num_con>昨日新增本土确诊病例.*?例)")
re_num = ("(currentConfirmedCount.{2}[0-9]+).*?(confirmedCount.{2}[0-9]+).*?(suspectedCount.{2}[0-9]+).*?(curedCount.{2}[0-9]+).*?(deadCount.{2}[0-9]+).*?(seriousCount.{2}[0-9]+).*?(suspectedIncr.*?[0-9]+).*?(currentConfirmedIncr.*?[0-9]+).*?(confirmedIncr.*?[0-9]+).*?(curedIncr.*?[0-9]+).*?(deadIncr.*?[0-9]+).*?(seriousIncr.*?[0-9]+).*?(yesterdayConfirmedCountIncr.*?[0-9]+).*?(yesterdaySuspectedCountIncr.*?[0-9]+).*?(highDangerCount.*?[0-9]+).*?(midDangerCount.*?[0-9]+)")

class covid_info():
    def __init__(self,c,d):
        self.cityname=c
        self.date=d
        self.url='http://api.tianapi.com/ncov/index?key=53d35b1cd0b2058b8506e165bba57f35'
        self.bs = BeautifulSoup(requests.get(self.url).content,"lxml")
        self.bs=self.bs.p.string
        self.string=str(self.bs)
        
        covid_contry=re.search(re_con,self.string)
        self.num = re.search(re_num,self.string)
        self.con=covid_contry[0]

    def country(self):
        ret_coun = '现存确诊'+self.num.group(1)+'\n无症状'+self.num.group(6)+'\n新增境外输入'+self.num.group(7)+'\n相比昨天现存确诊'+self.num.group(8)+'\n新增确诊'+self.num.group(9)+'\n新增治愈'+self.num.group(10)+'\n高风险地区'+self.num.group(15)+'\n中风险地区'+self.num.group(16)
        return(ret_coun)
        
    def city(self,cityname):
        self.cityname=cityname
        re_city1 = "本土病例.+?("+self.cityname+"[0-9]+.)"
        re_city2 = "title\W{3}"+self.cityname+".*?summary\W{3}(.*?)\""
        city_num = research(re_city1,self.string)
        city_news = research(re_city2,self.string)
        return(city_num+'\n简报：'+city_news)

    def area(self,cityname):
        self.cityname=cityname
        re_midarea = "mid|\""+self.cityname+"\w*\"|high"
        return(find_area(re_midarea,self.string))

def find_area(area,string):
    area_re = re.findall(area,string)
    if area_re==None:
        return("None")
    else:
        return(area_re)

def research(city,string):
    city_re = re.search(city,string,re.DOTALL)
    if city_re==None:
        return("None")
    else:
        city_num = city_re[1]
        return(city_num)

class covid_table():
    def __init__(self):
        self.url0='http://www.gov.cn/fuwu/fwtj.htm'
        bs = BeautifulSoup(requests.get(self.url0).content,"lxml")
        news = bs.body.div.div.div
        news_list = news.find(class_='news_box')
        news_list = news_list.div.ul
        news_url = dict()
        news_find = news_list.find_all("a",string=re.compile("新型冠状病毒肺炎疫情最新情况"))
        for i in news_find:
            news_url[i.string.strip()] = re.search("\".*?\"",str(i))[0].strip("\"")
        #get
        url_site = 'http://www.gov.cn/'
        self.numc_list = []
        self.numl_list = []
        self.date = []
        for n,l in news_url.items():
            bs = BeautifulSoup(requests.get(url_site+l).content,"lxml")
            page_num = str(bs.find(class_='pages_content'))
            self.date.append(re.search('(\d*?月\d*?)日',page_num).group(1))
            self.numc_list.append(int(re.search('新增确诊病例(.*?)例',page_num).group(1)))
            self.numl_list.append(int(re.search('新增无症状感染者(.*?)例',page_num).group(1)))


if __name__=='__main__':
    covid_result=covid_info(0,0)
    covid_result.area('吉林')
    c_table=covid_table()
