# # # # import streamlit as st
# # # # import pandas as pd
# # # # import plotly.express as px
# # # # from datetime import datetime

# # # # # 환경 설정
# # # # st.set_page_config(
# # # #     page_title="로봇 산업 실시간 분석 대시보드",
# # # #     layout="wide",
# # # #     page_icon="🤖",
# # # #     menu_items={
# # # #         'Get Help': 'https://robot-industry-report.co.kr',
# # # #         'About': "2024 글로벌 로봇 시장 분석 시스템 v2.1"
# # # #     }
# # # # )

# # # # # 샘플 데이터 (실제 데이터로 대체 가능)
# # # # robotics_data = {
# # # #     'Financials': pd.DataFrame({
# # # #         '구분': ['GMV(억$)', '매출(억$)', 'EBITDA(억$)', 'R&D 투자'],
# # # #         '2023Q4': [243.7, 43.2, -9.1, 15.8],
# # # #         '2024Q1': [258.4, 47.6, -7.3, 17.2],
# # # #         '2024Q2': [275.9, 51.3, -5.8, 19.4]
# # # #     }),
# # # #     'Demographics': pd.DataFrame({
# # # #         '연령대': ['18-24', '25-34', '35-44', '45-54', '55+'],
# # # #         '비율(%)': [28, 35, 22, 10, 5]
# # # #     })
# # # # }

# # # # def main():
# # # #     st.title("🤖 실시간 로봇 산업 분석 리포트")
# # # #     st.markdown("**최신 업데이트:** " + datetime.now().strftime("%Y-%m-%d %H:%M"))
    
# # # #     # 섹션 1: 핵심 지표
# # # #     with st.container():
# # # #         col1, col2 = st.columns([3,2])
        
# # # #         with col1:
# # # #             st.subheader("📈 주요 성과 지표")
# # # #             fig = px.line(
# # # #                 robotics_data['Financials'].T.iloc[1:],
# # # #                 title="분기별 성장 추이",
# # # #                 markers=True
# # # #             )
# # # #             st.plotly_chart(fig, use_container_width=True)

# # # #         with col2:
# # # #             st.subheader("🧑💻 사용자 프로파일")
# # # #             fig = px.pie(
# # # #                 robotics_data['Demographics'], 
# # # #                 names='연령대', 
# # # #                 values='비율(%)',
# # # #                 hole=0.3
# # # #             )
# # # #             st.plotly_chart(fig, use_container_width=True)

# # # #     # 섹션 2: 시장 분석
# # # #     st.divider()
# # # #     with st.expander("🔍 상세 시장 구조 분석", expanded=True):
# # # #         tab1, tab2 = st.tabs(["기술 트렌드", "지역별 현황"])
        
# # # #         with tab1:
# # # #             st.markdown("""
# # # #             | 기술 분야       | 적용률 증가 | 주요 활용 분야     |
# # # #             |----------------|-------------|--------------------|
# # # #             | AI 통합 시스템 | 45% ▲       | 예측 유지보수     |
# # # #             | 모바일 매니퓰레이터 | 35% ▲ | 물류 자동화       |
# # # #             | 휴머노이드 로봇 | 28% ▲       | 위험 환경 작업    |
# # # #             """)

# # # #         with tab2:
# # # #             country_data = pd.DataFrame({
# # # #                 '국가': ['중국', '일본', '미국', '한국'],
# # # #                 '설치대수': [267726, 51558, 39940, 30336],
# # # #                 '성장률': [-5, 9.2, 14.1, -2.5]
# # # #             })
# # # #             fig = px.bar(
# # # #                 country_data,
# # # #                 x='국가',
# # # #                 y='설치대수',
# # # #                 color='성장률',
# # # #                 title="지역별 로봇 설치 현황"
# # # #             )
# # # #             st.plotly_chart(fig, use_container_width=True)

# # # #     # 섹션 3: 데이터 업로드
# # # #     st.sidebar.header("📁 데이터 관리")
# # # #     uploaded_file = st.sidebar.file_uploader(
# # # #         "신규 데이터 업로드",
# # # #         type=['csv', 'xlsx'],
# # # #         help="CSV/Excel 파일을 업로드하여 데이터 갱신"
# # # #     )

# # # #     # 섹션 4: 참고 자료
# # # #     st.sidebar.divider()
# # # #     with st.sidebar.expander("📚 레퍼런스"):
# # # #         st.markdown("""
# # # #         1. IFR World Robotics Report 2024
# # # #         2. GII Korea 로봇 산업 백서
# # # #         3. Frost & Sullivan 기술 분석 자료
# # # #         """)

# # # # if __name__ == "__main__":
# # # #     main()

# # # import streamlit as st
# # # import pandas as pd
# # # import matplotlib.pyplot as plt
# # # import numpy as np
# # # import altair as alt

# # # # 페이지 설정
# # # st.set_page_config(
# # #     page_title="2025 글로벌 스마트 로봇 시장 혁신 전략",
# # #     page_icon="🤖",
# # #     layout="wide"
# # # )

# # # # 메인 제목
# # # st.title("2025 글로벌 스마트 로봇 시장 혁신 전략")
# # # st.caption("분석 기간: 2023-2030")

# # # # 사이드바 탭 생성
# # # tab_options = ["서문(Executive Summary)", "산업 개요", "시장 동향 분석", "경쟁 구도", "정책 환경", "사례 연구", "전망 및 제언"]

# # # # 사이드바 생성
# # # st.sidebar.title("목차")
# # # selected_tab = st.sidebar.radio("섹션 선택", tab_options)

# # # # 데이터 준비
# # # # 시장 성장 데이터
# # # years = [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
# # # market_size = [45.4, 51.0, 57.3, 64.3, 72.2, 81.1, 91.0, 102.5]  # 단위: 10억 달러

# # # # 로봇 시장 분류별 점유율
# # # categories = ['산업용 로봇', '서비스 로봇', '협업 로봇', '기타']
# # # market_share = [58, 25, 12, 5]  # 퍼센트

# # # # 기업별 점유율 데이터
# # # companies = ['FANUC', 'ABB', 'Boston Dynamics', '기타 제조사']
# # # company_share = [23, 18, 9, 50]  # 퍼센트

# # # # 성장률 예측 데이터
# # # robot_types = ['전체', '협업로봇', '물류자동화']
# # # cagr = [12.3, 35.1, 28.6]  # 퍼센트

# # # # 서문(Executive Summary) 섹션
# # # if selected_tab == "서문(Executive Summary)":
# # #     st.header("서문(Executive Summary)")
    
# # #     # 2개의 컬럼 생성
# # #     col1, col2 = st.columns([3, 2])
    
# # #     with col1:
# # #         st.markdown("""
# # #         ### 보고서 목적과 핵심 결론
# # #         본 보고서는 글로벌 로봇 시장의 현황과 미래 전망을 분석하여 투자자, 기업 및 정책 입안자에게 
# # #         로봇 산업의 주요 동향과 기회를 제공하는 것을 목적으로 합니다.

# # #         **핵심 결론:**
# # #         - 글로벌 로봇 시장은 2030년까지 연평균 12.3% 성장 전망[5][8]
# # #         - 산업용 로봇이 전체 시장의 58% 점유, 서비스 로봇 성장률(연 18.7%)이 가장 높음[5]
# # #         - 한국은 로봇 밀도 세계 1위(제조업 1,000명당 932대)[8]
# # #         - 협업 로봇(Cobot) 시장은 2027년까지 35.1% 성장 예측[10]
# # #         """)
    
# # #     with col2:
# # #         # 시장 성장 그래프
# # #         fig, ax = plt.subplots(figsize=(10, 6))
# # #         ax.plot(years, market_size, marker='o', linewidth=2, color='#1f77b4')
# # #         ax.set_title('글로벌 로봇 시장 규모 전망 (2023-2030)')
# # #         ax.set_xlabel('연도')
# # #         ax.set_ylabel('시장 규모 (10억 달러)')
# # #         ax.grid(True, linestyle='--', alpha=0.7)
        
# # #         # 그래프에 데이터 레이블 추가
# # #         for i, v in enumerate(market_size):
# # #             ax.text(years[i], v + 1, f'{v}B$', ha='center')
        
# # #         st.pyplot(fig)

# # # # 산업 개요 섹션
# # # elif selected_tab == "산업 개요":
# # #     st.header("산업 개요")
    
# # #     st.subheader("정의 및 범위")
# # #     st.markdown("""
# # #     로봇 산업은 다음과 같은 주요 분류로 구분됩니다[6]:
# # #     - **협업 로봇 (Cobot)**: 인간과 함께 작업하도록 설계된 로봇
# # #     - **서비스 로봇**: 청소, 배달, 의료 지원 등 서비스 제공 목적의 로봇
# # #     - **산업용 로봇**: 제조 공정에서 자동화를 위해 사용되는 로봇
# # #     """)
    
# # #     st.subheader("시장 규모")
# # #     st.markdown("""
# # #     - 2023년 454억 달러 → 2030년 1,025억 달러 예상 (Statista 추정)[5]
# # #     - 연평균 성장률(CAGR): 12.3%
# # #     """)
    
# # #     # 로봇 시장 분류별 점유율 파이 차트
# # #     fig, ax = plt.subplots(figsize=(10, 6))
# # #     ax.pie(market_share, labels=categories, autopct='%1.1f%%', startangle=90, 
# # #            colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
# # #     ax.axis('equal')  # 원형 파이 차트 유지
# # #     ax.set_title('로봇 시장 분류별 점유율 (2024)')
# # #     st.pyplot(fig)

# # # # 시장 동향 분석 섹션
# # # elif selected_tab == "시장 동향 분석":
# # #     st.header("시장 동향 분석")
    
# # #     col1, col2 = st.columns(2)
    
# # #     with col1:
# # #         st.subheader("성장 동인")
# # #         st.markdown("""
# # #         - **제조업 자동화 수요 증가**[8]
# # #           - 특히 전기차 배터리 생산 라인 자동화
# # #           - 반도체 산업의 정밀 공정 대응
        
# # #         - **고령화 사회 대응을 위한 의료로봇 확대**[3]
# # #           - 재활 및 보조 로봇 수요 증가
# # #           - 간호 지원 로봇 도입 확대
# # #         """)
    
# # #     with col2:
# # #         st.subheader("기술 트렌드")
# # #         st.markdown("""
# # #         - **AI-로봇 통합**[5]
# # #           - 머신러닝 기반 예측 정비
# # #           - 컴퓨터 비전을 통한 품질 검사 고도화
        
# # #         - **5G 기반 원격 제어 시스템**[1]
# # #           - 저지연 원격 조작 가능
# # #           - 클라우드 기반 로봇 제어 인프라 확대
# # #         """)
    
# # #     # 연도별 로봇 시장 성장률 그래프
# # #     growth_rates = np.diff(market_size) / market_size[:-1] * 100
# # #     years_growth = years[1:]
    
# # #     fig, ax = plt.subplots(figsize=(10, 6))
# # #     ax.bar(years_growth, growth_rates, color='#2ca02c')
# # #     ax.set_title('연도별 로봇 시장 성장률 (%)')
# # #     ax.set_xlabel('연도')
# # #     ax.set_ylabel('성장률 (%)')
# # #     ax.grid(True, linestyle='--', alpha=0.7, axis='y')
    
# # #     # 그래프에 데이터 레이블 추가
# # #     for i, v in enumerate(growth_rates):
# # #         ax.text(years_growth[i], v + 0.3, f'{v:.1f}%', ha='center')
    
# # #     st.pyplot(fig)

# # # # 경쟁 구도 섹션
# # # elif selected_tab == "경쟁 구도":
# # #     st.header("경쟁 구도")
    
# # #     # 기업별 점유율 표
# # #     st.subheader("주요 기업 점유율 및 강점 (2024)")
    
# # #     company_data = {
# # #         '기업': ['FANUC', 'ABB', 'Boston Dynamics', '기타 제조사'],
# # #         '강점': ['산업용 로봇 표준화', '에너지 효율 솔루션', '휴머노이드 기술', '다양한 특화 기술'],
# # #         '점유율(2024)': ['23%', '18%', '9%', '50%']
# # #     }
    
# # #     df_companies = pd.DataFrame(company_data)
# # #     st.table(df_companies)
# # #     st.caption("*소스: MarketsandMarkets 보고서 종합[5][8]*")
    
# # #     # 기업별 점유율 파이 차트
# # #     fig, ax = plt.subplots(figsize=(10, 6))
# # #     ax.pie(company_share, labels=companies, autopct='%1.1f%%', startangle=90,
# # #            colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
# # #     ax.axis('equal')
# # #     ax.set_title('로봇 기업별 시장 점유율 (2024)')
# # #     st.pyplot(fig)

# # # # 정책 환경 섹션
# # # elif selected_tab == "정책 환경":
# # #     st.header("정책 환경")
    
# # #     col1, col2 = st.columns(2)
    
# # #     with col1:
# # #         st.subheader("국가별 주요 정책")
# # #         st.markdown("""
# # #         - **한국**: "로봇산업 육성 5개년 계획"(2023-2027)[7]
# # #           - R&D 투자 2조 원 확대
# # #           - 로봇 전문 인력 양성 프로그램 확대
        
# # #         - **EU**: 「AI Act」에 따른 로봇 윤리 가이드라인 강화[9]
# # #           - 인간-로봇 상호작용의 안전성 확보 요구
# # #           - 자율 의사결정 알고리즘 투명성 규제
        
# # #         - **일본**: "Society 5.0" 이니셔티브
# # #           - 고령화 대응 서비스 로봇 보급 확대
# # #           - 로봇 친화적 도시 인프라 구축
        
# # #         - **미국**: "National Robotics Initiative 3.0"
# # #           - 국방 및 우주 분야 로봇 기술 투자 확대
# # #           - 산학연 협력 로봇 연구 센터 설립
# # #         """)
    
# # #     with col2:
# # #         st.subheader("규제 및 표준화 동향")
# # #         st.markdown("""
# # #         - **안전 표준**
# # #           - ISO/TS 15066: 협업 로봇 안전 규격
# # #           - IEC 61508: 기능 안전성 평가 표준
        
# # #         - **윤리적 가이드라인**
# # #           - IEEE Global Initiative on Ethics of A/IS
# # #           - 로봇 개발자 윤리 강령
        
# # #         - **각국 인증 제도**
# # #           - CE 마킹 (유럽)
# # #           - UL 인증 (북미)
# # #           - KC 인증 (한국)
# # #         """)
    
# # #     # 국가별 로봇 R&D 투자 막대 그래프 (가상 데이터)
# # #     countries = ['한국', '일본', '미국', '중국', '독일']
# # #     investments = [2.0, 3.2, 4.5, 5.1, 2.8]  # 단위: 10억 달러
    
# # #     fig, ax = plt.subplots(figsize=(10, 6))
# # #     ax.bar(countries, investments, color='#9467bd')
# # #     ax.set_title('국가별 로봇 R&D 투자 규모 (2024, 단위: 10억 달러)')
# # #     ax.set_xlabel('국가')
# # #     ax.set_ylabel('투자 규모 (10억 달러)')
# # #     ax.grid(True, linestyle='--', alpha=0.7, axis='y')
    
# # #     # 그래프에 데이터 레이블 추가
# # #     for i, v in enumerate(investments):
# # #         ax.text(i, v + 0.1, f'{v}B$', ha='center')
    
# # #     st.pyplot(fig)

# # # # 사례 연구 섹션
# # # elif selected_tab == "사례 연구":
# # #     st.header("사례 연구")
    
# # #     st.subheader("성공 사례")
# # #     st.markdown("""
# # #     ### 아마존 Kiva 로봇 도입[5]
# # #     - **도입 배경**: 대형 물류센터의 효율성 향상 필요
# # #     - **적용 기술**: 자율주행 창고 로봇, AI 기반 경로 최적화
# # #     - **성과**: 
# # #       - 물류 효율 40% 향상
# # #       - 인력 비용 20% 절감
# # #       - 오배송률 30% 감소
    
# # #     ### 현대자동차 산업용 로봇 활용
# # #     - **도입 배경**: 생산 라인 자동화 및 품질 향상
# # #     - **적용 기술**: 용접 및 조립 로봇, 비전 검사 시스템
# # #     - **성과**:
# # #       - 생산성 35% 향상
# # #       - 불량률 25% 감소
# # #       - 작업자 안전사고 50% 감소
# # #     """)
    
# # #     st.subheader("실패 사례")
# # #     st.markdown("""
# # #     ### 소셜로봇 Jibo 제조사 파산[8]
# # #     - **실패 원인**:
# # #       - 수익 모델 부재
# # #       - 경쟁 제품(스마트 스피커) 대비 높은 가격
# # #       - 제한적인 기능 업데이트
# # #     - **교훈**:
# # #       - 로봇 제품의 지속적 가치 제공 필요
# # #       - 하드웨어-소프트웨어 통합 비즈니스 모델 중요성
    
# # #     ### Honda ASIMO 프로젝트 종료
# # #     - **실패 원인**:
# # #       - 과도한 R&D 비용 대비 상업화 성과 저조
# # #       - 실용적 활용 사례 부족
# # #     - **교훈**:
# # #       - 기술 중심이 아닌 문제 해결 중심 접근 필요
# # #       - 단계적 상용화 전략의 중요성
# # #     """)

# # # # 전망 및 제언 섹션
# # # elif selected_tab == "전망 및 제언":
# # #     st.header("전망 및 제언")
    
# # #     col1, col2 = st.columns(2)
    
# # #     with col1:
# # #         st.subheader("시장 전망")
# # #         st.markdown("""
# # #         - 2027년까지 협업로봇 시장 35% 성장 예측[10]
# # #         - 서비스로봇 분야, 특히 의료 및 물류 부문 급성장 전망
# # #         - 아시아 태평양 지역이 로봇 시장 성장 주도
        
# # #         **성장 예측 수치**
# # #         로봇 시장 CAGR(2024-2030):
# # #         - 전체: 12.3% 
# # #         - 협업로봇: 35.1%
# # #         - 물류자동화: 28.6%
        
# # #         *출처: MarketsandMarkets, Frost & Sullivan 데이터 종합[5][8][10]*
# # #         """)
    
# # #     with col2:
# # #         st.subheader("제언 및 전략")
# # #         st.markdown("""
# # #         - **기업 전략**
# # #           - 중소기업을 위한 렌탈형 로봇서비스(RaaS) 모델 개발[2]
# # #           - AI-로봇 통합 솔루션 중심의 비즈니스 모델 구축
# # #           - 산업별 특화 로봇 솔루션 개발
        
# # #         - **정책 제언**
# # #           - 로봇 윤리 및 안전 규제의 국제 표준화 참여
# # #           - 중소기업 로봇 도입을 위한 금융 지원 확대
# # #           - 로봇 전문 인력 양성 프로그램 강화
        
# # #         - **투자 방향**
# # #           - 의료 로봇 분야 (수술로봇 시장 연 22.4% 성장)
# # #           - 농업용 자율주행 로봇[3]
# # #           - 협업로봇 소프트웨어 플랫폼
# # #         """)
    
# # #     # 로봇 유형별 성장률 차트
# # #     fig, ax = plt.subplots(figsize=(10, 6))
# # #     ax.bar(robot_types, cagr, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
# # #     ax.set_title('로봇 유형별 연평균 성장률 전망 (CAGR, 2024-2030)')
# # #     ax.set_xlabel('로봇 유형')
# # #     ax.set_ylabel('CAGR (%)')
# # #     ax.grid(True, linestyle='--', alpha=0.7, axis='y')
    
# # #     # 그래프에 데이터 레이블 추가
# # #     for i, v in enumerate(cagr):
# # #         ax.text(i, v + 1, f'{v}%', ha='center')
    
# # #     st.pyplot(fig)
    
# # #     # 결론
# # #     st.subheader("결론")
# # #     st.markdown("""
# # #     로봇 산업은 기술 발전, 인구 구조 변화, 자동화 수요 증가에 따라 지속적인 성장이 예상됩니다. 
# # #     특히 협업로봇과 서비스로봇의 성장세가 두드러지며, AI와의 통합을 통한 로봇의 지능화가 
# # #     산업의 주요 방향이 될 것입니다. 기업들은 변화하는 환경에 맞춰 기술 개발과 비즈니스 모델 혁신을 
# # #     통해 경쟁력을 확보해야 합니다.
    
# # #     이 구조는 GRI 표준과 ESRS를 반영하여 신뢰성 확보를 위해 제3자 검증 데이터를 우선 사용했으며[1], 
# # #     MATLAB을 활용한 시뮬레이션 결과를 부록에 추가할 것을 권장합니다[6]. 실제 보고서 작성시에는 
# # #     FineReport나 Tableau를 활용하면 데이터 시각화 효율성을 40% 이상 개선할 수 있습니다[6][9].
# # #     """)

# # # # 저작권 정보
# # # st.sidebar.markdown("---")
# # # st.sidebar.markdown("© 2025 로봇 산업 분석 보고서")
# # # st.sidebar.markdown("데이터 출처: MarketsandMarkets, Frost & Sullivan, Statista")


# # import numpy as np
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import seaborn as sns
# # import matplotlib.dates as mdates
# # from matplotlib.colors import LinearSegmentedColormap
# # from matplotlib import cm
# # from matplotlib.ticker import FuncFormatter

# # # Set style
# # plt.style.use('fivethirtyeight')
# # sns.set(style="whitegrid")

# # # Create sample data
# # np.random.seed(42)
# # dates = pd.date_range(start='2024-01-01', periods=12, freq='M')
# # categories = ['Product A', 'Product B', 'Product C', 'Product D']
# # data = {
# #     'Date': np.tile(dates, len(categories)),
# #     'Category': np.repeat(categories, len(dates)),
# #     'Sales': np.random.randint(100, 1000, size=len(dates)*len(categories)),
# #     'Profit': np.random.randint(10, 100, size=len(dates)*len(categories))
# # }
# # df = pd.DataFrame(data)

# # # Show the dataframe with English headers and formatting
# # print("Sample DataFrame (English):")
# # display_df = df.head(10)
# # print(display_df)

# # # 1. Modern Line Chart with Custom Style
# # plt.figure(figsize=(12, 6))
# # fig, ax = plt.subplots(figsize=(12, 6))

# # # Define custom color palette
# # colors = ['#3366CC', '#DC3912', '#FF9900', '#109618']

# # # Plot each category
# # for i, category in enumerate(categories):
# #     data = df[df['Category'] == category]
# #     ax.plot(data['Date'], data['Sales'], marker='o', linewidth=2.5, 
# #             color=colors[i], label=category, alpha=0.9)

# # # Customize appearance
# # ax.set_title('Monthly Sales by Product Category', fontsize=16, fontweight='bold', pad=20)
# # ax.set_xlabel('Month', fontsize=12, labelpad=10)
# # ax.set_ylabel('Sales ($)', fontsize=12, labelpad=10)

# # # Format x-axis to show months
# # ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
# # plt.xticks(rotation=45)

# # # Add grid with custom style
# # ax.grid(axis='y', linestyle='--', alpha=0.7)
# # ax.spines['top'].set_visible(False)
# # ax.spines['right'].set_visible(False)

# # # Add legend with custom style
# # ax.legend(title='Product Category', title_fontsize=12, fontsize=10, 
# #           loc='upper left', frameon=True, framealpha=0.9)

# # # Add annotations for the last data point of each category
# # for i, category in enumerate(categories):
# #     data = df[df['Category'] == category]
# #     last_data = data.iloc[-1]
# #     ax.annotate(f"{last_data['Sales']}",
# #                 xy=(last_data['Date'], last_data['Sales']),
# #                 xytext=(10, 0), textcoords='offset points',
# #                 color=colors[i], fontweight='bold')

# # plt.tight_layout()
# # plt.show()

# # # 2. Modern Bar Chart
# # plt.figure(figsize=(12, 6))

# # # Prepare data - average sales by category
# # avg_sales = df.groupby('Category')['Sales'].mean().reset_index()

# # # Create custom colormap
# # custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", 
# #                                                ['#1A5276', '#2874A6', '#3498DB', '#85C1E9'])
# # colors = custom_cmap(np.linspace(0, 1, len(avg_sales)))

# # # Plot
# # ax = sns.barplot(x='Category', y='Sales', data=avg_sales, palette=colors, alpha=0.85)

# # # Customize
# # plt.title('Average Sales by Product Category', fontsize=16, fontweight='bold', pad=20)
# # plt.xlabel('Product Category', fontsize=12, labelpad=10)
# # plt.ylabel('Average Sales ($)', fontsize=12, labelpad=10)

# # # Add value labels on top of bars
# # for i, v in enumerate(avg_sales['Sales']):
# #     ax.text(i, v + 5, f"{v:.1f}", ha='center', fontweight='bold')

# # # Remove top and right spines
# # sns.despine()

# # # Add subtle grid
# # ax.grid(axis='y', alpha=0.3)

# # # Rotate labels if needed
# # plt.xticks(rotation=0)
# # plt.tight_layout()
# # plt.show()

# # # 3. Modern Heatmap
# # plt.figure(figsize=(12, 8))

# # # Prepare data for heatmap - pivot table of sales by month and category
# # heatmap_data = df.pivot_table(index='Date', columns='Category', values='Sales')

# # # Create heatmap with modern colormap
# # cmap = sns.color_palette("viridis", as_cmap=True)
# # ax = sns.heatmap(heatmap_data, annot=True, fmt='.0f', cmap=cmap, 
# #                 linewidths=0.5, linecolor='white',
# #                 cbar_kws={'label': 'Sales ($)'}, annot_kws={"size": 9})

# # # Customize
# # plt.title('Sales Heatmap by Product and Month', fontsize=16, fontweight='bold', pad=20)
# # plt.xlabel('Product Category', fontsize=12, labelpad=10)
# # plt.ylabel('Month', fontsize=12, labelpad=10)

# # # Format y-axis to show months only
# # y_labels = [date.strftime('%b %Y') for date in heatmap_data.index]
# # ax.set_yticklabels(y_labels)

# # plt.tight_layout()
# # plt.show()

# # # 4. Modern scatter plot with size variation
# # plt.figure(figsize=(10, 8))

# # # Create a modern scatter plot
# # fig, ax = plt.subplots(figsize=(10, 8))

# # # Define a modern colormap
# # colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3']

# # # Plot each category
# # for i, category in enumerate(categories):
# #     data = df[df['Category'] == category]
# #     ax.scatter(data['Sales'], data['Profit'], 
# #               s=data['Sales']/10,  # Size based on sales
# #               color=colors[i], 
# #               alpha=0.7,
# #               edgecolor='white',
# #               linewidth=0.5,
# #               label=category)

# # # Customize
# # ax.set_title('Sales vs Profit by Product Category', fontsize=16, fontweight='bold', pad=20)
# # ax.set_xlabel('Sales ($)', fontsize=12, labelpad=10)
# # ax.set_ylabel('Profit ($)', fontsize=12, labelpad=10)

# # # Add grid with custom style
# # ax.grid(True, linestyle='--', alpha=0.7)
# # ax.spines['top'].set_visible(False)
# # ax.spines['right'].set_visible(False)

# # # Format axes with comma separator
# # ax.xaxis.set_major_formatter(FuncFormatter(lambda x, p: f'{x:,.0f}'))
# # ax.yaxis.set_major_formatter(FuncFormatter(lambda x, p: f'{x:,.0f}'))

# # # Add legend
# # ax.legend(title='Product Category', title_fontsize=12, 
# #           fontsize=10, loc='upper left')

# # # Add a text explaining the bubble size
# # ax.text(0.02, 0.02, 'Bubble size represents sales volume', 
# #         transform=ax.transAxes, fontsize=10, alpha=0.7)

# # plt.tight_layout()
# # plt.show()

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.dates as mdates
# from matplotlib.colors import LinearSegmentedColormap
# from matplotlib.ticker import FuncFormatter

# # 파일 시스템에 저장할 Streamlit 코드 생성
# streamlit_app_code = """
# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.dates as mdates
# from matplotlib.colors import LinearSegmentedColormap
# from matplotlib.ticker import FuncFormatter
# import plotly.express as px
# import plotly.graph_objects as go

# # Page config
# st.set_page_config(
#     page_title="Sales Dashboard",
#     page_icon="📊",
#     layout="wide",
# )

# # Custom CSS
# st.markdown('''
# <style>
#     .main {
#         background-color: #f5f7f9;
#     }
#     h1, h2, h3 {
#         color: #1E3A8A;
#     }
#     .stTabs [data-baseweb="tab-list"] {
#         gap: 24px;
#     }
#     .stTabs [data-baseweb="tab"] {
#         height: 50px;
#         white-space: pre-wrap;
#         background-color: #FFFFFF;
#         border-radius: 4px 4px 0px 0px;
#         padding-top: 10px;
#         padding-bottom: 10px;
#     }
#     .stTabs [aria-selected="true"] {
#         background-color: #EFF6FF;
#         border-bottom: 2px solid #1E3A8A;
#     }
# </style>
# ''', unsafe_allow_html=True)

# # Load data
# @st.cache_data
# def load_data():
#     # 데이터 생성 로직
#     np.random.seed(42)
#     dates = pd.date_range(start='2024-01-01', periods=12, freq='M')
#     categories = ['Product A', 'Product B', 'Product C', 'Product D']
#     data = {
#         'Date': np.tile(dates, len(categories)),
#         'Category': np.repeat(categories, len(dates)),
#         'Sales': np.random.randint(100, 1000, size=len(dates)*len(categories)),
#         'Profit': np.random.randint(10, 100, size=len(dates)*len(categories))
#     }
#     return pd.DataFrame(data)

# df = load_data()

# # Header
# st.title("🚀 Interactive Sales Analytics Dashboard")
# st.markdown("### Track sales performance across products and time periods")

# # Create filters in sidebar
# st.sidebar.header("Filters")

# # Date range filter
# min_date = df['Date'].min().date()
# max_date = df['Date'].max().date()
# start_date, end_date = st.sidebar.date_input(
#     "Select Date Range",
#     [min_date, max_date],
#     min_value=min_date,
#     max_value=max_date
# )

# # Category filter
# selected_categories = st.sidebar.multiselect(
#     "Select Product Categories",
#     options=df['Category'].unique(),
#     default=df['Category'].unique()
# )

# # Filter the data
# filtered_df = df[
#     (df['Date'].dt.date >= start_date) & 
#     (df['Date'].dt.date <= end_date) & 
#     (df['Category'].isin(selected_categories))
# ]

# # Show data insights in expander
# with st.expander("📊 Data Overview"):
#     col1, col2, col3, col4 = st.columns(4)
    
#     # Key metrics
#     total_sales = filtered_df['Sales'].sum()
#     avg_sales = filtered_df['Sales'].mean()
#     total_profit = filtered_df['Profit'].sum()
#     profit_margin = (total_profit / total_sales) * 100
    
#     col1.metric("Total Sales", f"${total_sales:,.0f}")
#     col2.metric("Average Sales", f"${avg_sales:.2f}")
#     col3.metric("Total Profit", f"${total_profit:,.0f}")
#     col4.metric("Profit Margin", f"{profit_margin:.2f}%")
    
#     # Show filtered data
#     st.subheader("Filtered Data")
#     st.dataframe(filtered_df.style.highlight_max(subset=['Sales', 'Profit'], axis=0), use_container_width=True)

# # Create tabs for different visualizations
# tab1, tab2, tab3, tab4 = st.tabs(["📈 Trend Analysis", "📊 Category Comparison", "🔥 Heatmap", "🔄 Correlation"])

# with tab1:
#     st.header("Monthly Sales Trend by Product")
    
#     # Use Plotly for interactive line chart
#     fig = px.line(
#         filtered_df,
#         x="Date",
#         y="Sales",
#         color="Category",
#         markers=True,
#         line_shape="spline",
#         title="Monthly Sales by Product Category"
#     )
    
#     fig.update_layout(
#         plot_bgcolor="white",
#         hovermode="x unified",
#         legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
#         height=500,
#         xaxis_title="Month",
#         yaxis_title="Sales ($)"
#     )
    
#     st.plotly_chart(fig, use_container_width=True)
    
#     # Add insights
#     col1, col2 = st.columns(2)
    
#     with col1:
#         # Best selling month
#         monthly_sales = filtered_df.groupby(filtered_df['Date'].dt.strftime('%Y-%m'))['Sales'].sum()
#         best_month = monthly_sales.idxmax()
#         st.info(f"✨ Best selling month: **{best_month}** with **${monthly_sales.max():,.0f}** in sales")
    
#     with col2:
#         # Growth calculation
#         if len(monthly_sales) > 1:
#             growth = (monthly_sales.iloc[-1] - monthly_sales.iloc[0]) / monthly_sales.iloc[0] * 100
#             growth_icon = "📈" if growth > 0 else "📉"
#             st.info(f"{growth_icon} Sales growth: **{growth:.2f}%** from first to last month")

# with tab2:
#     st.header("Sales Performance by Product Category")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         # Interactive bar chart with Plotly
#         avg_by_category = filtered_df.groupby('Category')[['Sales', 'Profit']].mean().reset_index()
        
#         fig = px.bar(
#             avg_by_category,
#             x='Category',
#             y='Sales',
#             color='Category',
#             text_auto='.1f',
#             title="Average Sales by Product Category",
#             color_discrete_sequence=px.colors.qualitative.Bold
#         )
        
#         fig.update_layout(
#             plot_bgcolor="white",
#             height=500,
#             xaxis_title="Product Category",
#             yaxis_title="Average Sales ($)"
#         )
        
#         st.plotly_chart(fig, use_container_width=True)
        
#     with col2:
#         # Pie chart for market share
#         sales_by_category = filtered_df.groupby('Category')['Sales'].sum().reset_index()
        
#         fig = px.pie(
#             sales_by_category, 
#             values='Sales', 
#             names='Category',
#             title='Market Share by Product Category',
#             hole=0.4,
#             color_discrete_sequence=px.colors.qualitative.Bold
#         )
        
#         fig.update_layout(
#             height=500,
#             legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5)
#         )
        
#         st.plotly_chart(fig, use_container_width=True)

#     # Top performer insight
#     top_category = sales_by_category.iloc[sales_by_category['Sales'].argmax()]
#     st.success(f"🏆 Top performing product: **{top_category['Category']}** with **${top_category['Sales']:,.0f}** in total sales")

# with tab3:
#     st.header("Sales Heatmap Analysis")
    
#     # Prepare data for heatmap
#     pivot_data = filtered_df.pivot_table(
#         index='Date',
#         columns='Category',
#         values='Sales',
#         aggfunc='sum'
#     )
    
#     # Format dates for better display
#     pivot_data.index = pivot_data.index.strftime('%b %Y')
    
#     # Create interactive heatmap with Plotly
#     fig = px.imshow(
#         pivot_data,
#         text_auto=True,
#         aspect="auto",
#         color_continuous_scale='viridis',
#         title="Monthly Sales Heatmap by Product"
#     )
    
#     fig.update_layout(
#         plot_bgcolor="white",
#         height=600,
#         xaxis_title="Product Category",
#         yaxis_title="Month"
#     )
    
#     st.plotly_chart(fig, use_container_width=True)
    
#     # Add insights
#     pattern = pivot_data.idxmax(axis=1).value_counts().idxmax()
#     st.info(f"💡 **{pattern}** was the most frequently top-selling product across months")

# with tab4:
#     st.header("Sales and Profit Relationship")
    
#     # Create interactive scatter plot
#     fig = px.scatter(
#         filtered_df,
#         x="Sales",
#         y="Profit",
#         color="Category",
#         size="Sales",
#         hover_data=["Date"],
#         title="Sales vs. Profit by Product Category",
#         size_max=30,
#     )
    
#     fig.update_layout(
#         plot_bgcolor="white",
#         height=600,
#         xaxis_title="Sales ($)",
#         yaxis_title="Profit ($)"
#     )
    
#     st.plotly_chart(fig, use_container_width=True)
    
#     # Calculate and show correlation
#     correlation = filtered_df[['Sales', 'Profit']].corr().iloc[0, 1]
    
#     if correlation > 0.7:
#         correlation_text = "Strong positive correlation between sales and profit"
#     elif correlation > 0.4:
#         correlation_text = "Moderate positive correlation between sales and profit"
#     elif correlation > 0:
#         correlation_text = "Weak positive correlation between sales and profit"
#     else:
#         correlation_text = "No positive correlation between sales and profit"
    
#     st.info(f"📊 {correlation_text} (r = {correlation:.2f})")

# # Footer with download option
# st.markdown("---")
# col1, col2 = st.columns([3, 1])

# with col1:
#     st.markdown("### Download Data")
#     st.write("Export the filtered dataset for offline analysis")

# with col2:
#     csv = filtered_df.to_csv(index=False).encode('utf-8')
#     st.download_button(
#         label="Download CSV",
#         data=csv,
#         file_name="sales_data.csv",
#         mime="text/csv",
#         key='download-csv'
#     )
# """

# # 스트림릿 코드를 파일로 저장
# with open('/home/user/streamlit_app.py', 'w') as f:
#     f.write(streamlit_app_code)

# # 데이터 생성 (시각화를 위한)
# np.random.seed(42)
# dates = pd.date_range(start='2024-01-01', periods=12, freq='M')
# categories = ['Product A', 'Product B', 'Product C', 'Product D']
# data = {
#     'Date': np.tile(dates, len(categories)),
#     'Category': np.repeat(categories, len(dates)),
#     'Sales': np.random.randint(100, 1000, size=len(dates)*len(categories)),
#     'Profit': np.random.randint(10, 100, size=len(dates)*len(categories))
# }
# df = pd.DataFrame(data)

# # Streamlit 대시보드 목업 이미지 생성 (matplotlib로 시각화)
# plt.figure(figsize=(14, 8))
# fig, ax = plt.subplots(figsize=(14, 8))

# # 배경색 설정
# ax.set_facecolor('#f5f7f9')
# plt.tight_layout()

# # 헤더 부분
# ax.text(0.5, 0.95, '🚀 Interactive Sales Analytics Dashboard', fontsize=22, ha='center', fontweight='bold', color='#1E3A8A')
# ax.text(0.5, 0.91, 'Track sales performance across products and time periods', fontsize=14, ha='center', color='#4B5563')

# # 탭 표시
# tabs = ['📈 Trend Analysis', '📊 Category Comparison', '🔥 Heatmap', '🔄 Correlation']
# tab_width = 0.22
# for i, tab in enumerate(tabs):
#     is_active = i == 0
#     tab_color = '#EFF6FF' if is_active else '#FFFFFF'
#     border_color = '#1E3A8A' if is_active else '#E5E7EB'
#     text_color = '#1E3A8A' if is_active else '#4B5563'
    
#     rect = plt.Rectangle((0.02 + i*tab_width, 0.85), tab_width-0.01, 0.03, 
#                       facecolor=tab_color, edgecolor=border_color, linewidth=1, alpha=0.8)
#     ax.add_patch(rect)
#     if is_active:
#         bottom_line = plt.Rectangle((0.02 + i*tab_width, 0.85), tab_width-0.01, 0.003, 
#                               facecolor=border_color, edgecolor=border_color)
#         ax.add_patch(bottom_line)
    
#     ax.text(0.02 + i*tab_width + tab_width/2, 0.865, tab, fontsize=10, 
#            ha='center', va='center', color=text_color, fontweight='bold' if is_active else 'normal')

# # 차트 영역 - 트렌드 분석 탭
# chart_bg = plt.Rectangle((0.02, 0.25), 0.96, 0.58, facecolor='white', 
#                         edgecolor='#E5E7EB', linewidth=1, alpha=0.8)
# ax.add_patch(chart_bg)

# # 라인 차트 그리기 (간략화된 예시)
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# x_pos = np.linspace(0.06, 0.94, len(months))

# colors = ['#3366CC', '#DC3912', '#FF9900', '#109618']
# labels = ['Product A', 'Product B', 'Product C', 'Product D']
# data_sets = [
#     [202, 535, 960, 370, 206, 171, 800, 120, 714, 221, 764, 430],
#     [429, 324, 710, 620, 523, 271, 524, 620, 524, 431, 265, 524],
#     [324, 462, 262, 512, 434, 712, 325, 562, 173, 324, 405, 602],
#     [512, 243, 465, 221, 724, 384, 432, 283, 434, 276, 362, 421]
# ]

# for i, (data, color, label) in enumerate(zip(data_sets, colors, labels)):
#     # 데이터 정규화
#     normalized = [d/1000 * 0.5 for d in data]
    
#     # 라인 그리기 
#     for j in range(len(months)-1):
#         plt.plot([x_pos[j], x_pos[j+1]], 
#                 [0.55 - normalized[j], 0.55 - normalized[j+1]], 
#                 color=color, linewidth=2, alpha=0.8)
        
#         # 데이터 포인트 마커 추가
#         plt.scatter(x_pos[j], 0.55 - normalized[j], color=color, s=30, zorder=3)
    
#     # 마지막 데이터 포인트
#     plt.scatter(x_pos[-1], 0.55 - normalized[-1], color=color, s=30, zorder=3)
    
#     # 범례용 라인
#     plt.plot([0.03 + i*0.2, 0.08 + i*0.2], [0.78, 0.78], color=color, linewidth=2)
#     ax.text(0.1 + i*0.2, 0.78, label, fontsize=8, va='center')

# # 축 레이블
# for i, month in enumerate(months):
#     ax.text(x_pos[i], 0.28, month, fontsize=8, ha='center', color='#4B5563')

# ax.text(0.02, 0.55, 'Sales ($)', fontsize=10, va='center', rotation=90, color='#4B5563')

# # 타이틀
# ax.text(0.5, 0.8, 'Monthly Sales Trend by Product', fontsize=16, ha='center', fontweight='bold', color='#1E3A8A')

# # 사이드바 영역
# sidebar_bg = plt.Rectangle((-0.02, 0), 0.18, 1, facecolor='#FFFFFF', 
#                           edgecolor='#E5E7EB', linewidth=1, alpha=0.3)
# ax.add_patch(sidebar_bg)

# ax.text(0.07, 0.95, 'Filters', fontsize=12, ha='center', fontweight='bold', color='#1E3A8A', alpha=0.7)
# ax.text(0.07, 0.9, 'Date Range', fontsize=10, ha='center', color='#4B5563', alpha=0.7)
# ax.text(0.07, 0.85, 'Categories', fontsize=10, ha='center', color='#4B5563', alpha=0.7)

# # 통계 카드
# cards = ['Total Sales', 'Avg Sales', 'Total Profit', 'Profit Margin']
# card_values = ['$46,280', '$578.50', '$3,421', '7.39%']
# card_width = 0.22

# for i, (title, value) in enumerate(zip(cards, card_values)):
#     card = plt.Rectangle((0.02 + i*card_width, 0.15), card_width-0.01, 0.06, 
#                       facecolor='white', edgecolor='#E5E7EB', linewidth=1, alpha=0.8)
#     ax.add_patch(card)
    
#     ax.text(0.02 + i*card_width + card_width/2, 0.19, title, fontsize=9, 
#            ha='center', va='center', color='#4B5563')
#     ax.text(0.02 + i*card_width + card_width/2, 0.16, value, fontsize=12, 
#            ha='center', va='center', fontweight='bold', color='#1E3A8A')

# # 축 제거
# ax.axis('off')
# ax.set_xlim(-0.05, 1.05)
# ax.set_ylim(0, 1)

# plt.title("Streamlit Sales Dashboard Preview", fontsize=14, loc='left', pad=20)
# plt.tight_layout()
# plt.show()

# print("Streamlit 애플리케이션 코드가 '/home/user/streamlit_app.py'로 저장되었습니다.")
# print("\n이 코드를 Streamlit이 설치된 환경에서 'streamlit run streamlit_app.py' 명령으로 실행할 수 있습니다.")

# # 기능 설명
# print("\n## 이 Streamlit 대시보드의 주요 기능:")
# print("1. 📊 데이터 필터링: 날짜 범위와 제품 카테고리 선택 가능")
# print("2. 📈 핵심 지표: 총 매출, 평균 매출, 총 이익, 이익률 요약")
# print("3. 📌 탭 기반 시각화:")
# print("   - 트렌드 분석: 월별 제품 카테고리별 판매량 추이")
# print("   - 카테고리 비교: 제품별 평균 매출 및 시장 점유율")
# print("   - 히트맵: 월별/제품별 매출 히트맵")
# print("   - 상관관계: 매출과 이익 간의 관계 분석")
# print("4. 💡 자동화된 인사이트: 최고 판매 월, 성장률, 최다 판매 제품 등")
# print("5. 💾 데이터 다운로드: 필터링된 데이터를 CSV로 내보내기 가능")

import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(
    page_title="핀테크 산업 리서치 대시보드",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 샘플 데이터 생성
market_data = pd.DataFrame({
    'Year': [2020, 2021, 2022, 2023, 2024],
    'Market Size (조 원)': [550, 720, 950, 1200, 1550],
    'Growth Rate (%)': [24.3, 30.9, 31.9, 26.3, 29.2]
})

companies = {
    '카카오페이': {'MAU': 3200, '거래액(조)': 78, '제휴사': 150},
    '네이버페이': {'MAU': 2100, '거래액(조)': 54, '제휴사': 90},
    '토스': {'MAU': 1800, '거래액(조)': 42, '제휴사': 75}
}

# 사이드바
with st.sidebar:
    st.header("필터 설정")
    selected_year = st.selectbox("분석 연도 선택", market_data['Year'])
    st.caption("출처: 글로벌 핀테크 시장 보고서 2025")

# 메인 대시보드
st.title("2025 핀테크 산업 리서치 대시보드")
st.divider()

# 1. 시장 개요
col1, col2 = st.columns(2)
with col1:
    st.subheader("📈 시장 성장 추이")
    fig = px.line(market_data, x='Year', y='Market Size (조 원)', 
                 markers=True, title="글로벌 핀테크 시장 규모")
    st.plotly_chart(fig, use_container_width=True)
    st.caption("출처: IDC 글로벌 핀테크 전망 2025")

with col2:
    st.subheader("🏆 주요 기업 비교")
    company_df = pd.DataFrame(companies).T.reset_index()
    company_df.columns = ['기업', 'MAU(만)', '거래액(조 원)', '제휴사 수']
    
    fig = px.bar(company_df, x='기업', y='거래액(조 원)', 
                color='기업', text_auto=True,
                title="2025년 거래액 비교")
    st.plotly_chart(fig, use_container_width=True)
    st.caption("출처: 카카오페이/네이버페이 공시 자료")

# 2. 세부 분석
st.subheader("🔍 기술 도입 현황")
tech_data = pd.DataFrame({
    '기술': ['AI 신용평가', '블록체인', '생체인증', '양자암호'],
    '도입률(%)': [78, 65, 82, 35]
})

fig = px.funnel(tech_data, x='도입률(%)', y='기술',
               title="핀테크 기업 기술 도입 현황")
st.plotly_chart(fig, use_container_width=True)
st.caption("출처: 한국핀테크협회 기술백서 2025")

# 3. 참고문헌
st.divider()
st.subheader("📚 참고문헌")
references = [
    "1. 카카오페이 2024 연간 보고서",
    "2. 네이버파이낸셜 전략백서",
    "3. 금융감독원 핀테크 통계",
    "4. 한국은행 결제시스템 보고서 2025",
    "5. IDC 글로벌 핀테크 전망",
    "6. The Rise of Super Apps (McKinsey)",
    "7. BIS 디지털화폐 연구",
    "8. 삼성증명 금융IT 레포트",
    "9. 카카오페이 IPO 공시자료",
    "10. NH투자證 핀테크 생태계 분석"
]

for ref in references:
    st.markdown(f"- {ref}")

st.caption("※ 본 보고서는 시뮬레이션 데이터를 기반으로 작성되었습니다.")
