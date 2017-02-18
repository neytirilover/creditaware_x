'''
This api has two classes

Card has the following method

Card(ip, user, pwd, db) connect to database
Card.select(id) select card of id
Card.search(text) search the card with similar name or company name to text
Card.search_by_id(id) search Card by id
Card.get_all_card() get all card infomation include id, name, comp_name
Card.update(data) update card infomation with data
Card.insert(data) insert new card with data
Card.set_pic(data) set picture
Card.delete(id) delete a card

User has the following method


'''




import _mysql
import os
import md5
import random, string, time, json, shutil


class Db:
	def __init__(self, ip, user, pwd, db):
		self.ip, self.user, self.pwd, self.db = ip, user, pwd, db

	def print_database_error(self, q):
		print "Data base excution error for '"+q+"'"
	
	def get_new_db(self):
		return _mysql.connect(self.ip, self.user, self.pwd, self.db)	
	
	def get_data(self, db):
		r = db.use_result()	
		result, temp = [], r.fetch_row()
		while(len(temp) != 0):
			result.append(temp[0])
			temp = r.fetch_row()
		return result
	def excute(self, query):
		try:
			r = self.get_new_db()
			r.query(query)
		except:
			self.print_database_error(query)
			return False
		return r

class Card(Db):
	def make_dict(self, l):
		if len(l) != 1 or len(l[0]) != 18: return None
		l = l[0]
		return {"name":l[1], "comp_name":l[2], "ann_fee":l[3], "reward_type":l[4], "reward_points":l[5], "reward_deadline":l[6], "reward_spend":l[7], "comment":l[8], "isChase524":l[9], "isChargeCard":l[10],"isFirstYearFree":l[11], "cardGrade":l[12], "isKeepable":l[13],"isHotelC":l[14],"isAirlineC":l[15],"hasFTF":l[16], "isDowngradable":l[17]}
	
	def select(self, id):
		self.id = id
		self.data = self.make_dict(self.search_by_id(id))

	def search_query(self, query):
		try:
			db = self.get_new_db()
			db.query(query)
		except:
			self.print_database_error(query)
			return
		return self.get_data(db)
	
	def search(self, text):
		query = "select * from card_info where `name` sounds like '"+text+"' or `comp_name` sounds like '"+text+"'"
		return self.search_query(query)
		
	def search_by_id(self, id):
		if type(id) is list:
			idl = ','.join(id)
			query = "select * from card_info where `id` in ("+idl+")"
		else:
			query = "select * from card_info where id = '"+id+"'"
		return self.search_query(query)
	
	# Be caution to use this function!
	def get_all_card(self):
		query = "select id, name, comp_name from card_info"
		return self.search_query(query)

		
	
	def update(self, new_data):
		if hasattr(self, 'data'):
			self.data.update(new_data)
		else:
			return False
		data = ""
		for key, value in new_data.iteritems():
			data += key +" = "+value+", "
		query = "update card_info set "+data[:-2]+" where id='"+self.id+"'"
		try:
			r = self.get_new_db()
			r.query(query)
		except:
			self.print_database_error(query)
		return True

	def insert(self, data):
		value = "0, '"+data['name']+"','"+data['comp_name']+"','"+data['ann_fee']+"','"+data['reward_type']+"','"+data['reward_points']+"','"+data['reward_deadline']+"','"+data['reward_spend']+"','"+data['comment']+"','"+data['isChase524']+"','"+data['isChargeCard']+"','"+data['isFirstYearFree']+"','"+data['cardGrade']+"','"+data['isKeepable']+"','"+data['isHotelC']+"','"+data['isAirlineC']+"','"+data['hasFTF']+"','"+data['isDowngradable']+"'"
		query = "insert into card_info values("+value+")"
		self.excute(query)
		return True
	
	def set_pic(self, data):
		name = self.id
		with open('./img/'+name, 'wb') as f:
			f.write(data)
		f.close()

	def delete(self, id):
		query = "delete from card_info where id='"+id+"'"
		self.excute(query)
		try:		
			os.remove('./img/'+id)
		except:
			print "Card no picture!"
		return True	
  
	def addColumn(self, clm):
		if len(clm)==0:
			print("You cannot add a new column with nothing!")
			return False
		query="alter table"+" card_info "+" add column "+clm
		self.excute(query)
		return True


class User(Db):
	def isExist(self, email):
		query = "select name from user_info where email='"+email+"'"
		db = self.excute(query)
		res = self.get_data(db)
		if len(res) >= 1:
			return True
		return False
	
	def register(self, email, name, pwd):
		pwd = md5.new(pwd).hexdigest()
		query = "insert into user_info values('"+email+"','"+name+"','"+pwd+"','','','')"
		self.excute(query)
		pp = './userinfo/'+md5.new(email).hexdigest()
		try:
			os.mkdir(pp)
		except:
			print "Can't create folder for user "+name
			return False
		return True
	
	def new_session(self):
		ss_random = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
		ss_time = time.strftime('%Y-%m-%d %H:%M:%S')
		query = "update user_info set session_key='"+ss_random+"', session_time='"+ss_time+"' where email='"+self.id+"'"
		self.excute(query)
		return ss_random, ss_time

	def session_check(self, email, skey):
		query = "select session_key, session_time from user_info where email='"+email+"'"
		dd = self.get_data(self.excute(query))[0]
		ctime = time.gmtime()
		stime = time.strptime(dd[1],'%Y-%m-%d %H:%M:%S')
		t = (time.mktime(ctime)-time.mktime(stime))/3600
		if t <= 48 and dd[0] == skey:
			self.id = email
			return True
		return False

	def login(self, email, pwd):
		if not self.isExist(email):
			print "No user with email "+email
			return False
		pwd = md5.new(pwd).hexdigest()
		query = "select pwd from user_info where email='"+email+"'"
		dd = self.get_data(self.excute(query))[0]
		if dd[0] == pwd:
			self.id = email
			return self.new_session()
		return False

	def change_pwd(self, pwd):
		query = "update user_info set pwd='"+md5.new(pwd).hexdigest()+"' where email='"+self.id+"'"
		if not self.excute(query):
			return False
		return True

	def change_name(self, name):
		query = "update user_info set name='"+name+"' where email='"+self.id+"'"
		if not self.excute(query):
			return False
		return True

	def get(self, filename):
		path = './userinfo/'+md5.new(self.id).hexdigest()+'/'+filename
		cc = {}
		try:
			with open(path, 'r') as f:
				cc = f.read()
				if cc != "":				
					cc = json.loads(cc)
				else:
					cc = {}
			f.close()
		except:
			False
		return cc
	def del_(self, id, filename):
		path = './userinfo/'+md5.new(self.id).hexdigest()+'/'+filename
		cc = self.get(filename)
		cc.pop(id, None)
		try:
			with open(path, 'w') as f:
				f.write(json.dumps(cc))
			f.close()
		except:
			return False
		return True
	
	def add(self, data, filename):
		path = './userinfo/'+md5.new(self.id).hexdigest()+'/'+filename
		cc = self.get(filename)
		cc.update(data)
		try:
			with open(path, 'w') as f:
				f.write(json.dumps(cc))
			f.close()
		except:
			return False
		return True
	
	def get_my_card(self):
		return self.get('mycard.json')
	
	def add_card(self, data):
		return self.add(data, 'mycard.json')

	def del_card(self, id):
		return self.del_(id, 'mycard.json')
	
	def my_list(self):
		c = Card(self.ip, self.user, self.pwd, self.db)
		l = c.get_all_card()
		cc = self.get_my_card()
		res = []
		for i in l:
			if not i[0] in cc:
				res.append(i)
		return res

	
	def get_rule(self):
		return self.get('rule.json')
	
	def find_new_key(self, dic):
		for i in range(1000):
			if not 'r'+str(i) in dic:
				return 'r'+str(i)
		return 'not new keys!'		
		
	def add_rule(self, id1, id2):
		rr = self.get_rule()
		if not [id1, id2] in rr.values():
			nk = self.find_new_key(rr)
			return self.add({nk:[id1, id2]}, 'rule.json')

	def del_rule(self, rid):
		return 	self.del_(rid, 'rule.json')	
	
	#this function can only be called by administrator!
	def delete(self, email):
		query = "delete from user_info where id='"+email+"'"
		self.excute(query)
		path = './userinfo/'+md5.new(email).hexdigest()+'/'
		shutil.rmtree(path)





#c.addColumn('isChase524 INT')
#c.addColumn('isChargeCard INT') 
#c.addColumn('isFirstYearFree INT')
#c.addColumn('cardGrade INT')
#c.addColumn('isKeepable INT')
#c.addColumn('isHotelC INT')
#c.addColumn('isAirlineC INT')
#c.addColumn('hasFTF INT')
#c.addColumn('isDowngradable INT')

#c.insert({'comp_name': 'Discover', 'reward_points': '0', 'ann_fee': '0', 'name': 'Discover Student', 'reward_deadline': '0', 'reward_type': 'cash back', 'reward_spend': '0', 'comment': '', 'isChase524':'0', 'isChargeCard':'0', 'isFirstYearFree':'1', 'cardGrade':'0', 'isKeepable':'1111', 'isHotelC':'0', 'isAirlineC':'0', 'hasFTF':'1', 'isDowngradable':'0'})
#c.delete('6')
#with open('./miles-card.png', 'rb') as f:
#	data = f.read()
#f.close()
#c.select('1')
#c.set_pic(data)
#print c.get_all_card()

#u.new_session()

#print u.add_card({'2':['2017-02-09 22:13:16', '4000', '100']})
#print u.add_card({'3':['2017-02-09 22:13:16', '4000', '100']})
#print u.add_card({'4':['2017-02-09 22:13:16', '4000', '100']})
#u.del_card('4')
#print u.get_my_card()
#print u.add_rule('1','2')
#print u.add_rule('1','3')
#print u.get_rule()
#print u.my_list()




