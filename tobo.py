tasks = []

while True:
    print("\n1. 新增待辦")
    print("2. 查看待辦")
    print("3. 離開")

    choice = input("請選擇：")

    if choice == "1":
        task = input("請輸入待辦事項：")
        if task:
            tasks.append(task)
            print("已新增。")
        else:
            print("待辦內容不能空白。")

    elif choice == "2":
        if not tasks:
            print("目前沒有待辦事項。")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

    elif choice == "3":
        print("再見！")
        break

    else:
        print("請輸入 1、2 或 3。")