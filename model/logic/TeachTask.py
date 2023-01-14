from model.base.MongoDBEntity import MongoDBEntity


class TeachTask(MongoDBEntity):
    kcdm = ''  # 课程代码
    kclb = ''  # 课程代码
    xf = 0.0  # 学分
    khfs = ''  # 考核方式
    kkxy = ''  # 开科学院
    xn = ''  # 学年
    xq = ''  # 学期
    zydm = ''  # 开课专业代码
    zymc = ''  # 开课专业名称
    kcxz = ''  # 课程性质
    jszgh = ''  # 教师职工号
    jsxm = ''  # 教师姓名
    xkkh = ''  # 选课课号
    qsz = ''  # 起始周
    jsz = ''  # 结束周
    cdbs = ''  # 教师类型
    bjmc = ''  # 班级名称
    qsjsz = ''  # 起始结束周
    zhxs = 0  # 总学时
    jkxs = 0  # 讲科学时
    syxs = 0  # 实验学时
    sjxs = 0  # 上机学时
    bjrs = 0  # 班级人数
    kcmc='' #课程名称
    isimport=0 #是否手工导入
    def __init__(self):
        self._COLLECTION_NAME = self.__class__.__name__.lower()
        self.kcdm = ''  # 课程代码
        self.kclb = ''  # 课程代码
        self.xf = 0.0  # 学分
        self.khfs = ''  # 考核方式
        self.kkxy = ''  # 开科学院
        self.xn = ''  # 学年
        self.xq = ''  # 学期
        self.zydm = ''  # 开课专业代码
        self.zymc = ''  # 开课专业名称
        self.kcxz = ''  # 课程性质
        self.jszgh = ''  # 教师职工号
        self.jsxm = ''  # 教师姓名
        self.xkkh = ''  # 选课课号
        self.qsz = ''  # 起始周
        self.jsz = ''  # 结束周
        self.cdbs = ''  # 教师类型
        self.bjmc = ''  # 班级名称
        self.qsjsz = ''  # 起始结束周
        self.zhxs = 0  # 总学时
        self.jkxs = 0  # 讲科学时
        self.syxs = 0  # 实验学时
        self.sjxs = 0  # 上机学时
        self.bjrs = 0 #班级人数
        self.kcmc = ''  # 课程名称
        self.kcb=[] #课程表
        self.isimport=0 #是否手工导入
