import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import os
from matplotlib.font_manager import FontProperties

# 设置中文字体（部署兼容）
font_path = os.path.join("fonts", "SimHei.ttf")
my_font = FontProperties(fname=font_path)
matplotlib.rcParams['font.family'] = my_font.get_name()
matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号

st.title("能力评估打分雷达图小程序")

questions = [
    "自身产品资源",
    "内容创作能力",
    "个人品牌影响力",
    "互动与沟通能力",
    "技术操作能力",
    "市场洞察能力",
    "团队协作能力",
    "持续学习能力",
    "资源整合能力"
]

scores = []

st.subheader("请为下列每项能力打分（0~10）：")
for q in questions:
    score = st.slider(q, 0, 10, 5)
    scores.append(score)

if st.button("生成雷达图"):
    values = scores + [scores[0]]
    angles = np.linspace(0, 2 * np.pi, len(scores), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
    ax.plot(angles, values, 'o-', linewidth=2)
    ax.fill(angles, values, alpha=0.25)
    ax.set_thetagrids(np.degrees(angles[:-1]), questions, fontproperties=my_font)
    ax.set_ylim(0, 10)

    st.pyplot(fig)