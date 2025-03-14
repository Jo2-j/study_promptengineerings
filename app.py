# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # 페이지 제목
# st.title("환율 변화 및 산업군 영향 분석 대시보드")

# # 데이터 업로드
# st.sidebar.header("데이터 업로드")
# uploaded_file = st.sidebar.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

# if uploaded_file:
#     # 데이터 로드
#     data = pd.read_csv(uploaded_file)
#     st.write("업로드된 데이터:")
#     st.write(data.head())

#     # 날짜 필터
#     st.sidebar.header("기간 필터")
#     start_date = st.sidebar.date_input("시작 날짜", value=pd.to_datetime(data['날짜']).min())
#     end_date = st.sidebar.date_input("종료 날짜", value=pd.to_datetime(data['날짜']).max())

#     if start_date > end_date:
#         st.error("시작 날짜는 종료 날짜보다 이전이어야 합니다.")
#     else:
#         # 선택된 기간에 따른 데이터 필터링
#         filtered_data = data[(pd.to_datetime(data['날짜']) >= start_date) & (pd.to_datetime(data['날짜']) <= end_date)]
#         st.write("선택된 기간에 따른 데이터:")
#         st.write(filtered_data)

#         # 환율 변화 시각화
#         st.subheader("기간별 환율 변화")
#         fig = px.line(filtered_data, x="날짜", y="매매가격", title="기간별 환율 변화")
#         st.plotly_chart(fig)

#         # # 산업군별 영향 분석
#         # st.subheader("산업군별 영향 분석")
#         # industry_impact = filtered_data.groupby("industry")["impact"].mean().reset_index()
#         # industry_impact = industry_impact.sort_values(by="impact", ascending=False)
#         # st.write(industry_impact)

#         # fig2 = px.bar(industry_impact, x="industry", y="impact", title="산업군별 평균 영향")
#         # st.plotly_chart(fig2)

# else:
#     st.info("먼저 데이터를 업로드하세요. CSV 파일에는 'date', 'exchange_rate', 'industry', 'impact' 열이 포함되어야 합니다.")


import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px


st.set_page_config(
    page_title="US Population Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")
 
alt.themes.enable("dark")

df_reshaped = pd.read_csv('/apps/study_promptengineerings/exchange_rates_filtered_2017_2021.csv')

with st.sidebar:
    st.title('🏂 US Population Dashboard')
    
    year_list = list(df_reshaped.year.unique())[::-1]
    
    selected_year = st.selectbox('Select a year', year_list, index=len(year_list)-1)
    df_selected_year = df_reshaped[df_reshaped.year == selected_year]
    df_selected_year_sorted = df_selected_year.sort_values(by="population", ascending=False)
 
    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
    heatmap = alt.Chart(input_df).mark_rect().encode(
            y=alt.Y(f'{input_y}:O', axis=alt.Axis(title="Year", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
            x=alt.X(f'{input_x}:O', axis=alt.Axis(title="", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
            color=alt.Color(f'max({input_color}):Q',
                             legend=None,
                             scale=alt.Scale(scheme=input_color_theme)),
            stroke=alt.value('black'),
            strokeWidth=alt.value(0.25),
        ).properties(width=900
        ).configure_axis(
        labelFontSize=12,
        titleFontSize=12
        ) 
    # height=300
    return heatmap

def make_choropleth(input_df, input_id, input_column, input_color_theme):
    choropleth = px.choropleth(input_df, locations=input_id, color=input_column, locationmode="USA-states",
                               color_continuous_scale=input_color_theme,
                               range_color=(0, max(df_selected_year.population)),
                               scope="usa",
                               labels={'population':'Population'}
                              )
    choropleth.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=350
    )
    return choropleth

def calculate_population_difference(input_df, input_year):
  selected_year_data = input_df[input_df['year'] == input_year].reset_index()
  previous_year_data = input_df[input_df['year'] == input_year - 1].reset_index()
  selected_year_data['population_difference'] = selected_year_data.population.sub(previous_year_data.population, fill_value=0)
  return pd.concat([selected_year_data.states, selected_year_data.id, selected_year_data.population, selected_year_data.population_difference], axis=1).sort_values(by="population_difference", ascending=False)

def make_donut(input_response, input_text, input_color):
  if input_color == 'blue':
      chart_color = ['#29b5e8', '#155F7A']
  if input_color == 'green':
      chart_color = ['#27AE60', '#12783D']
  if input_color == 'orange':
      chart_color = ['#F39C12', '#875A12']
  if input_color == 'red':
      chart_color = ['#E74C3C', '#781F16']
    
  source = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100-input_response, input_response]
  })
  source_bg = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100, 0]
  })
    
  plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          #domain=['A', 'B'],
                          domain=[input_text, ''],
                          # range=['#29b5e8', '#155F7A']),  # 31333F
                          range=chart_color),
                      legend=None),
  ).properties(width=130, height=130)
    
  text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=32, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{input_response} %'))
  plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          # domain=['A', 'B'],
                          domain=[input_text, ''],
                          range=chart_color),  # 31333F
                      legend=None),
  ).properties(width=130, height=130)
  return plot_bg + plot + text

def format_number(num):
    if num > 1000000:
        if not num % 1000000:
            return f'{num // 1000000} M'
        return f'{round(num / 1000000, 1)} M'
    return f'{num // 1000} K'

col = st.columns((1.5, 4.5, 2), gap='medium')

with col[0]:
    st.markdown('#### Gains/Losses')
 
    df_population_difference_sorted = calculate_population_difference(df_reshaped, selected_year)
 
    if selected_year > 2010:
        first_state_name = df_population_difference_sorted.states.iloc[0]
        first_state_population = format_number(df_population_difference_sorted.population.iloc[0])
        first_state_delta = format_number(df_population_difference_sorted.population_difference.iloc[0])
    else:
        first_state_name = '-'
        first_state_population = '-'
        first_state_delta = ''
    st.metric(label=first_state_name, value=first_state_population, delta=first_state_delta)
 
    if selected_year > 2010:
        last_state_name = df_population_difference_sorted.states.iloc[-1]
        last_state_population = format_number(df_population_difference_sorted.population.iloc[-1])   
        last_state_delta = format_number(df_population_difference_sorted.population_difference.iloc[-1])   
    else:
        last_state_name = '-'
        last_state_population = '-'
        last_state_delta = ''
    st.metric(label=last_state_name, value=last_state_population, delta=last_state_delta)
 
    
    st.markdown('#### States Migration')
 
    if selected_year > 2010:
        # Filter states with population difference > 50000
        # df_greater_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference_absolute > 50000]
        df_greater_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference > 50000]
        df_less_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference < -50000]
        
        # % of States with population difference > 50000
        states_migration_greater = round((len(df_greater_50000)/df_population_difference_sorted.states.nunique())*100)
        states_migration_less = round((len(df_less_50000)/df_population_difference_sorted.states.nunique())*100)
        donut_chart_greater = make_donut(states_migration_greater, 'Inbound Migration', 'green')
        donut_chart_less = make_donut(states_migration_less, 'Outbound Migration', 'red')
    else:
        states_migration_greater = 0
        states_migration_less = 0
        donut_chart_greater = make_donut(states_migration_greater, 'Inbound Migration', 'green')
        donut_chart_less = make_donut(states_migration_less, 'Outbound Migration', 'red')
 
    migrations_col = st.columns((0.2, 1, 0.2))
    with migrations_col[1]:
        st.write('Inbound')
        st.altair_chart(donut_chart_greater)
        st.write('Outbound')
        st.altair_chart(donut_chart_less)
Column 2
 
Next, the second column displays the choropleth map and heatmap using custom functions created earlier.
 
with col[1]:
    st.markdown('#### Total Population')
    
    choropleth = make_choropleth(df_selected_year, 'states_code', 'population', selected_color_theme)
    st.plotly_chart(choropleth, use_container_width=True)
    
    heatmap = make_heatmap(df_reshaped, 'year', 'states', 'population', selected_color_theme)
    st.altair_chart(heatmap, use_container_width=True)
Column 3
 
Finally, the third column shows the top states via a dataframe whereby the population are shown as a colored progress bar via the column_config parameter of st.dataframe.
 
An About section is displayed via the st.expander() container to provide information on the data source and definitions for terminologies used in the dashboard.
 
with col[2]:
    st.markdown('#### Top States')
 
    st.dataframe(df_selected_year_sorted,
                 column_order=("states", "population"),
                 hide_index=True,
                 width=None,
                 column_config={
                    "states": st.column_config.TextColumn(
                        "States",
                    ),
                    "population": st.column_config.ProgressColumn(
                        "Population",
                        format="%f",
                        min_value=0,
                        max_value=max(df_selected_year_sorted.population),
                     )}
                 )
    
    with st.expander('About', expanded=True):
        st.write('''
            - Data: [U.S. Census Bureau](<https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html>).
            - :orange[**Gains/Losses**]: states with high inbound/ outbound migration for selected year
            - :orange[**States Migration**]: percentage of states with annual inbound/ outbound migration > 50,000
            ''')
        
with col[1]:
    st.markdown('#### Total Population')
    
    choropleth = make_choropleth(df_selected_year, 'states_code', 'population', selected_color_theme)
    st.plotly_chart(choropleth, use_container_width=True)
    
    heatmap = make_heatmap(df_reshaped, 'year', 'states', 'population', selected_color_theme)
    st.altair_chart(heatmap, use_container_width=True)

with col[2]:
    st.markdown('#### Top States')
 
    st.dataframe(df_selected_year_sorted,
                 column_order=("states", "population"),
                 hide_index=True,
                 width=None,
                 column_config={
                    "states": st.column_config.TextColumn(
                        "States",
                    ),
                    "population": st.column_config.ProgressColumn(
                        "Population",
                        format="%f",
                        min_value=0,
                        max_value=max(df_selected_year_sorted.population),
                     )}
                 )
    
    with st.expander('About', expanded=True):
        st.write('''
            - Data: [U.S. Census Bureau](<https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html>).
            - :orange[**Gains/Losses**]: states with high inbound/ outbound migration for selected year
            - :orange[**States Migration**]: percentage of states with annual inbound/ outbound migration > 50,000
            ''')


import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

# 페이지 설정
st.set_page_config(
    page_title="환율 변화 및 산업군 영향 분석",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 테마 설정
alt.themes.enable("dark")

# 페이지 제목
st.title("📊 환율 변화 및 산업군 영향 분석 대시보드")

# 데이터 업로드
st.sidebar.header("데이터 업로드")
uploaded_file = st.sidebar.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file:
    # 데이터 로드
    data = pd.read_csv(uploaded_file)
    st.sidebar.success("데이터 업로드 완료!")

    # 날짜 필터
    st.sidebar.header("기간 필터")
    start_date = st.sidebar.date_input("시작 날짜", value=pd.to_datetime(data['날짜']).min())
    end_date = st.sidebar.date_input("종료 날짜", value=pd.to_datetime(data['날짜']).max())
    # 시작 날짜와 종료 날짜를 datetime 형식으로 변환
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # 필터링 조건 수정
    

    if start_date > end_date:
        st.error("시작 날짜는 종료 날짜보다 이전이어야 합니다.")
    else:
        # 선택된 기간에 따른 데이터 필터링
        filtered_data = data[(pd.to_datetime(data['날짜']) >= start_date) & (pd.to_datetime(data['날짜']) <= end_date)]
        # 컬럼 레이아웃
        col1, col2, col3 = st.columns([1.5, 4.5, 2])

        # 첫 번째 컬럼: 주요 통계
        with col1:
            st.markdown("### 주요 통계")
            st.metric(label="최대 환율", value=filtered_data['매매가격'].max())
            st.metric(label="최소 환율", value=filtered_data['매매가격'].min())
            st.metric(label="평균 환율", value=round(filtered_data['매매가격'].mean(), 2))

        # 두 번째 컬럼: 환율 변화 시각화
        with col2:
            st.markdown("### 📈 기간별 환율 변화")
            fig = px.line(filtered_data, x="날짜", y="매매가격", title="기간별 환율 변화", labels={"매매기준율": "환율", "날짜": "날짜"})
            fig.update_layout(template="plotly_dark", height=400)
            st.plotly_chart(fig, use_container_width=True)

        # 세 번째 컬럼: 산업군 영향 분석
        with col3:
            st.markdown("### 📊 산업군별 영향 분석")
            if "산업군" in data.columns and "영향도" in data.columns:
                industry_impact = filtered_data.groupby("산업군")["영향도"].mean().reset_index()
                industry_impact = industry_impact.sort_values(by="영향도", ascending=False)
                fig2 = px.bar(industry_impact, x="산업군", y="영향도", title="산업군별 평균 영향", labels={"산업군": "산업군", "영향도": "평균 영향도"})
                fig2.update_layout(template="plotly_dark", height=400)
                st.plotly_chart(fig2, use_container_width=True)
            else:
                st.warning("산업군 및 영향도 데이터가 없습니다.")

        # 추가 정보 섹션
        with st.expander("ℹ️ 데이터 설명"):
            st.write("""
            - **날짜**: 환율 데이터의 수집 날짜
            - **매매기준율**: 해당 날짜의 환율
            - **산업군**: 산업군 이름 (선택적)
            - **영향도**: 산업군이 받은 영향도 (선택적)
            """)

else:
    st.info("먼저 데이터를 업로드하세요. CSV 파일에는 '날짜', '매매기준율', '산업군', '영향도' 열이 포함되어야 합니다.")
