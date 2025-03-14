# # 필수 라이브러리 임포트
# import pandas as pd
# import pandas_datareader.wb as wb
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.preprocessing import StandardScaler
# import numpy as np
# import streamlit as st
# import warnings

# # 불필요한 경고 숨기기
# warnings.filterwarnings('ignore')
# st.set_option('deprecation.showPyplotGlobalUse', False)

# def main():
#     # 페이지 설정
#     st.set_page_config(
#         page_title="Iraq Infrastructure Analysis",
#         page_icon="🏗️",
#         layout="wide"
#     )
        
#     # 제목 및 소개
#     st.title("Iraq Infrastructure Indicators Analysis (2003-2023)")
#     st.markdown("""
#     This application analyzes the relationship between various infrastructure indicators 
#     in Iraq following the 2003 conflict. The data is sourced from the World Bank.
#     """)

#     # 사이드바 - 분석 기간 설정
#     st.sidebar.header("Analysis Parameters")
#     start_year = st.sidebar.slider("Start Year", 2000, 2020, 2003)
#     end_year = st.sidebar.slider("End Year", 2001, 2023, 2023)
    
#     # 데이터 로딩 상태 표시
#     with st.spinner('Fetching data from World Bank API...'):
#         # 세계은행 데이터 수집
#         indicators = {
#             'EG.ELC.ACCS.ZS': 'Electricity_Access',
#             'IT.CEL.SETS.P2': 'Mobile_Subscriptions',
#             'IT.NET.USER.ZS': 'Internet_Users',
#             'IS.RRS.TOTL.KM': 'Railway_Length',
#             'NY.GDP.MKTP.KD.ZG': 'GDP_Growth'
#         }
        
#         # 데이터 로드
#         @st.cache_data
#         def load_data(start_year, end_year):
#             df = wb.download(indicator=list(indicators.keys()), 
#                             country=['IRQ'], 
#                             start=start_year, 
#                             end=end_year).reset_index()
            
#             # 컬럼명 변경 및 전처리
#             df = df.rename(columns=indicators)
#             df['Year'] = df['year'].astype(int)
#             df = df.dropna().set_index('Year')
#             df = df.drop('country', axis=1)
            
#             # 복구 비용 계산
#             df['Recovery_Cost_Index'] = (
#                 (df['GDP_Growth']/100 * df['Mobile_Subscriptions']) + 
#                 (df['Electricity_Access'] * df['Railway_Length'])
#             )
            
#             # 데이터 정규화
#             scaler = StandardScaler()
#             df_scaled = pd.DataFrame(scaler.fit_transform(df), 
#                                     columns=df.columns, 
#                                     index=df.index)
#             return df, df_scaled
        
#         df, df_scaled = load_data(start_year, end_year)
    
#     # 데이터 탭과 시각화 탭
#     tab1, tab2, tab3 = st.tabs(["Data Overview", "Correlation Analysis", "Time Series Analysis"])
    
#     with tab1:
#         st.header("Infrastructure Data Overview")
#         st.dataframe(df)
        
#         # 기본 통계 정보
#         st.subheader("Statistical Summary")
#         st.dataframe(df.describe())
        
#         # 데이터 다운로드 버튼
#         csv = df.to_csv().encode('utf-8')
#         st.download_button(
#             label="Download Data as CSV",
#             data=csv,
#             file_name=f'iraq_infrastructure_data_{start_year}_{end_year}.csv',
#             mime='text/csv',
#         )
    
#     with tab2:
#         st.header("Correlation Analysis")
        
#         # 히트맵
#         st.subheader("Correlation Heatmap")
#         fig, ax = plt.subplots(figsize=(10, 8))
#         sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
#         plt.title('Infrastructure Indicators Correlation Analysis for Iraq (2003-2023)')
#         st.pyplot(fig)
        
#         # 상관관계 분석 설명
#         st.markdown("""
#         ### Key Insights:
#         - **Electricity Access** shows a strong correlation with Internet Users, indicating digital infrastructure development follows basic utilities.
#         - **Mobile Subscriptions** correlate with GDP Growth, suggesting telecommunications as a key economic driver.
#         - **Railway Length** has limited correlation with other metrics, possibly due to slower development of physical infrastructure.
#         """)
    
#     with tab3:
#         st.header("Time Series Analysis")
        
#         # 전기 접근성 vs 복구 비용
#         st.subheader("Energy Infrastructure Recovery Trends")
#         fig1, ax1 = plt.subplots(figsize=(10, 6))
#         ax1.plot(df.index, df['Electricity_Access'], label='Electricity Access')
#         ax1.plot(df.index, df['Recovery_Cost_Index'], label='Recovery Cost Index')
#         ax1.set_title('Energy Infrastructure Recovery Trends')
#         ax1.legend()
#         ax1.grid(True)
#         st.pyplot(fig1)
        
#         # 모바일 가입자 vs GDP 성장률
#         st.subheader("Mobile Subscriptions vs GDP Growth")
#         fig2, ax2 = plt.subplots(figsize=(10, 6))
#         scatter = ax2.scatter(df['Mobile_Subscriptions'], df['GDP_Growth'], 
#                    c=df.index, cmap='viridis')
#         ax2.set_xlabel('Mobile Subscriptions per 100 people')
#         ax2.set_ylabel('GDP Growth (%)')
#         ax2.grid(True)
#         # 컬러바 추가
#         cbar = plt.colorbar(scatter)
#         cbar.set_label('Year')
#         st.pyplot(fig2)
        
#         # 철도 인프라 투자 효과
#         st.subheader("Railway Infrastructure Expansion")
#         fig3, ax3 = plt.subplots(figsize=(10, 6))
#         ax3.bar(df.index, df['Railway_Length'], 
#                color=np.where(df['Railway_Length']>0, 'green', 'red'))
#         ax3.set_title('Annual Railway Infrastructure Expansion')
#         ax3.grid(True, axis='y')
#         st.pyplot(fig3)
        
#         # 인터넷 사용자 추이
#         st.subheader("Internet Users Trend")
#         fig4, ax4 = plt.subplots(figsize=(10, 6))
#         ax4.plot(df.index, df['Internet_Users'], marker='o', linestyle='-', color='blue')
#         ax4.set_title('Internet Users (% of population)')
#         ax4.grid(True)
#         st.pyplot(fig4)

#     # 결론
#     st.header("Conclusion")
#     st.markdown("""
#     The analysis shows significant progress in Iraq's infrastructure development since 2003, 
#     particularly in telecommunications and electricity access. The correlation between 
#     infrastructure indicators and economic growth highlights the importance of continued 
#     investment in these sectors for Iraq's reconstruction and development.
    
#     Mobile telecommunications appears to be a leading sector in the recovery, while physical 
#     infrastructure like railways shows slower progress, suggesting different priorities or 
#     challenges in reconstruction efforts.
#     """)

#     # 푸터
#     st.sidebar.markdown("---")
#     st.sidebar.info(
#         """
#         **Data Source:** World Bank Development Indicators  
#         **Analysis Period:** {} - {}
#         """.format(start_year, end_year)
#     )

# if __name__ == "__main__":
#     main()


# 필수 라이브러리 임포트
import pandas as pd
import pandas_datareader.wb as wb
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import numpy as np
import streamlit as st
import warnings

# 불필요한 경고 숨기기
warnings.filterwarnings('ignore')
# st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
    # 페이지 설정
    st.set_page_config(
        page_title="Iraq Infrastructure Analysis",
        page_icon="🏗️",
        layout="wide"
    )
    
    # 제목 및 소개
    st.title("Iraq Infrastructure Indicators Analysis (2003-2023)")
    st.markdown("""
    This application analyzes the relationship between various infrastructure indicators 
    in Iraq following the 2003 conflict. The data is sourced from the World Bank.
    """)

    # 사이드바 - 분석 기간 설정
    st.sidebar.header("Analysis Parameters")
    start_year = st.sidebar.slider("Start Year", 2000, 2020, 2003)
    end_year = st.sidebar.slider("End Year", 2001, 2023, 2023)
    
    # 데이터 로딩 상태 표시
    with st.spinner('Fetching data from World Bank API...'):
        # 세계은행 데이터 수집
        indicators = {
            'EG.ELC.ACCS.ZS': 'Electricity_Access',
            'IT.CEL.SETS.P2': 'Mobile_Subscriptions',
            'IT.NET.USER.ZS': 'Internet_Users',
            'IS.RRS.TOTL.KM': 'Railway_Length',
            'NY.GDP.MKTP.KD.ZG': 'GDP_Growth'
        }
        
        # 데이터 로드
        @st.cache_data
        def load_data(start_year, end_year):
            df = wb.download(indicator=list(indicators.keys()), 
                            country=['IRQ'], 
                            start=start_year, 
                            end=end_year).reset_index()
            
            # 컬럼명 변경 및 전처리
            df = df.rename(columns=indicators)
            df['Year'] = df['year'].astype(int)
            df = df.dropna().set_index('Year')
            df = df.drop('country', axis=1)
            
            # 복구 비용 계산
            df['Recovery_Cost_Index'] = (
                (df['GDP_Growth']/100 * df['Mobile_Subscriptions']) + 
                (df['Electricity_Access'] * df['Railway_Length'])
            )
            
            # 데이터 정규화
            scaler = StandardScaler()
            df_scaled = pd.DataFrame(scaler.fit_transform(df), 
                                    columns=df.columns, 
                                    index=df.index)
            return df, df_scaled
        
        df, df_scaled = load_data(start_year, end_year)
    
    # 데이터 탭과 시각화 탭
    tab1, tab2, tab3 = st.tabs(["Data Overview", "Correlation Analysis", "Time Series Analysis"])
    
    with tab1:
        st.header("Infrastructure Data Overview")
        st.dataframe(df)
        
        # 기본 통계 정보
        st.subheader("Statistical Summary")
        st.dataframe(df.describe())
        
        # 데이터 다운로드 버튼
        csv = df.to_csv().encode('utf-8')
        st.download_button(
            label="Download Data as CSV",
            data=csv,
            file_name=f'iraq_infrastructure_data_{start_year}_{end_year}.csv',
            mime='text/csv',
        )
    
    with tab2:
        st.header("Correlation Analysis")
        
        # 히트맵
        st.subheader("Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
        plt.title('Infrastructure Indicators Correlation Analysis for Iraq (2003-2023)')
        st.pyplot(fig)
        
        # 상관관계 분석 설명
        st.markdown("""
        ### Key Insights:
        - **Electricity Access** shows a strong correlation with Internet Users, indicating digital infrastructure development follows basic utilities.
        - **Mobile Subscriptions** correlate with GDP Growth, suggesting telecommunications as a key economic driver.
        - **Railway Length** has limited correlation with other metrics, possibly due to slower development of physical infrastructure.
        """)
    
    with tab3:
        st.header("Time Series Analysis")
        
        # 전기 접근성 vs 복구 비용
        st.subheader("Energy Infrastructure Recovery Trends")
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        ax1.plot(df.index, df['Electricity_Access'], label='Electricity Access')
        ax1.plot(df.index, df['Recovery_Cost_Index'], label='Recovery Cost Index')
        ax1.set_title('Energy Infrastructure Recovery Trends')
        ax1.legend()
        ax1.grid(True)
        st.pyplot(fig1)
        
        # 모바일 가입자 vs GDP 성장률
        st.subheader("Mobile Subscriptions vs GDP Growth")
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        scatter = ax2.scatter(df['Mobile_Subscriptions'], df['GDP_Growth'], 
                   c=df.index, cmap='viridis')
        ax2.set_xlabel('Mobile Subscriptions per 100 people')
        ax2.set_ylabel('GDP Growth (%)')
        ax2.grid(True)
        # 컬러바 추가
        cbar = plt.colorbar(scatter)
        cbar.set_label('Year')
        st.pyplot(fig2)
        
        # 철도 인프라 투자 효과
        st.subheader("Railway Infrastructure Expansion")
        fig3, ax3 = plt.subplots(figsize=(10, 6))
        ax3.bar(df.index, df['Railway_Length'], 
               color=np.where(df['Railway_Length']>0, 'green', 'red'))
        ax3.set_title('Annual Railway Infrastructure Expansion')
        ax3.grid(True, axis='y')
        st.pyplot(fig3)
        
        # 인터넷 사용자 추이
        st.subheader("Internet Users Trend")
        fig4, ax4 = plt.subplots(figsize=(10, 6))
        ax4.plot(df.index, df['Internet_Users'], marker='o', linestyle='-', color='blue')
        ax4.set_title('Internet Users (% of population)')
        ax4.grid(True)
        st.pyplot(fig4)

    # 결론
    st.header("Conclusion")
    st.markdown("""
    The analysis shows significant progress in Iraq's infrastructure development since 2003, 
    particularly in telecommunications and electricity access. The correlation between 
    infrastructure indicators and economic growth highlights the importance of continued 
    investment in these sectors for Iraq's reconstruction and development.
    
    Mobile telecommunications appears to be a leading sector in the recovery, while physical 
    infrastructure like railways shows slower progress, suggesting different priorities or 
    challenges in reconstruction efforts.
    """)

    # 푸터
    st.sidebar.markdown("---")
    st.sidebar.info(
        """
        **Data Source:** World Bank Development Indicators  
        **Analysis Period:** {} - {}
        """.format(start_year, end_year)
    )

if __name__ == "__main__":
    main()
