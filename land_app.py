import streamlit as st
import time

# 設定網頁分頁標籤與專業圖示
st.set_page_config(page_title="全國土地資產智慧分析平台", page_icon="🏛️", layout="wide")

# 自訂 CSS 樣式讓介面充滿機構感與科技感
st.markdown("""
<style>
/* 強制所有文字在任何模式下都是深藍色 */
html, body, [class*="css"], p, h1, h2, h3, h4, h5, h6, li, span, b, strong { color: #2C3E50 !important; }
.main-title { color: #2C3E50 !important; font-size: 32px; font-weight: bold; margin-bottom: 5px; }
.sub-title { color: #7F8C8D !important; font-size: 16px; margin-bottom: 25px; }
.card { background-color: #F8F9FA !important; padding: 20px; border-radius: 10px; border-left: 5px solid #2ECC71; margin-bottom: 20px; color: #2C3E50 !important; }
.alert-card { background-color: #FFF9E6 !important; padding: 20px; border-radius: 10px; border-left: 5px solid #F39C12; margin-bottom: 20px; color: #2C3E50 !important; }
.danger-card { background-color: #FDEDEC !important; padding: 20px; border-radius: 10px; border-left: 5px solid #E74C3C; margin-bottom: 20px; color: #2C3E50 !important; }
.pay-wall { background-color: #EBEDEF !important; padding: 25px; border-radius: 10px; border: 1px solid #AEB6BF; margin: 20px 0; color: #2C3E50 !important; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🏛️ 全國土地資產智慧分析平台</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">免費提供基礎地政與市場行情數據，將核心法規限制、複雜產權破解與專家處分策略列為加值服務。</p>', unsafe_allow_html=True)

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

if st.sidebar.button("🔍 開始進行 AI 潛力評估", type="primary"):
    st.session_state['analyzed'] = True
    if "富安段" not in section or "261" not in land_num:
        st.session_state['paid'] = False

if st.session_state.get('analyzed', False):
    if "富安段" in section and "261" in land_num:
        with st.spinner("🌍 正在安全連線內政部地籍圖資、實價登錄與國土計畫資料庫..."):
            time.sleep(0.8)
            
        st.success("🎉 報告基礎數據分析完成！")
        
        st.subheader("📋 土地基本現況與市場實價行情（免費公開）")
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("標的坐落", f"{city}{district}{section}")
        c2.metric("地號", f"{land_num} 地號")
        c3.metric("本案移轉面積", "21.78 坪")
        c4.metric("權利範圍 (持分)", "1/18")
        
        st.markdown("""
        <div class="card">
            <h4>📊 周邊土地實價登錄與市場行情摘要</h4>
            <p>經大數據比對本案周邊 500 公尺內、近兩年同性質之土地交易紀錄，分析結果如下：</p>
            <ul>
                <li><b>本案參考成交總價：</b> <span style="color:#E74C3C !important; font-size:18px; font-weight:bold;">561 萬元</span></li>
                <li><b>本案折算每坪單價：</b> <span style="color:#E74C3C !important; font-size:18px; font-weight:bold;">25.76 萬元 / 坪</span></li>
                <li><b>該區段市場整體區間：</b> 每坪約 24.5 萬 ~ 28.2 萬元，本案定價符合目前市場盤整行情。</li>
                <li><b>發展潛力備註：</b> 本區屬於<b>「社子島開發案」</b>預計徵收範圍，具備長期資產轉換潛力。</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        if pay_mode and not st.session_state['paid']:
            st.warning("🔒 核心法規限制與土地處分策略已被鎖定")
            
            st.markdown("""
            <div style="color: #2C3E50 !important;">
            <h3 style="color: #2C3E50 !important;">💡 您的土地符合開發行情，但謄本與產權中隱藏了關鍵地雷！</h3>
            <p style="color: #2C3E50 !important;">許多持分地主因看不懂法律術語、不熟處分程序而錯失變現良機，甚至誤踩法令盲區引發官司。支付 <b>NT$ 150 元</b> 立即解鎖 AI 開發專家的深度白話解析：</p>
            <ol style="color: #2C3E50 !important;">
                <li><b>法規障礙：</b> 為什麼名為「商業、住宅區」，現況卻連一間廁所都不能蓋？</li>
                <li><b>隱藏地雷：</b> 本案是否會被劃為「道路用地」？未來我的地會被變馬路嗎？</li>
                <li><b>多數決破局：</b> 有人想賣、有人不想賣？持分 1/18 該如何合法強行過戶變現？</li>
                <li><b>優購權陷阱：</b> 地上有別人的房子（地上物）？小心弄錯優先購買權順序，賣地反而被告！</li>
                <li><b>共有人擺爛：</b> 賣地後其他親戚裝死不收錢、拒接電話？如何利用「法院提存」合法免除後續爭議？</li>
            </ol>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="pay-wall">
                <h3 style="color: #2C3E50 !important;">🚀 立即解鎖完整「AI 土地價值防禦與處分策略報告」</h3>
                <p style="color: #E74C3C !important; font-size: 22px; font-weight: bold; margin: 5px 0;">限時解鎖價：NT$ 150 元</p>
                <p style="color: #566573 !important; font-size: 13px;">付費解鎖後即可觀看隱藏章節，並獲取專家一對一諮詢通道</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("💳 模擬小額付費解鎖"):
                st.session_state['paid'] = True
                st.rerun()
                
        else:
            if pay_mode and st.session_state['paid']:
                st.balloons()
                st.success("💰 支付成功！已解鎖由 20 年資深土開專家調教之 AI 深度報告：")
            
            st.subheader("🕵️‍♂️ AI 土地開發專家——深度法規與產權處分報告（已解鎖）")
            
            st.markdown("""
            <div class="card">
            <h3>📌 1. 使用分區的糖衣陷阱：細部計畫尚未完成</h3>
            <p><b>謄本原文：</b> 商業區、住宅區（細部計畫尚未完成，尚未能准許依變更後計畫用途使用）</p>
            <p><b>🧠 AI 白話翻譯：</b><br>
            這塊地未來確實是被劃在值錢的「商業區」和「住宅區」。但是，後面括號那句才是關鍵！<br>
            <b>「細部計畫尚未完成」</b>的意思是：政府大方向決定了，但具體細節（如馬路怎麼開、管線怎麼牽）都還沒定案。在細部計畫發布實施前，這塊地<b>完全被法令凍結，現況什麼都不能蓋</b>。這是一塊名義上的黃金，現況上的「素地期貨」。</p>
            </div>
            
            <div class="alert-card">
            <h3>⚠️ 2. 隱藏大雷：有一部分未來可能被變成人行道或馬路？</h3>
            <p><b>謄本原文：</b> 是否在道路用地(公共設施用地)應依建築線或俟地籍測量分割後，再確定。</p>
            <p><b>🧠 AI 白話翻譯：</b><br>
            這是目前<b>最大的不確定風險</b>。法令顯示這塊地有部分的範圍，未來很有可能會被劃成<b>「道路用地（公共設施）」</b>。<br>
            一旦變馬路，你就絕對不能蓋私人房屋。至於到底會被劃進去多少坪？現在必須等到未來政府拉出「建築線」或辦理「地籍分割」才能翻牌。在買賣談判時，這是土開團隊非常有力的砍價與談判籌碼。</p>
            </div>
            
            <div class="card">
            <h3>👥 3. 產權破局策略：親戚有人想賣、有人不想賣怎麼辦？</h3>
            <p><b>現況指標：</b> 本案權利範圍僅為持分 1/18</p>
            <p><b>🧠 AI 白話翻譯：</b><br>
            這代表這塊地被切成了 18 份，你人微言輕，一般民眾根本不敢買。但別擔心！根據<b>《土地法》第 34 條之一</b>，只要同意出賣的共有人人數與持分「雙雙過半」（或者出賣人的持分合計超過 2/3），<b>不需要全部親戚同意，就能合法將整塊土地整棟賣掉！</b> 不配合、反對的少數親戚，無法綁架您的資產處分權。</p>
            </div>

            <div class="danger-card">
            <h3>🚨 4. 優先購買權的隱形地雷：有地上物時的法律權利順序</h3>
            <p><b>實務風險：</b> 持分地若隨意轉售，未依法通知其他權利人，買賣將面臨撤銷或損害賠償官司。</p>
            <p><b>🧠 AI 白話翻譯：</b><br>
            當持分地有人要賣時，法律為了產權單純化，規定了極度嚴格的<b>「優先購買權」</b>。如果這塊持分地上有別人的房子（地上物），出賣時的優先順序是：<b>地上權人 ＞ 典權人 ＞ 租地建屋的承租人 ＞ 其他共有人</b>。<br>
            如果您在賣地前沒有依法發出存證信函通知這些順序在前的權利人，或者搞錯通知順序，不僅地政事務所會拒絕辦理過戶，您還可能面臨嚴重的法律損害賠償！這一步必須由專業土開團隊精準把關。</p>
            </div>

            <div class="card">
            <h3>🏦 5. 共有人擺爛裝死？利用「法院提存」合法安全變現</h3>
            <p><b>實務程序：</b> 通知後優購人逾期未回應，或反對共有人故意拒收買賣價金之處置。</p>
            <p><b>🧠 AI 白話翻譯：</b><br>
            當您成功利用多數決把土地賣掉後，那些當初極力反對、甚至擺爛裝死的親戚，如果故意拒接電話、不提供銀行帳號讓你匯款，該怎麼辦？<br>
            不用擔心！我們會協助您將那些反對親戚應得的買賣價金，依法<b>「提存到法院」</b>。只要款項成功進入法院的提存所，在法律上就等同於親戚已經收下這筆錢。此時，您就能合法、安全地走完過戶流程，徹底免除未來的產權糾紛，安心拿到您應得的變現金流！</p>
            </div>

            <div style="background-color: #E8F8F5 !important; padding: 25px; border-radius: 10px; border: 2px dashed #2ECC71; margin-top: 30px;">
            <h3 style="color: #117864 !important; margin-top:0;">🚀 專家最終處分建議與一對一媒合</h3>
            <p style="color: #2C3E50 !important;">產權零碎、家族意見不合、又有地上物牽扯的持分土地，放著只會一代傳一代越來越難處理。如果您想了解本案在未來區段徵收預估能配回多少坪建地，或是希望由專業土開團隊協助啟動「土地法34-1多數決處分與法院提存程序」，歡迎直接與我們聯絡。</p>
            <br>
            <div style="text-align: center;">
                <p style="font-weight: bold; font-size: 16px; color: #2C3E50 !important;">💡 想要安全合法破解複雜祖產、媒合現成買方變現？</p>
                <a href="https://line.me" target="_blank"><button style="background-color: #2ECC71 !important; color: white !important; border: none; padding: 14px 28px; border-radius: 8px; font-size: 16px; cursor: pointer; font-weight: bold;">📞 點我立即與「線上專業土地開發師」免費一對一諮詢</button></a>
                <p style="color: #7F8C8D !important; font-size: 12px; margin-top: 10px;">（此按鈕可直接導流到您的 LINE、電話或留單系統，為您本業捕捉精準客戶！）</p>
            </div>
            </div>
            """, unsafe_allow_html=True)
            
    else:
        st.error("💡 目前為測試版本，為了展示最完美的 AI 轉譯效果，請在左側輸入範例資料：地段請包含「富安段」，地號請輸入「261」。")
