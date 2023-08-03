from openpyxl import Workbook

# 워크북(workbook) 생성
workbook = Workbook()

# 활성화된 워크시트(worksheet) 가져오기
worksheet = workbook.active

# 한 줄(row)씩 데이터 입력하기 : 모델명, 크기, 가격(min), 가격(max)
worksheet.append(["더 뉴 아반떼", "준중형", 1960, 3203])
worksheet.append(["아반떼 N", "준중형", 3212, 3399])
worksheet.append(["쏘나타 뉴 라이즈", "중형", 2043, 2600])
worksheet.append(["쏘나타", "중형", 2249, 3706])

# 워크북(workbook) 저장하기
workbook.save("output.xlsx")