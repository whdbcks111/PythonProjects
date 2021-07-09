from school_menu import getMenu as getSchoolMenu
import datetime

while True:
    school_name = input('\n\n학교 이름을 입력하세요 (나가려면 엔터)\n  >>> ')

    if len(school_name) == 0:
        break

    print('불러오는 중...')
    menu_info = getSchoolMenu(school_name)

    if menu_info is None:
        print('해당하는 학교를 검색할 수 없습니다.')
        continue

    print('출력 내용을 선택하세요.\n  1. 오늘  2. 내일  3. 어제  4. 전체  5. 날짜 지정')

    select = 0
    while True:
        try:
            select = int(input('  >>> '))
            if not 1 <= select <= 5:
                print('1부터 5 사이의 정수를 입력하세요.')
                continue
            break
        except ValueError:
            print('숫자가 아닙니다. 다시 입력하세요.')

    print_list = {}

    if select == 0 or select == 4:
        print_list = menu_info
    elif select == 1:
        date_str = "%d.%d" % (datetime.date.today().month, datetime.date.today().day)
        print_list[date_str] = menu_info.get(date_str)
    elif select == 2:
        date_str = "%d.%d" % (datetime.date.today().month, datetime.date.today().day + 1)
        print_list[date_str] = menu_info.get(date_str)
    elif select == 3:
        date_str = "%d.%d" % (datetime.date.today().month, datetime.date.today().day - 1)
        print_list[date_str] = menu_info.get(date_str)
    elif select == 5:
        day = 0
        while True:
            try:
                day = int(input("며칠인 지 입력하세요 : "))
                break
            except ValueError:
                print('정수를 입력하세요.')
        date_str = "%d.%d" % (datetime.date.today().month, day)
        print_list[date_str] = menu_info.get(date_str)

    if len(print_list.values()) == 0:
        print("해당하는 날의 급식 정보가 없습니다.")
    else:
        for (d, data) in print_list.items():
            print("[ %s ]" % d)
            for (menu_type, menu_list) in data.items():
                print("  <%s>" % menu_type)
                for menu in menu_list:
                    print("   " + menu)
