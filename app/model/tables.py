#coding=utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:levis822@localhost:3306/med'
db = SQLAlchemy(app)


class ChineseDisease(db.Model):
   CDISid = db.Column(db.String(36), nullable=False, primary_key=True)
   code = db.Column(db.String(20), nullable=False)
   name = db.Column(db.String(100), nullable=False)
   parentcode = db.Column(db.String(20), nullable=False) #comment '无父节点,用-1代表'
   level = db.Column(db.Boolean, nullable=False) #comment '从1开始'
   isClassical = db.Column(db.Boolean, nullable=False, default=1) #comment '1:是标准的;0:非标准的'
   SPETid = db.Column(db.String(36), nullable=False, default=' ')
   illustration = db.Column(db.Text, nullable=False, default=' ')
   createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
   optrid = db.Column(db.String(36), nullable=False, default=' ')
   state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'

class dCase(db.Model):
   CASEid = db.Column(db.String(36), nullable=False, primary_key=True)
   SPETid = db.Column(db.String(36), nullable=False, default=' ')
   DTMPid = db.Column(db.String(36), nullable=False, default=' ')
   code = db.Column(db.String(20), nullable=False)
   outpatientCode = db.Column(db.String(20), nullable=False)
   caseKind = db.Column(db.SMALLINT, nullable=False)
   name = db.Column(db.String(20), nullable=False)
   age = db.Column(db.SMALLINT, nullable=False)
   month = db.Column(db.SMALLINT, nullable=False, default=0)
   gender = db.Column(db.Boolean, nullable=False) #comment '0:男;1:女'
   nationality = db.Column(db.Boolean, nullable=False)
   personSort = db.Column(db.Boolean, nullable=False)
   afflication = db.Column(db.String(200), nullable=False, default=' ')
   job = db.Column(db.String(20), nullable=False, default=' ')
   tel = db.Column(db.String(20), nullable=False, default=' ')
   address = db.Column(db.String(200), nullable=False, default=' ')
   birthplace = db.Column(db.String(6), nullable=False)
   liveplace = db.Column(db.String(6), nullable=False)
   education = db.Column(db.Boolean, nullable=False)
   marriage = db.Column(db.Boolean, nullable=False)
   ohistory = db.Column(db.Text, nullable=False, default=' ')
   phistory = db.Column(db.Text, nullable=False, default=' ')
   fhistory = db.Column(db.Text, nullable=False, default=' ')
   allergy = db.Column(db.Text, nullable=False, default=' ')
   extraMed = db.Column(db.String(500), nullable=False, default=' ')
   nhistory = db.Column(db.Text, nullable=False, default=' ')
   mresult = db.Column(db.Boolean, nullable=False)
   vresult = db.Column(db.String(500), nullable=False)
   illustration = db.Column(db.Text, nullable=False, default=' ')
   state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'
   createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
   optrid = db.Column(db.String(36), nullable=False, default=' ')
   hasFile = db.Column(db.Boolean, nullable=False, default=0) #comment '0:没有;1:有'
   preState = db.Column(db.Boolean, nullable=False)

class dMethod(db.Model):
   DMETid = db.Column(db.String(36), nullable=False, primary_key=True)
   code = db.Column(db.String(20), nullable=False)
   name = db.Column(db.String(100), nullable=False)
   parentcode = db.Column(db.String(20), nullable=False) #comment '无父节点,用-1代表'
   level = db.Column(db.Boolean, nullable=False) #comment '从1开始'
   isClassical = db.Column(db.Boolean, nullable=False, default=1) #comment '1:是标准的;0:非标准的'
   SPETid = db.Column(db.String(36), nullable=False, default=' ')
   illustration = db.Column(db.Text, nullable=False, default=' ')
   createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
   optrid = db.Column(db.String(36), nullable=False, default=' ')
   state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'

class dTemplate(db.Model):
   DTMPid = db.Column(db.String(36), nullable=False, primary_key=True)
   code = db.Column(db.String(20), nullable=False)
   name = db.Column(db.String(200), nullable=False)
   useClassCdis = db.Column(db.Boolean, nullable=False, default=0)
   useClassDmet = db.Column(db.Boolean, nullable=False, default=0)
   CDISid = db.Column(db.String(36), nullable=False, default=' ')
   WDISid = db.Column(db.String(36), nullable=False, default=' ')
   SEMCid = db.Column(db.String(36), nullable=False)
   DMETid = db.Column(db.String(36), nullable=False)
   takeWay = db.Column(db.Boolean, nullable=False)
   drugForm = db.Column(db.Boolean, nullable=False)
   SPETid = db.Column(db.String(36), nullable=False, default=' ')
   illustration = db.Column(db.Text, nullable=False, default=' ')
   createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
   optrid = db.Column(db.String(36), nullable=False, default=' ')
   state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'

class diagExam(db.Model):
   DIEXid = db.Column(db.String(36), nullable=False, primary_key=True)
   DIAGid = db.Column(db.String(36))
   EXAMid = db.Column(db.String(36))
   value = db.Column(db.String(200), nullable=False, default=' ')
   date = db.Column(db.DateTime)
   address = db.Column(db.String(100))
   illustration = db.Column(db.Text, nullable=False, default=' ')
   sequence = db.Column(db.INT, nullable=False, default=0)

class diagItem(db.Model):
   DIITid = db.Column(db.String(36), nullable=False, primary_key=True)
   DIREid = db.Column(db.String(36))
   dru_DRUGid = db.Column(db.String(36))
   DRUGid = db.Column(db.String(36))
   quality = db.Column(db.DECIMAL(18,4), nullable=False, default=0)
   sequence = db.Column(db.INT, nullable=False, default=0)
   illustration = db.Column(db.Text, nullable=False, default=' ')

class diagRecipe(db.Model):
   DIREid = db.Column(db.String(36), nullable=False, primary_key=True)
   DIAGid = db.Column(db.String(36))
   FREPid = db.Column(db.String(36))
   isCustomed = db.Column(db.Boolean, nullable=False, default=0)
   name = db.Column(db.String(36), nullable=False, default=' ')
   doctorAdvice = db.Column(db.Text, nullable=False, default=' ')
   drugForm = db.Column(db.Boolean, nullable=False)
   takeWay = db.Column(db.Boolean, nullable=False)
   quality = db.Column(db.SMALLINT, nullable=False)
   produceMethod = db.Column(db.String(100), nullable=False)
   usage = db.Column(db.String(100), nullable=False)

class diagSymptom(db.Model):
   DISYid = db.Column(db.String(36), nullable=False, primary_key=True)
   SYPMid = db.Column(db.String(36))
   DIAGid = db.Column(db.String(36))
   value = db.Column(db.String(200), nullable=False, default=' ')
   illustration = db.Column(db.Text, nullable=False, default=' ')
   sequence = db.Column(db.INT, nullable=False, default=0)

class diagnose(db.Model):
   DIAGid = db.Column(db.String(36), nullable=False, primary_key=True)
   CASEid = db.Column(db.String(36))
   CDISid = db.Column(db.String(36), nullable=False, default=' ')
   CDISid2 = db.Column(db.String(36), nullable=False, default=' ')
   WDISid = db.Column(db.String(36), nullable=False, default=' ')
   WDISid2 = db.Column(db.String(36), nullable=False, default=' ')
   SEMCid = db.Column(db.String(36), nullable=False)
   SEMCid2 = db.Column(db.String(36), nullable=False)
   SEMCid3 = db.Column(db.String(36), nullable=False)
   DMETid = db.Column(db.String(36), nullable=False)
   DMETid2 = db.Column(db.String(36), nullable=False)
   DMETid3 = db.Column(db.String(36), nullable=False)
   DIAGno = db.Column(db.Boolean, nullable=False, default=1)
   DIAGnum = db.Column(db.Boolean, nullable=False)
   DIAGday = db.Column(db.DateTime, nullable=False)
   lunarDay = db.Column(db.String(50), nullable=False, default=' ')
   solarTerm = db.Column(db.Boolean, nullable=False, default=0)
   DIAway = db.Column(db.Boolean, nullable=False, default=0)
   majorSue = db.Column(db.Text, nullable=False)
   illustration = db.Column(db.Text, nullable=False, default=' ')
   optrid = db.Column(db.String(36), nullable=False, default=' ')
   createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
   westernMed = db.Column(db.Text, nullable=False, default=' ')
   other = db.Column(db.Text, nullable=False, default=' ')
   preSEMCid = db.Column(db.String(36), nullable=False)

class drug(db.Model):
   DRUGid = db.Column(db.String(36), nullable=False, primary_key=True)
   code = db.Column(db.String(20), nullable=False)
   name = db.Column(db.String(50), nullable=False)
   unit = db.Column(db.String(10), nullable=False)
   alias = db.Column(db.String(100), nullable=False, default=' ')
   py = db.Column(db.String(20), nullable=False, default=' ')
   wb = db.Column(db.String(20), nullable=False, default=' ')
   isClassical = db.Column(db.Boolean, nullable=False, default=1) #comment '1:是标准的;0:非标准的'
   SPETid = db.Column(db.String(36), nullable=False, default=' ')
   illustration = db.Column(db.Text, nullable=False, default=' ')
   createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
   optrid = db.Column(db.String(36), nullable=False, default=' ')
   state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'

class dtmpExamination(db.Model):
   DTEXid = db.Column(db.String(36), nullable=False, primary_key=True)
   DTMPid = db.Column(db.String(36))
   EXAMid = db.Column(db.String(36))
   sequence = db.Column(db.INT, nullable=False)
   illustration = db.Column(db.Text, nullable=False)

class dtmpSymptom(db.Model):
   DTSYid = db.Column(db.String(36), nullable=False, primary_key=True)
   DTMPid = db.Column(db.String(36))
   SYPMid = db.Column(db.String(36))
   isFirst = db.Column(db.Boolean, nullable=False, default=1)
   sequence = db.Column(db.INT, nullable=False, default=0)
   illustration = db.Column(db.Text, nullable=False, default=' ')

class examination(db.Model):
   EXAMid = db.Column(db.String(36), nullable=False, primary_key=True)
   code = db.Column(db.String(20), nullable=False)
   name = db.Column(db.String(100), nullable=False)
   abbreviation = db.Column(db.String(50), nullable=False, default=' ')
   kind = db.Column(db.Boolean, nullable=False, default=0)
   normalValue = db.Column(db.String(200), nullable=False, default=' ')
   hasFile = db.Column(db.Boolean, nullable=False, default=0) #comment '0:没有;1:有'
   isClassical = db.Column(db.Boolean, nullable=False, default=1) #comment '1:是标准的;0:非标准的'
   SPETid = db.Column(db.String(36), nullable=False, default=' ')
   illustration = db.Column(db.Text, nullable=False, default=' ')
   createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
   optrid = db.Column(db.String(36), nullable=False, default=' ')
   state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'

class fixedrecipe(db.Model):
   FREPid = db.Column(db.String(36), nullable=False, primary_key=True)
   code = db.Column(db.String(20), nullable=False)
   name = db.Column(db.String(50), nullable=False)
   effect = db.Column(db.String(200), nullable=False, default=' ')
   py = db.Column(db.String(20), nullable=False, default=' ')
   wb = db.Column(db.String(20), nullable=False, default=' ')
   isClassical = db.Column(db.Boolean, nullable=False, default=1) #comment '1:是标准的;0:非标准的'
   SPETid = db.Column(db.String(36), nullable=False, default=' ')
   illustration = db.Column(db.Text, nullable=False, default=' ')
   createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
   optrid = db.Column(db.String(36), nullable=False, default=' ')
   state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'

class fixedrecipeItem(db.Model):
   FRITid = db.Column(db.String(36), nullable=False, primary_key=True)
   DRUGid = db.Column(db.String(36))
   FREPid = db.Column(db.String(36))
   quality = db.Column(db.DECIMAL(18,4), nullable=False, default=0)
   sequence = db.Column(db.INT, nullable=False, default=0)
   illustration = db.Column(db.Text, nullable=False, default=' ')

class integratedSym(db.Model):
   INSYid = db.Column(db.String(36), nullable=False, primary_key=True)
   SYPMid = db.Column(db.String(36))
   name = db.Column(db.String(50), nullable=False)
   valSort = db.Column(db.INT, nullable=False)
   sequence = db.Column(db.INT, nullable=False)

class semiotic(db.Model):
   SEMCid = db.Column(db.String(36), nullable=False, primary_key=True)
   CDISid = db.Column(db.String(36))
   code = db.Column(db.String(20), nullable=False)
   groupCode = db.Column(db.String(20), nullable=False, default=' ')
   name = db.Column(db.String(100), nullable=False)
   isClassical = db.Column(db.Boolean, nullable=False, default=1) #comment '1:是标准的;0:非标准的'
   SPETid = db.Column(db.String(36), nullable=False, default=' ')
   illustration = db.Column(db.Text, nullable=False, default=' ')
   createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
   optrid = db.Column(db.String(36), nullable=False, default=' ')
   state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'

class symptom(db.Model):
   SYPMid = db.Column(db.String(36), nullable=False, primary_key=True)
   code = db.Column(db.String(20), nullable=False)
   name = db.Column(db.String(50), nullable=False)
   parentcode = db.Column(db.String(20), nullable=False) #comment '无父节点,用-1代表'
   level = db.Column(db.Boolean, nullable=False) #comment '从1开始'
   kind = db.Column(db.Boolean, nullable=False, default=0) #comment '分为 望、闻、问、切'
   sort = db.Column(db.Boolean, nullable=False, default=1) #comment '1:主症,2:兼症'
   valSort = db.Column(db.INT, nullable=False, default=0) #comment '0:字符串;-1:checkbox;其他:下拉选项'
   hasFile = db.Column(db.Boolean, nullable=False, default=0) #comment '0:没有;1:有'
   isClassical = db.Column(db.Boolean, nullable=False, default=1) #comment '1:是标准的;0:非标准的'
   SPETid = db.Column(db.String(36), nullable=False, default=' ')
   illustration = db.Column(db.Text, nullable=False, default=' ')
   createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
   optrid = db.Column(db.String(36), nullable=False, default=' ')
   state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'

class WestenDisease(db.Model):
   WDISid = db.Column(db.String(36), nullable=False, primary_key=True)
   code = db.Column(db.String(20), nullable=False)
   name = db.Column(db.String(100), nullable=False)
   parentcode = db.Column(db.String(20), nullable=False) #comment '无父节点,用-1代表'
   level = db.Column(db.Boolean, nullable=False) #comment '从1开始'
   isClassical = db.Column(db.Boolean, nullable=False, default=1) #comment '1:是标准的;0:非标准的'
   SPETid = db.Column(db.String(36), nullable=False, default=' ')
   illustration = db.Column(db.Text, nullable=False, default=' ')
   createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
   optrid = db.Column(db.String(36), nullable=False, default=' ')
   state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'
