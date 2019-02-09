import card_tools

while True:
    # 显示菜单及功能
    card_tools.show_menu()
    action_str = input("请确认你的选择：")
    print("你选择的操作是【%s】" % action_str)
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            # 新建名片
            card_tools.add_card()
            # card_tools.add_card()
        elif action_str == "2":
            # 搜索名片
            card_tools.show_all()
        elif action_str == "3":
            # 显示全部
            card_tools.searon_card()
    elif action_str == "0":
            # 退出系统
        print("退出系统\n欢迎下次再来！")
        break
    else:
        print("选择错误，请重新选择")
