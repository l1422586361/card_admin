import ast

def show_all_list():
    """
    读取文件内容，以列表形式输出
    :return: 返回列表
    """
    file = open("LIST")
    list =[]
    while True:
        text = file.readline()
        if not text:
            break
        list.append(ast.literal_eval(text))  # 使用eval会有安全问题，ast.literal_eval则不会
    file.close()
    return list


def show_menu():
    print("*" * 50)
    print("欢迎【名片管理系统】 V 1.0")
    print()
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print()
    print("0.退出系统")
    print("*" * 50)

def add_card():
    print("新增名片")
    print("=" * 50 )
    # 1、提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    email_str = input("请输入邮箱：")
    # 2、使用用户输入的信息建立一个名片字典
    card_dict = {"name":name_str,"phone":phone_str,"email":email_str}
    cards_list = show_all_list()
    # 3、将名片字典添加到列表中
    cards_list.append(card_dict)
    update_list(cards_list)
    # 4、提示用户添加成功
    print()
    print("添加 %s 名片成功！" % name_str)
    # 打印表头
    for name in ("姓名","电话","邮箱"):
        print(name,end="\t\t")
    print()
    print("%s \t\t%s \t\t%s" % (card_dict["name"],
                                card_dict["phone"],
                                card_dict["email"]))
    print("=" * 50)

def show_all():
    # 打印分隔线
    print("显示全部")
    print("=" * 50)
    # 打印表头
    for name in ("姓名","电话","邮箱"):
        print(name,end="\t\t")
    print("")
    # 遍历名片列表依次输出字典信息
    cards_list = show_all_list()
    print(cards_list)
    for card_dict in cards_list:
        print("%s \t\t%s \t\t%s" % (card_dict["name"],
                                  card_dict["phone"],
                                  card_dict["email"]))
    print("=" * 50)
    pass
def searon_card():
    # 打印分隔线
    print("查询名片")
    print("=" * 50)
    cards_list = show_all_list()
    name_str = input("请输入您需要查询的名片姓名：")
    if len(cards_list) == 0:
        print("\n当前无名片记录！")
    else:
        for find_card in cards_list:
            if find_card["name"] == name_str and len(find_card)>0:
                print("已为您查到对应 %s 姓名的名片：" % name_str)
                print(find_card)
                deal_card(cards_list,find_card,name_str)
                break
            else:
                print("未查询到对应 %s 姓名的名片" % name_str)
    print("=" * 50)

def deal_card(cards_list,dict,name):
    """
对名片进行处理，处理操作分为修改、删除、返回
    :param dict: 传入的字典
    :param name: 用户输入的字符串
    :return: 为0时退出函数
    """
    action_str = input("确认对该名片记录做何操作：【1.修改】、【2.删除】、【0.返回首页】")
    if action_str in ("1","2"):
        if action_str == "1":
            dict["name"]=update_card(dict["name"],"姓名(空白则不修改)：")
            dict["phone"]=update_card(dict["phone"],"电话(空白则不修改)：")
            dict["email"]=update_card(dict["email"],"邮箱(空白则不修改)：")
            print("修改 %s 名片成功" % dict["name"])
            update_list(cards_list)
        else:
            cards_list.remove(dict)
            print("已完成对 %s 姓名的名片删除" % name)
            update_list(cards_list)
    elif action_str == "0":
        return
    else:
        print("输入操作有误，请重新输入！")
        deal_card(cards_list,dict,name)

def update_card(dict_value,tip):
    """
针对用户输入文本进行空白字符判断处理，空白则返回字典原值
    :param dict_value: 字典原值
    :param tip: 提示信息
    :return:
    """
    info = input(tip)
    if len(info)>0:
        return info
    else:
        return dict_value

def update_list(cards_list):
    """
    更新文件内容，将列表以格式输入至文件内（先清空文件内容，再输入1）
    :param cards_list: 列表
    """
    f = open("LIST","w")
    f.truncate()
    for i in cards_list:
        f.writelines(str(i)+"\n")
    print(cards_list)
    f.close()