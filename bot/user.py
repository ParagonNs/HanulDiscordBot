#user.py

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
ws = wb.active

def checkRow():
    for row in range(2, ws.max_row + 1):
        if ws.cell(row,1).value is None:
            return row
            break

def checkName(_name, _id):
    for row in range(2, ws.max_row+1):
        if ws.cell(row,1).value == _name and ws.cell(row,2).value == _id:
            break
            return false
        else:
            return true
            break
            
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
