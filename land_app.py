import streamlit as st
import time

# 設定網頁分頁標籤與圖示
st.set_page_config(page_title="全國土地資產智慧分析平台", page_icon="💰", layout="wide")

# 💎 全新 Fintech 數位理財風 CSS
st.markdown("""
<style>
/* 移除強制全域深藍色的設定，讓 Streamlit 自動適配深淺色模式 */
.main-title { font-size: 34px; font-weight: 900; margin-bottom: 5px; letter-spacing: -0.5px; }
.sub-title { font-size: 16px; margin-bottom: 25px; color: #64748B; line-height: 1.6; }

/* 現代感浮雕白卡片 */
.card { 
    background-color: #FFFFFF !important; 
    padding: 24px; 
    border-radius: 16px; 
    box-shadow: 0 4px 24px rgba(0,0,0,0.06); 
    border: 1px solid #F1F5F9;
    margin-bottom: 20px; 
}
.card h3 { color: #0F172A !important; font-size: 20px; font-weight: 800; border-bottom: 2px solid #F59E0B; padding-bottom: 10px; margin-top:0; }
.card p, .card li { color: #334155 !important; font-size: 15.5px; line-height: 1.7; }
.card b { color: #0F172A !important; }

/* 警示卡片 (柔和微距橘) */
.alert-card { 
    background-color: #FFFBEB !important; 
    padding: 24px; 
    border-radius: 16px; 
    border-left: 6px solid #F59E0B; 
    box-shadow: 0 4px 20px rgba(0,0,0,0.04); 
    margin-bottom: 20px; 
}
.alert-card h3 { color: #92400E !important; font-size: 20px; font-weight: 800; margin-top:0; }
.alert-card p, .alert-card b { color: #92400E !important; }

/* 危險卡片 (柔和微距紅) */
.danger-card { 
    background-color: #FEF2F2 !important; 
    padding: 24px; 
    border-radius: 16px; 
    border-left: 6px solid #EF4444; 
    box-shadow: 0 4px 20px rgba(0,0,0,0.04); 
    margin-bottom: 20px; 
}
.danger-card h3 { color: #991B1B !important; font-size: 20px; font-weight: 800; margin-top:0; }
.danger-card p, .danger-card b { color: #991B1B !important; }

/* 財富解鎖牆 (漸層微金) */
.pay-wall { 
    background: linear-gradient(135deg, #FFF8E1 0%, #FFECB3 100%) !important; 
    padding: 30px; 
    border-radius: 16px; 
    border: 1px solid #FFE082; 
    margin: 20px 0; 
    text-align: center; 
    box-shadow: 0 8px 24px rgba(245, 158, 11, 0.15);
}
.pay-wall h3 { color: #B9770E !important; font-size: 22px; font-weight: 900; margin-bottom: 10px; }
.pay-wall p { color: #566573 !important; }

/* 底部尊榮顧問卡 (深邃藍) */
.cta-card {
    background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%) !important;
    padding: 35px;
    border-radius: 16px;
    margin-top: 40px;
    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.3);
}
.cta-card h3 { color: #FFFFFF !important; margin-top:0; font-size: 22px; font-weight: 800; text-align: center;}
.cta-card p { color: #94A3B8 !important; text-align: center; line-height: 1.7;}
.highlight-text { color: #F8FAFC !important; font-weight: bold; font-size: 17px;}

/* 漸層高光按鈕 */
.btn-gold {
    background: linear-gradient(90deg, #F59E0B 0%, #F97316 100%);
    color: white !important;
    border: none;
    padding: 16px 32px;
    border-radius: 50px;
    font-size: 18px;
    font-weight: 900;
    cursor: pointer;
    box-shadow: 0 6px 20px rgba(249, 115, 22, 0.4);
    text-decoration: none;
    display: inline-block;
    margin-top: 15px;
    transition: all 0.3s ease;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">✨ 全國持分土地變現測算雷達</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">輸入地號，立刻分析您的持分碎地價值！結合大數據行情與產權法規，為您找出最安全、最快速的現金落袋方案。</p>', unsafe_allow_html=True)

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

if st.sidebar.button("🔍 立即測算我的土地價值", type="primary"):
    st.session_state['analyzed'] = True
    if "富安段" not in section or "261" not in land_num:
        st.session_state['paid'] = False

if st.session_state.get('analyzed', False):
    if "富安段" in section and "261" in land_num:
        with st.spinner("🌍 正在安全連線內政部實價登錄大數據..."):
            time.sleep(0.8)
            
        st.success("🎉 初步行情數據分析完成！")
        
        st.subheader("📋 您的資產現況與市場實價行情（免費公開）")
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("標的坐落", f"{city}{district}{section}")
        c2.metric("地號", f"{land_num} 地號")
        c3.metric("本案移轉面積", "21.78 坪")
        c4.metric("權利範圍 (持分)", "1/18")
        
        st.markdown("""
        <div class="card">
            <h4 style="color: #0F172A !important; font-weight: bold;">📊 周邊實價登錄行情摘要</h4>
            <p>經大數據比對本案周邊 500 公尺內、近兩年同性質之土地交易紀錄，為您的資產粗估如下：</p>
            <ul>
                <li><b>本案參考成交總價：</b> <span style="color:#EA580C !important; font-size:20px; font-weight:900;">561 萬元</span></li>
                <li><b>本案折算每坪單價：</b> <span style="color:#EA580C !important; font-size:20px; font-weight:900;">25.76 萬元 / 坪</span></li>
                <li><b>該區段市場整體區間：</b> 每坪約 24.5 萬 ~ 28.2 萬元，符合目前市場盤整行情。</li>
                <li><b>變現潛力備註：</b> 本區屬於<b>「社子島開發案」</b>預計徵收範圍，具備絕佳的現金轉換潛力。</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        if pay_mode and not st.session_state['paid']:
            
            st.markdown("""
            <div style="padding: 10px 0;">
            <h3 style="color: #0F172A !important; font-weight: 900;">💡 您的資產價值 561 萬，但小心 3 個產權地雷讓您領不到錢！</h3>
            <p style="color: #475569 !important; font-size: 16px;">許多持分小地主因為看不懂地政術語，遇到親戚刁難或不懂法規，錯失變現良機。支付 <b>NT$ 150 元</b> 立即解鎖您的專屬變現策略報告：</p>
            <ul style="color: #475569 !important; font-size: 15px; line-height: 1.8;">
                <li><b>1. 法規障礙：</b> 為什麼名為「商業區」，現況卻連一間廁所都不能蓋？</li>
                <li><b>2. 隱藏地雷：</b> 我的地未來會被政府強迫變馬路嗎？</li>
                <li><b>3. 邊緣人破局：</b> 持分只有 1/18，親戚不理我，該怎麼自己把錢拿回來？</li>
                <li><b>4. 賣地防身術：</b> 地上有別人的房子？小心賣地沒通知對的人，反而被告上法院！</li>
                <li><b>5. 拒絕親戚情緒勒索：</b> 親戚裝死不收錢？教您用「法院提存」合法拿到現金。</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="pay-wall">
                <h3>🚀 立即解鎖完整「持分變現與法規防禦報告」</h3>
                <p style="color: #D97706 !important; font-size: 26px; font-weight: 900; margin: 5px 0;">限時解鎖價：NT$ 150</p>
                <p style="color: #78909C !important; font-size: 14px;">(解鎖後即可觀看隱藏章節，並開啟專家免費諮詢通道)</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("💳 模擬小額付費解鎖 (Apple Pay / LINE Pay)"):
                st.session_state['paid'] = True
                st.rerun()
                
        else:
            if pay_mode and st.session_state['paid']:
                st.balloons()
                st.success("💰 付款成功！已為您解鎖專屬的產權變現報告：")
            
            st.subheader("🕵️‍♂️ 您的專屬持分地變現與防禦策略（已解鎖）")
            
            st.markdown("""
            <div class="card">
            <h3>📌 1. 使用分區的糖衣：現在什麼都不能蓋</h3>
            <p><b>謄本原文：</b> 商業區、住宅區（細部計畫尚未完成，尚未能准許依變更後計畫用途使用）</p>
            <p><b>💡 變現翻譯蒟蒻：</b><br>
            您的地未來確實是值錢的「商業區」和「住宅區」。但在政府把具體細節（馬路、管線）定案前，這塊地<b>完全被法令凍結，現況不能蓋任何東西</b>。這就像是一張「素地期貨」，現在賣出，就是把未來的增值潛力套現。</p>
            </div>
            
            <div class="alert-card">
            <h3>⚠️ 2. 隱藏大雷：有一部分未來可能被變成馬路</h3>
            <p><b>謄本原文：</b> 是否在道路用地(公共設施用地)應依建築線或俟地籍測量分割後，再確定。</p>
            <p><b>💡 變現翻譯蒟蒻：</b><br>
            法令顯示這塊地有部分範圍，未來很有可能會被劃成<b>「道路用地（公共設施）」</b>。一旦變馬路，就絕對不能蓋私人房屋。在談買賣時，這會是買方強烈砍價的藉口，需要透過專業談判來守住價格。</p>
            </div>
            
            <div class="card">
            <h3>👥 3. 產權破局策略：親戚不想賣怎麼辦？</h3>
            <p><b>現況指標：</b> 本案權利範圍僅為持分 1/18</p>
            <p><b>💡 變現翻譯蒟蒻：</b><br>
            這代表這塊地被切成了 18 份，一般民眾根本不敢買。但別擔心！根據<b>《土地法》第 34 條之一</b>，只要同意出賣的共有人人數與持分「雙雙過半」，<b>不需要全部親戚同意，就能合法將整塊土地賣掉！</b> 您不用再被少數親戚的情緒勒索綁架。</p>
            </div>

            <div class="danger-card">
            <h3>🚨 4. 優先購買權的隱形地雷：有地上物時的法律順序</h3>
            <p><b>實務風險：</b> 持分地若隨意轉售，未依法通知其他權利人，買賣將面臨撤銷或損害賠償。</p>
            <p><b>💡 變現翻譯蒟蒻：</b><br>
            當持分地有人要賣時，法律規定了極度嚴格的<b>「優先購買權」</b>。如果這塊持分地上有別人的房子，出賣時的優先順序是：<b>地上權人 ＞ 典權人 ＞ 租地建屋的承租人 ＞ 其他共有人</b>。<br>
            如果您賣地前沒有發存證信函通知對的人，地政事務所不僅會拒絕過戶，您還可能面臨嚴重的賠償官司！這一步非常需要專人替您把關。</p>
            </div>

            <div class="card">
            <h3>🏦 5. 親戚擺爛裝死？利用「法院提存」安全變現</h3>
            <p><b>實務程序：</b> 通知後優購人逾期未回應，或反對共有人故意拒收買賣價金之處置。</p>
            <p><b>💡 變現翻譯蒟蒻：</b><br>
            當您成功把土地賣掉後，那些極力反對、甚至擺爛裝死的親戚，如果故意拒接電話、不給你銀行帳號匯款怎麼辦？<br>
            很簡單！我們可以將反對親戚應得的錢，依法<b>「提存到法院」</b>。只要錢進了法院，法律上就等同於親戚已經收下。您就能合法、安全地走完過戶流程，安心把您那 1/18 的現金放進口袋！</p>
            </div>

            <div class="cta-card">
            <h3>🚀 把複雜的祖產，變成看得到的現金</h3>
            <p>產權零碎、家族意見不合的持分土地，放著只會一代傳一代，越來越不值錢。<br>
            如果您想知道這塊地 <span class="highlight-text">現在直接賣能拿多少現金</span>，或是希望由專業團隊幫您啟動 <span class="highlight-text">土地法34-1 與 法院提存程序</span>，甩開親戚糾紛...</p>
            <a href="https://line.me" target="_blank" class="btn-gold">💬 點我與「持分資產顧問」免費一對一諮詢</a>
            <p style="font-size: 12px; margin-top: 15px; opacity: 0.7;">(全程保密・免費評估變現方案)</p>
            </div>
            """, unsafe_allow_html=True)
            
    else:
        st.error("💡 目前為測試版本，請在左側輸入範例資料：地段請包含「富安段」，地號請輸入「261」。")
