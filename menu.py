def show_menu():
    print("====== MENU ======")
    print("1. 打招呼")
    print("2. 显示信息")
    print("0. 退出")
    print("==================")

def main():
    while True:
        show_menu()
        choice = input("请输入你的选择：")

        if choice == "1":
            print("你好，欢迎使用菜单程序！")
        elif choice == "2":
            print("作者：你的名字\n版本：v1.0")
        elif choice == "0":
            print("退出程序。")
            break
        else:
            print("无效的选项，请重新输入。")

if __name__ == "__main__":
    main()
