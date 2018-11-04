import jieba.analyse

# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式

# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))

# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))
content = '''智课 - 同样的时间，更高的分数|TOEFLIELTSSATGREGMAT更多
英语能力
职业规划
ACT
AP
考研
四级
六级
智适应训练营公开课线下服务
语培服务
留学服务
APP
注册登录
TOEFL
首页练习模考课程商城资讯
托福真题托福机经托福词汇托福资讯托福听力托福口语托福写作托福阅读托福资料下载
资料库
托福名师私人订制直达90分
15840元已有3284人购买
有效期：
120天
课程特色：
入学测试
模考&规划
1对1授课
逐题精讲
作业精批
督导&答疑
外教批改
在线咨询
课时数：
135课时
1对1课时：
32课时
48课时
64课时
96课时
128课时
160课时
240课时
立即购买免费咨询
课程概述
授课专家
课程介绍
1对1
专家课
练习
批改
学习资料

推荐内容
热门课程列表
1
托福名师私人订制直达100分-64课时
2
托福名师私人订制直达110分
3
托福名师私人订制直达体验班-阅读
4
托福名师私人订制直达体验班-口语
5
12月TOEFL强化周末班121505
最具品牌影响力教育机构
最具成长性的教育品牌
年度影响力教育品牌
我最信赖的教育品牌
年度创新成长企业百强
年度新势力教育机构
联系我们
客服热线：400-011-9191
客服邮箱：service@smartstudy.com
智课教育韦晓亮建议直达邮箱：ceo@innobuddy.com
智课教育韦晓亮建议直达微信：zkjywxljyzd
微信公众号
微博
智课APP
关于智课|加入我们|版权声明|服务协议|招商加盟|意见反馈|智课APP
© 2011~2020|北京创新伙伴教育科技有限公司|京ICP备13047080号'''
words = jieba.analyse.extract_tags(content, topK=10, withWeight=True)

print(words)
