# # # import requests
# # # import pandas as pd
# # # from bs4 import BeautifulSoup
# # # # API 엔드포인트와 매개변수 설정

# # # headers = [
# # # {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36' },

# # # ]

# # # tickers_cik = requests.get("https://www.sec.gov/files/company_tickers.json", headers=headers[0])
# # # df_ticker =     pd.json_normalize(pd.json_normalize(tickers_cik.json(),max_level=0).values[0])
# # # df_ticker["cik_str"] = df_ticker["cik_str"].astype(str).str.zfill(10)
# # # # df_ticker.set_index("ticker",inplace=True)
# # # df_ticker

# # # tic = 'AAPL'
# # # cik = df_ticker[df_ticker['ticker']==tic]['cik_str'].iloc[0]
# # # # API에 요청 보내기
# # # url = f"https://data.sec.gov/submissions/CIK{cik}.json"
# # # response = requests.get(url, headers=headers[0])
# # # # 응답 데이터 확인
# # # data = response.json()
# # # df_filing = pd.DataFrame(data['filings']['recent'])
# # # df_filing

# # # 이제 마지막입니다!! 공시 리스트 중에서 보고싶은 공시를 선정하여

# # # 해당 URL로 접근하면 됩니다!!

# # # 예시로는 배당정보가 포함된 가장 최근의 10-K의 보고서를 분석해보아요!!

# # # tic = 'AAPL'
# # # cik = df_ticker[df_ticker['ticker']==tic]['cik_str'].iloc[0]
# # # # API에 요청 보내기
# # # url = f"https://data.sec.gov/submissions/CIK{cik}.json"
# # # response = requests.get(url, headers=headers[0])
# # # # 응답 데이터 확인
# # # data = response.json()
# # # df_filing = pd.DataFrame(data['filings']['recent'])
# # # df_10K = df_filing[df_filing['form'] == '10-K'].reset_index(drop=True)
# # # df_10K

# # # recent_10K_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{df_10K['accessionNumber'].iloc[i].replace('-','')}/{df_10K['primaryDocument'].iloc[i]}"

# # # i = 0
# # # headers = [
# # # {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36' },

# # # ]
# # # recent_10K_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{df_10K['accessionNumber'].iloc[i].replace('-','')}/{df_10K['primaryDocument'].iloc[i]}"
# # # print(recent_10K_url)
# # # res =requests.get(recent_10K_url,  headers=headers[0]) ## AAPL
# # # res

# # import requests
# # import pandas as pd
# # import time

# # def get_edgar_filings(ticker):
# #     """
# #     주식 티커를 입력받아 SEC EDGAR 공시 정보를 가져오는 함수
    
# #     Parameters:
# #     ticker (str): 주식 티커 심볼 (예: 'AAPL')
    
# #     Returns:
# #     tuple: (모든 공시 DataFrame, 10-K 공시 DataFrame, 최근 10-K URL)
# #     """
    
# #     # HTTP 헤더 설정
# #     headers = {
# #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
# #     }
    
# #     try:
# #         # 1. CIK 번호 가져오기
# #         tickers_response = requests.get("https://www.sec.gov/files/company_tickers.json", headers=headers)
# #         if tickers_response.status_code != 200:
# #             raise Exception("티커 정보를 가져오는데 실패했습니다.")
            
# #         df_ticker = pd.json_normalize(pd.json_normalize(tickers_response.json(), max_level=0).values[0])
# #         df_ticker["cik_str"] = df_ticker["cik_str"].astype(str).str.zfill(10)
        
# #         # 입력된 티커에 해당하는 CIK 찾기
# #         if ticker not in df_ticker['ticker'].values:
# #             raise Exception(f"티커 '{ticker}'를 찾을 수 없습니다.")
            
# #         cik = df_ticker[df_ticker['ticker'] == ticker]['cik_str'].iloc[0]
        
# #         # 2. 공시 정보 가져오기
# #         time.sleep(0.1)  # SEC API 속도 제한 준수
# #         filings_url = f"https://data.sec.gov/submissions/CIK{cik}.json"
# #         filings_response = requests.get(filings_url, headers=headers)
        
# #         if filings_response.status_code != 200:
# #             raise Exception("공시 정보를 가져오는데 실패했습니다.")
            
# #         data = filings_response.json()
# #         df_filing = pd.DataFrame(data['filings']['recent'])
        
# #         # 3. 10-K 보고서만 필터링
# #         df_10K = df_filing[df_filing['form'] == '10-K'].reset_index(drop=True)
        
# #         # 4. 최근 10-K 보고서 URL 생성
# #         if len(df_10K) > 0:
# #             recent_10K_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{df_10K['accessionNumber'].iloc[0].replace('-','')}/{df_10K['primaryDocument'].iloc[0]}"
# #         else:
# #             recent_10K_url = None
            
# #         return df_filing, df_10K, recent_10K_url
    
# #     except Exception as e:
# #         print(f"에러 발생: {str(e)}")
# #         return None, None, None

# # def get_filing_content(url, headers):
# #     """
# #     공시 문서의 내용을 가져오는 함수
    
# #     Parameters:
# #     url (str): 공시 문서 URL
# #     headers (dict): HTTP 요청 헤더
    
# #     Returns:
# #     str: 공시 문서 내용
# #     """
# #     try:
# #         response = requests.get(url, headers=headers)
# #         if response.status_code == 200:
# #             return response.text
# #         else:
# #             raise Exception("문서를 가져오는데 실패했습니다.")
# #     except Exception as e:
# #         print(f"에러 발생: {str(e)}")
# #         return None

# # # 사용 예시
# # def main():
# #     ticker = "AAPL"  # 분석하고 싶은 티커 입력
    
# #     # 공시 정보 가져오기
# #     df_filing, df_10K, recent_10K_url = get_edgar_filings(ticker)
    
# #     if df_filing is not None:
# #         print(f"\n{ticker}의 전체 공시 목록:")
# #         print(df_filing.head())
        
# #         if len(df_10K) > 0:
# #             print(f"\n{ticker}의 10-K 보고서 목록:")
# #             print(df_10K.head())
            
# #             if recent_10K_url:
# #                 print(f"\n가장 최근 10-K 보고서 URL:")
# #                 print(recent_10K_url)
                
# #                 # 10-K 문서 내용 가져오기
# #                 headers = {
# #                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
# #                 }
# #                 content = get_filing_content(recent_10K_url, headers)
# #                 if content:
# #                     print("\n10-K 문서 내용 일부:")
# #                     print(content[:500] + "...")  # 처음 500자만 출력

# # if __name__ == "__main__":
# #     main()


# import requests
# import pandas as pd
# import time

# def get_edgar_filings(ticker, email):
#     """
#     주식 티커를 입력받아 SEC EDGAR 공시 정보를 가져오는 함수
    
#     Parameters:
#     ticker (str): 주식 티커 심볼 (예: 'AAPL')
#     email (str): SEC에 제공할 이메일 주소
    
#     Returns:
#     tuple: (모든 공시 DataFrame, 10-K 공시 DataFrame, 최근 10-K URL)
#     """
    
#     # SEC 요구사항에 맞는 헤더 설정
#     headers = {
#         'User-Agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 {email}',
#         'Accept': 'application/json',
#         'Host': 'data.sec.gov'
#     }
    
#     try:
#         # 1. CIK 번호 가져오기
#         tickers_response = requests.get(
#             "https://www.sec.gov/files/company_tickers.json",
#             headers=headers
#         )
#         if tickers_response.status_code != 200:
#             raise Exception(f"티커 정보를 가져오는데 실패했습니다. Status code: {tickers_response.status_code}")
            
#         df_ticker = pd.json_normalize(pd.json_normalize(tickers_response.json(), max_level=0).values[0])
#         df_ticker["cik_str"] = df_ticker["cik_str"].astype(str).str.zfill(10)
        
#         # 입력된 티커에 해당하는 CIK 찾기
#         if ticker not in df_ticker['ticker'].values:
#             raise Exception(f"티커 '{ticker}'를 찾을 수 없습니다.")
            
#         cik = df_ticker[df_ticker['ticker'] == ticker]['cik_str'].iloc[0]
        
#         # 2. 공시 정보 가져오기
#         time.sleep(0.1)  # SEC API 속도 제한 준수
#         filings_url = f"https://data.sec.gov/submissions/CIK{cik}.json"
#         filings_response = requests.get(filings_url, headers=headers)
        
#         if filings_response.status_code != 200:
#             raise Exception(f"공시 정보를 가져오는데 실패했습니다. Status code: {filings_response.status_code}")
            
#         data = filings_response.json()
#         df_filing = pd.DataFrame(data['filings']['recent'])
        
#         # 3. 10-K 보고서만 필터링
#         df_10K = df_filing[df_filing['form'] == '10-K'].reset_index(drop=True)
        
#         # 4. 최근 10-K 보고서 URL 생성
#         if len(df_10K) > 0:
#             recent_10K_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{df_10K['accessionNumber'].iloc[0].replace('-','')}/{df_10K['primaryDocument'].iloc[0]}"
#         else:
#             recent_10K_url = None
            
#         return df_filing, df_10K, recent_10K_url
    
#     except Exception as e:
#         print(f"에러 발생: {str(e)}")
#         return None, None, None

# def get_filing_content(url, email):
#     """
#     공시 문서의 내용을 가져오는 함수
    
#     Parameters:
#     url (str): 공시 문서 URL
#     email (str): SEC에 제공할 이메일 주소
    
#     Returns:
#     str: 공시 문서 내용
#     """
#     headers = {
#         'User-Agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 {email}',
#         'Accept': 'application/json',
#         'Host': 'www.sec.gov'
#     }
    
#     try:
#         response = requests.get(url, headers=headers)
#         if response.status_code == 200:
#             return response.text
#         else:
#             raise Exception(f"문서를 가져오는데 실패했습니다. Status code: {response.status_code}")
#     except Exception as e:
#         print(f"에러 발생: {str(e)}")
#         return None

# # 사용 예시
# def main():
#     ticker = "AAPL"  # 분석하고 싶은 티커 입력
#     email = "w01205250623@gmail.com"  # 여기에 실제 이메일 주소를 입력하세요
    
#     # 공시 정보 가져오기
#     df_filing, df_10K, recent_10K_url = get_edgar_filings(ticker, email)
    
#     if df_filing is not None:
#         print(f"\n{ticker}의 전체 공시 목록:")
#         print(df_filing.head())
        
#         if len(df_10K) > 0:
#             print(f"\n{ticker}의 10-K 보고서 목록:")
#             print(df_10K.head())
            
#             if recent_10K_url:
#                 print(f"\n가장 최근 10-K 보고서 URL:")
#                 print(recent_10K_url)
                
#                 # 10-K 문서 내용 가져오기
#                 content = get_filing_content(recent_10K_url, email)
#                 if content:
#                     print("\n10-K 문서 내용 일부:")
#                     print(content[:500] + "...")  # 처음 500자만 출력

# if __name__ == "__main__":
#     main()


import requests
import pandas as pd
import time

def get_edgar_filings(ticker, email):
    """
    주식 티커를 입력받아 SEC EDGAR 공시 정보를 가져오는 함수
    
    Parameters:
    ticker (str): 주식 티커 심볼 (예: 'AAPL')
    email (str): SEC에 제공할 이메일 주소
    
    Returns:
    tuple: (모든 공시 DataFrame, 10-K 공시 DataFrame)
    """
    
    headers = {
        'User-Agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 {email}'
    }
    
    try:
        # 1. CIK 번호 가져오기
        tickers_response = requests.get(
            "https://www.sec.gov/files/company_tickers.json",
            headers=headers
        )
        if tickers_response.status_code != 200:
            raise Exception(f"티커 정보를 가져오는데 실패했습니다. Status code: {tickers_response.status_code}")
            
        df_ticker = pd.json_normalize(pd.json_normalize(tickers_response.json(), max_level=0).values[0])
        df_ticker["cik_str"] = df_ticker["cik_str"].astype(str).str.zfill(10)
        
        if ticker not in df_ticker['ticker'].values:
            raise Exception(f"티커 '{ticker}'를 찾을 수 없습니다.")
            
        cik = df_ticker[df_ticker['ticker'] == ticker]['cik_str'].iloc[0]
        
        # 2. 공시 정보 가져오기
        time.sleep(0.1)
        filings_url = f"https://data.sec.gov/submissions/CIK{cik}.json"
        filings_response = requests.get(filings_url, headers=headers)
        
        if filings_response.status_code != 200:
            raise Exception(f"공시 정보를 가져오는데 실패했습니다. Status code: {filings_response.status_code}")
            
        data = filings_response.json()
        df_filing = pd.DataFrame(data['filings']['recent'])
        
        # 3. 10-K 보고서만 필터링
        df_10K = df_filing[df_filing['form'] == '10-K'].reset_index(drop=True)
        
        return df_filing, df_10K
    
    except Exception as e:
        print(f"에러 발생: {str(e)}")
        return None, None

def get_filing_document(ticker, accession_number, primary_doc, email):
    """
    특정 공시 문서를 가져오는 함수
    
    Parameters:
    ticker (str): 티커 심볼
    accession_number (str): 공시 문서 번호
    primary_doc (str): 주요 문서 이름
    email (str): SEC에 제공할 이메일 주소
    
    Returns:
    str: 공시 문서 내용
    """
    headers = {
        'User-Agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 {email}'
    }
    
    try:
        # CIK 가져오기
        tickers_response = requests.get(
            "https://www.sec.gov/files/company_tickers.json",
            headers=headers
        )
        df_ticker = pd.json_normalize(pd.json_normalize(tickers_response.json(), max_level=0).values[0])
        df_ticker["cik_str"] = df_ticker["cik_str"].astype(str).str.zfill(10)
        cik = df_ticker[df_ticker['ticker'] == ticker]['cik_str'].iloc[0]
        
        # URL 생성
        acc_no_clean = accession_number.replace('-', '')
        url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc_no_clean}/{primary_doc}"
        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"문서를 가져오는데 실패했습니다. Status code: {response.status_code}")
    except Exception as e:
        print(f"에러 발생: {str(e)}")
        return None

# 사용 예시
def main():
    ticker = "AAPL"
    email = "w01205250623@gmail.com"  # 여기에 실제 이메일 주소를 입력하세요
    
    # 공시 정보 가져오기
    df_filing, df_10K = get_edgar_filings(ticker, email)
    
    if df_filing is not None and df_10K is not None:
        print(f"\n{ticker}의 전체 공시 목록:")
        print(df_filing.head())
        
        if len(df_10K) > 0:
            print(f"\n{ticker}의 10-K 보고서 목록:")
            print(df_10K[['reportDate', 'form', 'primaryDocument', 'accessionNumber']].head())
            
            # 가장 최근 10-K 문서 가져오기
            latest_10k = df_10K.iloc[0]
            content = get_filing_document(
                ticker,
                latest_10k['accessionNumber'],
                latest_10k['primaryDocument'],
                email
            )
            
            if content:
                print("\n10-K 문서 내용 일부:")
                print(content[:500] + "...")

if __name__ == "__main__":
    main()
