#user.py
#code base ( richardlee-kr 's SuperBot )
#https://github.com/richardlee-kr/SuperBot

from openpyxl import load_workbook, Workbook

#Data list
u_id = 1 #유저의 id
u_name = 2 #유저의 이름
u_credit = 3 #유저의 크레딧
u_level = 4 #유저의 레벨( 메인 )
u_aresource = 5#유저가 가진 자원 A
u_bresource = 6#유저가 가진 자원 B
u_cresource = 7#유저가 가진 자원 C
u_dresource = 8#유저가 가진 자원 D
u_levelmining = 9 #유저의 채굴 레벨
u_miningcountupgrade = 10 #채굴 횟수 업그레이드
u_miningamountupgrade = 11 #채굴량 업그레이드
u_miningluckupgrade = 12 #행운( 채굴 ) 업그레이드
u_bankcredit = 13 #은행에 보관된 유저의 크레딧
u_bankrank = 14 #유저의 은행 등급
u_userbanktax = 15 #유저가 은행에 지불한 모든 수수료의 총합
u_usertax = 16 #유저가 지불한 모든 세금의 총합

#Default Data
default_credit = 100
default_level = 1
default_aresource = 0
default_bresource = 0
default_cresource = 0
default_dresource = 0
default_levelmining = 1
default_miningcountupgrade = 0
default_miningamountupgrade = 0
default_miningluckupgrade = 0
default_bankcredit = 500
default_bankrank = 1
default_banktax = 0
default_tax = 0

wb = load_workbook("userDB.xlsx")
ws = wb.create_sheet("User Data", 0 )

def loadFile():
    print("엑셀 파일을 불러옵니다.")
    wb = load_workbook("userDB.xlsx")
    ws = wb.create_sheet("User Data", 0 )
    
def saveFile():
    print("엑셀 파일을 저장합니다.")
    wb.save("userDB.xlsx")
    wb.close()
    
def checkUserNum():
    print("user.py의 checkUserNum 실행중")
    loadFile()
    count = 0
    for row in range(2, ws.max_row+1):
        if ws.cell(row,c_name).value != None:
            count = count+1
        else:
            count = count
    return count

def checkFirstRow():
    print("user.py의 checkFirstRow 실행중")
    loadFile()
    for row in range(2, ws.max_row + 1):
        if ws.cell(row,1).value is None:
            return row
            break
    _result = ws.max_row+1
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
        print(row, "번째 줄 name: ", ws.cell(row,c_name).value)
        print("입력된 name: ", _name)
        print("이름과 일치 여부: ", ws.cell(row, c_name).value == _name)
        print(row,"번째 줄 id: ", ws.cell(row,c_id).value)
        print("입력된 id: ", hex(_id))
        print("고유번호정보와 일치 여부: ", ws.cell(row, c_id).value == hex(_id))
        if ws.cell(row, c_name).value == _name and ws.cell(row,c_id).value == hex(_id):
            print("등록된  이름과 고유번호를 발견")
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
    
    print("유저 id | ", ws.cell(_row,u_id).value)
    ws.cell( row = _row, column = u_id, value = hex(_id))
    print("유저 이름 | ",  ws.cell( _row, u_name ).value)
    ws.cell( row = _row, column = u_name, value = _name)

    print("유저 초기 크레딧 | ",  ws.cell( _row, u_credit ).value)
    ws.cell( row = _row, column = u_credit, value = default_credit)
    
    

    

    saveFile()

    print("신규 데이터 생성 완료!")

def signup(_name, _id):
    _row = checkRow()
    
    ws.cell(_row, column = u_id, value = _name)
    ws.cell(_row, column = u_name, value = _id)
    ws.cell(_row, column = u_credit, value = default_credit)
    ws.cell(_row, column = u_level, value = defalt_level)
    ws.cell(_row, column = u_aresource, value = default_aresource)
    ws.cell(_row, column = u_bresource, value = default_bresource)
    ws.cell(_row, column = u_cresource, value = default_cresource)
    ws.cell(_row, column = u_dresource, value = default_dresource)
    ws.cell(_row, column = u_levelmining, value = defalt_levelmining)
    ws.cell(_row, column = u_miningcountupgrade, value = default_miningcountupgrade)
    ws.cell(_row, column = u_miningamountupgrade, value = default_miningamountupgrade)
    ws.cell(_row, column = u_miningluckupgrade, value = default_miningluckupgrade)
    ws.cell(_row, column = u_bankcredit, value = default_bankcredit)
    ws.cell(_row, column = u_bankrank, value = default_bankrank)
    ws.cell(_row, column = u_userbanktax, value = default_banktax)
    ws.cell(_row, column = u_usertax, value = default_tax)
    
    wb.save("userDB.xlsx")
