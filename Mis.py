# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib2,urllib,cookielib,os,re,time,datetime,threading
from bs4 import BeautifulSoup

class MIS:
  
  REFERERPAGE = 'http://mis.uic.edu.hk/mis/usr/index.do'
  LOGINPAGE = 'http://mis.uic.edu.hk/mis/usr/login.sec'
  BASEURL = 'http://mis.uic.edu.hk/mis/student/es/'
  ELECTIVE = 'http://mis.uic.edu.hk/mis/student/es/elective.do'
  ELEDETAIL = 'http://mis.uic.edu.hk/mis/student/es/eleDetail.do'
  SELECTPAGE = 'http://mis.uic.edu.hk/mis/student/es/select.do'

  DATAFILE = 'targetCourses.txt'


  def __init__(self, username, password):
    self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    self.opener.addheaders = [('Referer',self.REFERERPAGE)]
    self.targetCourses = []
    self.courses = []
    self.queryResult = []
    self.__login(username,password)
    self.__loadTargetCousesFromDataFile()
    self.__getAllCourses()


  def __getSoup(self,pageURL,paramaters=None):
    try:
      page = self.opener.open(pageURL,paramaters)
      html = "".join([line.strip() for line in page.read().decode('utf8').split("\n")])
      soup = BeautifulSoup(html)
      page.close()
      return soup
    except urllib2.URLError as e:
      print 'network error'
      print e
      exit(-1)
      

    
  def __login(self,username,password):
    paramaters = urllib.urlencode({'j_username':username,'j_password':password,'usertype':'student'})
    soup = self.__getSoup(self.LOGINPAGE,paramaters)
    try:
      who = soup.find("dd", "name").contents[1].contents[2].encode('utf-8')
    except AttributeError as e:
      print 'Login Failed'      
    else:
      print "\nWelcome, %s \n" % who.decode('utf8')


  def __getViewCoursesLink(self):
    soup = self.__getSoup(self.ELECTIVE)
    viewCoursesLinks = soup.findAll(title="Select Course")
    courseLinks = []
    for link in viewCoursesLinks:
      courseLinks.append(self.BASEURL + link['href'])
    return courseLinks


  def __getAllCourses(self):
    courseLinks = self.__getViewCoursesLink()
    for link in courseLinks:
      soup = self.__getSoup(link)
      courses = soup.find_all('td',id=True)
      for course in courses:
        self.courses.append({'id':course['id'],'name':course.string,'typeId':link[link.find('=')+1:]})


  def __selectCoursesFromqueryResult(self,targetList):
    for i in targetList:
      i = int(i)
      self.targetCourses.append(self.queryResult[i])


  def __loadTargetCousesFromDataFile(self):
    dataFilePath = os.path.abspath('.')+'/'+self.DATAFILE
    try:
      dataFile = open(dataFilePath,'r+')
      for line in dataFile.readlines():
        courseItems = line[0:-2].split(',')
        course = {}
        course['name'] = courseItems[0]
        course['id'] = courseItems[1]
        course['typeId'] = courseItems[2]
        self.targetCourses.append(course)
    except IOError as e:
      pass
   

  def displayAllCourses(self):
    print '-------------------------------------------\n'
    print '| Here are all the courses to be selected |\n'
    print '-------------------------------------------\n'
    for course in self.courses:
      print course.get('name')


  def findCourse(self,keyword=None):
    if not keyword:
      keyword = raw_input("plese input the keyword of course:")
    
    for course in self.courses:
      if course.get('name').lower().find(keyword.lower()) != -1:
        self.queryResult.append(course)


  def printqueryResult(self):
    print '\n'
    print '**** Here are all the result of finding the courses ****\n'   
    for i in range(len(self.queryResult)):
      print '[%d]' % i, self.queryResult[i].get('name')
    print '\n'


  def printTargetCourses(self):
    if self.targetCourses:
      print '**** Here are all your target courses ****\n'   
      for course in self.targetCourses:
        print course.get('name')
      print '\n'
    else:
      print 'No target course yet'


  def prepareSelect(self,keyword=None):
    if not self.courses:
      print "you can not select any course"
      return None
    if not keyword:
      keyword = raw_input("plese input the keyword of course:")
    self.findCourse(keyword)
    if not self.queryResult:
      print "Sorry, cannot find the course."
    else:
      self.printqueryResult()
      print 'plese input the number of the courses '
      print 'e.g: 1,2,3 \n'
      targetList = raw_input('choose:')
      print '\n'
      targetList = targetList.split(',')
      self.__selectCoursesFromqueryResult(targetList)


  def savetargetCourses(self):
    dataFilePath = os.path.abspath('.')+'/'+self.DATAFILE
    dataFile = open(dataFilePath,'w')
    for course in self.targetCourses:
      dataFile.write('%s,%s,%s\n' % (course.get('name'),course.get('id'),course.get('typeId')))
    dataFile.close()
   # print "save target courses finish"


  def selectSpecificCourse(self,course):
    parameters=urllib.urlencode({'id':course.get('id'),'electiveTypeId':course.get('typeId')})
    soup = self.__getSoup(self.SELECTPAGE,parameters)
    msg =  soup.find_all('script')[-1]
    p = re.compile(r"showMessage\('.+'\)")
    for m in p.finditer(str(msg)):
      msg = m.group().decode('utf8')
    return msg[msg.find('('):]


  def repeat(self,course):
    #self.mutex.acquire() 
    totleTimes = self.times
    while self.times > 0:     
      print course.get('name'),"-------", self.selectSpecificCourse(course) +"\n"
      self.times -= 1
      print "times:"+str(totleTimes - self.times), datetime.datetime.now()
    #self.mutex.release() 
     


  def testing(self):
    c = self.targetCourses[1]
    print self.selectSpecificCourse(c)


   #多线程提交选课请求。
  def multiThreading(self):
    dstart = datetime.datetime.now() 
    print "Main Thread Start At: " , dstart 

    self.times = 20
    self.sleepTime = 1.5
    course = self.targetCourses[0]

    thread_pool = [] 
    self.mutex = threading.Lock() 

    for i in range(10): 
      th = threading.Thread(target=self.repeat,args=(course,)) 
      thread_pool.append(th) 
       
    for i in range(10): 
      thread_pool[i].start() 

    for i in range(10): 
      threading.Thread.join(thread_pool[i]) 

    dend = datetime.datetime.now() 
    print "Main Thread End at: " ,dend , " time span " , dend-dstart;


def main():
  #xingzhi = MIS('studentID','password')
  #xingzhi.prepareSelect()
  #xingzhi.savetargetCourses()
  #xingzhi.multiThreading()
  #xingzhi.testing()
  # xingzhi.displayAllCourses()
  
  #
  # xingzhi.printTargetCourses()
  #xingzhi.testing()
  
  # xingzhi.findCourse()
  # xingzhi.printqueryResult()
  #xingzhi.prepareSelect("Music")
  #xingzhi.select()

if __name__ == "__main__":
    main()
