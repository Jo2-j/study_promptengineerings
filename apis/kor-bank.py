# # # # # # import requests
# # # # # # import xml.etree.ElementTree as ET

# # # # # # # 한국은행 Open API 인증키
# # # # # # API_KEY = "DA3T67WSL19LH0FK7A0Q"  # 한국은행에서 발급받은 인증키를 입력하세요.

# # # # # # # API 요청 파라미터
# # # # # # SERVICE_NAME = "StatisticTableList"  # 서비스명
# # # # # # REQUEST_TYPE = "xml"  # 요청 결과 형식 (xml 또는 json)
# # # # # # LANGUAGE = "kr"  # 언어 (kr: 한국어, en: 영어)
# # # # # # START_COUNT = 1  # 요청 시작 건수
# # # # # # END_COUNT = 10  # 요청 종료 건수
# # # # # # TABLE_CODE = "102Y004"  # 통계표코드 (선택사항)

# # # # # # # API URL 생성
# # # # # # url = f"https://ecos.bok.or.kr/api/{SERVICE_NAME}/{API_KEY}/{REQUEST_TYPE}/{LANGUAGE}/{START_COUNT}/{END_COUNT}/{TABLE_CODE}"

# # # # # # # API 호출
# # # # # # response = requests.get(url)

# # # # # # # 응답 데이터 처리
# # # # # # if response.status_code == 200:
# # # # # #     # XML 데이터를 파싱
# # # # # #     root = ET.fromstring(response.content)
    
# # # # # #     # 출력 예제: 통계표코드와 통계명 출력
# # # # # #     for item in root.findall(".//row"):
# # # # # #         stat_code = item.find("STAT_CODE").text
# # # # # #         stat_name = item.find("STAT_NAME").text
# # # # # #         print(f"통계표코드: {stat_code}, 통계명: {stat_name}")
# # # # # # else:
# # # # # #     print(f"API 요청 실패. 상태 코드: {response.status_code}, 메시지: {response.text}")


# # # # # import requests
# # # # # import xml.etree.ElementTree as ET
# # # # # import csv

# # # # # # 한국은행 Open API 인증키
# # # # # API_KEY = "DA3T67WSL19LH0FK7A0Q"  # 한국은행에서 발급받은 인증키를 입력하세요.

# # # # # # API 요청 파라미터
# # # # # SERVICE_NAME = "StatisticTableList"  # 서비스명
# # # # # REQUEST_TYPE = "xml"  # 요청 결과 형식 (xml 또는 json)
# # # # # LANGUAGE = "kr"  # 언어 (kr: 한국어, en: 영어)
# # # # # START_COUNT = 1  # 요청 시작 건수
# # # # # END_COUNT = 10  # 요청 종료 건수
# # # # # TABLE_CODE = "131Y010"  # 통계표코드 (선택사항)

# # # # # # API URL 생성
# # # # # url = f"https://ecos.bok.or.kr/api/{SERVICE_NAME}/{API_KEY}/{REQUEST_TYPE}/{LANGUAGE}/{START_COUNT}/{END_COUNT}/{TABLE_CODE}"

# # # # # # API 호출
# # # # # response = requests.get(url)

# # # # # # 응답 데이터 처리
# # # # # if response.status_code == 200:
# # # # #     # XML 데이터를 파싱
# # # # #     root = ET.fromstring(response.content)
    
# # # # #     # CSV 파일에 저장할 데이터 리스트
# # # # #     data_list = []
    
# # # # #     # 출력 예제: 통계표코드와 통계명 저장
# # # # #     for item in root.findall(".//row"):
# # # # #         stat_code = item.find("STAT_CODE").text
# # # # #         stat_name = item.find("STAT_NAME").text
# # # # #         cycle = item.find("CYCLE").text
# # # # #         org_name = item.find("ORG_NAME").text
# # # # #         data_list.append([stat_code, stat_name, cycle, org_name])
    
# # # # #     # CSV 파일 저장
# # # # #     csv_file_name = "korean_bank_statistics.csv"
# # # # #     with open(csv_file_name, mode="w", newline="", encoding="utf-8") as file:
# # # # #         writer = csv.writer(file)
# # # # #         # 헤더 작성
# # # # #         writer.writerow(["통계표코드", "통계명", "주기", "출처"])
# # # # #         # 데이터 작성
# # # # #         writer.writerows(data_list)
    
# # # # #     print(f"데이터가 '{csv_file_name}' 파일로 저장되었습니다.")
# # # # # else:
# # # # #     print(f"API 요청 실패. 상태 코드: {response.status_code}, 메시지: {response.text}")



# # # # import requests

# # # # # API 요청에 필요한 파라미터 설정
# # # # SERVICE_NAME = "StatisticSearch"  # API 서비스명
# # # # API_KEY = "DA3T67WSL19LH0FK7A0Q"                # 한국은행에서 발급받은 오픈API 인증키
# # # # REQUEST_TYPE = "json"              # 결과값의 파일 형식 (xml, json)
# # # # LANGUAGE = "kr"                   # 결과값의 언어 (kr: 국문, en: 영문)
# # # # START_COUNT = 1                   # 전체 결과값 중 시작 번호
# # # # END_COUNT = 10                    # 전체 결과값 중 끝 번호
# # # # TABLE_CODE = "131Y010"            # 통계표코드
# # # # FREQUENCY = "Q"                   # 주기 (년: A, 반년: S, 분기: Q, 월: M, 반월: SM, 일: D)
# # # # START_DATE = "2017"               # 검색 시작일자
# # # # END_DATE = "2017"                 # 검색 종료일자

# # # # # 선택적 통계항목코드
# # # # STAT_ITEM_CODE1 = "1100000"         # 통계항목1코드
# # # # STAT_ITEM_CODE2 = ""              # 통계항목2코드
# # # # STAT_ITEM_CODE3 = ""              # 통계항목3코드
# # # # STAT_ITEM_CODE4 = ""              # 통계항목4코드

# # # # # URL 템플릿 생성
# # # # url = f"https://ecos.bok.or.kr/api/{SERVICE_NAME}/{API_KEY}/{REQUEST_TYPE}/{LANGUAGE}/{START_COUNT}/{END_COUNT}/{TABLE_CODE}/{FREQUENCY}/{START_DATE}/{END_DATE}/{STAT_ITEM_CODE1}/{STAT_ITEM_CODE2}/{STAT_ITEM_CODE3}/{STAT_ITEM_CODE4}"

# # # # # API 호출
# # # # response = requests.get(url)

# # # # # 결과 출력
# # # # if response.status_code == 200:
# # # #     print(response.text)  # 성공 시 결과 출력
# # # # else:
# # # #     print(f"Error: {response.status_code}")  # 오류 발생 시 상태 코드 출력

# # # import requests
# # # import csv
# # # # API 요청에 필요한 파라미터 설정
# # # 서비스명 = "StatisticSearch"  # API 서비스명
# # # 인증키 = "DA3T67WSL19LH0FK7A0Q"  # 한국은행에서 발급받은 오픈API 인증키
# # # 요청유형 = "json"  # 결과값의 파일 형식 (xml, json)
# # # 언어구분 = "kr"  # 결과값의 언어 (kr: 국문, en: 영문)
# # # 요청시작건수 = 1  # 전체 결과값 중 시작 번호
# # # 요청종료건수 = 10  # 전체 결과값 중 끝 번호
# # # 통계표코드 = "131Y010"  # 통계표코드
# # # 주기 = "Q"  # 주기 (년: A, 반년: S, 분기: Q, 월: M, 반월: SM, 일: D)
# # # 검색시작일자 = "2017"  # 검색 시작일자
# # # 검색종료일자 = "2020"  # 검색 종료일자
# # # 통계항목코드1 = "1100000"  # 통계항목1코드
# # # 통계항목코드2 = "C20"  # 통계항목2코드
# # # # 통계항목코드3 = ""  # 통계항목3코드
# # # # 통계항목코드4 = ""  # 통계항목4코드

# # # # URL 템플릿 생성
# # # url = f"https://ecos.bok.or.kr/api/{서비스명}/{인증키}/{요청유형}/{언어구분}/{요청시작건수}/{요청종료건수}/{통계표코드}/{주기}/{검색시작일자}/{검색종료일자}/{통계항목코드1}/{통계항목코드2}"


# # # # API 호출
# # # response = requests.get(url)

# # # # 결과 처리 및 CSV 저장
# # # if response.status_code == 200:
# # #     # JSON 데이터로 변환 (API 응답 형식에 따라 수정 필요)
# # #     data = response.json()  # 응답이 JSON 형식일 경우
# # #     rows = data.get("StatisticSearch", [])  # 데이터의 키에 맞게 수정 필요
    
# # #     # CSV 파일 저장
# # #     with open("api_result.csv", mode="w", newline="", encoding="utf-8") as file:
# # #         writer = csv.writer(file)
        
# # #         # 헤더 작성 (필요에 따라 수정)
# # #         if rows:
# # #             header = rows[0].keys()
# # #             writer.writerow(header)
        
# # #         # 데이터 작성
# # #         for row in rows:
# # #             writer.writerow(row.values())
    
# # #     print("CSV 파일로 저장되었습니다: api_result.csv")
# # # else:
# # #     print(f"Error: {response.status_code}")  # 오류 발생 시 상태 코드 출력


# # import requests
# # import csv

# # # API 요청에 필요한 파라미터 설정
# # 서비스명 = "StatisticSearch"  # API 서비스명
# # 인증키 = "DA3T67WSL19LH0FK7A0Q"  # 한국은행에서 발급받은 오픈API 인증키
# # 요청유형 = "json"  # 결과값의 파일 형식 (xml, json)
# # 언어구분 = "kr"  # 결과값의 언어 (kr: 국문, en: 영문)
# # 요청시작건수 = 1  # 전체 결과값 중 시작 번호
# # 요청종료건수 = 10  # 전체 결과값 중 끝 번호
# # 통계표코드 = "131Y010"  # 통계표코드
# # 주기 = "Q"  # 주기 (년: A, 반년: S, 분기: Q, 월: M, 반월: SM, 일: D)
# # 검색시작일자 = "2017"  # 검색 시작일자
# # 검색종료일자 = "2020"  # 검색 종료일자
# # 통계항목코드1 = "1100000"  # 통계항목1코드
# # 통계항목코드2 = "C20"  # 통계항목2코드

# # # URL 템플릿 방식
# # url = f"https://ecos.bok.or.kr/api/{서비스명}/{인증키}/{요청유형}/{언어구분}/{요청시작건수}/{요청종료건수}/{통계표코드}/{주기}/{검색시작일자}/{검색종료일자}/{통계항목코드1}/{통계항목코드2}"

# # # params 방식
# # params = {
# #     "service": 서비스명,
# #     "authKey": 인증키,
# #     "format": 요청유형,
# #     "lang": 언어구분,
# #     "startCount": 요청시작건수,
# #     "endCount": 요청종료건수,
# #     "statCode": 통계표코드,
# #     "cycle": 주기,
# #     "startDate": 검색시작일자,
# #     "endDate": 검색종료일자,
# #     "itemCode1": 통계항목코드1,
# #     "itemCode2": 통계항목코드2,
# # }

# # # API 호출 (URL 방식)
# # response = requests.get(url, params=params)

# # # 결과 처리 및 CSV 저장
# # if response.status_code == 200:
# #     # JSON 데이터로 변환 (API 응답 형식에 따라 수정 필요)
# #     data = response.json()  # 응답이 JSON 형식일 경우
# #     rows = data.get("StatisticSearch", [])  # 데이터의 키에 맞게 수정 필요
    
# #     # CSV 파일 저장
# #     with open("api_result.csv", mode="w", newline="", encoding="utf-8") as file:
# #         writer = csv.writer(file)
        
# #         # 헤더 작성 (필요에 따라 수정)
# #         if rows:
# #             header = rows[0].keys()
# #             writer.writerow(header)
        
# #         # 데이터 작성
# #         for row in rows:
# #             writer.writerow(row.values())
    
# #     print("CSV 파일로 저장되었습니다: api_result.csv")
# # else:
# #     print(f"Error: {response.status_code}")  # 오류 발생 시 상태 코드 출력
# #     print(response.text)  # API에서 반환한 에러 메시지 출력


# import requests
# import csv

# # API 요청에 필요한 파라미터 설정
# 서비스명 = "StatisticSearch"  # API 서비스명
# 인증키 = "DA3T67WSL19LH0FK7A0Q"  # 한국은행에서 발급받은 오픈API 인증키
# 요청유형 = "json"  # 결과값의 파일 형식 (xml, json)
# 언어구분 = "kr"  # 결과값의 언어 (kr: 국문, en: 영문)
# 요청시작건수 = 1  # 전체 결과값 중 시작 번호
# 요청종료건수 = 10  # 전체 결과값 중 끝 번호
# 통계표코드 = "131Y010"  # 통계표코드
# 주기 = "Q"  # 주기 (년: A, 반년: S, 분기: Q, 월: M, 반월: SM, 일: D)
# 검색시작일자 = "2017"  # 검색 시작일자
# 검색종료일자 = "2020"  # 검색 종료일자
# 통계항목코드1 = "1100000"  # 통계항목1코드
# 통계항목코드2 = "C20"  # 통계항목2코드

# # URL 템플릿 방식
# url = f"https://ecos.bok.or.kr/api/{서비스명}/{인증키}/{요청유형}/{언어구분}/{요청시작건수}/{요청종료건수}/{통계표코드}/{주기}/{검색시작일자}/{검색종료일자}/{통계항목코드1}/{통계항목코드2}"

# # API 호출
# response = requests.get(url)

# # 결과 처리 및 CSV 저장
# if response.status_code == 200:
#     try:
#         # JSON 데이터로 변환
#         data = response.json()  # 응답이 JSON 형식일 경우
#         rows = data.get("StatisticSearch", [])  # 데이터의 키에 맞게 수정 필요
        
#         if not rows:
#             print("데이터가 없습니다.")
#         else:
#             # CSV 파일 저장
#             with open("api_result.csv", mode="w", newline="", encoding="utf-8") as file:
#                 writer = csv.writer(file)
                
#                 # 헤더 작성
#                 header = rows[0].keys()
#                 writer.writerow(header)
                
#                 # 데이터 작성
#                 for row in rows:
#                     writer.writerow(row.values())
            
#             print("CSV 파일로 저장되었습니다: api_result.csv")
#     except Exception as e:
#         print(f"데이터 처리 중 오류 발생: {e}")
# else:
#     print(f"Error: {response.status_code}")  # 오류 발생 시 상태 코드 출력
#     print(response.text)  # API에서 반환한 에러 메시지 출력


import requests
import csv

# API 요청에 필요한 파라미터 설정
서비스명 = "StatisticSearch"
인증키 = "DA3T67WSL19LH0FK7A0Q"
요청유형 = "json"
언어구분 = "kr"
요청시작건수 = 1
요청종료건수 = 1000
통계표코드 = "131Y010"
주기 = "Q"
검색시작일자 = "2019Q1"
검색종료일자 = "2019Q2"
통계항목코드1 = "1100000"
통계항목코드2 = "C20"

# URL 템플릿 방식
url = f"https://ecos.bok.or.kr/api/{서비스명}/{인증키}/{요청유형}/{언어구분}/{요청시작건수}/{요청종료건수}/{통계표코드}/{주기}/{검색시작일자}/{검색종료일자}/{통계항목코드1}/{통계항목코드2}"

# API 호출
response = requests.get(url)


# # HTTP 요청 성공 여부 확인
# if response.status_code == 200:
#     # JSON 데이터로 변환
#     data = response.json()
    
#     # 데이터 구조 확인 및 CSV 저장
#     if "StatisticSearch" in data:
#         rows = data["StatisticSearch"]
        
#         if rows:  # 데이터가 존재할 경우
#             with open("api_result.csv", mode="w", newline="", encoding="utf-8") as file:
#                 writer = csv.writer(file)
                
#                 # 헤더 작성
#                 header = rows[0].keys()
#                 writer.writerow(header)
                
#                 # 데이터 작성
#                 for row in rows:
#                     writer.writerow(row.values())
            
#             print("CSV 파일로 저장되었습니다: api_result.csv")
#         else:
#             print("데이터가 없습니다.")
#     else:
#         print("JSON 응답에서 'StatisticSearch' 키를 찾을 수 없습니다.")
# else:
#     print(f"HTTP 요청 실패: {response.status_code}")
#     print("응답 내용:", response.text)

import csv
import requests

# HTTP 요청 성공 여부 확인
if response.status_code == 200:
    # JSON 데이터로 변환
    data = response.json()
    print("API 응답 데이터:", data)  # 응답 데이터 출력

    # 데이터 구조 확인 및 CSV 저장
    if "StatisticSearch" in data:
        rows = data["StatisticSearch"]
        print("StatisticSearch 데이터:", rows)  # StatisticSearch 키의 값 출력

        # rows가 딕셔너리일 경우 처리
        if isinstance(rows, dict):
            print("rows는 딕셔너리입니다.")

            # 딕셔너리를 리스트로 변환
            rows_list = [rows]  # 딕셔너리를 리스트로 감싸기

            with open("api_result.csv", mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                # 헤더 작성
                header = rows.keys()
                writer.writerow(header)

                # 데이터 작성
                writer.writerow(rows.values())

            print("CSV 파일로 저장되었습니다: api_result.csv")
        else:
            print("rows가 딕셔너리가 아닙니다.")
    else:
        print("JSON 응답에서 'StatisticSearch' 키를 찾을 수 없습니다.")
else:
    print(f"HTTP 요청 실패: {response.status_code}")
    print("응답 내용:", response.text)
