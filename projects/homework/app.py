from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient('localhost',27017)
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/homework', methods=['POST'])
def save():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    number_receive = request.form['number_give']

    orders = {
            'name':name_receive, 
            'count':count_receive, 
            'address':address_receive, 
            'number':number_receive
        }
    db.orders.insert_one(orders)
    return jsonify({'result':'success','msg':'등록 성공했습니다!'})
        
@app.route('/homework', methods=['GET'])
def find():
    # DB에 저장된 값을 조회
    orders = list(db.orders.find({}, {'_id':0}))
    # 조회한 값을 클라이언트에 반환
    return jsonify({'result':'success','orders': orders})

if __name__ == '__main__':
    app.run( '0.0.0.0' , port=5000, debug=True)