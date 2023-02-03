import feedparser
from dateutil import parser



# data = []
# NBC = feedparser.parse("https://www.click2houston.com/arc/outboundfeeds/rss/category/news/local/?outputType=xml&size=10")
# NBC_Entries = NBC.entries  
# for item in NBC_Entries:
#     title = item['title']  
#     print(title)

# print(NBC_Entries)


# def sort_dict_by_value(d, reverse = False):
#   return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

# print("Original dictionary elements:")
# colors = {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}

# print(colors)
# print("\nSort (ascending) the said dictionary elements by value:")
# print(sort_dict_by_value(colors))
# print("\nSort (descending) the said dictionary elements by value:")
# print(sort_dict_by_value(colors, True))


publishedTime = [
    {
     "published": parser.parse("Fri, 27 Jan 2023 00:06:07 +0000"),
    },
    {
    "published": parser.parse("Thu, 26 Jan 2023 14:39:44 GMT"),
    },
    {
    "published": parser.parse("Thu, 26 Jan 2023 20:14:39 GMT"),
    },
]

sorted_dict = sorted(publishedTime["published"], key=lambda item: item[1])

print(sorted_dict)

# sorted_dict = sorted([(value, key)
# for (key, value) in publishedTime.items()])


# sorted_dict = sorted(publishedTime["published"])

# print(sorted_dict)

# x = parser.parse("Fri, 27 Jan 2023 00:06:07 +0000")

# x =[parser.parse("Fri, 27 Jan 2023 00:06:07 +0000"),parser.parse("Thu, 26 Jan 2023 14:39:44 GMT"),parser.parse("Thu, 26 Jan 2023 20:14:39 GMT") ]
# print(sorted(x))