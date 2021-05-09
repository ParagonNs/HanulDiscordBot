#user.py
#code base ( richardlee-kr 's SuperBot )
#https://github.com/richardlee-kr/SuperBot

from openpyxl import load_workbook, Workbook

wb = load_workbook("BotDB.xlsx", data_only = True)
wus = wb.create_sheet("User Data", 0 )
wns = wb.create_sheet("Country Data", 1 )

def loadFile():
    print("엑셀 파일을 불러옵니다.")
    wb = load_workbook("BotDB.xlsx")
    wus = wb.create_sheet("User Data", 0 )
    
def saveFile():
    print("엑셀 파일을 저장합니다.")
    wb.save("BotDB.xlsx")
    wb.close()
    
def checkUserNum():
    print("user.py의 checkUserNum 실행중")
    loadFile()
    count = 0
    for row in range(2, wus.max_row+1):
        if wus.cell(row,User_data_list[1]).value != None:
            count = count+1
        else:
            count = count
    return count

def checkFirstRow():
    print("user.py의 checkFirstRow 실행중")
    loadFile()
    for row in range(2, wus.max_row + 1):
        if wus.cell(row,1).value is None:
            return row
            break
    _result = wus.max_row+1
    saveFile()
    return _result

def checkUser(_name, _id):
    print("user.py의 checkUser 실핼중")
    print(str(_name) + "<" + str(_id) + ">의 존재 여부 확인")
    loadFile()
    userNum = checkUserNum()
    print("등록된 유저수: ", userNum)
    print("이름과 고유번호 탐색")
    print("")
    for row in range(2, 3+userNum):
        print(row, "번째 줄 name: ", wus.cell(row,User_data_list[1]).value)
        print("입력된 name: ", _name)
        print("이름과 일치 여부: ", wus.cell(row, User_data_list[1]).value == _name)
        print(row,"번째 줄 id: ", wus.cell(row, User_data_list[0]).value)
        print("입력된 id: ", hex(_id))
        print("유저 고유 번호 와 일치 여부: ", wus.cell(row, User_data_list[0]).value == hex(_id))
        if wus.cell(row, User_data_list[1]).value == _name and wus.cell(row, User_data_list[0]).value == hex(_id):
            print("등록된  이름과 유저 고유 번호를 발견")
            print("등록된  값의 위치: ",  row, "번째 줄")
            saveFile()
            return True, row
            break
        else:
            print("등록된 정보를 탐색 실패, 재탐색 실시")
    saveFile()
    print("발견 실패")
    return False, None
            
def Signup(_name, _id):
    print("user.py의 signup 실행중")
    loadFile()
    _row = checkFirstRow()
    print("가장 처음으로 빈 행 : ", _row)
    print("신규 데이터를 생성합니다.")
    
    #Data list
    User_data_list[ hex(_id), _name, 100, 1, 0, 0, 0, 0, 1, 0, 0, 0, 500, 1, 0, 0 ]
    #id, name, credit, 유저의 레벨( 메인 ), 유저가 가진 자원 A, 유저가 가진 자원 B
    #유저가 가진 자원 C, 유저가 가진 자원 D, 유저의 채굴 레벨, 채굴 횟수 업그레이드, 채굴량 업그레이드, 행운( 채굴 ) 업그레이드
    #은행에 보관된 유저의 크레딧, 유저의 은행 등급, 유저가 은행에 지불한 모든 수수료의 총합, 유저가 지불한 모든 세금의 총합
    
    for i in range( 0, len( User_data_list )):
        wus.cell( _row, column = i + 1, value = User_data_list[i])

    saveFile()

    print("신규 데이터 생성 완료!")
    
