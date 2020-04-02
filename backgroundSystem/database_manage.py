import pymysql
import mysql.connector
import time
class DataBase(object):
    def __init__(self,ip,usr,password_,db_):
        self.db = pymysql.connect(host=ip,user=usr,password=password_,database=db_, port=3306,unix_socket=None, charset='utf8')
        self.cursor = self.db.cursor()
    def creatTables(self):
        sql = '''
                CREATE TABLE IF NOT EXISTS `user_info`(
                `user_id` INT UNSIGNED AUTO_INCREMENT,
                `user_name` VARCHAR(20) NOT NULL,
                `password` VARCHAR(16) NOT NULL,
                `e-mail` VARCHAR(32) NOT NULL,
                `reserve_1` VARCHAR(20),
                `reserve_2` VARCHAR(20),
                `reserve_3` VARCHAR(20),
                PRIMARY KEY ( `user_id` )
                )ENGINE=InnoDB DEFAULT CHARSET=utf8;
                '''
        self.exeSql(sql)
        sql = '''
                CREATE TABLE IF NOT EXISTS `course_info`(
                `course_id` INT UNSIGNED AUTO_INCREMENT,
                `course_name` VARCHAR(40) NOT NULL,
                `begin_time` VARCHAR(26) NOT NULL,
                `teacher` VARCHAR(10) NOT NULL,
                `belong_class` VARCHAR(30),
                `enter_user` INT UNSIGNED,
                `classroom` VARCHAR(40),
                `reserve_1` VARCHAR(20),
                `reserve_2` VARCHAR(20),
                `reserve_3` VARCHAR(20),
                PRIMARY KEY ( `course_id` )
                )ENGINE=InnoDB DEFAULT CHARSET=utf8;
                '''
        self.exeSql(sql)
        sql = '''
                CREATE TABLE IF NOT EXISTS `relation_course_user`(
                `index` INT UNSIGNED AUTO_INCREMENT,
                `user_id` INT UNSIGNED NOT NULL,
                `course_id` INT UNSIGNED NOT NULL,
                `reserve_1` VARCHAR(20),
                `reserve_2` VARCHAR(20),
                PRIMARY KEY ( `index` )
                )ENGINE=InnoDB DEFAULT CHARSET=utf8;
                '''
        self.exeSql(sql)
    def insertCourse(self,course_name,begin_time,teacher,belong_class,enter_user,classroom):
        sql = '''
                INSERT INTO course_info 
                    (course_name, begin_time,teacher,belong_class,enter_user,classroom)
                    VALUES
                    ('%s', '%s','%s','%s',%d,'%s');'''%(course_name, begin_time,teacher,belong_class,enter_user,classroom)
        self.exeSql(sql)
    def insertRelation(self,user_id,course_id):
        sql = '''
                INSERT INTO relation_course_user 
                    (user_id, course_id)
                    VALUES
                    (%d, %d);'''%(user_id,course_id)   
        self.exeSql(sql)
    def insertUser(self,email):
        sql = '''
                INSERT INTO user_info(user_name,password,`e-mail` )
                       VALUES ('testuser', '123456','%s');'''%(email)
        self.exeSql(sql)


    def exeSql(self,sql):
        try:
            self.cursor.execute(sql)
            # 提交到数据库执行
            #print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'执行sql成功')
            self.db.commit()
        except:
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'执行sql出错'+sql)
            
            self.db.rollback()
            # 如果发生错误则回滚
        #db.rollback()
    def getUserEmail(self,course_id):
        sql = """
                select `e-mail` from user_info where (user_id in
                    (select user_id from relation_course_user where (course_id = %d)));"""%(course_id)
        self.cursor.execute(sql)
            #    获取所有记录列表
        results = self.cursor.fetchall()
        return results
    def getCourseDay(self,time):
        sql = """SELECT course_id,course_name,begin_time,classroom 
                FROM course_info where begin_time REGEXP '^%s';"""%(time)
        #sql = "select *from course_info"
        course_list = []
        try:
        # 执行SQL语句
            self.cursor.execute(sql)
            #    获取所有记录列表
            results = self.cursor.fetchall()
            #print(str(results))
            for x in results:
                dict_course = {'course_id':'','course_name':'','begin_time':'','classroom':''}
                dict_course['course_id'] = x[0]
                dict_course['course_name'] = x[1]
                dict_course['begin_time'] = x[2][-4:]
                dict_course['classroom'] = x[3]
                course_list.append(dict_course)
            return course_list
        except:
            print (sql+"Error: unable to fetch data")
    
    
   

if __name__ == "__main__":  
    database = DataBase('47.99.95.58','root','Z001221z','courseRemindSystem')
    #database.creatTables()
    #insertCourse(self,course_name,begin_time,teacher,belong_class,enter_user,classroom)
 
    x = 1
    while x<9:
        y = 2
        while y<14:
            database.insertRelation(x,y)
            y = y+1
        x = x+1


    #print(str(database.getCourseDay('4')))
    #database.getCourseDay('20200402')