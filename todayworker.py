import datetime
#设置，可按需更改
stu:list=["陈悦妍","黄湘宜","江雨函","李梦佳","林虹佳","李佳瑾","李佳璐","邱嘉涵","魏子昕","王佳欣","谢可一","张雅雯","赵奕涵","卓梓滢","郑筱雅","朱雨汐","张瑾萱","陈王子君","陈子滔","陈劲远","陈纯锐","方霁云","何东晟","江森洪","刘星宇","李国韬","林仁杰","潘辰禹","唐浩轩","王锦煌","吴仁俊","吴漱恺","吴宜芃","吴永祥","谢积烁","俞越","郑博文","张旭凯","郑开元","李蓉","王子诚","许可馨","王允浩","郑诗宇","魏敦豪","陈欣荣"]
renshu:int=46#人数
starttime:datetime.datetime=datetime.datetime(2019,9,3)#开始日期
def toDatetime(date):
    return datetime.datetime(date.year,date.month,date.day)
def gettodayworker():
    return (toDatetime(datetime.date.today())-starttime).days%renshu+1
def getworkerof(of):
    return (of-starttime).days%renshu+1
if __name__=="__main__":
    i=gettodayworker()
    print("今天%d号%s当值"%(i,stu[i-1]))
    i=getworkerof(datetime.datetime(2019,10,10))
    print("2019.10.10%d号%s当值"%(i,stu[i-1]))