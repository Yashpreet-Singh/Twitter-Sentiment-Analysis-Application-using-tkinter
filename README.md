# Twitter-Sentiment-Analysis-using-tkinter
We designed an application which performs sentiment analysis on Twitter on tweets that matched particular keywords provided by the user. For example if a user is interested in performing sentiment analysis on tweets which contain the word “Obama” he / she will enter that keyword and the application will perform the appropriate sentiment analysis and display the results for the user in pie chart in positive,negative or neutral sentiment.

There can be two approaches to sentiment analysis.
1. Lexicon-based methods
2. Machine Learning-based methods.
In this project, we will be using a Lexicon-based method.
Lexicon based methods define a list of positive and negative words, with a valence — (eg ‘nice’: +2, ‘good’: +1, ‘terrible’: -1.5 etc). The algorithm looks up a text to find all known words. It then combines their individual results by summing or averaging. 

Installing Dependencies:

1)pip install tweepy

This package will be used for handling the Twitter API.
Tweepy supports OAuth authentication. Authentication is handled by the tweepy.OAuthHandler class.An OAuthHandler instance must be created by passing a consumer token and secret.
On this auth instance, we will call a function set_access_token by passing the access_token and access_token_secret.Finally, we create our tweepy API instance by passing this auth instance into the API function of tweepy.
              
2)pip install textblob

This package will be used for the sentiment analysis.
TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

3)pip install matplotlib

This package is used for plotting graphs.

Matplotlib is a plotting library for the Python programming language . It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK+.
The sentiment property returns a named tuple of the form Sentiment (polarity, subjectivity). The polarity score is a float within the range [-1.0, 1.0] where 1.0 reflects the sentence being positive and -1.0 reflects the sentence being negative.
