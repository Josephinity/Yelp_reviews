execfile("/Users/xiaobaby/GitHub/Yelp_reviews/YelpJSONtoDataFrame.py")
#returns a dictionary of (restaurant.id) : (df)(all reviews of restaurant.id) pairs
def reviewLists(restaurants):
    res=pd.DataFrame(columns=['id','posted_date','review','review_rating'])
    for i in range(0,len(restaurants)):
        res = res.append(getReviews(restaurants[i:i+1]),ignore_index=True)
    res['posted_days']=[timeFromNow(date) for date in res.posted_date]
    return res
    
    
#get reviews from all restaurant urls
def getReviews(restaurant):
    print('restaurant id is '+restaurant.id.values[0])
    print('review count :%i ,review rating: %i' %(restaurant.review_count,restaurant.rating))
    df=pd.DataFrame(columns=['id','review','review_rating','posted_date'])
    count=0
    while count<int(restaurant.review_count):  
        url=restaurant.url.values[0]+'?start=%i'%count
        print(url)
        response = urllib2.urlopen(url)
        html = response.read()
        tmp = htmlToDataFrame(html)
        tmp['id'] = restaurant.id.values[0]
        df = df.append(tmp,ignore_index=True)
        count+=20
    return df
    
    
#process html files 
from bs4 import BeautifulSoup as bs
def htmlToDataFrame(html):
    soup = bs(html, 'html.parser')
    #get rating list
    page1_ratings=[float(r.get('content')) for r in soup.find_all(itemprop='ratingValue')[1:]]
    #get review list
    page1_reviews=soup.find_all('p',itemprop='description')
    page1_dates=[str(s)[15:25] for s in soup.find_all('meta',itemprop='datePublished')]
    return pd.DataFrame({"review":stripHTMLTags(page1_reviews)
                         ,"review_rating":page1_ratings
                         ,"posted_date":page1_dates})
                         
#strip html tags
import re
def stripHTMLTags(reviews):
    res = [str(review).replace('<p itemprop="description" lang="en">','').replace('<br>',' ')
            .replace('</br>','').replace('</p>',' ').replace('\xc2\xa0',' ') 
            for review in reviews]
    return [re.sub('\!+','!',s) for s in res]
    
    
#get post_date from now in days
from datetime import datetime
def timeFromNow(date):
    d0=datetime.strptime(date, "%Y-%m-%d")
    return (datetime.now()-d0).days
    

#control which restaurnts to query for reviews from here
reviews=reviewLists(restaurants[1:2])
pprint.pprint(reviews)