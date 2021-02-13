from random import randint

fourfourtwo = {
'id':0,
'name':'Four Four Two',
'url': 'https://www.fourfourtwo.com/news/page/{}'.format(randint(8000,15180))
}

mirror = {
'id':1,
'name':'Mirror',
'url':'https://www.mirror.co.uk/sport/football/news/?pageNumber={}'.format(randint(3997,7400))
}

talksport = {
'id':2,
'name':'Talksport',
'url':'https://talksport.com/football/page/{}/'.format(randint(2150,4184))
}

caughtoffside = {
'id':3,
'name':'Caught Offside',
'url':'https://www.caughtoffside.com/tags/transfer-rumours/page/{}/'.format(randint(2400,4150))
}

tribalfootball = {
'id':4,
'name': 'Tribal Football',
'url':'https://www.tribalfootball.com/transfers?page={}'.format(randint(3000,3500))
}

football_italia = {
'id':5,
'name': 'Football Italia',
'url':'https://www.football-italia.net/news?page={}'.format(2700,3800)
}
