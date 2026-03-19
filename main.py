import streamlit as st

def knapsack(max_weight, items):
    n = len(items)
    dp = [0] * (max_weight + 1)
    for w, v in items:
        for j in range(max_weight, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + v)
    return dp[max_weight]

st.title("🎉 背包算法智能决策助手")
st.subheader("基于01背包算法的最优选择计算器")

max_weight = st.number_input("请输入最大容量/预算", min_value=1, value=5)

st.subheader("添加物品（重量 & 价值）")
col1, col2 = st.columns(2)

with col1:
    w1 = st.number_input("物品1 重量", min_value=1, value=2)
    v1 = st.number_input("物品1 价值", min_value=1, value=5)
with col2:
    w2 = st.number_input("物品2 重量", min_value=1, value=3)
    v2 = st.number_input("物品2 价值", min_value=1, value=6)
with col1:
    w3 = st.number_input("物品3 重量", min_value=1, value=4)
    v3 = st.number_input("物品3 价值", min_value=1, value=6)

items = [(w1, v1), (w2, v2), (w3, v3)]

if st.button("🧮 计算最优方案"):
    max_value = knapsack(max_weight, items)
    st.success(f"在容量 {max_weight} 下，能获得的最大价值为：{max_value}")
    st.write("这是你亲手实现的背包算法在实际应用中的效果！")
