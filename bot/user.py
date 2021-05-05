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

#Default Data
default_credit = 100
default_level = 1

wb = load_workbook("userDB.xlsx")
ws = wb.active

def signup(_name, _id):
    ws.cell(row=2, column=u_id, value=_name)
    ws.cell(row=2, column=u_name, value =_id)
    ws.cell(row=2, column=u_credit, value = default_credit)
    ws.cell(row=2, column=u_level, value = defailt_level)

    wb.save("userDB.xlsx")
