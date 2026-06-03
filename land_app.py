import streamlit as st
import time

st.set_page_config(page_title="全國土地資產智慧分析平台 | 專家免費估價", page_icon="📈", layout="centered")

# 📰 財經新聞雜誌風 CSS 
st.markdown("""
<style>
[data-testid="stAppViewContainer"] { background-color: #F8F9FA !important; }
[data-testid="stHeader"] { background-color: #F8F9FA !important; }
.stMarkdown p, .stMarkdown span, .stMarkdown li, label, div { color: #222222 !important; }

/* 財訊經典紅標題 */
.main-title { 
    color: #CC0000 !important; 
    font-size: 36px; 
    font-weight: 900; 
    margin-bottom: 10px; 
    border-bottom: 4px solid #CC0000; 
    padding-bottom: 10px;
    letter-spacing: 1px;
}
.sub-title { 
    font-size: 16px; 
    margin-bottom: 30px; 
    color: #333333 !important; 
    font-weight: bold;
    line-height: 1.6; 
    background-color: #FFF0F0;
    padding: 15px;
    border-left: 5px solid #CC0000;
}

/* 報紙專欄方塊感 */
.card { 
    background-color: #FFFFFF !important; 
    padding: 30px; 
    border-radius: 4px; 
    border: 1px solid #E0E0E0;
    border-top: 5px solid #CC0000;
    margin-top: 20px; 
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
}
.card h3 { color: #CC0000 !important; font-size: 24px; font-weight: 900; margin-top:0; border-bottom: 1px dashed #E0E0E0; padding-bottom: 10px;}
.card p, .card li { color: #222222 !important; font-size: 16px; line-height: 1.8; }
.card b { color: #000000 !important; }

/* 表單區塊強制白底與邊框 */
div[data-baseweb="input"] > div { background-color: #FFFFFF !important; border: 1px solid #CCCCCC !important;}
div[data-baseweb="select"] > div { background-color: #FFFFFF !important; border: 1px solid #CCCCCC !important;}
textarea { background-color: #FFFFFF !important; border: 1px solid #CCCCCC !important; color: #222222 !important;}

/* 衝動型行動按鈕 (亮眼黃) */
div.stButton > button {
    background-color: #FFEB3B !important;
    color: #CC0000 !important;
    border: 2px solid #FBC02D !important;
    width: 100% !important;
    padding: 20px 0 !important;
    border-radius: 4px !important;
    font-size: 22px !important;
    font-weight: 900 !important;
    cursor: pointer;
    box-shadow: 0 4px 0px #FBC02D !important;
    transition: all 0.2s ease !important;
}
div.stButton > button:hover {
    background-color: #FFF176 !important;
    transform: translateY(2px);
    box-shadow: 0 2px 0px #FBC02D !important;
}
div.stButton > button p {
    color: #CC0000 !important;
    font-size: 22px !important;
    font-weight: 900 !important;
    margin: 0 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">📈 權威土地資產變現團隊：專屬人工精準估價</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">系統自動估價往往因「地形、法定空地、法規盲區」而嚴重失準。請留下您的土地基本資料，我們的資深土開法務團隊將親自為您調閱真實地籍圖資，進行【免費且最精準的變現評估】。</p>', unsafe_allow_html=True)

# 使用 st.form 確保使用者填完所有資料才送出
with st.form("lead_gen_form"):
    st.subheader("📍 1. 土地基本資料")
    c1, c2 = st.columns(2)
    city = c1.selectbox("縣市", ["台北市", "新北市", "桃園市", "台中市", "台南市", "高雄市", "其他"])
    district = c2.text_input("鄉鎮市區 (如：士林區)")
    
    c3, c4 = st.columns(2)
    section = c3.text_input("地段 (如：富安段)")
    land_num = c4.text_input("地號 (如：261)")

    st.markdown("---")
    st.subheader("📋 2. 產權現況補充 (選填)")
    c5, c6 = st.columns(2)
    holding_numerator = c5.number_input("您的持分 (分子)", min_value=1, value=1)
    holding_denominator = c6.number_input("您的持分 (分母)", min_value=1, value=18)
    
    note = st.text_area("您目前遇到的困難或變現期望？", placeholder="例如：親戚不配合出售、想了解是否會被徵收、急需資金等...")

    st.markdown("---")
    st.subheader("📞 3. 聯絡方式 (分析報告接收窗口)")
    c7, c8 = st.columns(2)
    contact_name = c7.text_input("您的稱呼 (必填，如：陳先生)")
    contact_phone = c8.text_input("聯絡電話 或 LINE ID (必填)")

    # 提交按鈕
    submit = st.form_submit_button("🚀 送出資料，申請專家免費鑑價")

# 提交後的邏輯處理
if submit:
    if not contact_name or not contact_phone:
        st.error("⚠️ 提醒您：請務必填寫「您的稱呼」與「聯絡方式」，以便專家將分析報告回傳給您！")
    else:
        # 模擬資料傳輸的等待時間
        with st.spinner("🔒 資料加密傳送至專家後台..."):
            time.sleep(1.5)
            
        st.success(f"🎉 申請成功！感謝您對本團隊的信任，{contact_name}。")
        
        st.markdown("""
        <div class="card">
        <h3>✅ 您的案件已進入專家審查流程</h3>
        <p>我們的資深土地開發團隊將會在 <b>24 小時內</b> 進行以下專業作業：</p>
        <ul>
            <li><b>圖資調閱：</b> 調閱內政部真實地籍圖與土地登記謄本。</li>
            <li><b>法規排除：</b> 比對最新都市計畫，確認是否有道路徵收或禁建風險。</li>
            <li><b>變現策略：</b> 針對您的持分現況，評估最佳的《土地法34-1條》或持分收購變現途徑。</li>
        </ul>
        <p style="background-color:#FFEBEE; padding:10px; border-radius:4px; font-weight:bold; color:#B71C1C;">
        📩 報告完成後，我們將透過您留下的聯絡方式優先與您聯繫。請保持手機暢通，或留意 LINE 訊息！
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.balloons()
