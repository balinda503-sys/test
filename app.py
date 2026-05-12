streamlit
google-generativeai

.env
__pycache__/

import streamlit as st
import google.generativeai as genai

# --- 1. 設定頁面基本資訊 ---
st.set_page_config(page_title="Gemini 連線測試", layout="centered")

# --- 2. 初始化 API 連線 ---
def init_gemini():
    try:
        # 從後台 Secrets 讀取金鑰
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        return genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"金鑰設定錯誤: {e}")
        st.stop()

model = init_gemini()

# --- 3. 側邊欄與標題 ---
st.title("🚀 Gemini API 連線測試")
st.info("若能成功收到 AI 回覆，表示你的 GitHub 與 Secrets 環境配置正確！")

with st.sidebar:
    st.header("環境狀態")
    st.success("API 金鑰已載入")
    st.write("模型版本: gemini-1.5-flash")

# --- 4. 互動介面與邏輯 ---
user_input = st.text_input("輸入一段話測試連線 (例如: 你好):")

if user_input:
    with st.spinner("AI 正在回應中..."):
        try:
            # 呼叫 API
            response = model.generate_content(user_input)
            
            # 顯示結果
            st.divider()  # 分隔線
            st.subheader("🤖 AI 的回應:")
            st.write(response.text)
            st.success("連線成功!")
            
        except Exception as e:
            st.error(f"連線失敗，請檢查 API 配額或網路連線: {e}")
