streamlit
google-generativeai

.env
__pycache__/

import streamlit as st
import google.generativeai as genai

# ==========================================
# 1. 初始化設定 (API Configuration)
# ==========================================
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"❌ 金鑰設定錯誤: {e}")
    st.stop()

# ==========================================
# 2. 頁面標題與說明 (UI Header)
# ==========================================
st.title("🚀 Gemini API 連線測試")
st.info("若能成功收到 AI 回覆，表示你的 GitHub 與 Secrets 環境配置正確！")

# ==========================================
# 3. 使用者輸入與互動 (User Interaction)
# ==========================================
user_input = st.text_input("輸入一段話測試連線 (例如: 你好):")

if user_input:
    with st.spinner("⏳ AI 正在回應中..."):
        try:
            # 呼叫 API
            response = model.generate_content(user_input)
            
            # ==========================================
            # 4. 顯示結果 (Display Results)
            # ==========================================
            st.subheader("🤖 AI 的回應:")
            st.write(response.text)
            st.success("✅ 連線成功!")
            
        except Exception as e:
            st.error(f"❌ 連線失敗: {e}")
