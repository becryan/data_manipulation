import urllib2
from bs4 import BeautifulSoup

#from the website : Health Engine
quote_page="https://healthengine.com.au/find/bulk-billing-gp/VIC/Page-"

data=[]
names=[]
addresses=[]
suburbs=[]

for qp in range(0,45):
    this_page=quote_page+str(qp)
    webpage=urllib2.urlopen(this_page)
    soup=BeautifulSoup(webpage,'html.parser')

    doctors_container=soup.find_all("div",attrs={'class':'search-main-dets'})
    print qp,'page scraped'

    for indiv_doctor in doctors_container:
    
        if indiv_doctor.find('h2',attrs={'class': 'search-main-title'}) is not None:
        
            name=indiv_doctor.a.text
            names.append(name.strip())
        
            suburb=indiv_doctor.find('h3',attrs={'class': 'search-suburb'})
            if suburb is None:
                suburbs.append("")
            else:
                suburbs.append(suburb.text.strip())
        
            address=indiv_doctor.find('div',attrs={'class':'search-addie'})
            addresses.append(address.text.strip())


import pandas as pd

test_df=pd.DataFrame({'name':names,'address':addresses,'suburb':suburbs})


#print test_df['address']

write=pd.ExcelWriter('bulk_billed_list1.xlsx')
test_df.to_excel(write,'Sheet1')
