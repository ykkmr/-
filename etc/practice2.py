from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 
movie = db.movies.find_one({'title':'매트릭스'}) # movie라는 변수를 꼭 써줘야 평점(star)을 찾는것 같이 이용할 수 있다.
print(movie['star'])

movies = list(db.movies.find({'star':movie['star']})) # 찾을 대상이 여러개일때는 list를 꼭 붙여준다.
print(movies[0]['title'])

for title in movies:
 print(title['title'])


db.movies.update_many({'star':movie['star']}, {'$set':{'star':0}})
