import django, logging, notasquare, urllib, urllib2, json

def call_api(url, POST=None, GET={}):
    if POST is not None:
        req = urllib2.Request(url, POST)
        res = urllib2.urlopen(req)
        return res.read()
    else:
        res = urllib.urlopen(url + '?' + urllib.urlencode(GET))
        return res.read()
