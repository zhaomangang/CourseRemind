from log import *
from my_email import *
from database_manage import *
import time
class Remind(object):
    def __init__(self):
        self.loger = LogManagement('D:\\code\\python\\CourseRemind\\backgroundSystem\\log\\system_run_log.txt')
        self.loger.logRecord('开启系统')
        self.week_today = self.getWeekToday()
        self.ema = MyEmail()
        self.database = DataBase('47.99.95.58','root','Z001221z','courseRemindSystem')
        self.course_list = []
        #print(self.getTimeNow())
        
        self.whileRemind()
        

    
    def whileRemind(self):
        self.loger.logRecord('开始加载当日课表')
        #每天固定时段查询明天课表加载进系统
        result = self.database.getCourseDay(time.strftime('%Y%m%d',time.localtime(time.time())))
        for x in result:
            self.course_list.append(x)
            result = self.database.getCourseDay(self.getWeekToday())
        for x in result:
            self.course_list.append(x)
        self.loger.logRecord('当日课表加载完成')
        self.ema.sendEmail(['zhaomangang@qq.com'],'电磁汪','mason','系统运行日志','系统启动成功')
        while True:
            time_temp = int(time.strftime('%H%M',time.localtime(time.time())))
            if(time_temp>0 and time_temp<100):
                self.course_list.clear()
                self.loger.logRecord('开始加载次日课表')
                
                #每天固定时段查询明天课表加载进系统
                result = self.database.getCourseDay(time.strftime('%Y%m%d',time.localtime(time.time())))
                for x in result:
                    self.course_list.append(x)
                result = self.database.getCourseDay(self.getWeekToday())
                for x in result:
                    self.course_list.append(x)
                self.loger.logRecord('次日课表加载完成')
                self.ema.sendEmail(['zhaomangang@qq.com'],'电磁汪','mason','系统运行日志','课表加载完成')
            for x in self.course_list:
                #print(x)
                time_course_h = int(x['begin_time'][0:2])
                time_course_m = int(x['begin_time'][2:4])
                
                time_now_h = int(time.strftime('%H',time.localtime(time.time())))
                if(time_course_h==time_now_h):
                    #print(time_course_m)
                    if(15>time_course_m - int(time.strftime('%M',time.localtime(time.time())))):
                        #sender_name,recver_name,subject,text
                        # em.sendEmail('电磁汪','mason','您有新的课程','课程内容等.......')
                        text = "课程名:%s\n上课时间:%s\n教室:%s\n\n\n\n祝好！\n谢谢！"%(x['course_name'],x['begin_time'],x['classroom'])
                        self.ema.sendEmail(self.database.getUserEmail(int(x['course_id'])),'电磁汪','订阅者','15分钟后有课',text)
                        index = self.course_list.index(x)
                        #print(index)
                        del self.course_list[index]
                else:
                    time_cou = int(x[0:4])
                    time_no = int(time.strftime('%H%M',time.localtime(time.time())))
                    if(55 > time_cou - time_no):
                        #sender_name,recver_name,subject,text
                        # em.sendEmail('电磁汪','mason','您有新的课程','课程内容等.......')
                        text = "课程名:%s\n上课时间:%s\n教室:%s\n\n\n\n祝好！\n谢谢！"%(x['course_name'],x['begin_time'],x['classroom'])
                        self.ema.sendEmail(self.database.getUserEmail(int(x['course_id'])),'电磁汪','订阅者','15分钟后有课',text)
                        index = self.course_list.index(x)
                        #print(index)
                        del self.course_list[index]

                #if(time_now-time_temp)




    def getTimeNow(self):
        time_now = int(time.strftime('%Y%m%d%H%M',time.localtime(time.time())))
        return time_now

    def getWeekToday(self):
        week_now = time.strftime('%a',time.localtime(time.time()))
        #Monday，Tuesday、Wednesday、Thursday、Friday、Saturday 、Sunday
        if('Mon'==week_now):
            return '01'
        if('Tue'==week_now):
            return '02'
        if('Wed'==week_now):
            return '03'
        if('Thu'==week_now):
            return '04'
        if('Fri'==week_now):
            return '05'
        if('Sat'==week_now):
            return '06'
        if('Sun'==week_now):
            return '07'

if __name__ == "__main__": 
    remind = Remind()
    self.loger.logRecord('系统关闭')
    self.ema.sendEmail(['zhaomangang@qq.com'],'电磁汪','mason','系统运行日志','系统关闭')
