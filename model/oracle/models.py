# coding: utf-8
from sqlalchemy import Column, Index, Table, VARCHAR, text
from sqlalchemy.dialects.oracle.base import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Xxkjxrwb(Base):
    __tablename__ = 'xxkjxrwb'

    xn = Column(VARCHAR(10))
    xq = Column(NUMBER(1, 0, False))
    kcdm = Column(VARCHAR(10))
    kcmc = Column(VARCHAR(110))
    kcxz = Column(VARCHAR(30))
    kclb = Column(VARCHAR(30))
    kcgs = Column(VARCHAR(30))
    xf = Column(VARCHAR(5))
    zxs = Column(VARCHAR(9))
    sksj = Column(VARCHAR(400))
    skdd = Column(VARCHAR(255))
    rs = Column(NUMBER(5, 0, False))
    kkxy = Column(VARCHAR(18))
    kkx = Column(VARCHAR(30))
    jszgh = Column(VARCHAR(10))
    jsxm = Column(VARCHAR(50))
    xkkh = Column(VARCHAR(35), primary_key=True)
    zddh = Column(VARCHAR(20))
    jcmc = Column(VARCHAR(80), server_default=text("'.'"))
    zz = Column(VARCHAR(40), server_default=text("'.'"))
    cbs = Column(VARCHAR(60), server_default=text("'.'"))
    bb = Column(VARCHAR(15), server_default=text("'.'"))
    sfyxjc = Column(VARCHAR(10))
    xkzt = Column(VARCHAR(1), server_default=text("'1'"))
    yxyq = Column(VARCHAR(100))
    xzdx = Column(VARCHAR(100))
    mxdx = Column(VARCHAR(250))
    xqbs = Column(VARCHAR(30))
    khfs = Column(VARCHAR(6))
    lrsj = Column(VARCHAR(30))
    mm = Column(VARCHAR(20))
    lrsz = Column(VARCHAR(4), server_default=text("'??'"))
    tkbs = Column(NUMBER(1, 0, False))
    tkyy = Column(VARCHAR(100))
    zc = Column(VARCHAR(20))
    zkzbrs = Column(NUMBER(3, 0, False))
    jsyq = Column(VARCHAR(200))
    jccbsj = Column(VARCHAR(12))
    kssj = Column(VARCHAR(100))
    yxrs = Column(NUMBER(4, 0, False))
    jszws = Column(NUMBER(4, 0, False))
    zkzrs = Column(NUMBER(4, 0, False))
    xqyq = Column(VARCHAR(1))
    tjqr = Column(VARCHAR(12))
    sfkk = Column(VARCHAR(2))
    bz = Column(VARCHAR(250))
    qsjsz = Column(VARCHAR(50))
    qsz = Column(NUMBER(4, 0, False))
    jsz = Column(NUMBER(4, 0, False))
    jys = Column(VARCHAR(50))
    pscj = Column(VARCHAR(20))
    qmcj = Column(VARCHAR(20))
    sycj = Column(VARCHAR(8))
    sybj = Column(VARCHAR(250))
    qzcj = Column(VARCHAR(8))
    shtg = Column(VARCHAR(2))
    bjgl = Column(NUMBER(5, 2, True))
    yxl = Column(NUMBER(5, 2, True))
    kssjd = Column(VARCHAR(4))
    skh = Column(VARCHAR(30))
    ksfs = Column(VARCHAR(4))
    zcfy = Column(NUMBER(asdecimal=False), server_default=text("""\
0

"""))
    price = Column(VARCHAR(50))
    cjlrfs = Column(VARCHAR(10))
    sfkpj = Column(VARCHAR(4), server_default=text("'?'"))
    mkzh = Column(VARCHAR(20), index=True)
    sfxgxk = Column(VARCHAR(10), server_default=text("""\
'?'

"""))
    zhxs = Column(VARCHAR(9), server_default=text("""\
'0'

"""))
    jkxs = Column(VARCHAR(9), server_default=text("""\
'0'

"""))
    syxs = Column(VARCHAR(9), server_default=text("""\
'0'

"""))
    sjxs = Column(VARCHAR(9), server_default=text("""\
'0'

"""))
    ksrq = Column(VARCHAR(12))
    ts = Column(VARCHAR(2))
    xxbj = Column(VARCHAR(2), server_default=text("'?'"))
    jcbh = Column(VARCHAR(80))
    jxrw = Column(VARCHAR(50))
    skfsmc = Column(VARCHAR(50))
    sqsm = Column(VARCHAR(300))
    sfkdc = Column(VARCHAR(10), server_default=text("'?'"))
    kkxyqr = Column(VARCHAR(50))
    sfpdg = Column(VARCHAR(4), server_default=text("'?'"))
    sfkpx = Column(VARCHAR(10), server_default=text("'?'"))
    kcsjxs = Column(VARCHAR(9))
    xtkxs = Column(VARCHAR(9))
    knsjxs = Column(VARCHAR(9))
    kwsjxs = Column(VARCHAR(9))
    bkqr1 = Column(VARCHAR(4))
    mmfscg = Column(VARCHAR(2))
    jcjssl = Column(VARCHAR(20))
    kwxs = Column(VARCHAR(9), server_default=text("""\
'0'

"""))
    sybjs = Column(VARCHAR(5))
    nj = Column(VARCHAR(4))
    zymc = Column(VARCHAR(10))
    hjqk = Column(VARCHAR(80))
    tdr = Column(VARCHAR(50))
    jxbmc = Column(VARCHAR(200))
    sksj_jtsj = Column(VARCHAR(200))
    cjbl1 = Column(VARCHAR(8))
    cjbl2 = Column(VARCHAR(8))
    cjbl3 = Column(VARCHAR(8))
    cjbl4 = Column(VARCHAR(8))
    cjbl5 = Column(VARCHAR(8))
    cjbl6 = Column(VARCHAR(8))
    cjbl7 = Column(VARCHAR(8))
    cjbl8 = Column(VARCHAR(8))
    cjbl9 = Column(VARCHAR(8))
    cjbl10 = Column(VARCHAR(8))
    tjcjsj = Column(VARCHAR(20))
    lc = Column(VARCHAR(30))
    pscjcx = Column(VARCHAR(8))
    qzcjcx = Column(VARCHAR(8))
    qmcjcx = Column(VARCHAR(8))
    sycjcx = Column(VARCHAR(8))
    pslrsz = Column(VARCHAR(20), server_default=text("""\
'??'

"""))
    yxtjqr = Column(VARCHAR(12))
    syjx = Column(NUMBER(asdecimal=False), server_default=text("1"))
    ssjxjhh = Column(VARCHAR(100))
    bzxx = Column(VARCHAR(254))
    pscjbl = Column(VARCHAR(10))
    qzcjbl = Column(VARCHAR(10))
    qmcjbl = Column(VARCHAR(10))
    sycjbl = Column(VARCHAR(10))
    jcdj = Column(VARCHAR(50))
    tjlx = Column(VARCHAR(20))
    cxrs = Column(VARCHAR(20))
    sfkzp = Column(VARCHAR(10), server_default=text("""\
'?'

"""))
    ksxs = Column(VARCHAR(4))
    yxtjqrr = Column(VARCHAR(20))
    yxtjqrsj = Column(VARCHAR(20))
    tjqrr = Column(VARCHAR(20))
    tjqrsj = Column(VARCHAR(20))
    sfcjqzks = Column(VARCHAR(4))
    qzkssfjs = Column(VARCHAR(4))
    qzksfs = Column(VARCHAR(4))
    qmksfs = Column(VARCHAR(4))
    ysrl = Column(NUMBER(4, 0, False))
    sksj_bjew = Column(VARCHAR(255))
    klcjqssj = Column(VARCHAR(20))
    klcjjssj = Column(VARCHAR(20))
    lcjjz = Column(VARCHAR(20))
    pscjzg = Column(VARCHAR(8))
    qzcjzg = Column(VARCHAR(8))
    qmcjzg = Column(VARCHAR(8))
    sycjzg = Column(VARCHAR(8))
    sfcjsx = Column(VARCHAR(2), server_default=text("""\
'?'

"""))
    sfdjc = Column(VARCHAR(4), server_default=text("""\
'?'

"""))
    fcjxcjxs = Column(VARCHAR(8))
    ljczgh = Column(VARCHAR(20))
    jcbz = Column(VARCHAR(250))
    ljcsj = Column(VARCHAR(20))
    ggkc = Column(VARCHAR(2))
    lcjjszgh = Column(VARCHAR(20))
    xtjqr = Column(VARCHAR(20))
    xtjqrr = Column(VARCHAR(20))
    xtjqrsj = Column(VARCHAR(20))
    bz1 = Column(VARCHAR(32))
    xkfs = Column(VARCHAR(1))
    sfxsytk = Column(VARCHAR(1))
    gzlkclx = Column(VARCHAR(100))
    kssj_qz = Column(VARCHAR(100))
    kssjd_qz = Column(VARCHAR(100))
    ksrq_qz = Column(VARCHAR(12))
    khfs_qz = Column(VARCHAR(28))
    ksfs_qz = Column(VARCHAR(4))
    sfwlkc = Column(VARCHAR(10))


class Yhb(Base):
    __tablename__ = 'yhb'

    yhm = Column(VARCHAR(12), primary_key=True, nullable=False)
    kl = Column(VARCHAR(128), nullable=False)
    js = Column(VARCHAR(10), primary_key=True, nullable=False)
    xm = Column(VARCHAR(50))
    szdw = Column(VARCHAR(40))
    ty = Column(VARCHAR(2))
    dlm = Column(VARCHAR(20), index=True)
    xqdm = Column(VARCHAR(20))
    cxyyhmm = Column(VARCHAR(5))
    ipdz = Column(VARCHAR(200))
    macdz = Column(VARCHAR(200))
    kcqbxx = Column(VARCHAR(2))
    kjcgn = Column(VARCHAR(100))
    dlstsjcgn = Column(VARCHAR(100))
    sfqzjc = Column(VARCHAR(2))
    jskcmm = Column(VARCHAR(128))
    jsmm = Column(VARCHAR(128))
    xxmc = Column(VARCHAR(80))
    sfcwyh = Column(VARCHAR(2))
    zymc = Column(VARCHAR(50))
    dlmkl = Column(VARCHAR(128))
    authorities = Column(VARCHAR(2000))
    mmsxsj = Column(VARCHAR(30), server_default=text("""\
to_char(sysdate,'YYYY-MM-DD HH24:MI:SS')
"""))


class Xydmb(Base):
    __tablename__ = 'xydmb'

    xydm = Column(VARCHAR(2), primary_key=True)
    xymc = Column(VARCHAR(30), nullable=False)
    kcgs = Column(VARCHAR(30))
    xqdm = Column(VARCHAR(1))
    xyywmc = Column(VARCHAR(40))
    xyjc = Column(VARCHAR(20))
    xylx = Column(VARCHAR(20))
    xyzylj = Column(VARCHAR(100))
    bylwsfkx = Column(VARCHAR(8), server_default=text("""\
'??'

"""))
    xyyhsfkx = Column(VARCHAR(10))
    sfbj = Column(VARCHAR(10))
    sfjszhxs = Column(VARCHAR(4), server_default=text("'?'"))
    sftj = Column(VARCHAR(6), server_default=text("""\
'?' 

"""))
    tyjgdm = Column(VARCHAR(10))
    tyjgmc = Column(VARCHAR(50))
    sfgy = Column(VARCHAR(1))


class Bjdmb(Base):
    __tablename__ = 'bjdmb'

    bjdm = Column(VARCHAR(15), primary_key=True)
    bjmc = Column(VARCHAR(35), nullable=False)
    sszydm = Column(VARCHAR(6))
    nj = Column(NUMBER(4, 0, False))
    kx = Column(VARCHAR(1), server_default=text("""\
null
"""))
    ssxydm = Column(VARCHAR(4))
    ssxqdm = Column(VARCHAR(2))
    bynd = Column(NUMBER(4, 0, False))
    fdyxm = Column(VARCHAR(12))
    fdylxfs = Column(VARCHAR(30))
    bjjc = Column(VARCHAR(30))
    xz = Column(NUMBER(2, 0, False))
    cc = Column(VARCHAR(20))
    zcrs = Column(NUMBER(asdecimal=False))
    yxj = Column(VARCHAR(1))
    zyfx = Column(VARCHAR(150))
    xscbj = Column(VARCHAR(50))
    kbbj = Column(VARCHAR(4))
    jcrs = Column(NUMBER(asdecimal=False))
    bds = Column(VARCHAR(50))
    bzrxm = Column(VARCHAR(30))
    bzrzgh = Column(VARCHAR(12))
    dsxm1 = Column(VARCHAR(30))
    dsxm2 = Column(VARCHAR(30))
    bzrxm2 = Column(VARCHAR(30))
    ds1lxfs = Column(VARCHAR(255))
    ds2lxfs = Column(VARCHAR(255))
    bzr1lxfs = Column(VARCHAR(255))
    bzr2lxfs = Column(VARCHAR(255))
    ssxsxydm = Column(VARCHAR(10))
    kbbz = Column(VARCHAR(600))
    ssqddm = Column(VARCHAR(600))
    sfyx = Column(VARCHAR(4))
    bjywmc = Column(VARCHAR(80))
    pkxqdm = Column(VARCHAR(20))
    bxxs = Column(VARCHAR(255))
    mzzdxs = Column(VARCHAR(10))
    lsh = Column(VARCHAR(100))
    bzxh = Column(VARCHAR(20))


t_cjcxb = Table(
    'cjcxb', metadata,
    Column('xn', VARCHAR(10)),
    Column('xq', NUMBER(1, 0, False)),
    Column('xy', VARCHAR(30)),
    Column('xy_xsxy', VARCHAR(50)),
    Column('zymc', VARCHAR(40)),
    Column('dqszj', NUMBER(4, 0, False)),
    Column('xzb', VARCHAR(50)),
    Column('xh', VARCHAR(20), nullable=False),
    Column('xm', VARCHAR(50)),
    Column('kcmc', VARCHAR(110)),
    Column('xf', VARCHAR(5)),
    Column('cj', VARCHAR(17)),
    Column('zscj', NUMBER(5, 1, True)),
    Column('bkcj', VARCHAR(8)),
    Column('cxcj', VARCHAR(8)),
    Column('xkkh', VARCHAR(50), nullable=False),
    Column('sfzc', VARCHAR(10)),
    Column('xjzt', VARCHAR(20)),
    Column('sfzx', VARCHAR(4)),
    Column('kcxz', VARCHAR(30))
)
t_cjbmaxview = Table(
    'cjbmaxview', metadata,
    Column('xn', VARCHAR(10)),
    Column('xq', NUMBER(1, 0, False)),
    Column('xkkh', VARCHAR(50), nullable=False),
    Column('xh', VARCHAR(20), nullable=False),
    Column('xm', VARCHAR(50)),
    Column('kcmc', VARCHAR(110)),
    Column('qzxs', NUMBER(3, 1, True)),
    Column('xf', VARCHAR(5)),
    Column('cj', VARCHAR(8)),
    Column('zscj', NUMBER(5, 1, True)),
    Column('jd', NUMBER(asdecimal=False)),
    Column('bz', VARCHAR(250)),
    Column('xgsj', VARCHAR(200)),
    Column('xgs', VARCHAR(100)),
    Column('cxbj', NUMBER(1, 0, False)),
    Column('tzf', VARCHAR(20)),
    Column('tzfjd', NUMBER(3, 1, True)),
    Column('kcdm', VARCHAR(100)),
    Column('pscj', VARCHAR(20)),
    Column('qmcj', VARCHAR(20)),
    Column('sycj', VARCHAR(8)),
    Column('bkcj', VARCHAR(8)),
    Column('cxcj', VARCHAR(8)),
    Column('kcxz', VARCHAR(30)),
    Column('tj', NUMBER(1, 0, False)),
    Column('tjbz', NUMBER(1, 0, False)),
    Column('tzjd', NUMBER(3, 1, True)),
    Column('cxxnxq', VARCHAR(12)),
    Column('qzcj', VARCHAR(8)),
    Column('fxbj', VARCHAR(10)),
    Column('jf', NUMBER(asdecimal=False)),
    Column('kcgs', VARCHAR(20)),
    Column('xsqr', VARCHAR(4)),
    Column('zhxs', VARCHAR(20)),
    Column('bzxx', VARCHAR(150)),
    Column('dxqjl', VARCHAR(2)),
    Column('bkcj_tzf', VARCHAR(8)),
    Column('bkcj_bz', VARCHAR(10)),
    Column('llcj', VARCHAR(20)),
    Column('llzscj', VARCHAR(20)),
    Column('xmdm', VARCHAR(100)),
    Column('xmmc', VARCHAR(50)),
    Column('qmcj_bf', VARCHAR(20)),
    Column('gaxs', VARCHAR(20)),
    Column('jycj', VARCHAR(8)),
    Column('jybkcj', VARCHAR(8)),
    Column('fjf', VARCHAR(4)),
    Column('cjjf_bz', VARCHAR(100)),
    Column('cj1', VARCHAR(8)),
    Column('cj2', VARCHAR(8)),
    Column('cj3', VARCHAR(8)),
    Column('cj4', VARCHAR(8)),
    Column('cj5', VARCHAR(8)),
    Column('cj6', VARCHAR(8)),
    Column('cj7', VARCHAR(8)),
    Column('cj8', VARCHAR(8)),
    Column('cj9', VARCHAR(8)),
    Column('cj10', VARCHAR(8)),
    Column('zpn', VARCHAR(40)),
    Column('bkcjn', VARCHAR(40)),
    Column('cxcjn', VARCHAR(40)),
    Column('zpz', NUMBER(asdecimal=False)),
    Column('bkcjz', NUMBER(asdecimal=False)),
    Column('cxcjz', NUMBER(asdecimal=False)),
    Column('mcjn', NUMBER(asdecimal=False)),
    Column('mcjx', VARCHAR(10))
)

t_cxcjbview = Table(
    'cxcjbview', metadata,
    Column('xn', VARCHAR(10)),
    Column('xq', NUMBER(1, 0, False)),
    Column('xkkh', VARCHAR(50), nullable=False),
    Column('xh', VARCHAR(20), nullable=False),
    Column('xm', VARCHAR(50)),
    Column('kcmc', VARCHAR(110)),
    Column('qzxs', NUMBER(3, 1, True)),
    Column('xf', VARCHAR(5)),
    Column('cj', VARCHAR(8)),
    Column('zscj', NUMBER(5, 1, True)),
    Column('jd', NUMBER(asdecimal=False)),
    Column('bz', VARCHAR(250)),
    Column('xgsj', VARCHAR(200)),
    Column('xgs', VARCHAR(100)),
    Column('cxbj', NUMBER(1, 0, False)),
    Column('tzf', VARCHAR(20)),
    Column('tzfjd', NUMBER(3, 1, True)),
    Column('kcdm', VARCHAR(100)),
    Column('pscj', VARCHAR(20)),
    Column('qmcj', VARCHAR(20)),
    Column('sycj', VARCHAR(8)),
    Column('bkcj', VARCHAR(8)),
    Column('cxcj', VARCHAR(8)),
    Column('kcxz', VARCHAR(30)),
    Column('tj', NUMBER(1, 0, False)),
    Column('tjbz', NUMBER(1, 0, False)),
    Column('tzjd', NUMBER(3, 1, True)),
    Column('cxxnxq', VARCHAR(12)),
    Column('qzcj', VARCHAR(8)),
    Column('fxbj', VARCHAR(10)),
    Column('jf', NUMBER(asdecimal=False)),
    Column('kcgs', VARCHAR(20)),
    Column('xsqr', VARCHAR(4)),
    Column('bzxx', VARCHAR(150)),
    Column('dxqjl', VARCHAR(2)),
    Column('bkcj_tzf', VARCHAR(8)),
    Column('bkcj_bz', VARCHAR(10)),
    Column('llcj', VARCHAR(20)),
    Column('llzscj', VARCHAR(20)),
    Column('xmdm', VARCHAR(100)),
    Column('xmmc', VARCHAR(50)),
    Column('qmcj_bf', VARCHAR(20)),
    Column('gaxs', VARCHAR(20)),
    Column('jycj', VARCHAR(8)),
    Column('jybkcj', VARCHAR(8)),
    Column('fjf', VARCHAR(4)),
    Column('cxcjdt', VARCHAR(53))
)


class Jsxxb(Base):
    __tablename__ = 'jsxxb'

    zgh = Column(VARCHAR(10), primary_key=True)
    xm = Column(VARCHAR(50), nullable=False)
    xb = Column(VARCHAR(2))
    csrq = Column(VARCHAR(20))
    lxdh = Column(VARCHAR(30))
    emldz = Column(VARCHAR(40))
    jzglb = Column(VARCHAR(20))
    bm = Column(VARCHAR(30))
    ks = Column(VARCHAR(30))
    zw = Column(VARCHAR(30))
    zc = Column(VARCHAR(30))
    jxzlpj = Column(VARCHAR(1000))
    jsjj = Column(VARCHAR(3000))
    bkmc = Column(VARCHAR(20))
    dj = Column(NUMBER(1, 0, False))
    xl = Column(VARCHAR(28))
    jxyjfx = Column(VARCHAR(30))
    yxj = Column(VARCHAR(1), server_default=text("""\
null
"""))
    ksfb = Column(VARCHAR(2), server_default=text("""\
null
"""))
    zymc = Column(VARCHAR(40))
    byyx = Column(VARCHAR(50))
    kssrm = Column(VARCHAR(10))
    pkyq = Column(VARCHAR(8))
    ywjszg = Column(VARCHAR(4), server_default=text("""\
null
"""))
    rszgh = Column(VARCHAR(10))
    lbmc = Column(VARCHAR(20))
    jsjb = Column(VARCHAR(20))
    telnumber = Column(VARCHAR(20))
    tellx = Column(VARCHAR(50))
    sfsysry = Column(VARCHAR(2))
    sfwp = Column(VARCHAR(2), server_default=text("'?'"))
    lrxy = Column(VARCHAR(100))
    kskyf = Column(VARCHAR(4))
    jsxs = Column(NUMBER(asdecimal=False))
    kl = Column(VARCHAR(10))
    lrbkxy = Column(VARCHAR(50))
    mtzdkpks = Column(VARCHAR(4))
    szc = Column(VARCHAR(20))
    szcsj = Column(VARCHAR(20))
    xzcsj = Column(VARCHAR(20))
    kjsh = Column(VARCHAR(250))
    dmtczz = Column(VARCHAR(10))
    qdjszgsj = Column(VARCHAR(20))
    sfzg = Column(VARCHAR(20))
    zzmm = Column(VARCHAR(50))
    mz = Column(VARCHAR(30))
    xw = Column(VARCHAR(20))
    cjgzsj = Column(VARCHAR(10))
    bysj = Column(VARCHAR(10))
    sfzh = Column(VARCHAR(50))
    jszgzh = Column(VARCHAR(50))
    zjjszgrzh = Column(VARCHAR(50))
    jg = Column(VARCHAR(20))
    sjly = Column(VARCHAR(20))
    jsxmpy = Column(VARCHAR(20), index=True)
    zdbyzg = Column(VARCHAR(2))
    pkbz = Column(VARCHAR(1000))
    kczcbj = Column(VARCHAR(10))
    shfwfx = Column(VARCHAR(50))
    jl = Column(VARCHAR(20))
    zxxl = Column(VARCHAR(20))
    ywjsxm = Column(VARCHAR(100))
    jssybj = Column(VARCHAR(2), server_default=text("""\
'T'

"""))
    xyjg = Column(VARCHAR(50))
    jsrzqxsj = Column(VARCHAR(50))
    zcxq = Column(VARCHAR(50))
    sfyxjjs = Column(VARCHAR(2))
    lxsj = Column(VARCHAR(50))
    sfzdwp = Column(VARCHAR(2))


class Jxjhcjb(Base):
    __tablename__ = 'jxjhcjb'

    xn = Column(VARCHAR(9), primary_key=True, nullable=False)
    xq = Column(VARCHAR(1), primary_key=True, nullable=False)
    xh = Column(VARCHAR(20), primary_key=True, nullable=False)
    kcdm = Column(VARCHAR(15), primary_key=True, nullable=False)
    kcxz = Column(VARCHAR(30))
    mcjnzx = Column(NUMBER(asdecimal=False))
    zpzz = Column(NUMBER(asdecimal=False))
    mcjx = Column(VARCHAR(20))
    bkcj = Column(VARCHAR(20))
    mcxcjx = Column(VARCHAR(20))
    mcxcjn = Column(NUMBER(asdecimal=False))
    zyfx = Column(VARCHAR(50))
    xuh = Column(NUMBER(asdecimal=False), primary_key=True, nullable=False)
    kcmc = Column(VARCHAR(100))
    xf = Column(VARCHAR(5))


class Kcb(Base):
    __tablename__ = 'kcb'
    __table_args__ = (
        Index('kcb_index', 'xkkh'),
    )
    xkkh = Column(VARCHAR(40), primary_key=True)
    xqj = Column(NUMBER(asdecimal=False))
    djj = Column(NUMBER(asdecimal=False))
    skcd = Column(NUMBER(asdecimal=False))
    dsz = Column(VARCHAR(6))
    qsz = Column(NUMBER(asdecimal=False))
    jsz = Column(NUMBER(asdecimal=False))
    kcb = Column(VARCHAR(800))

class Tjkbapqkb(Base):
    __tablename__ = 'tjkbapqkb'
    __table_args__ = (
        Index('tjkbapqkb_sj', 'xqj', 'sjdxh', 'dsz'),
    )

    tjkbdm = Column(VARCHAR(50), primary_key=True, nullable=False)
    xqj = Column(NUMBER(1, 0, False), primary_key=True, nullable=False)
    sjdxh = Column(NUMBER(2, 0, False), primary_key=True, nullable=False)
    xkkh = Column(VARCHAR(35), primary_key=True, nullable=False, index=True)
    qssj = Column(NUMBER(2, 0, False), primary_key=True, nullable=False)
    jssj = Column(NUMBER(2, 0, False), primary_key=True, nullable=False)
    dsz = Column(VARCHAR(6), primary_key=True, nullable=False)
    kcdm = Column(VARCHAR(10))
    jsbh = Column(VARCHAR(10), index=True)
    jszgh = Column(VARCHAR(10), primary_key=True, nullable=False)
    zws = Column(NUMBER(asdecimal=False))
    sknr = Column(VARCHAR(2), primary_key=True, nullable=False)
    qssjd = Column(NUMBER(2, 0, False), primary_key=True, nullable=False)
    qhbz = Column(VARCHAR(6))
    yxxxk = Column(VARCHAR(8))
    syycsk = Column(VARCHAR(8))
    z1 = Column(VARCHAR(4))
    z2 = Column(VARCHAR(4))
    z3 = Column(VARCHAR(4))
    z4 = Column(VARCHAR(4))
    z5 = Column(VARCHAR(4))
    z6 = Column(VARCHAR(4))
    z7 = Column(VARCHAR(4))
    z8 = Column(VARCHAR(4))
    z9 = Column(VARCHAR(4))
    z10 = Column(VARCHAR(4))
    z11 = Column(VARCHAR(4))
    z12 = Column(VARCHAR(4))
    z13 = Column(VARCHAR(4))
    z14 = Column(VARCHAR(4))
    z15 = Column(VARCHAR(4))
    z16 = Column(VARCHAR(4))
    z17 = Column(VARCHAR(4))
    z18 = Column(VARCHAR(4))
    z19 = Column(VARCHAR(4))
    z20 = Column(VARCHAR(4))
    z21 = Column(VARCHAR(4))
    z22 = Column(VARCHAR(4))
    z23 = Column(VARCHAR(4))
    z24 = Column(VARCHAR(4))
    z25 = Column(VARCHAR(4))
    kc = Column(VARCHAR(4))
    kc2 = Column(NUMBER(4, 0, False))
    yqdm = Column(VARCHAR(8))
    kkxy = Column(VARCHAR(30))
    z0 = Column(VARCHAR(4), server_default=text("""\
'0'
"""))



class Xsjbxxb(Base):
    __tablename__ = 'xsjbxxb'
    __table_args__ = (
        Index('xsjbxxb_index', 'xh', 'xzb', 'dqszj'),
    )

    xh = Column(VARCHAR(20), primary_key=True)
    xm = Column(VARCHAR(50))
    xb = Column(VARCHAR(2))
    csrq = Column(VARCHAR(10))
    zzmm = Column(VARCHAR(50))
    mz = Column(VARCHAR(15))
    jg = Column(VARCHAR(40))
    lydq = Column(VARCHAR(50))
    xy = Column(VARCHAR(30))
    xi = Column(VARCHAR(30))
    zymc = Column(VARCHAR(40), index=True)
    xzb = Column(VARCHAR(50), index=True)
    xz = Column(NUMBER(1, 0, False))
    xxnx = Column(NUMBER(2, 0, False))
    xjzt = Column(VARCHAR(20), server_default=text("'?'"))
    dqszj = Column(NUMBER(4, 0, False), index=True)
    pyfx = Column(VARCHAR(20))
    zyfx = Column(VARCHAR(30), index=True)
    zylb = Column(VARCHAR(20))
    rxrq = Column(VARCHAR(10))
    byzx = Column(VARCHAR(50))
    ssh = Column(VARCHAR(50))
    dzyxdz = Column(VARCHAR(40))
    lxdh = Column(VARCHAR(100))
    zkzh = Column(VARCHAR(20))
    sfzh = Column(VARCHAR(20))
    gatm = Column(VARCHAR(10))
    jkzk = Column(VARCHAR(10))
    ywxw = Column(VARCHAR(2))
    bz = Column(VARCHAR(250))
    mm = Column(VARCHAR(128))
    bdh = Column(VARCHAR(12))
    yydj = Column(NUMBER(1, 0, False))
    kh = Column(VARCHAR(30))
    zssj = Column(VARCHAR(20))
    rxzf = Column(VARCHAR(8))
    sfyxxs = Column(VARCHAR(2))
    xslb = Column(VARCHAR(10))
    dj = Column(VARCHAR(50), server_default=text("'00000000000000000000000000000000000000000000000000'"))
    sfgspydy = Column(VARCHAR(2))
    lqmcjyh = Column(VARCHAR(20))
    xmpy = Column(VARCHAR(50))
    yhzh = Column(VARCHAR(100))
    jxbmc = Column(VARCHAR(200))
    rdsj = Column(VARCHAR(20))
    zydm = Column(VARCHAR(4))
    ljbym = Column(VARCHAR(20))
    sfly = Column(VARCHAR(100))
    sfkzc = Column(VARCHAR(2), server_default=text("'?'"))
    cc = Column(VARCHAR(20))
    yzbm = Column(VARCHAR(10))
    yycj = Column(VARCHAR(10))
    kx = Column(VARCHAR(10), server_default=text("'0'"))
    sfzx = Column(VARCHAR(4), server_default=text("'?'"))
    xszh = Column(VARCHAR(20))
    userid = Column(VARCHAR(40))
    kslb = Column(VARCHAR(20))
    sfzc = Column(VARCHAR(10), server_default=text("""\
'?'

"""))
    ydlb = Column(VARCHAR(100))
    zym = Column(VARCHAR(20))
    byrq = Column(VARCHAR(10))
    csd = Column(VARCHAR(200))
    ljb = Column(VARCHAR(50))
    ljbc = Column(VARCHAR(50))
    ljbh = Column(VARCHAR(50))
    dzzch = Column(VARCHAR(50))
    ksh = Column(VARCHAR(50))
    ccqj = Column(VARCHAR(50))
    dlmc = Column(VARCHAR(50))
    kstz = Column(VARCHAR(20))
    tc = Column(VARCHAR(100))
    rxfs = Column(VARCHAR(20))
    sfzds = Column(VARCHAR(2), server_default=text("'?'"))
    bxxs = Column(VARCHAR(10))
    bxlx = Column(VARCHAR(40))
    xxxs = Column(VARCHAR(10))
    zsjj = Column(VARCHAR(4))
    shbj = Column(VARCHAR(6))
    yshbj = Column(VARCHAR(6))
    zxwyyz = Column(VARCHAR(20))
    zxwyjbmc = Column(VARCHAR(10))
    sfbzlb = Column(VARCHAR(50), server_default=text("""\
'1'

"""))
    dlm = Column(VARCHAR(20), index=True)
    sfkpj = Column(VARCHAR(4), server_default=text("'?'"))
    jtszd = Column(VARCHAR(120))
    lys = Column(VARCHAR(20))
    sfqr = Column(VARCHAR(2))
    sflxs = Column(VARCHAR(10))
    telnumber = Column(VARCHAR(20))
    tellx = Column(VARCHAR(50))
    xsmm = Column(VARCHAR(128))
    sfqxy = Column(VARCHAR(4))
    byf = Column(VARCHAR(20))
    xscbj = Column(VARCHAR(50))
    sfpdg = Column(VARCHAR(4), server_default=text("'?'"))
    kl = Column(VARCHAR(20))
    yktid = Column(VARCHAR(50))
    lqpc = Column(VARCHAR(50))
    ksjc = Column(VARCHAR(100))
    ybyzy = Column(VARCHAR(50))
    lqzy = Column(VARCHAR(50))
    zslb = Column(VARCHAR(20))
    sfcglx = Column(VARCHAR(2))
    yzydm = Column(VARCHAR(6))
    yzymc = Column(VARCHAR(50))
    fdjs = Column(VARCHAR(20), index=True)
    lqh = Column(VARCHAR(50))
    dsxm1 = Column(VARCHAR(30))
    dsxm2 = Column(VARCHAR(30))
    bzrxm1 = Column(VARCHAR(30))
    bzrxm2 = Column(VARCHAR(30))
    ds1lxfs = Column(VARCHAR(250))
    ds2lxfs = Column(VARCHAR(250))
    bzr1lxfs = Column(VARCHAR(250))
    bzr2lxfs = Column(VARCHAR(250))
    hkszd = Column(VARCHAR(100))
    tdzy = Column(VARCHAR(10))
    sg = Column(VARCHAR(4))
    tz = Column(VARCHAR(4))
    qfqk = Column(VARCHAR(20))
    zzdd = Column(VARCHAR(250))
    ywrxrq = Column(VARCHAR(20))
    ywbyrq = Column(VARCHAR(20))
    ywcsrq = Column(VARCHAR(20))
    xy_xsxy = Column(VARCHAR(50))
    pyfs = Column(VARCHAR(30))
    zjlx = Column(VARCHAR(50))
    wpdw = Column(VARCHAR(50))
    wpdwdq = Column(VARCHAR(50))
    bysjzg = Column(VARCHAR(20))
    wpkh = Column(VARCHAR(50))
    xyd = Column(VARCHAR(30))
    dlmmm = Column(VARCHAR(128))
    whcd = Column(VARCHAR(8))
    rwsj = Column(VARCHAR(10))
    rwdq = Column(VARCHAR(20))
    ssjq = Column(VARCHAR(20))
    ydw = Column(VARCHAR(50))
    xjbh = Column(VARCHAR(15))
    rxpzsh = Column(VARCHAR(20))
    xylb = Column(VARCHAR(20))
    ejxk = Column(VARCHAR(20))
    ejxkssyy = Column(VARCHAR(20))
    jxpckzxx = Column(VARCHAR(4))
    xsxxxgyh = Column(VARCHAR(20))
    sfnz = Column(VARCHAR(2))
    hkxz = Column(VARCHAR(10))
    sfyb = Column(VARCHAR(2))
    sfsb = Column(VARCHAR(2))
    njkypckz = Column(VARCHAR(1))
    qfbs = Column(VARCHAR(2))
    ywxm = Column(VARCHAR(50))
    enstunum = Column(VARCHAR(20))
    zhfmynme = Column(VARCHAR(30))
    zhfstnme = Column(VARCHAR(30))
    sfbbxsz = Column(VARCHAR(2), server_default=text("""\
'?'

"""))
    bbxszsj = Column(VARCHAR(10))
    hcpyhzt = Column(VARCHAR(8), server_default=text("""\
'???'

"""))
    bz1 = Column(VARCHAR(250))
    bz2 = Column(VARCHAR(20))
    bz3 = Column(VARCHAR(240))
    lysfdm = Column(VARCHAR(10))
    lysdm = Column(VARCHAR(10))
    lyxdm = Column(VARCHAR(10))
    yhkh = Column(VARCHAR(25))
    xmpyxdqr = Column(VARCHAR(1))
    dj1 = Column(VARCHAR(20))
    mmsxsj = Column(VARCHAR(30), server_default=text("""\
to_char(sysdate,'YYYY-MM-DD HH24:MI:SS')
"""))
    sfkdc = Column(VARCHAR(2), server_default=text("""\
'?'
"""))
    gj = Column(VARCHAR(20))
    rxnj = Column(VARCHAR(10))
    sfhzc = Column(VARCHAR(2))
    hdxw = Column(VARCHAR(50))
    byjl = Column(VARCHAR(50))
    hzh = Column(VARCHAR(30))
    hzyxq = Column(VARCHAR(20))
    hzlx = Column(VARCHAR(30))
    qzyxq = Column(VARCHAR(20))
    sfyjb = Column(VARCHAR(20))
    jbqksm = Column(VARCHAR(200))
    zjxy = Column(VARCHAR(50))
    gzdw = Column(VARCHAR(100))
    jzxm = Column(VARCHAR(20))
    jzcw = Column(VARCHAR(20))
    jzdzyxdz = Column(VARCHAR(100))
    jzlxdh = Column(VARCHAR(100))
    sfcnr = Column(VARCHAR(2))
    zhswdbr = Column(VARCHAR(50))
    dbrdh = Column(VARCHAR(30))
    xxsj = Column(VARCHAR(20))
    sfgfs = Column(VARCHAR(2))


class Xskcb(Base):
    __tablename__ = 'xskcb'
    __table_args__ = (
        Index('xskcb_xh_xkkh', 'xh', 'xkkh'),
    )

    xn = Column(VARCHAR(10), primary_key=True, nullable=False)
    xq = Column(VARCHAR(1), primary_key=True, nullable=False)
    xh = Column(VARCHAR(20), primary_key=True, nullable=False)
    xkkh = Column(VARCHAR(50), primary_key=True, nullable=False, index=True)
    xqj = Column(NUMBER(1, 0, False), primary_key=True, nullable=False)
    djj = Column(NUMBER(2, 0, False), primary_key=True, nullable=False)
    skcd = Column(NUMBER(asdecimal=False), primary_key=True, nullable=False)
    dsz = Column(VARCHAR(4), primary_key=True, nullable=False)
    qsz = Column(VARCHAR(2), primary_key=True, nullable=False)
    jsz = Column(VARCHAR(2), primary_key=True, nullable=False)
    kcb = Column(VARCHAR(255))
    xkcs = Column(VARCHAR(50), server_default=text("""\
'syxm'
"""))
    xsf = Column(VARCHAR(1), server_default=text("'1'"))


class Zydmb(Base):
    __tablename__ = 'zydmb'

    zydm = Column(VARCHAR(4), primary_key=True)
    zymc = Column(VARCHAR(40), nullable=False, index=True)
    zylb = Column(VARCHAR(20))
    xz = Column(NUMBER(2, 0, False))
    xw = Column(VARCHAR(20), server_default=text("null"))
    zypymb = Column(VARCHAR(1000))
    zypyyq = Column(VARCHAR(2000))
    zykc = Column(VARCHAR(1000))
    tskc = Column(VARCHAR(1000))
    zyywmc = Column(VARCHAR(40))
    ssxydm = Column(VARCHAR(2))
    yxj = Column(VARCHAR(1), server_default=text("'1'"))
    ssxdm = Column(VARCHAR(4))
    zyjc = Column(VARCHAR(30))
    tjzydm = Column(VARCHAR(8))
    cc = Column(VARCHAR(20))
    xklb = Column(VARCHAR(30))
    bz = Column(VARCHAR(250))
    zszydm = Column(VARCHAR(10))
    tjzymc = Column(VARCHAR(40))
    sfwy = Column(VARCHAR(2))
    sfsf = Column(VARCHAR(2))
    sfexw = Column(VARCHAR(2))
    kxlb = Column(VARCHAR(20))
    bks = Column(VARCHAR(4))
    ssxsxydm = Column(VARCHAR(10))
    sfxs = Column(VARCHAR(2), server_default=text("""\
'0'
"""))
    xkjxpt = Column(VARCHAR(30))
    bkflmc = Column(VARCHAR(10))
    ywxwlb = Column(VARCHAR(50))
    gbxh = Column(VARCHAR(2))


class Zykcxsfpb(Base):
    __tablename__ = 'zykcxsfpb'

    zydm = Column(VARCHAR(6), primary_key=True, nullable=False)
    z9 = Column(VARCHAR(2))
    z10 = Column(VARCHAR(2))
    zymc = Column(VARCHAR(40))
    z11 = Column(VARCHAR(2))
    z12 = Column(VARCHAR(2))
    z13 = Column(VARCHAR(2))
    z14 = Column(VARCHAR(2))
    z15 = Column(VARCHAR(2))
    z16 = Column(VARCHAR(2))
    z17 = Column(VARCHAR(2))
    z1 = Column(VARCHAR(2))
    z18 = Column(VARCHAR(2))
    z19 = Column(VARCHAR(2))
    z20 = Column(VARCHAR(2))
    nj = Column(VARCHAR(4), primary_key=True, nullable=False)
    z21 = Column(VARCHAR(2))
    z22 = Column(VARCHAR(2))
    z23 = Column(VARCHAR(2))
    z24 = Column(VARCHAR(2))
    z25 = Column(VARCHAR(2))
    xymc = Column(VARCHAR(40))
    z2 = Column(VARCHAR(2))
    bjdm = Column(VARCHAR(10), primary_key=True, nullable=False)
    bjmc = Column(VARCHAR(35))
    cs = Column(VARCHAR(1))
    xn = Column(VARCHAR(9), primary_key=True, nullable=False)
    xq = Column(VARCHAR(1), primary_key=True, nullable=False)
    kcdm = Column(VARCHAR(10), primary_key=True, nullable=False)
    kcmc = Column(VARCHAR(110))
    kslx = Column(VARCHAR(10), primary_key=True, nullable=False)
    kss = Column(VARCHAR(4))
    z3 = Column(VARCHAR(2))
    z4 = Column(VARCHAR(2))
    z5 = Column(VARCHAR(2))
    z6 = Column(VARCHAR(2))
    z7 = Column(VARCHAR(2))
    z8 = Column(VARCHAR(2))
    xkkh = Column(VARCHAR(50), primary_key=True, nullable=False, index=True)
    ypxs = Column(VARCHAR(4))
    jsxm = Column(VARCHAR(40))
    jxrl_sfdy = Column(VARCHAR(4))


class Jxrwb(Base):
    __tablename__ = 'jxrwb'
    __table_args__ = (
        Index('jxrwb_zhdm', 'zhdm', 'fadm'),
        Index('indx_jxrwb_xn_xq', 'xn', 'xq'),
        Index('jxrwb_zhdm_fadm', 'xn', 'xq', 'zhdm', 'fadm', 'kcdm')
    )

    jxjhh = Column(VARCHAR(10), primary_key=True, nullable=False)
    zydm = Column(VARCHAR(6))
    zymc = Column(VARCHAR(40))
    xn = Column(VARCHAR(10))
    xq = Column(NUMBER(1, 0, False))
    kcdm = Column(VARCHAR(10))
    kcmc = Column(VARCHAR(110))
    xf = Column(VARCHAR(5))
    zxs = Column(VARCHAR(9))
    khfs = Column(VARCHAR(8))
    jxbxh = Column(NUMBER(2, 0, False))
    kcxz = Column(VARCHAR(30))
    kclb = Column(VARCHAR(30))
    jxbssx = Column(NUMBER(4, 0, False))
    jxbsxx = Column(NUMBER(4, 0, False))
    jxbbs = Column(NUMBER(2, 0, False))
    rs = Column(NUMBER(4, 0, False))
    kkxy = Column(VARCHAR(30))
    kkx = Column(VARCHAR(30))
    jszgh = Column(VARCHAR(10))
    jsxm = Column(VARCHAR(50))
    xkkh = Column(VARCHAR(35), primary_key=True, nullable=False, index=True)
    fzbs = Column(VARCHAR(3))
    qsz = Column(NUMBER(4, 0, False))
    jsz = Column(NUMBER(4, 0, False))
    zddh = Column(VARCHAR(20))
    jcmc = Column(VARCHAR(350), server_default=text("'???'"))
    zz = Column(VARCHAR(100), server_default=text("'.'"))
    cbs = Column(VARCHAR(250), server_default=text("'.'"))
    bb = Column(VARCHAR(100), server_default=text("'.'"))
    sfyxjc = Column(VARCHAR(10))
    xqyq = Column(VARCHAR(1))
    cdbs = Column(VARCHAR(20))
    rwxfbs = Column(VARCHAR(5))
    apbz = Column(VARCHAR(1))
    bz = Column(VARCHAR(250))
    xkzt = Column(VARCHAR(1), server_default=text("'1'"))
    skdd = Column(VARCHAR(255))
    sksj = Column(VARCHAR(450))
    fxbs = Column(NUMBER(1, 0, False))
    bkmc = Column(VARCHAR(20))
    dj = Column(NUMBER(1, 0, False))
    jsxh = Column(NUMBER(2, 0, False), server_default=text("1"))
    lrsj = Column(VARCHAR(30))
    mm = Column(VARCHAR(20))
    sysgs = Column(NUMBER(2, 0, False))
    lrsz = Column(VARCHAR(4), server_default=text("'??'"))
    syrl = Column(NUMBER(3, 0, False))
    sfsyb = Column(VARCHAR(2), server_default=text("'?'"))
    sfyjs = Column(VARCHAR(2), server_default=text("'?'"))
    jccbsj = Column(VARCHAR(12))
    zybs = Column(NUMBER(1, 0, False))
    kssj = Column(VARCHAR(100))
    xzdx = Column(VARCHAR(80))
    rl = Column(NUMBER(4, 0, False), server_default=text("0"))
    yxrs = Column(NUMBER(4, 0, False))
    pxbbs = Column(VARCHAR(20))
    tjqr = Column(VARCHAR(12))
    sfyjf = Column(VARCHAR(20), server_default=text("""\
null
"""))
    zybj = Column(NUMBER(1, 0, False))
    jsbj = Column(NUMBER(1, 0, False))
    bjmc = Column(VARCHAR(35), primary_key=True, nullable=False)
    sybj = Column(VARCHAR(250))
    zc = Column(VARCHAR(20))
    qsjsz = Column(VARCHAR(100))
    zyl = Column(NUMBER(4, 0, False))
    jys = Column(VARCHAR(50))
    zhxs = Column(VARCHAR(9))
    jkxs = Column(VARCHAR(9))
    syxs = Column(VARCHAR(9))
    syjs = Column(VARCHAR(40))
    hbyj = Column(VARCHAR(200))
    skh = Column(VARCHAR(200))
    zyfx = Column(VARCHAR(30), primary_key=True, nullable=False, server_default=text("'???'"))
    mkzh = Column(VARCHAR(100))
    jxbmc = Column(VARCHAR(254))
    pscj = Column(VARCHAR(20))
    qmcj = Column(VARCHAR(20))
    sycj = Column(VARCHAR(8))
    sczt = Column(VARCHAR(10), server_default=text("'1'"))
    sycdbs = Column(VARCHAR(20))
    sfxk = Column(VARCHAR(2))
    bkkcmc = Column(VARCHAR(40))
    jwcls = Column(NUMBER(1, 0, False))
    skfsmc = Column(VARCHAR(20))
    qzxs = Column(VARCHAR(3))
    xb = Column(VARCHAR(2))
    qzcj = Column(VARCHAR(8))
    sjxs = Column(VARCHAR(10), server_default=text("""\
'0'

"""))
    shtg = Column(VARCHAR(2))
    mxdx = Column(VARCHAR(250))
    bjgl = Column(NUMBER(5, 2, True))
    yxl = Column(NUMBER(5, 2, True))
    fdy = Column(VARCHAR(50))
    kssjd = Column(VARCHAR(4))
    ksfs = Column(VARCHAR(4))
    mkzhdm = Column(VARCHAR(50))
    zyfxmkdm = Column(VARCHAR(50))
    zyfxmk = Column(VARCHAR(100))
    price = Column(VARCHAR(100))
    cjlrfs = Column(VARCHAR(10))
    sfkpj = Column(VARCHAR(4), server_default=text("'?'"))
    ksrq = Column(VARCHAR(12))
    ts = Column(VARCHAR(2))
    jcbh = Column(VARCHAR(80))
    jxrw = Column(VARCHAR(50))
    sfkdc = Column(VARCHAR(10), server_default=text("'?'"))
    syxmbj = Column(VARCHAR(4))
    sfpdg = Column(VARCHAR(4), server_default=text("'?'"))
    pscjbl = Column(VARCHAR(10))
    qzcjbl = Column(VARCHAR(10))
    qmcjbl = Column(VARCHAR(10))
    sycjbl = Column(VARCHAR(10))
    sfkpx = Column(VARCHAR(10), server_default=text("'?'"))
    kcsjxs = Column(VARCHAR(9))
    xtkxs = Column(VARCHAR(9))
    knsjxs = Column(VARCHAR(9))
    kwsjxs = Column(VARCHAR(9))
    bkqr1 = Column(VARCHAR(4))
    sybjs = Column(VARCHAR(5))
    sfdjc = Column(VARCHAR(10), server_default=text("""\
'?'

"""))
    mmfscg = Column(VARCHAR(2))
    jcjssl = Column(VARCHAR(20))
    rwxkrs = Column(VARCHAR(10))
    cbdate = Column(VARCHAR(10))
    sfxbh = Column(VARCHAR(4))
    sjkmc = Column(VARCHAR(20))
    jsbh = Column(VARCHAR(20))
    kwxs = Column(VARCHAR(9), server_default=text("""\
'0'

"""))
    kssfpdct = Column(VARCHAR(2))
    hjqk = Column(VARCHAR(80))
    tdr = Column(VARCHAR(50))
    fdjszgh = Column(VARCHAR(50))
    fadm = Column(VARCHAR(8))
    zhdm = Column(VARCHAR(8))
    bjgs = Column(VARCHAR(8))
    pkdsz = Column(VARCHAR(6))
    cbsj = Column(VARCHAR(10))
    jcdj = Column(VARCHAR(150))
    skbh = Column(VARCHAR(6))
    jjlp = Column(VARCHAR(5))
    sksj_jtsj = Column(VARCHAR(200))
    bj = Column(VARCHAR(2))
    dbzxs = Column(VARCHAR(3))
    cjbl1 = Column(VARCHAR(8))
    cjbl2 = Column(VARCHAR(8))
    cjbl3 = Column(VARCHAR(8))
    cjbl4 = Column(VARCHAR(8))
    cjbl5 = Column(VARCHAR(8))
    cjbl6 = Column(VARCHAR(8))
    cjbl7 = Column(VARCHAR(8))
    cjbl8 = Column(VARCHAR(8))
    cjbl9 = Column(VARCHAR(8))
    cjbl10 = Column(VARCHAR(8))
    tybj = Column(VARCHAR(2))
    tjcjsj = Column(VARCHAR(20))
    sjqsjsz = Column(VARCHAR(20))
    sjjszgh = Column(VARCHAR(20), index=True)
    sjjsxm = Column(VARCHAR(20))
    sjzzs = Column(VARCHAR(20))
    jczs = Column(VARCHAR(40))
    jcys = Column(VARCHAR(40))
    pscjcx = Column(VARCHAR(8))
    qzcjcx = Column(VARCHAR(8))
    qmcjcx = Column(VARCHAR(8))
    sycjcx = Column(VARCHAR(8))
    pslrsz = Column(VARCHAR(20), server_default=text("""\
'??'

"""))
    yxtjqr = Column(VARCHAR(12))
    jsrwqr = Column(VARCHAR(10))
    pklh = Column(VARCHAR(40))
    jxhbbj = Column(VARCHAR(5))
    pkjsbh = Column(VARCHAR(40))
    bjrs = Column(VARCHAR(10))
    syjx = Column(NUMBER(asdecimal=False), server_default=text("1"))
    pcbzlb = Column(VARCHAR(20))
    pcxzmc = Column(VARCHAR(50))
    bzxx = Column(VARCHAR(254))
    rlxz = Column(VARCHAR(2))
    pkr = Column(VARCHAR(10))
    tjlx = Column(VARCHAR(20))
    cxrs = Column(VARCHAR(20))
    sfkzp = Column(VARCHAR(10), server_default=text("""\
'?'

"""))
    bkkcdm = Column(VARCHAR(10))
    rltzbj = Column(VARCHAR(4), server_default=text("""\
'0'

"""))
    zxsfa = Column(VARCHAR(50))
    pkydsj = Column(VARCHAR(100))
    yxtjqrr = Column(VARCHAR(20))
    yxtjqrsj = Column(VARCHAR(20))
    tjqrr = Column(VARCHAR(20))
    tjqrsj = Column(VARCHAR(20))
    sfcjqzks = Column(VARCHAR(4))
    qzkssfjs = Column(VARCHAR(4))
    qzksfs = Column(VARCHAR(4))
    qmksfs = Column(VARCHAR(4))
    ysrl = Column(NUMBER(4, 0, False))
    klcjqssj = Column(VARCHAR(20))
    klcjjssj = Column(VARCHAR(20))
    lcjjz = Column(VARCHAR(20))
    sksj_bjew = Column(VARCHAR(255))
    pscjzg = Column(VARCHAR(8))
    qzcjzg = Column(VARCHAR(8))
    qmcjzg = Column(VARCHAR(8))
    sycjzg = Column(VARCHAR(8))
    fcjxcjxs = Column(VARCHAR(8))
    xzdxdm = Column(VARCHAR(200))
    mxdxdm = Column(VARCHAR(200))
    ljczgh = Column(VARCHAR(20))
    jcbz = Column(VARCHAR(250))
    ljcsj = Column(VARCHAR(20))
    ggkc = Column(VARCHAR(2))
    lcjjszgh = Column(VARCHAR(20))
    xtjqr = Column(VARCHAR(20))
    xtjqrr = Column(VARCHAR(20))
    xtjqrsj = Column(VARCHAR(20))
    bz2 = Column(VARCHAR(200))
    kssj_qz = Column(VARCHAR(100))
    kssjd_qz = Column(VARCHAR(100))
    ksrq_qz = Column(VARCHAR(12))
    khfs_qz = Column(VARCHAR(28))
    ksfs_qz = Column(VARCHAR(4))
