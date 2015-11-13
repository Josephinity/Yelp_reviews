execfile("/Users/xiaobaby/GitHub/Yelp_reviews/QueryYelpAPI.py")
#search for restaurants from YelpAPI
def getJSON(term,location):
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--term', dest='term', default=term, type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location', default=location, type=str, help='Search location (default: %(default)s)')

    input_values = parser.parse_known_args()
    try:
        return query_api(input_values[0].term, input_values[0].location)
    except urllib2.HTTPError as error:
        sys.exit('Encountered HTTP error {0}. Abort program.'.format(error.code))
        


#control input query from here
LOCATION_LIST=['bethesda, MD','stanford, CA','Cupertino, CA','Miami, FL','Milpitas','Washington DC', 
               'Salt Lake City', 'Boston', 'Buffalo, NY']

businesses=[getJSON('japanese',loc) for loc in LOCATION_LIST]


import pandas as pd
import numpy
#allow dataframe to carry long strings
pd.set_option('max_colwidth',1024)
#filter useful variables
def createDataFrames(businesses):
    column_names=[
                u'is_claimed',u'rating',u'review_count',u'name',
                u'categories',u'location',u'url',u'is_closed',
                u'id',u'snippet_text'
              ]
    dataframes=[pd.DataFrame( [[ business[i][key] if key in column_names else '' for key in column_names]
         for i in range(0,20)],columns=column_names) for business in businesses]
    return dataframes
    
    
#seperate address info into multiple attributes
def getAddress(dataframe):
    COLUMNS = [u'name', u'rating', u'review_count', u'snippet_text', u'categories', u'is_closed', 
           u'street', u'city', u'state_code', u'postal_code', u'latitude', u'longitude',u'id',
           u'url', u'is_claimed']
    LOCATION_KEYS=['country_code','postal_code','state_code','address','coordinate','city']
    address = pd.DataFrame(
                [[dataframe.location[i][key] for key in LOCATION_KEYS] for i in range(0,20)],
                columns=[key for key in LOCATION_KEYS]
            )
    address['latitude']=[float(address['coordinate'][i]['latitude']) for i in range(0,20)]
    address['longitude']=[float(address['coordinate'][i]['longitude']) for i in range(0,20)]
    dataframe=pd.concat([df, address], axis=1)
    dataframe.rename(columns={'address':'street'},inplace=True)
    dataframe.street=dataframe.street[0][0]
    return dataframe[COLUMNS]


def mergeDataFrames(lists):
    res=lists[0]
    for i in range(1,len(lists)):
        res=res.append(lists[i],ignore_index=True)
    print('Acquired %i restaurants in total' %len(res))
    return res
    
    
#parse JSON to DFs
dataframes=createDataFrames(businesses)
#merge DFs
restaurants_by_areas=[getAddress(df)for df in dataframes]
restaurants=mergeDataFrames(restaurants_by_areas)


pprint.pprint(restaurants[:5])