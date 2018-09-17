# from xml.etree.ElementTree import parse
# # 解析XML文件
# doc = parse('testxml')
# # 获取对应的节点
# def f():
#     for item in doc.iterfind('ResponseEntity\resStatus'):
#         # 获取属性对应的值
#         title = item.findtext('resStatus')
#         print(title)
#         print()
# f()

from xml.etree.ElementTree import parse
# 解析XML
doc = parse('testxml')
# 获取根节点
root = doc.getroot()
# 获取根节点下面的下一节点
def f():
    for data in root.findall('resStatus'):
        for report in data.findall('resStatus'):
            for targets in report.findall('resStatus'):
                for target in targets.findall('resStatus'):
                    print('扫描ip：', end='')
    # 获取属性对应的值
                    ip = target.find('resStatus').text
                    print(ip)
f()
{"resStatus":1000,"resMsg":null,"params":{"finAccount":{"sortColumns":null,"systemName":null,"queryColumnId":null,"id":null,"regUserId":null,"userName":null,"accountType":null,"passwd":null,"nowMoney":100680483.33,"freezeMoney":1053600.00,"useableMoney":99626883.33,"state":null,"createTime":null,"createTimeBegin":null,"createTimeEnd":null,"modifyTime":null,"modifyTimeBegin":null,"modifyTimeEnd":null,"useableMoneyStart":null,"useableMoneyEnd":null,"beforeNowMoney":null,"totalAmount":102046135.13},"lastLoginTime":1536658282000,"showProducts":0,"accInvest":1,"regUser":{"sortColumns":null,"systemName":null,"queryColumnId":null,"id":1140,"code":"","login":15510000011,"nickName":"鸿坤金服","passwd":"******","identify":1,"type":1,"headPortrait":"head_portrait/default_portrait.jpg","lastLoginTime":1536659418714,"lastLoginTimeBegin":null,"lastLoginTimeEnd":null,"state":1,"createTime":1533092315000,"createTimeBegin":null,"createTimeEnd":null,"modifyTime":1533092719000,"modifyTimeBegin":null,"modifyTimeEnd":null,"vipFlag":1,"userIds":[]}}}