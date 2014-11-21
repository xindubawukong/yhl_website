# coding: utf-8
from pymongo import *
import pymongo
import json
import jieba
from bson import ObjectId
################################################
MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017
MONGO_USER = ""
MONGO_PASS = ""
################################################

search_field = [
"gender",
"coach",
"title",
"team_name",
"coach",
"class",
"name",
"gender",
"department"
]

men = "new_test1105"

class MongoClient(object):
	"""docstring for  MongoClient"""
	def __init__(self,
				 host=MONGO_HOST,
                 port=MONGO_PORT,
                 username=MONGO_USER,
                 password=MONGO_PASS):
		self.db = Connection(host, port)["testm"]
		self.db[men].ensure_index('s_id', unique=True);
	#doc_type 为 人的表的名称，如“man”
	def get_doc_by_id(self, doc_type, _id):
		return self.db[doc_type].find_one(dict(_id=_id))

	def insert_doc(self, doc_type, doc):
		_id = self.db[doc_type].insert(doc)
		return _id
	
	def get_doc_by_name(self, doc_type, name):
		return self.db[doc_type].find_one(dict(name=name))	

	def get_doc_by_student_id(self, doc_type, s_id):
		return self.db[doc_type].find_one(dict(s_id=s_id))

	def get_doc_by_team(self, doc_type, team):
		g = self.db[doc_type].find(dict(team=team))
		lists = []
		for each in g:
			lists.append(each)
		return lists
	
	def remove_doc_by_name(self, doc_type, name):
		return self.db[doc_type].remove(dict(name=name))

	def update_doc_by_s_id(self, s_id, doc_type, change_type, change):
		return self.db[doc_type].update(dict(s_id=s_id),  {'$set':{change_type:change}})

	def update_racing_score(self, s_id, racing_name, racing_score):
		s = self.db[doc_type].find_one(dict(s_id=s_id))
		gl = s["score"]
		racelis = []
		racelis.append(racing_name)
		racelis.append(racing_score)
		gl.append(racelis)
		self.db["racing"].insert(racelis)
		self.db[doc_type].update(dict(s_id=s_id),  {'$set':{"score":gl}})

	def search_doc(self, doc_type, str1):
		lists = []
		str_list = []
		ll = str1.split()
		for str in ll:
			str_listg = jieba.cut(str)
			for each in str_listg:
				str_list.append(each)
		
		l = len(str_list)
		k = 0

		for each in self.db[doc_type].find():
			k = 0
			for seg in str_list:
				flag = 0
				for field in search_field:
					if seg in each[field]:
						print seg, each[field]
						flag = 1
						break
				if flag == 1:
					k += 1
			if k >= l / 2.0:
				lists.append(each)
		return lists

	#doctype 为资源
	def insert_resource(self, doc_type, doc):
		_id = self.db[doc_type].insert(doc)
		return _id

	def get_resource(self, doc_type):
		g = self.db[doc_type].find().sort([("date", pymongo.ASCENDING)])
		lists = []
		for each in g:
			lists.append(each)
		return lists
	def get_resource_by_id(self, doc_type, _id):
		return self.db[doc_type].find_one(dict(_id=ObjectId(_id)))


	#doctype 为 申请
	def insert_application(self, doc_type, doc):
		_id = self.db[doc_type].insert(doc)
		return _id

	def get_application(self, doc_type):
		g = self.db[doc_type].find().sort([("date", pymongo.ASCENDING)])
		lists = []
		for each in g:
			lists.append(each)
		return lists


	def get_user_application(self, doc_type, username):
		g = self.db[doc_type].find({'s_id': username}).sort([("date", pymongo.ASCENDING)])
		lists = []
		for each in g:
			lists.append(each)
		return lists

	def change_application_state(self, doc_type, state, _id):
		#state 是"accepted" # rejected \ suspending 中的一个
		self.db[doc_type].update({"_id": ObjectId(_id)}, {"$set":{"state":state}})


	#doctype 为 teamApplication
	def insert_teamApplication(self, doc_type, doc):
		_id = self.db[doc_type].insert(doc)
		return _id

	def get_teamApplication(self, doc_type):
		g = self.db[doc_type].find().sort([("date", pymongo.ASCENDING)])
		lists = []
		for each in g:
			lists.append(each)
		return lists


	def get_teamApplication_by_id(self, doc_type, _id):
		return self.db[doc_type].find_one(dict(_id=ObjectId(_id)))


	def get_user_teamApplication(self, doc_type, username):
		g = self.db[doc_type].find({'s_id': username}).sort([("date", pymongo.ASCENDING)])
		lists = []
		for each in g:
			lists.append(each)
		return lists

	def change_teamApplication_state(self, doc_type, state, _id):
		#state 是"accepted" # rejected \ suspending 中的一个
		self.db[doc_type].update({"_id": ObjectId(_id)}, {"$set":{"state":state}})
		


'''
teamApplication = {
	"s_id" : "2012011000",
	"teamName" : "244545313",
	"date" : "20120111",
	"state" : "accepted" # rejected \ suspending
}


application = {
	"s_id" : "2012011000",
	"resource_id" : "244545313",
	"date" : "20120111",
	"state" : "accepted" # rejected \ suspending
}


resource = {
	"loc" : "综体",
	"date" : "20120111",
	"desc" : "kdasjdkasjdkjdkdasdjas"
}


MClient = MongoClient()
post = {
	"team_type" : "AA",
	"title" : "队长",
	"team_name" : "xxx",
	"coach" : "xxx",
	"name" : "杨凯峪",
	"gender" : "男",
	"birthday" : ["1999", "1", "1"],
	"political_status" : "党员",
	"department":"计算机",
	"class" : "22",
	"s_id" : "20111111113",
	"rank" : {"GPA" : "90", "ranking" : "10", "total" : "40"},
	"telephone" : "18811333333",
	"email" : "askd@gmail.com",
	"Address" :	"紫荆2#",
	"social_work" : [],
	"score"		  : []
}
post1 = {
	"team_type" : "AA",
	"title" : "队长",
	"team_name" : "xxx",
	"coach" : "xxx",
	"name" : "徐梓哲",
	"gender" : "男",
	"birthday" : ["1999", "1", "1"],
	"political_status" : "团员",
	"department":"自动化",
	"class" : "23",
	"s_id" : "20111111111",
	"rank" : {"GPA" : "90", "ranking" : "10", "total" : "40"},
	"telephone" : "18811333333",
	"email" : "askd@gmail.com",
	"Address" :	"紫荆2#",
	"social_work" : [],
	"score"		  : []
}
post2 = {
	"team_type" : "AA",
	"title" : "队长",
	"team_name" : "xxx",
	"coach" : "xxx",
	"name" : "魏洪浩",
	"gender" : "男",
	"birthday" : ["1999", "1", "1"],
	"political_status" : "团员",
	"department":"软院",
	"class" : "25",
	"s_id" : "20111111112",
	"rank" : {"GPA" : "90", "ranking" : "10", "total" : "40"},
	"telephone" : "18811333333",
	"email" : "askd@gmail.com",
	"Address" :	"紫荆2#",
	"social_work" : [],
	"score"		  : []
}
post3 = {
	"team_type" : "AA",
	"title" : "队长",
	"team_name" : "xxx",
	"coach" : "xxx",
	"name" : "代文韬",
	"gender" : "男",
	"birthday" : ["1999", "1", "1"],
	"political_status" : "团员",
	"department":"电子",
	"class" : "24",
	"s_id" : "20111111114",
	"rank" : {"GPA" : "90", "ranking" : "10", "total" : "40"},
	"telephone" : "18811333333",
	"email" : "askd@gmail.com",
	"Address" :	"紫荆2#",
	"social_work" : [],
	"score"		  : []
}
MClient.insert_doc("new_test1105", post)
MClient.insert_doc("new_test1105", post1)
MClient.insert_doc("new_test1105", post2)
MClient.insert_doc("new_test1105", post3)

print MClient.search_doc("new_test1105", "电子代")


'''

'''
client = MongoClient()
db = client.test_database
collection = db.test_collection

post = {
	"team" : "A",
	"title" : "captain",
	"t_name" : "xxx",
	"coach" : "xxx",
	"name" : "xxx",
	"gender" : "male",
	"birthday" : ["1999", "1", "1"],
	"pos" : {"department":"cs", "class" : "23"} ,
	"s_id" : "20111111111",
	"rank" : {"GPA" : "90", "ranking" : "10", "total" : "40"},
	"telephone" : "18811333333",
	"email" : "askd@gmail.com",
	"Address" :	"zijing2#",
	"social_work" : "dsada"
}


posts = db.post1
post_id = posts.insert(post)

'''