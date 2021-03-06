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

# (C) 2010 by Stefan Marsiske, <stefan.marsiske@gmail.com>

from lenx.view.models import Pippi
from lenx.view.doc import Doc
from lenx.view.db import Pippies, Frags, Docs
from django.core.management import setup_environ
from lenx import settings
from lenx.brain import lcs
setup_environ(settings)
import sys, os

docs={}

def main():
    print "updateing pippies.relevance"
    pippies=Pippies.find({},['docs','len'])
    pippieslen=pippies.count()
    i=1
    for pippi in pippies:
        if (i*100/pippieslen)!=((i-1)*100/pippieslen):
            if (i*100/pippieslen) % 10 == 0:
                sys.stdout.write("%d" % (i*100/pippieslen))
                sys.stdout.flush()
            else:
                sys.stdout.write('.')
                sys.stdout.flush()
        if len(pippi['docs'])>0:
                Pippies.update({'_id' : pippi['_id']},
                               { '$set': { 'relevance': float(pippi['len'])/float(len(pippi['docs'])),
                                           'docslen': len(pippi['docs']),}, })
        i=i+1
    sys.stdout.write('\n')
    sys.stdout.flush()

    print "updateing docs.idf"
    docs=Docs.find({},['termcnt','docid','stemsid','rawid'])
    docslen=docs.count()
    i=1
    for dd in docs:
        if (i*100/docslen)!=((i-1)*100/docslen):
            if (i*100/docslen) % 10 == 0:
                sys.stdout.write("%d" % (i*100/docslen))
                sys.stdout.flush()
            else:
                sys.stdout.write('.')
                sys.stdout.flush()
        Docs.update({'_id': dd['_id']},{ '$set': { 'tfidf': Doc(d=dd).tfidf } })
        i=i+1
    sys.stdout.write('\n')
    sys.stdout.flush()

    # this is to slow, we need to find another way around this
    #frags=Frags.find()
    #fragslen=frags.count()
    #i=1
    #for f in frags:
    #    print "%.2f" % (float(i)/float(fragslen)*100)
    #    p=Pippies.find_one({'_id': f['pippi']},['pippi'])
    #    doc=Docs.find_one({'_id': f['doc']},['tokens'])
    #    d=Doc('',d=doc)
    #    Frags.update({'_id' : f['_id']},
    #                 { '$set': { 'score': sum([d.tfidf.get(t,0) for t in p['pippi']])}})
    #    i=i+1

if __name__ == "__main__":
    #import os
    #import cProfile
    #cProfile.run('main()', '/tmp/bp-%d.prof' % (os.getpid()))
    main()
