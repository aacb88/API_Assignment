import urllib2, json
import re

#setting up search results for Benghazi
SEARCH_TEXT = 'Benghazi'
BEGIN = False
END = False
POST_BEGIN = False
POST_END = False
#setting up search results under specific case number
CASE = 'F-2014-20439'
COLLECTION = False
PAGE = '1'
START = '1'
LIMIT = '500'
def clean_json(json):
    '''
    Turn dirty State Department JSON into clean JSON.
    '''
    return re.sub(r'new Date\(.*?\)', '""', json)

# Apply the above function like so ...

dirty_json = urllib2.urlopen('https://foia.state.gov/searchapp/Search/SubmitSimpleQuery?searchText=%s&beginDate=%s&endDate=%s&postedBeginDate=%s&postedEndDate=%s&caseNumber=%s&collectionMatch=%s&page=%s&start=%s&limit=%s' % (SEARCH_TEXT, BEGIN, END, POST_BEGIN, POST_END, CASE, COLLECTION, PAGE, START, LIMIT)).read()
valid_json = clean_json(dirty_json)
data = json.loads(valid_json)

#printing PDF links
for link in data['Results']:
    print link['pdfLink']
