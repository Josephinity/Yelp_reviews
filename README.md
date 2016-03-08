# Yelp_reviews
 Sentiment Analysis of Yelp Reviews - predicting restaurant ratings with user reviews together with some other information provided by the YelpAPI



##Topic 
Opinion mining on Yelp Reviews
Backup
Influence of demographic variance and cuisine types on restaurant reviews

##Goals
Fit models to predict review ratings from review texts
Find keywords that affect the ratings of reviews most
Additional Goal
Discover the most significant aspects of opinions contained in the reviews (e.g. service, decor, food etc)

##Data Source
Restaurant Info - from Yelp API https://www.yelp.com/developers/documentation/v2/search_api
Reviews & Ratings - html from Yelp webpages

##Data Overview
50 restaurants with attributes
	[ u‘name', u'rating', u'review_count', u'snippet_text', u’categories’, u'is_closed', u'street', 		u’city', u'state_code', u'postal_code' , u'latitude', u'longitude', u'id', u'url', u’is_claimed']

21675 pieces of reviews with attributes
	[u'id', u'posted_date', u'posted_days', u'review', u’review_rating']

##Target Variable
review_rating

##Models and Tools
On data processing
	api querying
	beautiful soup 4

On statistical analysis 
	NLTK, Stanford POS_TAGGERS
	Bag of Words Representation of text
	chi.square
	n-gram detecion
	TF-idf normalization
	Naive Bayes Classifier
	RandomForests
	Variable Importance Analysis
	Cross Validation
