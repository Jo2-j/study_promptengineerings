# import requests
# import csv
# from datetime import datetime, timedelta

# # 요청 URL
# base_url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON"

# # 인증키 (발급받은 인증키를 입력하세요)
# authkey = "P3WaE8loX2Z2Z2IX6Nw4dNNbmH5PVCkz"

# # CSV 파일 저장 경로
# output_file = "exchange_rates_filtered_2017_2021.csv"

# # CSV 파일 헤더 작성
# with open(output_file, mode="w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["날짜", "통화명", "매매가격"])

# # 날짜 범위 설정 (2017-01-01 ~ 2021-12-31)
# start_date = datetime(2017, 2, 10)
# end_date = datetime(2017, 2, 27)
# current_date = start_date

# # 날짜별로 API 요청
# while current_date <= end_date:
#     # 요청 변수 설정
#     params = {
#         "authkey": authkey,
#         "searchdate": current_date.strftime("%Y%m%d"),  # 날짜 형식: YYYYMMDD
#         "data": "AP01"  # API 타입
#     }

#     # API 요청
#     response = requests.get(base_url, params=params, verify=False)

#     # 응답 데이터 처리
#     if response.status_code == 200:
#         data = response.json()
#         with open(output_file, mode="a", newline="", encoding="utf-8") as file:
#             writer = csv.writer(file)
#             for item in data:
#                 writer.writerow([
#                     current_date.strftime("%Y-%m-%d"),  # 날짜
#                     item.get("cur_nm"),                # 통화명
#                     item.get("kftc_deal_bas_r")        # 매매가격
#                 ])
#     else:
#         print(f"요청 실패: {current_date.strftime('%Y-%m-%d')}, 상태 코드: {response.status_code}")

#     # 다음 날짜로 이동
#     current_date += timedelta(days=1)

# print(f"데이터가 {output_file} 파일에 저장되었습니다.")


import requests
import csv
from datetime import datetime, timedelta

# 요청 URL
base_url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON"

# 인증키 (발급받은 인증키를 입력하세요)
authkey = "P3WaE8loX2Z2Z2IX6Nw4dNNbmH5PVCkz"

# CSV 파일 저장 경로
output_file = "exchange_rates_filtered_2017_2021.csv"

# CSV 파일 헤더 작성
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["날짜", "통화명", "매매가격"])

# 날짜 범위 설정 (2017-01-01 ~ 2021-12-31)
start_date = datetime(2017, 2, 10)
end_date = datetime(2021, 2, 11)
current_date = start_date

# 필터링할 통화명
target_currencies = ["위안화", "미국 달러", "일본 옌"]

# 날짜별로 API 요청
while current_date <= end_date:
    # 요청 변수 설정
    params = {
        "authkey": authkey,
        "searchdate": current_date.strftime("%Y%m%d"),  # 날짜 형식: YYYYMMDD
        "data": "AP01"  # API 타입
    }

    # API 요청
    response = requests.get(base_url, params=params, verify=False)

    # 응답 데이터 처리
    if response.status_code == 200:
        data = response.json()
        with open(output_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for item in data:
                # 통화명 필터링
                if item.get("cur_nm") in target_currencies:
                    writer.writerow([
                        current_date.strftime("%Y-%m-%d"),  # 날짜
                        item.get("cur_nm"),                # 통화명
                        item.get("kftc_deal_bas_r")        # 매매가격
                    ])
    else:
        print(f"요청 실패: {current_date.strftime('%Y-%m-%d')}, 상태 코드: {response.status_code}")

    # 다음 날짜로 이동
    current_date += timedelta(days=1)

print(f"데이터가 {output_file} 파일에 저장되었습니다.")
