import requests
import json
import re
import uuid
import time
import datetime
from BeautifulSoup import BeautifulSoup
import sys


# Gets the authors at the specified url and returns a list of 
# python dictionaries: {'profession': '', 'name': ''}
def get_quotes(author_url):
    quote_objects = [];
    count = 0;
    # For each letter from a - z
    for c in range(97, 98):
        char = chr(c);
        # For each page of authors
        for i in range(1,2):
            url = author_url + char + str(i);
            # url = 'http://www.brainyquote.com/authors/d';
            response = requests.get(url);
            if (response.url != url and i != 1):
                print '-----------> next letter'
                break;
            html = response.content;
            soup = BeautifulSoup(html);
            table = soup.find('tbody');

            # For each author
            for row in table.findAll('tr'):
                block = [];
                author = {};
                for cell in row.findAll('td'):
                    text = cell.text;
                    block.append(text);
                author['name'] = block[0];
                author['profession'] = block[1];

                # Get each page of quotes
                for j in range (1, 2):
                    count = count + 1;

                    quote_url = 'http://www.brainyquote.com/quotes/authors/' + char + '/' + author['name'].replace('.', '').replace(' ', '_').replace('\'', '').replace('-', '').replace(',','').replace(':','').lower() + '_' + str(j) + '.html' ;
                    ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S');
                    print str(count) +  ': ' + ts + ' ' + quote_url;
                    res = requests.get(quote_url);
                    if (res.url != quote_url and j != 1):
                        print '--------> next author'
                        break;
                    page = res.content;
                    soup_quote = BeautifulSoup(page);
                    if (soup_quote):
                        quotes = soup_quote.find(id="quotesList");
                        if (quotes):
                            for div in quotes.findAll(attrs={'class': re.compile("masonryitem")}):
                                quote_details = [];
                                for field in div.findAll("a"):
                                    if (field.text != ''):
                                        quote_details.append(field.text);
                                topics = [];
                                for index in range (2, len(quote_details)):
                                    topics.append(quote_details[index]);
                                uid = str(uuid.uuid4());
                                quote = {uid: {'author': author, 'quote': quote_details[0], 'topics': topics}};
                                quote_objects.append(quote);
                        else:
                            print '-----------------Error getting quote at above url------------------------'
                    else:
                        print '-----------------Error getting quote at above url------------------------'
    return quote_objects;

def get_motivational_quotes(url):
    # Get each page of quotes
    count = 0;
    quote_objects = {};
    quote_objects['quotes'] = {};
    for i in range (1, 10):
        count = count + 1;
        quote_url = 'https://www.brainyquote.com/quotes/topics/topic_motivational' + str(i) + '.html';
        ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S');
        print str(count) +  ': ' + ts + ' ' + quote_url;
        res = requests.get(quote_url);
        if (res.url != quote_url and j != 1):
            print '--------> next page'
            return quote_objects;
        page = res.content;
        soup_quote = BeautifulSoup(page);
        if (soup_quote):
            quotes = soup_quote.find(id="quotesList");
            if (quotes):
                for div in quotes.findAll(attrs={'class': re.compile("masonryitem")}):
                    quote_details = [];
                    for field in div.findAll("a"):
                        if (field.text != ''):
                            quote_details.append(field.text);
                    topics = [];
                    for index in range (2, len(quote_details)):
                        topics.append(quote_details[index]);
                    uid = str(uuid.uuid4());
                    topics.append('Motivational');
                    quote_objects['quotes'][uid] = {'author': quote_details[1], 'quote': quote_details[0].replace('&#39;', '\''), 'topics': topics};
                    # print quote;
            else:
                print '-----------------Error getting quote at above url------------------------'
        else:
            print '-----------------Error getting quote at above url------------------------'
    for i in range (1, 40):
        count = count + 1;
        quote_url = 'https://www.brainyquote.com/quotes/topics/topic_sports' + str(i) + '.html';
        ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S');
        print str(count) +  ': ' + ts + ' ' + quote_url;
        res = requests.get(quote_url);
        if (res.url != quote_url and j != 1):
            print '--------> next page'
            return quote_objects;
        page = res.content;
        soup_quote = BeautifulSoup(page);
        if (soup_quote):
            quotes = soup_quote.find(id="quotesList");
            if (quotes):
                for div in quotes.findAll(attrs={'class': re.compile("masonryitem")}):
                    quote_details = [];
                    for field in div.findAll("a"):
                        if (field.text != ''):
                            quote_details.append(field.text);
                    topics = [];
                    for index in range (2, len(quote_details)):
                        topics.append(quote_details[index]);
                    uid = str(uuid.uuid4());
                    topics.append('Sports');
                    quote_objects['quotes'][uid] = {'author': quote_details[1], 'quote': quote_details[0].replace('&#39;', '\''), 'topics': topics};
                    # print quote;
            else:
                print '-----------------Error getting quote at above url------------------------'
        else:
            print '-----------------Error getting quote at above url------------------------'
    
    for i in range (1, 16):
        count = count + 1;
        quote_url = 'https://www.brainyquote.com/quotes/topics/topic_inspirational' + str(i) + '.html';
        ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S');
        print str(count) +  ': ' + ts + ' ' + quote_url;
        res = requests.get(quote_url);
        if (res.url != quote_url and j != 1):
            print '--------> next page'
            return quote_objects;
        page = res.content;
        soup_quote = BeautifulSoup(page);
        if (soup_quote):
            quotes = soup_quote.find(id="quotesList");
            if (quotes):
                for div in quotes.findAll(attrs={'class': re.compile("masonryitem")}):
                    quote_details = [];
                    for field in div.findAll("a"):
                        if (field.text != ''):
                            quote_details.append(field.text);
                    topics = [];
                    for index in range (2, len(quote_details)):
                        topics.append(quote_details[index]);
                    uid = str(uuid.uuid4());
                    topics.append('Inspirational');
                    quote_objects['quotes'][uid] = {'author': quote_details[1], 'quote': quote_details[0].replace('&#39;', '\''), 'topics': topics};
                    # print quote;
            else:
                print '-----------------Error getting quote at above url------------------------'
        else:
            print '-----------------Error getting quote at above url------------------------'
    



    return quote_objects;

def main():
    # quotes = get_quotes('http://www.brainyquote.com/authors/');
    motivational_quotes = get_motivational_quotes('https://www.brainyquote.com/quotes/topics/topic_motivational.html');
    file_ = open('quotes.json', 'w')
    # file_.write(json.dumps(quotes));
    file_.write(json.dumps(motivational_quotes));
    file_.close();
main()