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

from BeautifulSoup import BeautifulSoup
import re

CELEXCODES={ "1": { "Sector": "Treaties",
                    "Document Types" : { "D": "Treaty of Amsterdam 1997",
                                         "M": "Treaty on the European Union, Maastricht 1992 - EU Treaty - consolidated version 1997",
                                         "E": "EEC Treaty 1957 - EEC Treaty - consolidated version 1992 - EEC Treaty - consolidated version 1997",
                                         "K": "ECSC Treaty 1951",
                                         "A": "EURATOM Treaty 1957",
                                         "U": "Single European Act 1986",
                                         "G": "Groenland Treaty 1985",
                                         "R": "Treaty amending certain financial provisions 1975",
                                         "F": "Treaty amending certain budgetary provisions 1970",
                                         "F": "Merger Treaty 1965",
                                         "B": "Accession Treaty 1972 (United Kingdom, Denmark, Ireland, Norway)",
                                         "H": "Accession Treaty 1979 (Greece)",
                                         "I": "Accession Treaty 1985 (Spain, Portugal)",
                                         "N": "Accession Treaty 1994 (Austria, Sweden, Finland, Norway)",
                                         }},
             "2": { "Sector": "External Agreements",
                    "Document Types" : { "A":"Agreements with non-member States or international organisations",
                                         "D":"Acts of bodies created by international agreements",
                                         "P":"Acts of parliamentary bodies created by international agreements",
                                         "X":"Other Acts ",},},
             "3": { "Sector": "Legislation",
                    "Document Types" : { "E":"Common Foreign and Security Policy (CFSP) - common positions / joint actions / common strategies",
                                         "F":"Justice and Home Affairs (JHA) - common positions / framework decisions",
                                         "R":"Regulations",
                                         "L":"Directives",
                                         "D":"Decisions sui generis",
                                         "S":"ECSC Decisions of general interest",
                                         "M":"Non-opposition to a notified concentration",
                                         "J":"Non-opposition to a notified joint venture",
                                         "B":"Budget",
                                         "K":"Recommendations ECSC",
                                         "O":"Guidelines ECB",
                                         "H":"Recommendations",
                                         "A":"Avis",
                                         "G":"Resolutions",
                                         "C":"Declarations",
                                         "Q":"Institutional arrangements, Rules of Procedure, Internal agreements",
                                         "X":"Other documents",},},
             "4": { "Sector": "Internal Agreements",
                    "Document Types" : { "D":"Decisions of the representatives of the governments of the Member States",
                                         "X":"Other acts",},},
             "5": { "Sector": "Proposals + preparatory documents",
                    "Document Types" : { "AG":"Council - common positions",
                                         "KG":"Council - assent ECSC",
                                         "IG":"Member States - Initiatives",
                                         "XG":"Council - other acts",
                                         "PC":"COM Documents - proposals for legislation",
                                         "DC":"COM Documents - other documents",
                                         "SC":"SEC Documents",
                                         "XC":"Commission - other acts",
                                         "AP":"EP - legislative resolution",
                                         "BP":"EP - budget",
                                         "IP":"EP - other resolutions",
                                         "XP":"EP - other acts",
                                         "AA":"Court of Auditors - opinions",
                                         "TA":"Court of Auditors - reports",
                                         "SA":"Court of Auditors - special reports",
                                         "XA":"Court of Auditors - other acts",
                                         "AB":"ECB - opinions",
                                         "HB":"ECB - recommendations",
                                         "XB":"ECB - other acts",
                                         "AE":"ESC - opinions on consultation",
                                         "IE":"ESC - other opinions",
                                         "XE":"ESC - other acts",
                                         "AR":"CR - opinions on consultation",
                                         "IR":"CR - other opinions",
                                         "XR":"CR - other acts",
                                         "AK":"ECSC Com. - opinions",
                                         "XK":"ECSC Com. - other acts",
                                         "XX":"Other acts ", }, },
             "6": { "Sector": "Case Law",
                    "Document Types" : { "A":"Court of First Instance Judgments",
                                         "B":"Court of First Instance - Orders",
                                         "D":"Court of First Instance - Third Party Proceedings",
                                         "F":"Court of First Instance - Opinions",
                                         "H":"Court of First Instance - Case report",
                                         "C":"Court of Justice - Conclusions of the Avocate-General",
                                         "J":"Court of Justice - Judgments",
                                         "O":"Court of Justice - Orders",
                                         "P":"Court of Justice - Case report",
                                         "S":"Court of Justice - Seizure",
                                         "T":"Court of Justice - Third Party Proceedings",
                                         "V":"Court of Justice - Opinions",
                                         "X":"Court of Justice - Rulings",},},
             "7": { "Sector": "National Implementation",
                    "Document Types" : {"L":"National Implementation Measures - implementation of directives",},},
             "9": { "Sector": "European Parliamentary Questions",
                    "Document Types" : { "E":"European European Parliament - Written Questions",
                                         "H":"European European Parliament - Questions at Questiontime",
                                         "O":"European European Parliament - Oral questions",},},
             "C": { "Sector": "OJC Documents", "Document Types" : {},},
             "E": { "Sector": "EFTA Documents",
                    "Document Types" : { "A":"International Agreements",
                                         "C":"Acts of the EFTA Surveillance Authority",
                                         "G":"Acts of the EFTA Standing Committee",
                                         "J":"Decisions, Orders, Consultative opinions of the EFTA Court",
                                         "P":"Pending cases of the EFTA Court",
                                         "X":"EFTA - Other Acts",},},
             }

class Eurlex():
    def __init__(self, celexid):
        code=celexid.split(":")[1]
        st=7 if code[6].isalpha() else 6
        self.__dict__={'sector': code[0],
                       'year': code[1:5],
                       'doctype': code[5:st],
                       'refno': code[st:],
                       }

    def __getattr__(self, name):
        if name == 'typeDesc':
            return CELEXCODES[self.sector]['Document Types'][self.doctype] if self.doctype != 'C' else CELEXCODES[self.sector]['Sector']
        if name in self.__dict__:
            return self.__dict__[name]
        else:
            raise AttributeError, name

    def __setattr__(self, name, value):
        if name in self.__dict__.keys():
            self.__dict__[name]=value
        else: raise AttributeError, name

    def __unicode__(self):
        if self.sector=='3' and self.doctype=='L':
            return "%s/%s/EEC" % (self.year, self.refno)
        return "%s %s/%s" % (self.typeDesc,
                             self.year,
                             self.refno)

    def __repr__(self):
        return self.__unicode__()

    def extractMetadata(self,raw):
        soup = BeautifulSoup(unicode(raw))
        return {
            'dates' : fltr(soup.find(text="Dates").findNext('ul').findAll(text=True)),
            'class' : fltr(soup.find(text="Classifications").findNext('ul').findAll(text=True)),
            'misc'  : fltr(soup.find(text="Miscellaneous information").findNext('ul').findAll(text=True)),
            'proc'  : fltr(soup.find(text="Procedure").findNext('ul').findAll(text=True)),
            'rels'  : fltr(soup.find(text="Relationship between documents").findNext('ul').findAll(text=True)),
            }

def fltr(lst):
    return [x for x in lst if not re.search(r"\s*\\n',\s*'\s*",x)]

if __name__ == "__main__":
    print Eurlex("CELEX:31994D0006:EN:HTML")
    print Eurlex("CELEX:31994L0006:EN:HTML")
    print Eurlex("CELEX:51994XP006:EN:HTML")

    # test metadata extraction
    #import urllib2
    #EURLEXURL="http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri="
    #text = urllib2.urlopen(url).read()
    import pprint
    tcom=Eurlex("CELEX:32009L0140:EN:HTML")
    f=open("../arch/CELEX:32009L0140:EN:NOT.html",'U')
    html=f.readlines()
    f.close()
    pprint.pprint(tcom.extractMetadata(html))

    ecom=Eurlex("CELEX:32004L0048:EN:HTML")
    f=open("../arch/CELEX:32004L0048:EN:NOT.html",'U')
    html=f.readlines()
    f.close()
    pprint.pprint(ecom.extractMetadata(html))