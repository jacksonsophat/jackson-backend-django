import feedparser




data = []
KHOU = feedparser.parse("https://www.khou.com/feeds/syndication/rss/news/local")
KHOU_Entries = KHOU.entries  
for item in KHOU_Entries:
    title = item['title']  
    print(title)

# print(KHOU_Entries)

