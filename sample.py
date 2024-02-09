def blog():
	url = 'https://medium.com/feed/@alexmarginean'

	response = requests.get(url)
	content = BeautifulSoup(response.content, 'html.parser')

	content = str(content).replace('<![CDATA[','').replace(']]>','')
	content = BeautifulSoup(content, 'html.parser')

	articles = content.find_all('item')
	articles_html = []

	for article in articles:
		article_html = []
		tag = article.find('category')
		if tag != None:
			title = article.find('title').text
			link = article.find('guid').text
			subtitle = None
			for subtitle in article.find_all('p', attrs={'class': 'medium-feed-snippet'}):
				subtitle = subtitle.text
			for img in article.find_all('img', src=True):
				img = img['src']
			date = article.find('pubdate').text
			date = str(date).replace(' GMT','')
			date = date[:16]

			if subtitle == None:
				subtitle = article.find('content:encoded')
				img = subtitle.find('img', src=True)
				img = img['src']

				subtitle = subtitle.text

			subtitle = subtitle[:130]
			subtitle = subtitle+"..."
