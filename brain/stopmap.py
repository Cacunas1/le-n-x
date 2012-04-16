#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

stopmap={
    'de': [u"aber", u"alle", u"allem", u"allen", u"aller", u"alles", u"als", u"also", u"am", u"an", u"ander", u"andere", u"anderem", u"anderen", u"anderer", u"anderes", u"anderm", u"andern", u"anderr", u"anders", u"auch", u"auf", u"aus", u"bei", u"bin", u"bis", u"bist", u"da", u"damit", u"dann", u"der", u"den", u"des", u"dem", u"die", u"das", u"daß", u"derselbe", u"derselben", u"denselben", u"desselben", u"demselben", u"dieselbe", u"dieselben", u"dasselbe", u"dazu", u"dein", u"deine", u"deinem", u"deinen", u"deiner", u"deines", u"denn", u"derer", u"dessen", u"dich", u"dir", u"du", u"dies", u"diese", u"diesem", u"diesen", u"dieser", u"dieses", u"doch", u"dort", u"durch", u"ein", u"eine", u"einem", u"einen", u"einer", u"eines", u"einig", u"einige", u"einigem", u"einigen", u"einiger", u"einiges", u"einmal", u"er", u"ihn", u"ihm", u"es", u"etwas", u"euer", u"eure", u"eurem", u"euren", u"eurer", u"eures", u"für", u"gegen", u"gewesen", u"hab", u"habe", u"haben", u"hat", u"hatte", u"hatten", u"hier", u"hin", u"hinter", u"ich", u"mich", u"mir", u"ihr", u"ihre", u"ihrem", u"ihren", u"ihrer", u"ihres", u"euch", u"im", u"in", u"indem", u"ins", u"ist", u"jede", u"jedem", u"jeden", u"jeder", u"jedes", u"jene", u"jenem", u"jenen", u"jener", u"jenes", u"jetzt", u"kann", u"kein", u"keine", u"keinem", u"keinen", u"keiner", u"keines", u"können", u"könnte", u"machen", u"man", u"manche", u"manchem", u"manchen", u"mancher", u"manches", u"mein", u"meine", u"meinem", u"meinen", u"meiner", u"meines", u"mit", u"muss", u"musste", u"nach", u"nicht", u"nichts", u"noch", u"nun", u"nur", u"ob", u"oder", u"ohne", u"sehr", u"sein", u"seine", u"seinem", u"seinen", u"seiner", u"seines", u"selbst", u"sich", u"sie", u"ihnen", u"sind", u"so", u"solche", u"solchem", u"solchen", u"solcher", u"solches", u"soll", u"sollte", u"sondern", u"sonst", u"über", u"um", u"und", u"uns", u"unse", u"unsem", u"unsen", u"unser", u"unses", u"unter", u"viel", u"vom", u"von", u"vor", u"während", u"war", u"waren", u"warst", u"was", u"weg", u"weil", u"weiter", u"welche", u"welchem", u"welchen", u"welcher", u"welches", u"wenn", u"werde", u"werden", u"wie", u"wieder", u"will", u"wir", u"wird", u"wirst", u"wo", u"wollen", u"wollte", u"würde", u"würden", u"zu", u"zum", u"zur", u"zwar", u"zwischen",],
    'da': [u"og", u"i", u"jeg", u"det", u"at", u"en", u"den", u"til", u"er", u"som", u"på", u"de", u"med", u"han", u"af", u"for", u"ikke", u"der", u"var", u"mig", u"sig", u"men", u"et", u"har", u"om", u"vi", u"min", u"havde", u"ham", u"hun", u"nu", u"over", u"da", u"fra", u"du", u"ud", u"sin", u"dem", u"os", u"op", u"man", u"hans", u"hvor", u"eller", u"hvad", u"skal", u"selv", u"her", u"alle", u"vil", u"blev", u"kunne", u"ind", u"når", u"være", u"dog", u"noget", u"ville", u"jo", u"deres", u"efter", u"ned", u"skulle", u"denne", u"end", u"dette", u"mit", u"også", u"under", u"have", u"dig", u"anden", u"hende", u"mine", u"alt", u"meget", u"sit", u"sine", u"vor", u"mod", u"disse", u"hvis", u"din", u"nogle", u"hos", u"blive", u"mange", u"ad", u"bliver", u"hendes", u"været", u"thi", u"jer", u"sådan",],
    'en': [u"i", u"me", u"my", u"myself", u"we", u"our", u"ours", u"ourselves", u"you", u"your", u"yours", u"yourself", u"yourselves", u"he", u"him", u"his", u"himself", u"she", u"her", u"hers", u"herself", u"it", u"its", u"itself", u"they", u"them", u"their", u"theirs", u"themselves", u"what", u"which", u"who", u"whom", u"this", u"that", u"these", u"those", u"am", u"is", u"are", u"was", u"were", u"be", u"been", u"being", u"have", u"has", u"had", u"having", u"do", u"does", u"did", u"doing", u"would", u"should", u"could", u"ought", u"i'm", u"you're", u"he's", u"she's", u"it's", u"we're", u"they're", u"i've", u"you've", u"we've", u"they've", u"i'd", u"you'd", u"he'd", u"she'd", u"we'd", u"they'd", u"i'll", u"you'll", u"he'll", u"she'll", u"we'll", u"they'll", u"isn't", u"aren't", u"wasn't", u"weren't", u"hasn't", u"haven't", u"hadn't", u"doesn't", u"don't", u"didn't", u"won't", u"wouldn't", u"shan't", u"shouldn't", u"can't", u"cannot", u"couldn't", u"mustn't", u"let's", u"that's", u"who's", u"what's", u"here's", u"there's", u"when's", u"where's", u"why's", u"how's", u"a", u"an", u"the", u"and", u"but", u"if", u"or", u"because", u"as", u"until", u"while", u"of", u"at", u"by", u"for", u"with", u"about", u"against", u"between", u"into", u"through", u"during", u"before", u"after", u"above", u"below", u"to", u"from", u"up", u"down", u"in", u"out", u"on", u"off", u"over", u"under", u"again", u"further", u"then", u"once", u"here", u"there", u"when", u"where", u"why", u"how", u"all", u"any", u"both", u"each", u"few", u"more", u"most", u"other", u"some", u"such", u"no", u"nor", u"not", u"only", u"own", u"same", u"so", u"than", u"too", u"very", u"one", u"every", u"least", u"less", u"many", u"now", u"ever", u"never", u"say", u"says", u"said", u"also", u"get", u"go", u"goes", u"just", u"made", u"make", u"put", u"see", u"seen", u"whether", u"like", u"well", u"back", u"even", u"still", u"way", u"take", u"since", u"another", u"however", u"two", u"three", u"four", u"five", u"first", u"second", u"new", u"old", u"high", u"long",],
    'es': [u"de", u"la", u"que", u"el", u"en", u"y", u"a", u"los", u"del", u"se", u"las", u"por", u"un", u"para", u"con", u"no", u"una", u"su", u"al", u"lo", u"como", u"más", u"pero", u"sus", u"le", u"ya", u"o", u"este", u"sí", u"porque", u"esta", u"entre", u"cuando", u"muy", u"sin", u"sobre", u"también", u"me", u"hasta", u"hay", u"donde", u"quien", u"desde", u"todo", u"nos", u"durante", u"todos", u"uno", u"les", u"ni", u"contra", u"otros", u"ese", u"eso", u"ante", u"ellos", u"e", u"esto", u"mí", u"antes", u"algunos", u"qué", u"unos", u"yo", u"otro", u"otras", u"otra", u"él", u"tanto", u"esa", u"estos", u"mucho", u"quienes", u"nada", u"muchos", u"cual", u"poco", u"ella", u"estar", u"estas", u"algunas", u"algo", u"nosotros", u"mi", u"mis", u"tú", u"te", u"ti", u"tu", u"tus", u"ellas", u"nosotras", u"vosotros", u"vosotras", u"os", u"mío", u"mía", u"míos", u"mías", u"tuyo", u"tuya", u"tuyos", u"tuyas", u"suyo", u"suya", u"suyos", u"suyas", u"nuestro", u"nuestra", u"nuestros", u"nuestras", u"vuestro", u"vuestra", u"vuestros", u"vuestras", u"esos", u"esas", u"estoy", u"estás", u"está", u"estamos", u"estáis", u"están", u"esté", u"estés", u"estemos", u"estéis", u"estén", u"estaré", u"estarás", u"estará", u"estaremos", u"estaréis", u"estarán", u"estaría", u"estarías", u"estaríamos", u"estaríais", u"estarían", u"estaba", u"estabas", u"estábamos", u"estabais", u"estaban", u"estuve", u"estuviste", u"estuvo", u"estuvimos", u"estuvisteis", u"estuvieron", u"estuviera", u"estuvieras", u"estuviéramos", u"estuvierais", u"estuvieran", u"estuviese", u"estuvieses", u"estuviésemos", u"estuvieseis", u"estuviesen", u"estando", u"estado", u"estada", u"estados", u"estadas", u"estad", u"he", u"has", u"ha", u"hemos", u"habéis", u"han", u"haya", u"hayas", u"hayamos", u"hayáis", u"hayan", u"habré", u"habrás", u"habrá", u"habremos", u"habréis", u"habrán", u"habría", u"habrías", u"habríamos", u"habríais", u"habrían", u"había", u"habías", u"habíamos", u"habíais", u"habían", u"hube", u"hubiste", u"hubo", u"hubimos", u"hubisteis", u"hubieron", u"hubiera", u"hubieras", u"hubiéramos", u"hubierais", u"hubieran", u"hubiese", u"hubieses", u"hubiésemos", u"hubieseis", u"hubiesen", u"habiendo", u"habido", u"habida", u"habidos", u"habidas", u"soy", u"eres", u"es", u"somos", u"sois", u"son", u"sea", u"seas", u"seamos", u"seáis", u"sean", u"seré", u"serás", u"será", u"seremos", u"seréis", u"serán", u"sería", u"serías", u"seríamos", u"seríais", u"serían", u"era", u"eras", u"éramos", u"erais", u"eran", u"fui", u"fuiste", u"fue", u"fuimos", u"fuisteis", u"fueron", u"fuera", u"fueras", u"fuéramos", u"fuerais", u"fueran", u"fuese", u"fueses", u"fuésemos", u"fueseis", u"fuesen", u"siendo", u"sido", u"tengo", u"tienes", u"tiene", u"tenemos", u"tenéis", u"tienen", u"tenga", u"tengas", u"tengamos", u"tengáis", u"tengan", u"tendré", u"tendrás", u"tendrá", u"tendremos", u"tendréis", u"tendrán", u"tendría", u"tendrías", u"tendríamos", u"tendríais", u"tendrían", u"tenía", u"tenías", u"teníamos", u"teníais", u"tenían", u"tuve", u"tuviste", u"tuvo", u"tuvimos", u"tuvisteis", u"tuvieron", u"tuviera", u"tuvieras", u"tuviéramos", u"tuvierais", u"tuvieran", u"tuviese", u"tuvieses", u"tuviésemos", u"tuvieseis", u"tuviesen", u"teniendo", u"tenido", u"tenida", u"tenidos", u"tenidas", u"tened",],
    'fi': [u"olla", u"olen", u"olet", u"on", u"olemme", u"olette", u"ovat", u"ole", u"oli", u"olisi", u"olisit", u"olisin", u"olisimme", u"olisitte", u"olisivat", u"olit", u"olin", u"olimme", u"olitte", u"olivat", u"ollut", u"olleet", u"en", u"et", u"ei", u"emme", u"ette", u"eivät", u"minä", u"minun", u"minut", u"minua", u"minussa", u"minusta", u"minuun", u"minulla", u"minulta", u"minulle", u"sinä", u"sinun", u"sinut", u"sinua", u"sinussa", u"sinusta", u"sinuun", u"sinulla", u"sinulta", u"sinulle", u"hän", u"hänen", u"hänet", u"häntä", u"hänessä", u"hänestä", u"häneen", u"hänellä", u"häneltä", u"hänelle", u"me", u"meidän", u"meidät", u"meitä", u"meissä", u"meistä", u"meihin", u"meillä", u"meiltä", u"meille", u"te", u"teidän", u"teidät", u"teitä", u"teissä", u"teistä", u"teihin", u"teillä", u"teiltä", u"teille", u"he", u"heidän", u"heidät", u"heitä", u"heissä", u"heistä", u"heihin", u"heillä", u"heiltä", u"heille", u"tämä", u"tämän", u"tätä", u"tässä", u"tästä", u"tähän", u"tällä", u"tältä", u"tälle", u"tänä", u"täksi", u"tuo", u"tuon", u"tuota", u"tuossa", u"tuosta", u"tuohon", u"tuolla", u"tuolta", u"tuolle", u"tuona", u"tuoksi", u"se", u"sen", u"sitä", u"siinä", u"siitä", u"siihen", u"sillä", u"siltä", u"sille", u"sinä", u"siksi", u"nämä", u"näiden", u"näitä", u"näissä", u"näistä", u"näihin", u"näillä", u"näiltä", u"näille", u"näinä", u"näiksi", u"nuo", u"noiden", u"noita", u"noissa", u"noista", u"noihin", u"noilla", u"noilta", u"noille", u"noina", u"noiksi", u"ne", u"niiden", u"niitä", u"niissä", u"niistä", u"niihin", u"niillä", u"niiltä", u"niille", u"niinä", u"niiksi", u"kuka", u"kenen", u"kenet", u"ketä", u"kenessä", u"kenestä", u"keneen", u"kenellä", u"keneltä", u"kenelle", u"kenenä", u"keneksi", u"ketkä", u"keiden", u"ketkä", u"keitä", u"keissä", u"keistä", u"keihin", u"keillä", u"keiltä", u"keille", u"keinä", u"keiksi", u"mikä", u"minkä", u"minkä", u"mitä", u"missä", u"mistä", u"mihin", u"millä", u"miltä", u"mille", u"minä", u"miksi", u"mitkä", u"joka", u"jonka", u"jota", u"jossa", u"josta", u"johon", u"jolla", u"jolta", u"jolle", u"jona", u"joksi", u"jotka", u"joiden", u"joita", u"joissa", u"joista", u"joihin", u"joilla", u"joilta", u"joille", u"joina", u"joiksi", u"että", u"ja", u"jos", u"koska", u"kuin", u"mutta", u"niin", u"sekä", u"sillä", u"tai", u"vaan", u"vai", u"vaikka", u"kanssa", u"mukaan", u"noin", u"poikki", u"yli", u"kun", u"niin", u"nyt", u"itse",],
    'fr': [u"au", u"aux", u"avec", u"ce", u"ces", u"dans", u"de", u"des", u"du", u"elle", u"en", u"et", u"eux", u"il", u"je", u"la", u"le", u"leur", u"lui", u"ma", u"mais", u"me", u"même", u"mes", u"moi", u"mon", u"ne", u"nos", u"notre", u"nous", u"on", u"ou", u"par", u"pas", u"pour", u"qu", u"que", u"qui", u"sa", u"se", u"ses", u"son", u"sur", u"ta", u"te", u"tes", u"toi", u"ton", u"tu", u"un", u"une", u"vos", u"votre", u"vous", u"c", u"d", u"j", u"l", u"à", u"m", u"n", u"s", u"t", u"y", u"été", u"étée", u"étées", u"étés", u"étant", u"suis", u"es", u"est", u"sommes", u"êtes", u"sont", u"serai", u"seras", u"sera", u"serons", u"serez", u"seront", u"serais", u"serait", u"serions", u"seriez", u"seraient", u"étais", u"était", u"étions", u"étiez", u"étaient", u"fus", u"fut", u"fûmes", u"fûtes", u"furent", u"sois", u"soit", u"soyons", u"soyez", u"soient", u"fusse", u"fusses", u"fût", u"fussions", u"fussiez", u"fussent", u"ayant", u"eu", u"eue", u"eues", u"eus", u"ai", u"as", u"avons", u"avez", u"ont", u"aurai", u"auras", u"aura", u"aurons", u"aurez", u"auront", u"aurais", u"aurait", u"aurions", u"auriez", u"auraient", u"avais", u"avait", u"avions", u"aviez", u"avaient", u"eut", u"eûmes", u"eûtes", u"eurent", u"aie", u"aies", u"ait", u"ayons", u"ayez", u"aient", u"eusse", u"eusses", u"eût", u"eussions", u"eussiez", u"eussent", u"ceci", u"celà ", u"cet", u"cette", u"ici", u"ils", u"les", u"leurs", u"quel", u"quels", u"quelle", u"quelles", u"sans", u"soi",],
    'hu': [u"a", u"ahogy", u"ahol", u"aki", u"akik", u"akkor", u"alatt", u"által", u"általában", u"amely", u"amelyek", u"amelyekben", u"amelyeket", u"amelyet", u"amelynek", u"ami", u"amit", u"amolyan", u"amíg", u"amikor", u"át", u"abban", u"ahhoz", u"annak", u"arra", u"arról", u"az", u"azok", u"azon", u"azt", u"azzal", u"azért", u"aztán", u"azután", u"azonban", u"bár", u"be", u"belül", u"benne", u"cikk", u"cikkek", u"cikkeket", u"csak", u"de", u"e", u"eddig", u"egész", u"egy", u"egyes", u"egyetlen", u"egyéb", u"egyik", u"egyre", u"ekkor", u"el", u"elég", u"ellen", u"elõ", u"elõször", u"elõtt", u"elsõ", u"én", u"éppen", u"ebben", u"ehhez", u"emilyen", u"ennek", u"erre", u"ez", u"ezt", u"ezek", u"ezen", u"ezzel", u"ezért", u"és", u"fel", u"felé", u"hanem", u"hiszen", u"hogy", u"hogyan", u"igen", u"így", u"illetve", u"ill.", u"ill", u"ilyen", u"ilyenkor", u"ison", u"ismét", u"itt", u"jó", u"jól", u"jobban", u"kell", u"kellett", u"keresztül", u"keressünk", u"ki", u"kívül", u"között", u"közül", u"legalább", u"lehet", u"lehetett", u"legyen", u"lenne", u"lenni", u"lesz", u"lett", u"maga", u"magát", u"majd", u"majd", u"már", u"más", u"másik", u"meg", u"még", u"mellett", u"mert", u"mely", u"melyek", u"mi", u"mit", u"míg", u"miért", u"milyen", u"mikor", u"minden", u"mindent", u"mindenki", u"mindig", u"mint", u"mintha", u"mivel", u"most", u"nagy", u"nagyobb", u"nagyon", u"ne", u"néha", u"nekem", u"neki", u"nem", u"néhány", u"nélkül", u"nincs", u"olyan", u"ott", u"össze", u"õ", u"õk", u"õket", u"pedig", u"persze", u"rá", u"s", u"saját", u"sem", u"semmi", u"sok", u"sokat", u"sokkal", u"számára", u"szemben", u"szerint", u"szinte", u"talán", u"tehát", u"teljes", u"tovább", u"továbbá", u"több", u"úgy", u"ugyanis", u"új", u"újabb", u"újra", u"után", u"utána", u"utolsó", u"vagy", u"vagyis", u"valaki", u"valami", u"valamint", u"való", u"vagyok", u"van", u"vannak", u"volt", u"voltam", u"voltak", u"voltunk", u"vissza", u"vele", u"viszont", u"volna",],
# frequency list from here: https://invokeit.wordpress.com/frequency-word-lists/
    'is': [u"ég", u"að", u"er", u"það", u"ekki", u"í", u"og", u"þú", u"við", u"á", u"hann", u"þetta", u"hvað", u"sem", u"mér", u"til", u"með", u"þér", u"en", u"fyrir", u"um", u"af", u"var", u"þig", u"mig", u"því", u"já", u"hún", u"nei", u"allt", u"þá", u"ef", u"eru", u"bara", u"ert", u"svo", u"þeir", u"þið", u"okkur", u"eftir", u"vera", u"eins", u"ertu", u"hér", u"veit", u"gera", u"lagi", u"hefur", u"nú", u"frá", u"e", u"þegar", u"hvernig", u"fara", u"honum", u"hef", u"út", u"verður", u"aftur", u"upp", u"þessu", u"vel", u"verið", u"ekkert", u"minn", u"sé", u"hver", u"svona", u"hana", u"eða", u"ykkur", u"vil", u"hverju", u"úr", u"get", u"segja", u"komdu", u"erum", u"hvar", u"aldrei", u"hafa", u"eitthvað", u"gott", u"hérna", u"maður", u"hjá", u"viltu", u"fá", u"sagði", u"þau", u"getur", u"inn", u"koma", u"okkar", u"herra", u"núna", u"þarna", u"kannski", u"hans", u"mín", u"þar", u"tala", u"þarf", u"þess", u"þeim", u"þín", u"væri", u"farðu", u"henni", u"takk", u"fer", u"líka", u"þinn", u"held", u"sjá", u"rétt", u"áfram", u"sér", u"mjög", u"verð", u"kemur", u"gert", u"vegna", u"þessi", u"enn", u"sá", u"þakka", u"saman", u"einn", u"komið", u"gæti", u"a", u"alltaf", u"kom", u"allir", u"of", u"vita", u"skal", u"enginn", u"má", u"yfir", u"farið", u"hafi", u"ætla", u"dag", u"förum", u"þær", u"heldur", u"veistu", u"hr", u"hefði", u"hingað", u"sig", u"niður", u"sama", u"mitt", u"mikið", u"átt", u"guð", u"höfum", u"láttu", u"segðu", u"pabbi", u"einhver", u"heim", u"aðeins", u"bíddu", u"áður", u"segir", u"þessa", u"finnst", u"vertu", u"getum", u"tíma", u"i", u"vildi", u"góður", u"fyrirgefðu", u"vill", u"hefurðu", u"meira", u"mamma", u"gerðu", u"satt", u"verðum", u"eitt", u"þitt", u"jæja", u"fór", u"stað", u"halda", u"taka", u"annað", u"verða", u"veist", u"ykkar", u"hvert", u"sagt", u"alla", u"voru", u"vilt", u"gerir", u"leið", u"sjáðu", u"menn", u"fram", u"séð", u"gerði", u"mun", u"láta", u"hvaða", u"kvöld", u"hvort", u"öll", u"fólk", u"ó", u"elskan", u"myndi", u"fjandinn", u"þ", u"einu", u"ao", u"ár", u"hennar", u"vinur", u"geri", u"síðan", u"hélt", u"eina", u"hættu", u"vissi", u"auðvitað", u"ætti", u"sinni", u"þeirra", u"þessum", u"þannig", u"eruð", u"halló", u"pú", u"drepa", u"mína", u"strax", u"þína", u"alveg", u"skil", u"reyna", u"án", u"langar", u"finna", u"þennan", u"neitt", u"geturðu", u"vinna", u"viss", u"öllum", u"morgun", u"undir", u"engin", u"taktu", u"hvers", u"hugsa", u"áttu", u"frú", u"hæ", u"mínum", u"gengur", u"varð", u"heyrðu", u"einmitt", u"lengi", u"kem", u"haltu", u"heldurðu", u"elska", u"hvenær", u"þangað", u"fimm", u"varst", u"fékk", u"virðist", u"segi", u"góða", u"komast", u"eigum", u"lengur", u"líður", u"vilja", u"gerðist", u"þarft", u"gaman", u"kominn", u"átti", u"ná", u"mann", u"eiga", u"jack", u"þínum", u"sæll", u"burt", u"lífi", u"èg", u"fyrsta", u"inni", u"fyrst", u"geta", u"þykir", u"hafði", u"petta", u"öllu", u"handa", u"frábært", u"betur", u"leitt", u"þurfum", u"héðan", u"ætlarðu", u"ú", u"hægt", u"illa", u"fyrr", u"hitta", u"góð", u"málið", u"nóg", u"sinn", u"alvöru", u"hjálpa", u"einhvern", u"nótt", u"r", u"jú", u"komum", u"aò", u"nema", u"ára", u"ferð", u"gegn", u"hlýtur", u"víst", u"fengið", u"sjálfur", u"mál", u"ad", u"daginn", u"ein", u"áhyggjur", u"annars", u"leita", u"hafið", u"búinn", u"à", u"pao", u"tveir", u"orðið", u"heiti", u"langt", u"haldið", u"deyja", u"ættir", u"gat", u"erfitt", u"faðir", u"líf", u"hve", u"heima", u"minni", u"máli", u"enga", u"mátt", u"engar", u"h", u"hætta", u"meðan", u"spyrja", u"aõ", u"skiptir", u"mínu", u"samt", u"john", u"heyra", u"mínútur", u"gerum", u"sýna", u"kann", u"gefa", u"tvö", u"vorum", u"tekur", u"mínir", u"maðurinn", u"fæ", u"hvern", u"fær", u"heitir", u"ætlar", u"gerast", u"ganga", u"skilurðu", u"komst", u"gangi", u"klukkan", u"fínt", u"bless", u"lítur", u"sagðir", u"tíu", u"stundum", u"tók", u"vio", u"allar", u"nokkuð", u"baka", u"uppi", u"sért", u"gerist", u"heyrt", u"alls", u"hjálp", u"skjóta", u"stendur", u"þinni", u"sex", u"g", u"líkar", u"vantar", u"látið", u"skilið", u"góðan", u"líklega", u"fann", u"allan", u"þótt", u"sérðu", u"nota", u"kona", u"færð", u"segirðu", u"þessari", u"fannst", u"ö", u"verði", u"fleiri", u"manni", u"jafnvel", u"afsakið", u"engan", u"úti", u"trúi", u"man", u"hefðir", u"þekki", u"pér", u"afsakaðu", u"lokið", u"árum", u"bílinn", u"yrði", u"tvær", u"sjáumst", u"mömmu", u"s", u"m", u"nógu", u"konan", u"daga", u"kemst", u"hví", u"hlustaðu", u"milli", u"tvo", u"tekið", u"varstu", u"hugmynd", u"tími", u"manstu", u"byrja", u"værir", u"þó", u"new", u"sú", u"fjandans", u"engu", u"búið", u"betra", u"kalla", u"bíða", u"besta", u"leyfðu", u"ættum", u"eigin", u"ha", u"undan", u"beint", u"annan", u"næstum", u"konu", u"svolítið", u"sonur", u"orð",],
    'it': [u"ad", u"al", u"allo", u"ai", u"agli", u"all", u"agl", u"alla", u"alle", u"con", u"col", u"coi", u"da", u"dal", u"dallo", u"dai", u"dagli", u"dall", u"dagl", u"dalla", u"dalle", u"di", u"del", u"dello", u"dei", u"degli", u"dell", u"degl", u"della", u"delle", u"in", u"nel", u"nello", u"nei", u"negli", u"nell", u"negl", u"nella", u"nelle", u"su", u"sul", u"sullo", u"sui", u"sugli", u"sull", u"sugl", u"sulla", u"sulle", u"per", u"tra", u"contro", u"io", u"tu", u"lui", u"lei", u"noi", u"voi", u"loro", u"mio", u"mia", u"miei", u"mie", u"tuo", u"tua", u"tuoi", u"tue", u"suo", u"sua", u"suoi", u"sue", u"nostro", u"nostra", u"nostri", u"nostre", u"vostro", u"vostra", u"vostri", u"vostre", u"mi", u"ti", u"ci", u"vi", u"lo", u"la", u"li", u"le", u"gli", u"ne", u"il", u"un", u"uno", u"una", u"ma", u"ed", u"se", u"perché", u"anche", u"come", u"dov", u"dove", u"che", u"chi", u"cui", u"non", u"più", u"quale", u"quanto", u"quanti", u"quanta", u"quante", u"quello", u"quelli", u"quella", u"quelle", u"questo", u"questi", u"questa", u"queste", u"si", u"tutto", u"tutti", u"a", u"c", u"e", u"i", u"l", u"o", u"ho", u"hai", u"ha", u"abbiamo", u"avete", u"hanno", u"abbia", u"abbiate", u"abbiano", u"avrò", u"avrai", u"avrà", u"avremo", u"avrete", u"avranno", u"avrei", u"avresti", u"avrebbe", u"avremmo", u"avreste", u"avrebbero", u"avevo", u"avevi", u"aveva", u"avevamo", u"avevate", u"avevano", u"ebbi", u"avesti", u"ebbe", u"avemmo", u"aveste", u"ebbero", u"avessi", u"avesse", u"avessimo", u"avessero", u"avendo", u"avuto", u"avuta", u"avuti", u"avute", u"sono", u"sei", u"è", u"siamo", u"siete", u"sia", u"siate", u"siano", u"sarò", u"sarai", u"sarà", u"saremo", u"sarete", u"saranno", u"sarei", u"saresti", u"sarebbe", u"saremmo", u"sareste", u"sarebbero", u"ero", u"eri", u"era", u"eravamo", u"eravate", u"erano", u"fui", u"fosti", u"fu", u"fummo", u"foste", u"furono", u"fossi", u"fosse", u"fossimo", u"fossero", u"essendo", u"faccio", u"fai", u"facciamo", u"fanno", u"faccia", u"facciate", u"facciano", u"farò", u"farai", u"farà", u"faremo", u"farete", u"faranno", u"farei", u"faresti", u"farebbe", u"faremmo", u"fareste", u"farebbero", u"facevo", u"facevi", u"faceva", u"facevamo", u"facevate", u"facevano", u"feci", u"facesti", u"fece", u"facemmo", u"faceste", u"fecero", u"facessi", u"facesse", u"facessimo", u"facessero", u"facendo", u"sto", u"stai", u"sta", u"stiamo", u"stanno", u"stia", u"stiate", u"stiano", u"starò", u"starai", u"starà", u"staremo", u"starete", u"staranno", u"starei", u"staresti", u"starebbe", u"staremmo", u"stareste", u"starebbero", u"stavo", u"stavi", u"stava", u"stavamo", u"stavate", u"stavano", u"stetti", u"stesti", u"stette", u"stemmo", u"steste", u"stettero", u"stessi", u"stesse", u"stessimo", u"stessero", u"stando",],
    'nl': [u"de", u"en", u"van", u"ik", u"te", u"dat", u"die", u"in", u"een", u"hij", u"het", u"niet", u"zijn", u"is", u"was", u"op", u"aan", u"met", u"als", u"voor", u"had", u"er", u"maar", u"om", u"hem", u"dan", u"zou", u"of", u"wat", u"mijn", u"men", u"dit", u"zo", u"door", u"over", u"ze", u"zich", u"bij", u"ook", u"tot", u"je", u"mij", u"uit", u"der", u"daar", u"haar", u"naar", u"heb", u"hoe", u"heeft", u"hebben", u"deze", u"u", u"want", u"nog", u"zal", u"me", u"zij", u"nu", u"ge", u"geen", u"omdat", u"iets", u"worden", u"toch", u"al", u"waren", u"veel", u"meer", u"doen", u"toen", u"moet", u"ben", u"zonder", u"kan", u"hun", u"dus", u"alles", u"onder", u"ja", u"eens", u"hier", u"wie", u"werd", u"altijd", u"doch", u"wordt", u"wezen", u"kunnen", u"ons", u"zelf", u"tegen", u"na", u"reeds", u"wil", u"kon", u"niets", u"uw", u"iemand", u"geweest", u"andere",],
    'no': [u"og", u"i", u"jeg", u"det", u"at", u"en", u"et", u"den", u"til", u"er", u"som", u"på", u"de", u"med", u"han", u"av", u"ikke", u"ikkje", u"der", u"så", u"var", u"meg", u"seg", u"men", u"ett", u"har", u"om", u"vi", u"min", u"mitt", u"ha", u"hadde", u"hun", u"nå", u"over", u"da", u"ved", u"fra", u"du", u"ut", u"sin", u"dem", u"oss", u"opp", u"man", u"kan", u"hans", u"hvor", u"eller", u"hva", u"skal", u"selv", u"sjøl", u"her", u"alle", u"vil", u"bli", u"ble", u"blei", u"blitt", u"kunne", u"inn", u"når", u"være", u"kom", u"noen", u"noe", u"ville", u"dere", u"som", u"deres", u"kun", u"ja", u"etter", u"ned", u"skulle", u"denne", u"for", u"deg", u"si", u"sine", u"sitt", u"mot", u"å", u"meget", u"hvorfor", u"dette", u"disse", u"uten", u"hvordan", u"ingen", u"din", u"ditt", u"blir", u"samme", u"hvilken", u"hvilke", u"sånn", u"inni", u"mellom", u"vår", u"hver", u"hvem", u"vors", u"hvis", u"både", u"bare", u"enn", u"fordi", u"før", u"mange", u"også", u"slik", u"vært", u"være", u"båe", u"begge", u"siden", u"dykk", u"dykkar", u"dei", u"deira", u"deires", u"deim", u"di", u"då", u"eg", u"ein", u"eit", u"eitt", u"elles", u"honom", u"hjå", u"ho", u"hoe", u"henne", u"hennar", u"hennes", u"hoss", u"hossen", u"ikkje", u"ingi", u"inkje", u"korleis", u"korso", u"kva", u"kvar", u"kvarhelst", u"kven", u"kvi", u"kvifor", u"me", u"medan", u"mi", u"mine", u"mykje", u"no", u"nokon", u"noka", u"nokor", u"noko", u"nokre", u"si", u"sia", u"sidan", u"so", u"somt", u"somme", u"um", u"upp", u"vere", u"vore", u"verte", u"vort", u"varte", u"vart",],
    'pt': [u"de", u"a", u"o", u"que", u"e", u"do", u"da", u"em", u"um", u"para", u"com", u"não", u"uma", u"os", u"no", u"se", u"na", u"por", u"mais", u"as", u"dos", u"como", u"mas", u"ao", u"ele", u"das", u"à", u"seu", u"sua", u"ou", u"quando", u"muito", u"nos", u"já", u"eu", u"também", u"só", u"pelo", u"pela", u"até", u"isso", u"ela", u"entre", u"depois", u"sem", u"mesmo", u"aos", u"seus", u"quem", u"nas", u"me", u"esse", u"eles", u"você", u"essa", u"num", u"nem", u"suas", u"meu", u"às", u"minha", u"numa", u"pelos", u"elas", u"qual", u"nós", u"lhe", u"deles", u"essas", u"esses", u"pelas", u"este", u"dele", u"tu", u"te", u"vocês", u"vos", u"lhes", u"meus", u"minhas", u"teu", u"tua", u"teus", u"tuas", u"nosso", u"nossa", u"nossos", u"nossas", u"dela", u"delas", u"esta", u"estes", u"estas", u"aquele", u"aquela", u"aqueles", u"aquelas", u"isto", u"aquilo", u"estou", u"está", u"estamos", u"estão", u"estive", u"esteve", u"estivemos", u"estiveram", u"estava", u"estávamos", u"estavam", u"estivera", u"estivéramos", u"esteja", u"estejamos", u"estejam", u"estivesse", u"estivéssemos", u"estivessem", u"estiver", u"estivermos", u"estiverem", u"hei", u"há", u"havemos", u"hão", u"houve", u"houvemos", u"houveram", u"houvera", u"houvéramos", u"haja", u"hajamos", u"hajam", u"houvesse", u"houvéssemos", u"houvessem", u"houver", u"houvermos", u"houverem", u"houverei", u"houverá", u"houveremos", u"houverão", u"houveria", u"houveríamos", u"houveriam", u"sou", u"somos", u"são", u"era", u"éramos", u"eram", u"fui", u"foi", u"fomos", u"foram", u"fora", u"fôramos", u"seja", u"sejamos", u"sejam", u"fosse", u"fôssemos", u"fossem", u"for", u"formos", u"forem", u"serei", u"será", u"seremos", u"serão", u"seria", u"seríamos", u"seriam", u"tenho", u"tem", u"temos", u"tém", u"tinha", u"tínhamos", u"tinham", u"tive", u"teve", u"tivemos", u"tiveram", u"tivera", u"tivéramos", u"tenha", u"tenhamos", u"tenham", u"tivesse", u"tivéssemos", u"tivessem", u"tiver", u"tivermos", u"tiverem", u"terei", u"terá", u"teremos", u"terão", u"teria", u"teríamos", u"teriam",],
    'ru': [u"É", u"×", u"×Ï", u"ÎÅ", u"ÞÔÏ", u"ÏÎ", u"ÎÁ", u"Ñ", u"Ó", u"ÓÏ", u"ËÁË", u"Á", u"ÔÏ", u"×ÓÅ", u"ÏÎÁ", u"ÔÁË", u"ÅÇÏ", u"ÎÏ", u"ÄÁ", u"ÔÙ", u"Ë", u"Õ", u"ÖÅ", u"×Ù", u"ÚÁ", u"ÂÙ", u"ÐÏ", u"ÔÏÌØËÏ", u"ÅÅ", u"ÍÎÅ", u"ÂÙÌÏ", u"×ÏÔ", u"ÏÔ", u"ÍÅÎÑ", u"ÅÝÅ", u"ÎÅÔ", u"Ï", u"ÉÚ", u"ÅÍÕ", u"ÔÅÐÅÒØ", u"ËÏÇÄÁ", u"ÄÁÖÅ", u"ÎÕ", u"×ÄÒÕÇ", u"ÌÉ", u"ÅÓÌÉ", u"ÕÖÅ", u"ÉÌÉ", u"ÎÉ", u"ÂÙÔØ", u"ÂÙÌ", u"ÎÅÇÏ", u"ÄÏ", u"×ÁÓ", u"ÎÉÂÕÄØ", u"ÏÐÑÔØ", u"ÕÖ", u"×ÁÍ", u"ÓËÁÚÁÌ", u"×ÅÄØ", u"ÔÁÍ", u"ÐÏÔÏÍ", u"ÓÅÂÑ", u"ÎÉÞÅÇÏ", u"ÅÊ", u"ÍÏÖÅÔ", u"ÏÎÉ", u"ÔÕÔ", u"ÇÄÅ", u"ÅÓÔØ", u"ÎÁÄÏ", u"ÎÅÊ", u"ÄÌÑ", u"ÍÙ", u"ÔÅÂÑ", u"ÉÈ", u"ÞÅÍ", u"ÂÙÌÁ", u"ÓÁÍ", u"ÞÔÏÂ", u"ÂÅÚ", u"ÂÕÄÔÏ", u"ÞÅÌÏ×ÅË", u"ÞÅÇÏ", u"ÒÁÚ", u"ÔÏÖÅ", u"ÓÅÂÅ", u"ÐÏÄ", u"ÖÉÚÎØ", u"ÂÕÄÅÔ", u"Ö", u"ÔÏÇÄÁ", u"ËÔÏ", u"ÜÔÏÔ", u"ÇÏ×ÏÒÉÌ", u"ÔÏÇÏ", u"ÐÏÔÏÍÕ", u"ÜÔÏÇÏ", u"ËÁËÏÊ", u"ÓÏ×ÓÅÍ", u"ÎÉÍ", u"ÚÄÅÓØ", u"ÜÔÏÍ", u"ÏÄÉÎ", u"ÐÏÞÔÉ", u"ÍÏÊ", u"ÔÅÍ", u"ÞÔÏÂÙ", u"ÎÅÅ", u"ËÁÖÅÔÓÑ", u"ÓÅÊÞÁÓ", u"ÂÙÌÉ", u"ËÕÄÁ", u"ÚÁÞÅÍ", u"ÓËÁÚÁÔØ", u"×ÓÅÈ", u"ÎÉËÏÇÄÁ", u"ÓÅÇÏÄÎÑ", u"ÍÏÖÎÏ", u"ÐÒÉ", u"ÎÁËÏÎÅÃ", u"Ä×Á", u"ÏÂ", u"ÄÒÕÇÏÊ", u"ÈÏÔØ", u"ÐÏÓÌÅ", u"ÎÁÄ", u"ÂÏÌØÛÅ", u"ÔÏÔ", u"ÞÅÒÅÚ", u"ÜÔÉ", u"ÎÁÓ", u"ÐÒÏ", u"×ÓÅÇÏ", u"ÎÉÈ", u"ËÁËÁÑ", u"ÍÎÏÇÏ", u"ÒÁÚ×Å", u"ÓËÁÚÁÌÁ", u"ÔÒÉ", u"ÜÔÕ", u"ÍÏÑ", u"×ÐÒÏÞÅÍ", u"ÈÏÒÏÛÏ", u"Ó×ÏÀ", u"ÜÔÏÊ", u"ÐÅÒÅÄ", u"ÉÎÏÇÄÁ", u"ÌÕÞÛÅ", u"ÞÕÔØ", u"ÔÏÍ", u"ÎÅÌØÚÑ", u"ÔÁËÏÊ", u"ÉÍ", u"ÂÏÌÅÅ", u"×ÓÅÇÄÁ", u"ËÏÎÅÞÎÏ", u"×ÓÀ", u"ÍÅÖÄÕ",],
    'se': [u"och", u"det", u"att", u"i", u"en", u"jag", u"hon", u"som", u"han", u"på", u"den", u"med", u"var", u"sig", u"för", u"så", u"till", u"är", u"men", u"ett", u"om", u"hade", u"de", u"av", u"icke", u"mig", u"du", u"henne", u"då", u"sin", u"nu", u"har", u"inte", u"hans", u"honom", u"skulle", u"hennes", u"där", u"min", u"man", u"ej", u"vid", u"kunde", u"något", u"från", u"ut", u"när", u"efter", u"upp", u"vi", u"dem", u"vara", u"vad", u"över", u"än", u"dig", u"kan", u"sina", u"här", u"ha", u"mot", u"alla", u"under", u"någon", u"eller", u"allt", u"mycket", u"sedan", u"ju", u"denna", u"själv", u"detta", u"åt", u"utan", u"varit", u"hur", u"ingen", u"mitt", u"ni", u"bli", u"blev", u"oss", u"din", u"dessa", u"några", u"deras", u"blir", u"mina", u"samma", u"vilken", u"er", u"sådan", u"vår", u"blivit", u"dess", u"inom", u"mellan", u"sådant", u"varför", u"varje", u"vilka", u"ditt", u"vem", u"vilket", u"sitta", u"sådana", u"vart", u"dina", u"vars", u"vårt", u"våra", u"ert", u"era", u"vilkas",],
    }

import hunspell

lang_map={'en': 'en_US',
          'hu': 'hu_HU',
          'da': 'da_DK',
          'de': 'de_DE',
          'es': 'es_ES',
          'fi': 'fi_FI',
          'fr': 'fr_FR',
          'is': 'is_IS',
          'it': 'it_IT',
          'nl': 'nl_NL',
          # 'no': '',
          'pt': 'pt_PT',
          'ru': 'ru_RU',
          'se': 'se_SE',
          }

#DICT_PATH = '/usr/share/hunspell'
#stopstems={}
#for lang in ['en','hu','de']:
#    DICT=DICT_PATH+'/'+lang_map[lang]
#    # start stemming
#    engine = hunspell.HunSpell(DICT+'.dic', DICT+'.aff')
#    stems=[engine.stem(word.encode('utf8')) for word in stopmap[lang]]
#    stopstems[lang]=set([x[0] for x in stems if x])
#print stopstems

stopstems={'de': set(['andere', 'all', 'weiter', 'andern', 'dasselbe', 'selbst', 'anders', 'als', 'wirst', 'dessen', 'dazu', 'auf', 'dich', 'wen', 'demselben', 'aus', 'derselbe', 'sonst', 'hatte', 'hat', 'bin', 'musste', 'waren', 'mein', 'da', 'doch', 'einmal', 'etwa', 'du', 'bis', 'hin', 'viel', 'die', 'haben', 'ihn', 'dir', 'nur', 'sollen', 'hinter', 'welch', 'zu', 'wo', 'es', 'er', 'ohne', 'ich', 'meinen', 'werden', 'indem', 'dein', 'jede', 'denselben', 'wollen', 'dort', 'und', 'manch', 'kannst', 'nicht', 'weg', 'habe', 'auch', 'zur', 'uns', 'bist', 'ob', 'ist', 'weil', 'hier', 'einig', 'solch', 'zum', 'wie', 'aber', 'ihr', 'nach', 'gewesen', 'desselben', 'damit', 'wir', 'ihm', 'einen', 'jene', 'sind', 'oder', 'einigen', 'euer', 'dieselbe', 'was', 'von', 'sondern', 'willst', 'mich', 'nun', 'bei', 'musst', 'der', 'des', 'um', 'dann', 'dem', 'den', 'sein', 'ein', 'wieder', 'noch', 'vom', 'unter', 'gegen', 'am', 'an', 'im', 'zwischen', 'vor', 'in', 'euch', 'derer', 'also', 'sich', 'sie', 'so', 'mir', 'mit', 'durch', 'zwar', 'dies', 'sehr', 'jetzt', 'man', 'kein', 'wird', 'machen', 'unser']),
         'en': set(['all', "she'll", 'just', "don't", 'being', 'over', 'both', 'four', "won't", 'during', 'go', 'still', 'its', 'before', 'now', 'also', "we've", 'less', 'had', 'should', "he'd", 'to', 'only', "here's", 'th', 'under', 'has', 'ought', 'do', 'them', 'his', 'above', 'get', 'very', "they'd", 'cannot', 'every', "you've", 'they', 'not', 'yourselves', 'one', 'him', 'nor', "we'll", 'like', 'did', "they've", "wasn't", 'she', 'each', 'further', 'through', 'where', "mustn't", "isn't", 'few', 'because', 'says', "you'd", 'doing', 'some', 'back', 'up', 'see', 'are', 'our', 'ourselves', "shan't", 'even', 'what', 'said', 'for', 'since', 'below', 'does', "shouldn't", "they'll", 'between', 'new', 'three', 'ever', 'be', 'we', "doesn't", 'never', 'however', 'here', 'let', "hadn't", "aren't", 'by', 'on', 'about', 'would', 'of', 'could', 'against', "weren't", 'or', "can't", 'first', 'this', 'own', 'into', 'yourself', 'down', 'put', 'least', "couldn't", 'old', 'your', 'second', "you're", 'long', 'from', 'her', 'their', 'there', 'two', 'been', 'why', 'whom', "we're", 'goes', 'themselves', 'was', 'until', 'more', 'himself', 'way', 'that', 'with', "didn't", 'but', 'too', 'herself', 'than', 'those', 'he', 'me', "they're", 'myself', 'made', 'these', "hasn't", 'while', "haven't", 'were', 'my', "wouldn't", 'say', "we'd", 'and', 'is', 'am', 'it', 'an', 'high', 'as', 'itself', 'at', 'have', 'in', 'seen', 'any', 'if', 'again', 'no', 'make', 'when', 'same', 'how', 'another', 'other', 'take', 'which', 'aft', 'you', 'out', 'who', 'most', 'whether', 'such', "he'll", 'a', 'off', 'i', 'many', 'well', "she'd", "you'll", 'so', 'five', 'the', 'once']),
         'hu': set([u"által", u"jó", u"valaki", u"azonban", u"nagy", u"itt", u"volta", u"néhány", u"újra", u"olyan", u"kell", u"talán", u"továbbá", u"össze", u"lett", u"valami", u"ami", u"belül", u"számára", u"éppen", u"közül", u"de", u"persze", u"keresztül", u"néha", u"minden", u"egyes", u"volt", u"ilyenkor", u"egész", u"más", u"már", u"valamint", u"saját", u"míg", u"el", u"szemben", u"ismét", u"kívül", u"vele", u"meg", u"eddig", u"egyre", u"ez", u"ilyen", u"sem", u"így", u"jobban", u"csak", u"mely", u"emilyen", u"tovább", u"legalább", u"viszont", u"ekkor", u"be", u"ahol", u"felé", u"s", u"ill.", u"maga", u"semmi", u"vagyis", u"amíg", u"milyen", u"nélkül", u"aki", u"szerint", u"amely", u"mindenki", u"sok", u"mert", u"én", u"erre", u"át", u"és", u"azért", u"akkor", u"illetve", u"szinte", u"hogy", u"hogyan", u"amolyan", u"miért", u"új", u"van", u"fel", u"mintha", u"utolsó", u"aztán", u"teljes", u"nagyon", u"vissza", u"hiszen", u"keres", u"igen", u"mivel", u"egyetlen", u"ott", u"jól", u"általában", u"cikk", u"amikor", u"egyik", u"mindig", u"mikor", u"mellett", u"alatt", u"elég", u"való", u"ugyanis", u"még", u"tehát", u"nincs", u"az", u"bár", u"ezért", u"után", u"arra", u"mint", u"pedig", u"úgy", u"ne", u"másik", u"arról", u"ellen", u"hanem", u"most", u"nem", u"között", u"ahogy", u"rá", u"a", u"egy", u"e", u"azután", u"majd", u"ki", u"benne", u"utána", u"egyéb"]),
         'is': set([u'að', u'aðeins', u'af', u'aftur', u'aldrei', u'allir', u'allt', u'alltaf', u'áður', u'áfram', u'átt', u'bara', u'bíða', u'dagur', u'e', u'eða', u'ef', u'eftir', u'eiga', u'einhver', u'einn', u'eins', u'eitthvað', u'ekkert', u'ekki', u'en', u'enginn', u'enn', u'ertu', u'ég', u'fara', u'fá', u'fer', u'finna', u'frá', u'fyrir', u'fyrirgefa', u'förum', u'gera', u'gert', u'geta', u'gott', u'góður', u'guð', u'hafa', u'halda', u'hana', u'hann', u'hans', u'hefurðu', u'heim', u'henni', u'herra', u'hér', u'hérna', u'hingað', u'hjá', u'honum', u'hr', u'hún', u'hvar', u'hver', u'hvernig', u'inn', u'í', u'já', u'kannski', u'koma', u'kominn', u'lag', u'lagi', u'láta', u'líka', u'líkur', u'maður', u'með', u'mega', u'mér', u'mig', u'mikið', u'minn', u'mitt', u'mín', u'mjög', u'nei', u'niður', u'nú', u'núna', u'of', u'og', u'okkar', u'okkur', u'pabbi', u'rétt', u'sama', u'saman', u'sá', u'segja', u'sem', u'sig', u'sjá', u'skulu', u'svo', u'svona', u'takk', u'tala', u'til', u'tími', u'um', u'upp', u'úr', u'út', u'vegna', u'veistu', u'vel', u'velja', u'vera', u'verða', u'verð', u'við', u'viður', u'vilja', u'viltu', u'vita', u'væri', u'yfir', u'ykkur', u'það', u'þakka', u'þar', u'þarna', u'þau', u'þá', u'þegar', u'þeim', u'þeir', u'þess', u'þessa', u'þessi', u'þessu', u'þetta', u'þér', u'þið', u'þig', u'þinn', u'þín', u'þurfa', u'þú', u'því', u'þær', u'ætla',]),
} 
