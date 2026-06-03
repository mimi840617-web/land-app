import streamlit as st
import time

# 設定網頁分頁標籤與圖示 
st.set_page_config(page_title="全國土地資產智慧分析平台", page_icon="📈", layout="wide")

# 📰 財經新聞雜誌風 + 強制白底 CSS (已修復所有黑底字/隱形字問題)
st.markdown("""
<style>
/* 🌟 強制整個網站變成白底/淺灰底，無視手機的深色模式 🌟 */
[data-testid="stAppViewContainer"] { background-color: #F8F9FA !important; }
[data-testid="stHeader"] { background-color: #F8F9FA !important; }
[data-testid="stSidebar"] { background-color: #FFFFFF !important; }

/* 強制所有一般文字為深黑色 */
.stMarkdown p, .stMarkdown span, .stMarkdown li, label, div { color: #222222 !important; }

/* ⬇️ 終極修復：針對左側輸入框與下拉選單強制白底黑字 ⬇️ */
div[data-baseweb="select"] > div { background-color: #FFFFFF !important; color: #222222 !important; border: 1px solid #CCCCCC !important; }
div[data-baseweb="select"] span { color: #222222 !important; }
/* 修正下拉選單中「選中的字」 */
div[data-baseweb="select"] div[class*="singleValue"] { color: #222222 !important; } 

div[data-baseweb="base-input"] > input { background-color: #FFFFFF !important; color: #222222 !important; -webkit-text-fill-color: #222222 !important; }
div[data-baseweb="popover"] { background-color: #FFFFFF !important; }
ul[data-baseweb="menu"] { background-color: #FFFFFF !important; }
li[role="option"] { color: #222222 !important; background-color: #FFFFFF !important; }
li[role="option"]:hover { background-color: #F0F0F0 !important; }

/* 修正勾選框文字 */
label[data-baseweb="checkbox"] div { color: #222222 !important; }
/* 修正側邊欄的標題字 (1. 輸入土地基本資料 等) */
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 { color: #CC0000 !important; }
/* ⬆️ 終極修復結束 ⬆️ */

/* 財訊經典紅標題 */
.main-title { 
    color: #CC0000 !important; 
    font-size: 36px; 
    font-weight: 900; 
    margin-bottom: 15px; 
    border-bottom: 4px solid #CC0000; 
    padding-bottom: 10px;
    letter-spacing: 1px;
}
.sub-title { 
    font-size: 18px; 
    margin-bottom: 25px; 
    color: #111111 !important; 
    font-weight: bold;
    line-height: 1.6; 
}

/* 報紙專欄方塊感 (銳利邊角、鮮明紅頂線) */
.card { 
    background-color: #FFFFFF !important; 
    padding: 24px; 
    border-radius: 2px; 
    border: 1px solid #E0E0E0;
    border-top: 5px solid #CC0000;
    margin-bottom: 20px; 
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
.card h3 { color: #CC0000 !important; font-size: 22px; font-weight: 900; margin-top:0; }
.card p, .card li { color: #222222 !important; font-size: 16px; line-height: 1.8; }
.card b { color: #000000 !important; }

/* 警示卡片 (鮮明紅底) */
.alert-card { 
    background-color: #FFF0F0 !important; 
    padding: 24px; 
    border-radius: 2px; 
    border-left: 6px solid #E53935; 
    margin-bottom: 20px; 
}
.alert-card h3 { color: #B71C1C !important; font-size: 22px; font-weight: 900; margin-top:0; }
.alert-card p, .alert-card b { color: #B71C1C !important; font-size: 16px; line-height: 1.8;}

/* 強烈警告卡片 (黑底紅字，極度吸睛) */
.danger-card { 
    background-color: #212121 !important; 
    padding: 24px; 
    border-radius: 2px; 
    border-left: 6px solid #F44336; 
    margin-bottom: 20px; 
}
.danger-card h3 { color: #FFCDD2 !important; font-size: 22px; font-weight: 900; margin-top:0; }
.danger-card p, .danger-card b { color: #FFFFFF !important; font-size: 16px; line-height: 1.8;}

/* 獨家報導解鎖牆 (雜誌訂閱感) */
.pay-wall { 
    background-color: #FAFAFA !important; 
    padding: 30px; 
    border-radius: 2px; 
    border: 2px dashed #CC0000; 
    margin: 25px 0; 
    text-align: center; 
}
.pay-wall h3 { color: #CC0000 !important; font-size: 26px; font-weight: 900; margin-bottom: 10px; background-color: #FFEBEE; display: inline-block; padding: 5px 15px;}
.pay-wall p { color: #333333 !important; font-size: 16px; font-weight: bold;}

/* 底部專案導流卡 (財訊經典紅底黃字) */
.cta-card {
    background-color: #CC0000 !important;
    padding: 40px;
    border-radius: 2px;
    margin-top: 40px;
    text-align: center;
    border: 4px solid #8B0000;
}
.cta-card h3 { color: #FFFFFF !important; margin-top:0; font-size: 26px; font-weight: 900; }
.cta-card p { color: #FFEBEE !important; font-size: 16px; line-height: 1.8;}

/* 衝動型行動按鈕 (亮眼黃) */
.btn-news {
    background-color: #FFEB3B !important;
    color: #CC0000 !important;
    border: none;
    padding: 16px 36px;
    border-radius: 4px;
    font-size: 20px;
    font-weight: 900;
    cursor: pointer;
    text-decoration: none;
    display: inline-block;
    margin-top: 20px;
    box-shadow: 0 4px 0px #FBC02D;
    transition: all 0.2s ease;
}
.btn-news:active {
    transform: translateY(4px);
    box-shadow: 0 0px 0px #FBC02D;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">📈【獨家分析】全國持分土地變現測算</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">輸入地號，系統將結合內政部大數據與法規盲區，為您產出最具權威性的「資產變現與防禦報告」！</p>', unsafe_allow_html=True)

# 側邊欄輸入設定
st.sidebar.header("📍 1. 輸入土地基本資料")
city = st.sidebar.selectbox("縣市", ["台北市", "新北市", "桃園市", "其他"])
district = st.sidebar.selectbox("鄉鎮市區", ["士林區", "北投區", "內湖區", "其他"])
section = st.sidebar.text_input("地段", value="富安段二小段")
land_num = st.sidebar.text_input("地號", value="261")

st.sidebar.markdown("---")
st.sidebar.header("⚙️ 2. 微型服務商業模式")
pay_mode = st.sidebar.checkbox("開啟「付費 150 元解鎖完整報告」功能", value=True)

if 'paid' not in st.session_state:
    st.session_state['paid'] = False

if st.sidebar.button("🔍 立即測算本案價值", type="primary"):
    st.session_state['analyzed'] = True
    if "富安段" not in section or "261" not in land_num:
        st.session_state['paid'] = False

if st.session_state.get('analyzed', False):
    if "富安段" in section and "261" in land_num:
        with st.spinner("🌍 系統正連線內政部實價登錄大數據..."):
            time.sleep(0.8)
            
        st.success("🎉 行情數據檢索完成！")
        
        st.subheader("📋 標的現況與市場實價行情（免費公開）")
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("標的坐落", f"{city}{district}{section}")
        c2.metric("地號", f"{land_num} 地號")
        c3.metric("本案移轉面積", "21.78 坪")
        c4.metric("權利範圍 (持分)", "1/18")
        
        st.markdown("""
        <div class="card">
            <h4 style="color: #000000 !important; font-weight: 900;">📊 周邊實價登錄大數據分析</h4>
            <p>經系統比對本案周邊 500 公尺內、近兩年同性質之土地交易紀錄，評估結果如下：</p>
            <ul>
                <li><b>本案參考成交總價：</b> <span style="color:#CC0000 !important; font-size:22px; font-weight:900;">561 萬元</span></li>
                <li><b>本案折算每坪單價：</b> <span style="color:#CC0000 !important; font-size:22px; font-weight:900;">25.76 萬元 / 坪</span></li>
                <li><b>該區段市場整體區間：</b> 每坪約 24.5 萬 ~ 28.2 萬元，符合目前市場盤整行情。</li>
                <li><b>變現潛力備註：</b> 本區屬於<b>「社子島開發案」</b>預計徵收範圍，長線具備絕佳資金效益。</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        if pay_mode and not st.session_state['paid']:
            
            st.markdown("""
            <div style="padding: 10px 0;">
            <h3 style="color: #CC0000 !important; font-weight: 900; font-size: 24px;">⛔ 警告：您的資產價值達 561 萬，但隱藏 3 大產權地雷！</h3>
            <p style="color: #111111 !important; font-size: 16px; font-weight: bold;">多數持分地主因缺乏地政與法規常識，錯失變現良機或陷入家族官司。支付 <b>NT$ 150 元</b> 立即解鎖專屬【變現與防禦深度報告】：</p>
            <ul style="color: #333333 !important; font-size: 16px; line-height: 1.8;">
                <li><b>1. 法規障礙：</b> 名為「商業區」，為何現況連一間廁所都不能蓋？</li>
                <li><b>2. 隱藏地雷：</b> 本案未來會被政府強迫劃為「馬路」嗎？</li>
                <li><b>3. 邊緣人破局：</b> 持分僅 1/18，親戚不配合，如何單獨強勢變現？</li>
                <li><b>4. 賣地防身術：</b> 賣地未依法通知優先購買權人，小心面臨天價索賠！</li>
                <li><b>5. 破解情緒勒索：</b> 親戚拒絕收錢？教您使用「法院提存」合法入袋。</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="pay-wall">
                <h3>🔓 立即解鎖【獨家持分變現報告】</h3>
                <p style="color: #CC0000 !important; font-size: 28px; font-weight: 900; margin: 10px 0;">限時查閱價：NT$ 150</p>
                <p style="color: #555555 !important; font-size: 14px;">(解鎖後即享完整專家解析，並開通免費顧問諮詢權限)</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("💳 立即付款解鎖 (支援 LINE Pay / 信用卡)"):
                st.session_state['paid'] = True
                st.rerun()
                
        else:
            if pay_mode and st.session_state['paid']:
                st.balloons()
                st.success("💰 付款成功！已為您開通深度報告閱覽權限：")
            
            st.subheader("🕵️‍♂️ 專家獨家揭密：持分地變現與防禦策略（已解鎖）")
            
            st.markdown("""
            <div class="card">
            <h3>📌 1. 商業區的糖衣陷阱</h3>
            <p><b>產權調閱：</b> 商業區、住宅區（細部計畫尚未完成，尚未能准許依變更後計畫用途使用）</p>
            <p><b>【專家深度解析】</b><br>
            您的地段未來確實是高價值的「商業/住宅區」。但在政府將具體細節（如道路、管線）定案前，這塊地<b>完全被法令凍結，現況禁止任何開發</b>。這猶如一張「素地期貨」，此時出售即是將未來的增值潛力提前套現，規避漫長等待的風險。</p>
            </div>
            
            <div class="alert-card">
            <h3>⚠️ 2. 道路用地徵收風險</h3>
            <p><b>產權調閱：</b> 是否在道路用地(公共設施用地)應依建築線或俟地籍測量分割後，再確定。</p>
            <p><b>【專家深度解析】</b><br>
            系統偵測到此地段有部分範圍，未來極可能被劃為<b>「道路用地（公共設施）」</b>。一旦成為道路，將喪失建築價值。在市場買賣談判時，這往往是買方大幅砍價的致命點，必須依靠專業團隊進行估價防禦。</p>
            </div>
            
            <div class="card">
            <h3>👥 3. 產權破局：甩開少數反對者</h3>
            <p><b>現況指標：</b> 本案權利範圍僅為持分 1/18</p>
            <p><b>【專家深度解析】</b><br>
            持分極度零碎，一般市場買家拒絕承接。但實務上可利用<b>《土地法》第 34 條之一</b>：只要同意出售的共有人人數與持分「雙過半」，即可<b>合法將整塊土地強制處分</b>。您無須再受少數不配合的親戚牽制，掌握主動變現權。</p>
            </div>

            <div class="danger-card">
            <h3>🚨 4. 優先購買權：勿踩損害賠償地雷</h3>
            <p><b>實務風險：</b> 持分地若隨意轉售，未依法通知其他權利人，買賣將面臨撤銷或賠償。</p>
            <p><b>【專家深度解析】</b><br>
            法律明訂極度嚴格的<b>「優先購買權」</b>。若地上有他人建物，出賣的法定優先順序為：<b>地上權人 ＞ 典權人 ＞ 租地建屋承租人 ＞ 其他共有人</b>。<br>
            若未依法發出存證信函通知正確的順位人，地政機關將退件不予過戶，賣方更可能面臨官司索賠！程序必須滴水不漏。</p>
            </div>

            <div class="card">
            <h3>🏦 5. 法院提存：破解親戚拒收價金</h3>
            <p><b>實務程序：</b> 面對反對共有人故意拒收買賣價金之處置。</p>
            <p><b>【專家深度解析】</b><br>
            若成功售出土地，但反對的親戚故意拒接電話、拒絕提供銀行帳號，企圖阻撓過戶怎麼辦？<br>
            實務上，我們可將該親戚應得之價金，依法<b>「提存至法院」</b>。一旦款項進入法院提存所，法律上視同對方已收受。您即可合法、安全地完成過戶，將屬於您的現金安穩落袋！</p>
            </div>

            <div class="cta-card">
            <h3>啟動您的資產變現計畫</h3>
            <p>零碎、帶有糾紛的持分祖產，只會隨著繼承世代越切越碎，最終淪為死資產。<br>
            如果您想得知本案 <span style="color:#FFEB3B; font-weight:bold;">當前的直接收購價</span>，或是委託專業團隊為您啟動 <span style="color:#FFEB3B; font-weight:bold;">土地法34-1 與 法院提存程序</span>...</p>
            <a href="https://line.me" target="_blank" class="btn-news">專人一對一免費鑑價與諮詢 ➔</a>
            <p style="font-size: 13px; margin-top: 15px; color:#FFCDD2 !important;">(本平台由資深土地開發法務團隊營運・全程保密)</p>
            </div>
            """, unsafe_allow_html=True)
            
    else:
        st.error("💡 目前為測試版本，請在左側輸入範例資料：地段請包含「富安段」，地號請輸入「261」。")
