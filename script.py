import urllib
from bs4 import BeautifulSoup
import csv
 
list = ["textilesmanmade/adityabirlanuvo/ABN01","infrastructuregeneral/adaniportsspecialeconomiczone/MPS","bankspublicsector/allahabadbank/AB15","constructioncontractingrealestate/anantraj/ARI","autolcvshcvs/ashokleyland/AL"]
 
 
 
 
 
 
 
 
book = csv.writer(open('StockInfo.csv','wb'))
book.writerow(["Name","Price","Absolute Increase","Percent Increase"])
i = 0
 
while i<len(list):
        url = "http://www.moneycontrol.com/india/stockpricequote/" + list[i]
        htmlfile = urllib.urlopen(url)
        soup = BeautifulSoup(htmlfile)
        price = soup.find("span",id="Nse_Prc_tick",class_="PA2")
        price2 = price.find("strong").string
        print price2
        increase = soup.find("div",class_="FL gL_13 PT15")
        increase2 = increase.find("span").find("strong").string
        print increase2
        #print increase.next_sibling
        percent2 = increase.find("span").next_sibling
        print percent2
        name2 = soup.find("h1",class_="b_42").string

        print i
       
        book.writerow([name2,price2,increase2,percent2])
       
        i+=1