import streamlit as st
import time

st.set_page_config(page_title="全國土地資產智慧分析平台", page_icon="🏛️", layout="wide")

# 自訂 CSS 樣式：暖色系科技專業風格
st.markdown("""
<style>
/* 整體背景與主要文字 */
.main-title { color: #D35400; font-size: 34px; font-weight: 800; margin-bottom: 5px; text-shadow: 1px 1px 2px rgba(0,0,0,0.1); }
.sub-title { color: #7F8C8D; font-size: 16px; margin-bottom: 25px; border-bottom: 2px solid #F39C12; padding-bottom: 10px; }

/* 基礎數據卡片 (科技感微暖) */
.card { background: linear-gradient(145deg, #FFF9F2, #FFF3E0); padding: 22px; border-radius: 12px; border-left: 6px solid #F39C12; margin-bottom: 22px; color: #2C3E50 !important; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
.card h3, .card h4, .card p, .card b { color: #34495E !important; }

/* 警告/地雷卡片 (警示紅黃) */
.alert-card { background: linear-gradient(145deg, #FDEDEC, #FADBD8); padding: 22px; border-radius: 12px; border-left: 6px solid #E74C3C; margin-bottom: 22px; color: #2C3E50 !important; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
.alert-card h3 { color: #C0392B !important; }
.alert-card p, .alert-card b { color: #34495E !important; }

/* 付費牆區塊 (專業灰橘) */
.pay-wall { background-color: #F8F9F9; padding: 30px; border-radius: 15px; border: 2px solid #E59866; margin: 25px 0; color: #2C3E50 !important; text-align: center; box-shadow: 0 8px 15px rgba(230, 126, 34, 0.15); }
.pay-wall h3 { color: #D35400 !important; font-weight: 700; }

/* 修正深色模式文字隱形 */
.stMarkdown p { color: inherit; } 
div[data-testid="stMarkdownContainer"] > p { color: inherit; }
.unlock-desc { color: #F2F3F4 !important; background-color: rgba(255,255,255,0.05); padding: 15px; border-radius: 8px; } 
.unlock-desc h3, .unlock-desc p, .unlock-desc li { color: #EAECEE !important; }

/* 導流區塊 (溫暖橘紅) */
.cta-box { background: linear-gradient(135deg, #FFF0E6 0%, #FDEBD0 100%); padding: 28px; border-radius: 12px; border: 2px dashed #E67E22; margin-top: 35px; color: #2C3E50 !important; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
.cta-box h3 { color: #D35400 !important; margin-top:0; font-weight: bold; }
.cta-box p { color: #34495E !important; }
.cta-btn { background: linear-gradient(90deg, #E74C3C, #F39C12); color: white; border: none; padding: 16px 32px; border-radius: 30px; font-size: 18px; cursor: pointer; font-weight: bold; box-shadow: 0 6px 12px rgba(231, 76, 60, 0.3); transition: transform 0.2s; text-decoration: none; display: inline-block; }
.cta-btn:hover { transform: scale(1.05); color: white; text-decoration: none; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🏛️ 全國土地資產智慧分析平台</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">免費提供基礎地政與市場行情數據，將核心法規限制與專家處分策略列為加值服務。</p>', unsafe_allow_html=True)

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
                <li><b>本案參考成交總價：</b> <span style="color:#E74C3C; font-size:18px; font-weight:bold;">561 萬元</span></li>
                <li><b>本案折算每坪單價：</b> <span style="color:#E74C3C; font-size:18px; font-weight:bold;">25.76 萬元 / 坪</span></li>
                <li><b>該區段市場整體區間：</b> 每坪約 24.5 萬 ~ 28.2 萬元，本案定價符合目前市場盤整行情。</li>
                <li><b>發展潛力備註：</b> 本區屬於<b>「社子島開發案」</b>預計徵收範圍，具備長期資產轉換潛力。</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        if pay_mode and not st.session_state['paid']:
            st.warning("🔒 核心法規限制與土地處分策略已被鎖定")
            
            st.markdown("""
            <div class="unlock-desc">
            <h3 style="color: #F39C12 !important;">💡 您的土地符合開發行情，但謄本中隱藏了 3 個關鍵風險！</h3>
            <p>許多地主因看不懂地政術語而錯失變現良機、或誤踩法令盲區。支付 <b>NT$ 150 元</b> 立即解鎖 AI 開發專家的深度白話分析：</p>
            <ol>
                <li>為什麼名為「商業區/住宅區」，現況卻連一間廁所都不能蓋？（解析細部計畫未完成的糖衣陷阱）</li>
                <li>本案是否會被劃為「道路用地/公共設施用地」？未來會被變馬路嗎？</li>
                <li>持分 1/18 這麼零碎，建商不理、別人不買，該如何合法破局與變現？</li>
            </ol>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="pay-wall">
                <h3>🚀 立即解鎖完整「AI 土地價值防禦與處分策略報告」</h3>
                <p style="color: #E74C3C !important; font-size: 24px; font-weight: bold; margin: 10px 0;">限時解鎖價：NT$ 150 元</p>
                <p style="color: #7F8C8D !important; font-size: 14px;">付費解鎖後即可觀看隱藏章節，並獲取專家一對一諮詢通道</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("💳 模擬小額付費解鎖"):
                st.session_state['paid'] = True
                st.rerun()
                
        else:
            if pay_mode and st.session_state['paid']:
                st.balloons()
                st.success("💰 支付成功！已解鎖由 20 年資深土開專家調教之 AI 深度報告：")
            
            st.subheader("🕵️‍♂️ AI 土地開發專家——深度法規與策略報告（已解鎖）")
            
            st.markdown("""
            <div class="card">
            <h3>📌 1. 使用分區的糖衣陷阱：細部計畫尚未完成</h3>
            <p><b>謄本原文：</b> 商業區、住宅區（細部計畫尚未完成，尚未能准許依變更後計畫用途使用）</p>
            <p><b>🧠 AI 白話翻譯：</b><br>
            這塊地在政府的大藍圖裡，未來的確被劃在值錢的「商業區」和「住宅區」。但是，後面括號那句才是關鍵！<br>
            <b>「細部計畫尚未完成」</b>的意思是：政府大方向決定了，但具體細節（如馬路怎麼開、管線怎麼牽）都還沒定案。在細部計畫發布實施前，這塊地<b>完全被法令凍結，現況什麼都不能蓋</b>。這是一塊名義上的黃金，現況上的「素地期貨」。</p>
            </div>
            
            <div class="alert-card">
            <h3>⚠️ 2. 隱藏大雷：有一部分未來可能被變成人行道或馬路？</h3>
            <p><b>謄本原文：</b> 是否在道路用地(公共設施用地)應依建築線或俟地籍測量分割後，再確定。</p>
            <p><b>🧠 AI 白話翻譯：</b><br>
            這是這塊地目前<b>最大的不確定風險</b>。法令顯示這塊地有部分的範圍，未來很有可能會被劃成<b>「道路用地（公共設施）」</b>。<br>
            一旦變馬路，你就絕對不能蓋私人房屋。至於到底會被劃進去多少坪？現在誰也不知道，必須等到未來政府拉出「建築線」或辦理「地籍分割」才能翻牌。在買賣談判時，這是非常有力的砍價藉口。</p>
            </div>
            
            <div class="card">
            <h3>👥 3. 產權複雜度：持分 1/18 的處分策略</h3>
            <p><b>謄本原文：</b> 持分移轉 (1/18)</p>
            <p><b>🧠 AI 白話翻譯：</b><br>
            這代表這塊地被切成了 18 份，你只擁有其中的 1 份（約 21.78 坪）。<br>
            在台灣，想要賣整塊地或合建，通常需要共有人人數和持分「都過半」同意。你只有 1/18，人微言輕。一般民眾絕對不敢買這種地，這種產權實務上只有兩種去處：<b>一是賣給其他的土地大共有人，二是專業的土地開發商（例如我們團隊）</b>，透過法律途徑分割產權或強制收購來破局。</p>
            </div>
            
            <div class="cta-box">
            <h3>🚀 專家最終處分建議與一對一媒合</h3>
            <p>產權這麼碎、開發還要等 10 年以上，如果您現在急需現金流，與其放著資產凍結，不如在此時點以市價變現。我們平台有合作的資深土地開發團隊，專門協助處理社子島複雜持分土地的處分與整合。</p>
            <br>
            <div style="text-align: center;">
                <p style="font-weight: bold; font-size: 17px; color: #D35400 !important; margin-bottom: 20px;">💡 想知道本案在未來區段徵收預估能配回多少坪建地？或者想直接媒合現成買方變現？</p>
                <a href="https://line.me" target="_blank" class="cta-btn">📞 點我立即與「線上專業土地開發師」免費一對一諮詢</a>
                <p style="color: #7F8C8D !important; font-size: 13px; margin-top: 15px;">（此按鈕可直接導流到您的 LINE、電話或留單系統，為您本業捕捉精準客戶！）</p>
            </div>
            </div>
            """, unsafe_allow_html=True)
            
    else:
        st.error("💡 目前為 MVP 測試版本，為了展示最完美的 AI 轉譯效果，請在左側輸入範例資料：地段請包含「富安段」，地號請輸入「261」。")