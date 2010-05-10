#!/usr/bin/env python
#    This file is part of le(n)x.

#    le(n)x is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    le(n)x is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with le(n)x.  If not, see <http://www.gnu.org/licenses/>.

# (C) 2009-2010 by Stefan Marsiske, <stefan.marsiske@gmail.com>

from django.conf import settings
DICTDIR=settings.DICT_PATH
from lenx.brain import cache as Cache
CACHE=Cache.Cache(settings.CACHE_PATH)

from lenx.brain import hunspell # get pyhunspell here: http://code.google.com/p/pyhunspell/
import nltk.tokenize # get this from http://www.nltk.org/
from BeautifulSoup import BeautifulSoup # apt-get?
from pymongo import Connection
from operator import itemgetter

LANG='en_US'
DICT=DICTDIR+'/'+LANG
EURLEXURL="http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri="

conn = Connection()
db=conn.pippi
Docs=db.docs
Pippies=db.pippies

class Pippi():
    def __init__(self, pippi, oid=None):
        f=None
        if oid:
            # get by mongo oid
            frag=Pippies.find_one({"_id": oid})
        else:
            # get by pippi
            frag=Pippies.find_one({"pippi": pippi})
        if(frag):
            self.__dict__=frag
        else:
            self.__dict__={}
            self.__dict__['pippi'] = pippi
            self.__dict__['len'] = len(pippi)
            self.__dict__['docs'] = [] # should a be a list of {'pos':p,'txt':txt,'l':l,'doc':_id}
            self.save()

    def save(self):
        self.__dict__['_id']=Pippies.save(self.__dict__)

    def __getattr__(self, name):
        if name in self.__dict__.keys():
            return self.__dict__[name]
        else: raise AttributeError, name

    def __setattr__(self, name, value):
        if name in self.__dict__.keys():
            self.__dict__[name]=value
        else: raise AttributeError, name

    def getStr(self):
        return " ".join(eval(self.frag)).encode('utf8')

    def __unicode__(self):
        return unicode(self.frag)+":"+unicode(self.l)+"\n"+unicode(self.doc_set.all())

""" class representing a distinct document, does stemming, some minimal nlp, can be saved and loaded """
class Doc():
    #computed_attrs = [ 'raw', 'text', 'tokens', 'stems', 'spos', 'wpos', 'title', 'subject']
    computed_attrs = [ 'raw', 'text', 'tokens', 'stems', 'title', 'subject']

    def __init__(self,eurlexid,oid=None,d=None):
        if oid:
            # get by mongo oid
            d=Docs.find_one({"_id": oid})
        elif eurlexid:
            # get by eurlexid
            d=Docs.find_one({"eurlexid": eurlexid})
        if d:
            # load the values
            self.__dict__=d
            if d.has_key('stems'):
                # convert stems back to tuples - mongo only does lists
                self.__dict__['stems'] = tuple([tuple(x) for x in d['stems']])
        elif eurlexid:
            # create a new document
            self.__dict__={}
            self.__dict__['eurlexid'] = eurlexid
            self.__dict__['pippies'] = [] # should a be a list of {'pos':p,'txt':txt,'l':l,'frag':frag._id}
            self.save()
        else:
            raise KeyError('empty eurlexid')

    def __getattr__(self, name):
        # handle and cache calculated properties
        dirty=False
        if name in self.computed_attrs and name not in self.__dict__.keys():
            dirty=True
            if name == 'raw':
                self.raw=self._getraw()
            if name == 'text':
                self.text=self._gettext()
            #if name in ['tokens', 'wpos']:
            #    self.tokens,self.wpos=self._gettokens()
            if name == 'tokens':
                self.tokens=self._gettokens()
            #if name in ['stems', 'spos']:
            #    self.stems,self.spos=self._getstems()
            if name == 'stems':
                self.stems=self._getstems()
            if name == 'title':
                self.title=self._gettitle()
            if name == 'subject':
                self.subject=self._getsubj()
        if name in self.__dict__.keys():
            # we calculated some value so we should store it.
            if dirty: self.save()
            return self.__dict__[name]
        else:
            raise AttributeError, name

    def __setattr__(self, name, value):
        if name in self.__dict__.keys() or name in self.computed_attrs:
            self.__dict__[name]=value
        else: raise AttributeError, name

    def __unicode__(self):
        return self.eurlexid

    def save(self):
        self.__dict__['_id']=Docs.save(self.__dict__)

    def _getraw(self, cache=CACHE):
        return cache.fetchUrl(EURLEXURL+self.eurlexid)

    def _gettext(self, cache=CACHE):
        soup = BeautifulSoup(self.raw)
        # TexteOnly is the id used on eur-lex pages containing distinct docs
        return [unicode(x) for x in soup.find(id='TexteOnly').findAll(text=True)]

    def _gettokens(self):
        # start tokenizing
        tokens=[]
        #wpos={}
        #i=0
        for frag in self.text:
            if not frag: continue
            words=nltk.tokenize.wordpunct_tokenize(unicode(frag))
            tokens+=words
            # store positions of words
            #for word in words:
            #    wpos[word]=wpos.get(word,[])+[i]
            #    i+=1
        #return (tokens,wpos)
        return tokens

    def _getstems(self):
        # start stemming
        engine = hunspell.HunSpell(DICT+'.dic', DICT+'.aff')
        stems=[]
        #spos={}
        #i=0
        for word in self.tokens:
            # stem each word and count the results
            stem=engine.stem(word.encode('utf8'))
            if stem:
                stems.append((stem[0],))
            else:
                stems.append(('',))
            #spos[stem]=spos.get(stem,[])+[i]
            #i+=1
        #return (stems,spos)
        return tuple(stems)

    def _getHTMLMetaData(self, attr):
        soup = BeautifulSoup(self.raw)
        res=map(lambda x: (x and x.has_key('content') and x['content']) or "", soup.findAll('meta',attrs={'name':attr}))
        return '|'.join(res).encode('utf-8')

    def _gettitle(self):
        return self._getHTMLMetaData('DC.description')

    def _getsubj(self):
        return self._getHTMLMetaData('DC.subject')

    def getFrag(self,start,len):
        return " ".join(self.tokens[start:start+len]).encode('utf8')

    def getRelatedDocs(self, cutoff=7):
        return [Doc('',oid=oid)
                for oid in set([doc['doc']
                                for frag in Pippies.find({'docs.doc' : self._id,
                                                          'len' : { '$gte' : int(cutoff) }},
                                                         ['docs.doc'])
                                for doc in frag['docs']
                                if doc['doc'] != self._id])]

    def getDocFrags(self, cutoff=7):
        # returns the doc, with only the frags which are filtered by the cutoff and disctinct ordered by their location.
        return sorted(
            # either this code
            #filter(lambda x: x['l']>cutoff,
            #       self.pippies),
            # or this newer code
            [x for x in self.pippies if x['l']>cutoff],
            key=itemgetter('pos'))

