from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.

db = client.dbsparta  
same_ages = list(db.users.find({'age':21}))

all_users = list(db.users.find())
for user in all_users:
  print(user)

user = db.users.find_one({'name':'bobby'},{'_id':False})
print(user)

db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
user = db.users.find_one({'name':'bobby'})
print(user)

db.users.delete_one({'name':'bobby'})
user = db.users.find_one({'name':'bobby'})
print(user)