# 示例：用Streamlit展示爬取结果
import streamlit as st
import pandas as pd

# 假设你已经爬到了数据，存在df里
df = pd.read_csv('my_data.csv',encoding='utf-8-sig')

st.title("我的爬虫作品展示")
st.write("这是我从XX网站爬取的数据")
st.dataframe(df)  # 自动适配屏幕大小
#强制重启
