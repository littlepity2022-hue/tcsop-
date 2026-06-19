import streamlit as st
import datetime

# 1. 設定網頁標題與寬度
st.set_page_config(page_title="SOP 智能核對系統", page_icon="📋", layout="centered")

st.title("⚡ 極速 SOP 智能核對系統")
st.caption("把複雜的長篇大論，變成 5 秒內能完成的互動防呆表單")

# 2. 建立分頁 (新增了 ADC 異常處理，調整為 6 個 Tab)
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "1️⃣ 首日量", 
    "2️⃣ 核發", 
    "🏠 3️⃣ HAH", 
    "🏢 4️⃣ 輕安居", 
    "🚨 5️⃣ ADC 異常", # <--- 新增大主題
    "📝 貼新 SOP"
])

# ==========================================
# 分頁 1：首日量審核 
# ==========================================
with tab1:
    st.header("📋 主題 1：首日量審核")
    st.subheader("1️⃣ 基礎流程")
    step1 = st.checkbox("✅ 刷取藥袋/餐包上 QR code")
    
    if step1:
        st.subheader("2️⃣ 處方退藥流程")
        with st.expander("💻 點此查看：系統退藥操作步驟 (步驟 1~3)", expanded=False):
            st.info("💡 依照以下路徑於系統操作：\n**步驟 1：一般退藥收藥** (住院調劑 ➔ 退藥-收藥作業)\n**步驟 2：特殊藥品退藥** (特殊藥品系統 ➔ 特殊藥品系統-退藥)\n**步驟 3：入庫** (實體藥品入 ADC)")

        patient_status = st.radio(
            "📍 病人目前狀態：",
            ["請選擇...", "🏥 住院", "🚑 急診在院中", "💼 急診出院帶藥"],
            horizontal=True
        )

        if patient_status == "🏥 住院":
            st.info("💡 住院退藥流程")
            st.checkbox("審核當下若已DC：確認系統自動回簽 (未領退藥)")
            st.checkbox("審核完才DC：藥品直上病房，由護理端啟退藥，交由樓下住院藥師處理")
            st.checkbox("例外確認：若是貼片審核完成才DC，直接在藥局進行啟退藥")
        elif patient_status == "🚑 急診在院中":
            st.warning("⚠️ 病人還在醫院 (未結帳 / 三日未領)")
            st.checkbox("醫生DC後，確認藥局印出DC總張")
            st.checkbox("若已發出，急診發藥藥師當班追回 (假日由急診值班負責)")
        elif patient_status == "💼 急診出院帶藥":
            st.success("💳 病人急診出院 (已結帳 / 未領藥清單上有)")
            st.checkbox("急診護理端書記手退，由急診ADC補藥時一併帶回")
            st.checkbox("ADC補藥藥師輸入『實收量』，按下確認鍵")
            st.checkbox("點選子畫面『確認退藥退庫』")
            st.checkbox("大夜藥師確認發藥後，將狀態轉發藥")

        st.divider()

        st.subheader("3️⃣ 🏥 8C 中繼站處理流程")
        col_8c_1, col_8c_2 = st.columns(2)
        with col_8c_1:
            st.checkbox("✅ 審核完成後，於左上角蓋『中繼站』印章")
        with col_8c_2:
            st.checkbox("✅ 放置於架上『中繼站專用』籃")

        st.markdown("#### 🛏️ 轉床處理原則與交班")
        st.checkbox("🔍 當班已刷取每日落實交班，並確認交班完畢")
        
        bed_status = st.radio(
            "請確認系統顯示之最新轉床狀態：",
            ["請選擇...", "🔵 已轉床 (需送至新病床)", "🟡 未轉床 (需留交班)", "🔴 三日仍未轉床或出院 (異常交辦)"],
            horizontal=False
        )

        if bed_status == "🔵 已轉床 (需送至新病床)":
            st.success("✅ 行動：請將藥袋上改為【新床號】，並請傳送送至【新病床】。")
            st.checkbox("已修改新床號並通知傳送")
        elif bed_status == "🟡 未轉床 (需留交班)":
            st.warning("⚠️ 行動：未轉床務必【留交班】。")
            st.checkbox("已確實留下交班紀錄")
        elif bed_status == "🔴 三日仍未轉床或出院 (異常交辦)":
            st.error("🚨 警告：若三日仍未轉床或出院，請立刻將該筆處方交由【線上主管】處理！")
            st.checkbox("已通報並交由線上主管")

        st.divider()

        st.subheader("4️⃣ ❄️ 冷藏藥品處理")
        col1, col2 = st.columns(2)
        with col1:
            st.checkbox("將藥品放置於冰箱")
        with col2:
            st.checkbox("於護理站貼『有冷藏藥』磁鐵提醒")

        st.divider()

        st.subheader("5️⃣ 🚨 管制藥 1-3 級")
        st.checkbox("紀錄單放藥袋內，簽收單釘藥袋上，放於『管制藥待領』籃")
        st.checkbox("確認傳送/護理端領藥紀錄時間並繳回，歸於『管單』籃")
        
        with st.expander("👉 點此展開：管制藥貼片 (Fentanyl) 嚴格核發流程", expanded=False):
            patch_1 = st.checkbox("第一步：確認使用頻率為 ST 且當天換片 (有疑慮需致電護理站)")
            if patch_1:
                patch_2 = st.checkbox("第二步：貼片放於麻盒櫃『管制藥貼片暫放區』，等待氣送廢片及紀錄表")
                if patch_2:
                    patch_3 = st.checkbox("第三步：填寫 Fentanyl 貼片追蹤紀錄本")
                    if patch_3:
                        patch_4 = st.radio("數量與紀錄表是否正確吻合？", ["請核對...", "✅ 無誤", "❌ 數量不符 / 紀錄表不完整"])
                        if patch_4 == "✅ 無誤":
                            st.success("🎉 可放置於『管制藥待領』籃！完成核發。")
                        elif patch_4 == "❌ 數量不符 / 紀錄表不完整":
                            st.error("🛑 異常處理：一律請對方填寫切結書！")

# ==========================================
# 分頁 2：核發作業中心 
# ==========================================
with tab2:
    st.header("📦 主題 2：核發作業中心")
    
    dispense_type = st.radio(
        "🎯 請問您目前要處理哪項作業？",
        [
            "請選擇...", 
            "💊 單位請領管制藥", 
            "💉 Home TPN", 
            "🩸 骨髓捐贈藥品", 
            "⚕️ Thyrogen", 
            "👶 嬰兒室公費疫苗/血液製劑",
            "🏠 門診居家照護(管制針劑)",
            "🚑 急診發藥注意事項",
            "🔍 住院病人(自備藥)藥物辨識"
        ],
        horizontal=True
    )
    
    st.divider()

    if dispense_type == "🔍 住院病人(自備藥)藥物辨識":
        st.subheader("🔍 住院病人(自備藥)藥物辨識流程")
        st.info("💡 前提：醫囑端會將藥品送至【急診藥局】，並啟動多團隊照會『#9 非本院藥局之外觀辨識』。")

        st.markdown("#### 1️⃣ 確認負責藥師與時段")
        duty_role = st.radio(
            "🕒 請問目前的時段狀態是？",
            ["請選擇...", "🧑‍🏫 諮詢櫃台【開櫃】時段", "🌙 其他時段 (夜間/假日)"],
            horizontal=True
        )

        if duty_role == "🧑‍🏫 諮詢櫃台【開櫃】時段":
            st.success("👉 此時段由 **【DI藥師】** 負責完成。")
        elif duty_role == "🌙 其他時段 (夜間/假日)":
            st.warning("👉 此時段由 **【首日量藥師(值班)】** 負責完成。")

        if duty_role != "請選擇...":
            st.divider()
            st.markdown("#### 2️⃣ 系統表單確認防呆")
            with st.expander("💻 點此查看系統表單路徑", expanded=True):
                st.markdown("1. 進入系統點選上方選單：`藥局_主管` ➔ `入院管理`\n2. 點擊頁籤：`多團隊照會` ➔ `藥學照會清單`")

            has_order = st.radio(
                "系統上是否查到該筆照會單號？",
                ["請確認...", "✅ 是，有查到單號", "❌ 否，查無此單號"],
                horizontal=True
            )

            if has_order == "❌ 否，查無此單號":
                st.error("🚨 異常防呆：查無照會單！")
                st.checkbox("📞 必須【電聯臨床端】協助啟單 (開啟 #9 非本院藥局之外觀辨識)")
            
            elif has_order == "✅ 是，有查到單號":
                st.markdown("#### 3️⃣ 執行辨識與結案")
                st.checkbox("🔍 執行藥物外觀辨識作業")
                st.checkbox("✍️ 將辨識後的【藥品名稱】輸入表單內容中，並提供用藥建議")
                st.caption("*(註：目前表單有預設文字模板，可依照需求增減內容)*")
                
                st.markdown("#### 4️⃣ 結案聯絡與藥物歸還")
                col_end1, col_end2 = st.columns(2)
                with col_end1:
                    st.checkbox("📞 辨識完成，【電聯臨床端】告知")
                with col_end2:
                    st.checkbox("📦 將藥品送回【護理站】")
                
                st.success("🎉 完成自備藥外觀辨識流程！")

    elif dispense_type == "💊 單位請領管制藥":
        st.subheader("💊 單位請領管制藥 (平日 周一～周五)")
        unit_type = st.radio("📍 請選擇送單單位類型：", ["請選擇...", "🏢 非 ADC 單位", "🏥 ADC 單位"], horizontal=True)
        if unit_type == "🏢 非 ADC 單位":
            st.error("⏰ 【時間防呆】注意：9:30 後不收單！")
            st.checkbox("確認單位送出【請領單】與【空瓶】(一對一更換)")
            st.checkbox("核對：空瓶數與請領數量是否符合？")
            st.checkbox("核對：電子管箋是否正確？")
            st.info("♻️ 備註：報廢量不須送回藥局銷毀，由原單位直接進行銷毀。")
        elif unit_type == "🏥 ADC 單位":
            st.warning("⏰ 【時間防呆】注意：9:00 送單！(逾期由藥庫與督導處理)")
            st.checkbox("依照排程，接收單位送出之請領單")
            st.checkbox("核對：電子管箋是否正確？")
            st.info("♻️ 備註：報廢量不須送回藥局銷毀，由原單位直接銷毀。補藥由補藥藥師依核發量收回空瓶。")

    elif dispense_type == "💉 Home TPN":
        # ... (略, 與之前相同)
        pass

# ==========================================
# 分頁 3：HAH 居家在宅醫療
# ==========================================
with tab3:
    st.header("🏠 HAH 居家在宅醫療：二院區 B1 領藥")
    # ... (略, 與之前相同)
    pass

# ==========================================
# 分頁 4：輕安居作業
# ==========================================
with tab4:
    st.header("🏢 主題 4：輕安居作業 SOP")
    # ... (略, 與之前相同)
    pass

# ==========================================
# 分頁 5：ADC 特殊狀況處理流程 (🔥🔥 本次新增大主題 🔥🔥)
# ==========================================
with tab5:
    st.header("🚨 主題 5：ADC 特殊狀況處理流程")
    st.caption("依照異常類型進行分流防呆處置")

    # 第一層防呆：判斷 ADC 異常類型
    adc_issue_type = st.radio(
        "🔍 請問您目前遇到什麼類型的 ADC 異常？",
        [
            "請選擇...",
            "🛠️ (1) 操作上問題 (醫囑取藥/盤點等操作相關)",
            "💻 (2) 資訊異常 (醫囑後已審核，但正常流程無法開櫃)",
            "📦 (3) 庫存量不一致 (實際庫存與電腦畫面不符)",
            "💥 (4) ADC 當機或無法審核 (導致無法給藥)"
        ],
        horizontal=False
    )

    st.divider()

    # 情境 1：操作問題
    if adc_issue_type == "🛠️ (1) 操作上問題 (醫囑取藥/盤點等操作相關)":
        st.subheader("🛠️ ADC 操作問題處置")
        st.info("💡 處置方式：請先查閱操作手冊，若無法解決請連繫主管。")
        st.checkbox("✅ 已查閱操作手冊或連繫自己的主管")

    # 情境 2：資訊系統異常
    elif adc_issue_type == "💻 (2) 資訊異常 (醫囑後已審核，但正常流程無法開櫃)":
        st.subheader("💻 ADC 資訊系統異常處置")
        st.warning("⚠️ 處置方式：硬體/系統層級異常，無法自行排除。")
        st.checkbox("📞 立即請護理站/現場人員聯繫【資訊護理師】處理")

    # 情境 3：庫存不一致
    elif adc_issue_type == "📦 (3) 庫存量不一致 (實際庫存與電腦畫面不符)":
        st.subheader("📦 ADC 庫存量不一致處置")
        
        st.markdown("#### 第一步：系統校正")
        st.checkbox("✅ 已依照【實際庫存量】重新輸入並更新電腦數量")
        
        st.markdown("#### 第二步：主管通報 (依時段)")
        adc_time_shift = st.radio("🕒 請問目前的時段是？", ["請選擇...", "🌞 平日白天", "🌙 值班時段 (夜間/假日)"], horizontal=True)
        
        if adc_time_shift == "🌞 平日白天":
            st.success("🗣️ 平日處置：請告知【線上主管】即可。")
            st.checkbox("✅ 已告知線上主管")
        elif adc_time_shift == "🌙 值班時段 (夜間/假日)":
            st.error("🚨 值班時段處置：需通報並留下交班紀錄！")
            st.checkbox("🗣️ 已告知【on call 主管】")
            st.checkbox("✍️ 已填寫【交班紀錄單】")

    # 情境 4：大當機 / 無法給藥 (最複雜的情境)
    elif adc_issue_type == "💥 (4) ADC 當機或無法審核 (導致無法給藥)":
        st.subheader("💥 ADC 異常 / 藥局無法審核給藥處置")
        
        adc_location = st.radio(
            "📍 請問發生當機/異常的 ADC 站點是？",
            ["請選擇...", "🚑 急診 ADC", "🏥 住院 ADC"],
            horizontal=True
        )

        if adc_location == "🚑 急診 ADC":
            st.error("🚨 【急診 ADC 異常】(平日與值班時段皆適用此流程)")
            st.checkbox("1️⃣ 【立即告知】急診人員")
            st.checkbox("2️⃣ 請急診人員用 **【專用手寫處方箋】** 來藥局取藥")
            
            with st.expander("👀 點此展開：急診 ADC 專用手寫處方箋 常見品項參考", expanded=False):
                st.markdown("""
                *包含但不限於以下緊急用藥，詳見實體表單：*
                - Alteplase 50mg/vial
                - Ketorolac 30mg/amp
                - Tramadol 100mg/2ml (管4)
                - Fentanyl 針劑 (大/小)
                - Morphine 針劑
                - Propofol 200mg/20ml (管4)
                - Midazolam 5mg/1ml (管4)
                - Diazepam 10mg/2ml (管4)
                """)
            
            st.checkbox("3️⃣ 藥師手寫藥袋")
            
            st.markdown("#### 通報流程")
            er_shift = st.radio("請問目前時段？", ["平日白天", "值班時段 (夜間/假日)"], horizontal=True)
            if er_shift == "平日白天":
                st.checkbox("🗣️ 已告知【線上主管】")
            else:
                st.checkbox("🗣️ 已告知【on call 主管】")
                st.checkbox("✍️ 已填寫【交班紀錄單】")

        elif adc_location == "🏥 住院 ADC":
            st.warning("⚠️ 【住院 ADC 異常】")
            ip_shift = st.radio("請問目前時段？", ["請選擇...", "🌞 平日白天", "🌙 值班時段 (夜間/假日)"], horizontal=True)
            
            if ip_shift == "🌞 平日白天":
                st.info("💡 註：住院平日日時段異常 ➔ 請先告知【線上主管】處理。")
                st.checkbox("✅ 已告知線上主管")
                
            elif ip_shift == "🌙 值班時段 (夜間/假日)":
                st.error("🚨 住院值班時段緊急取藥流程：")
                st.checkbox("1️⃣ 【告知】護理站相關人員")
                st.checkbox("2️⃣ 請護理站填寫 **【藥品處理單】** 來藥局取藥")
                st.caption("*(注意：急診是用手寫處方箋，住院是用藥品處理單)*")
                st.checkbox("3️⃣ 藥師手寫藥袋")
                st.checkbox("🗣️ 4️⃣ 告知【on call 主管】")
                st.checkbox("✍️ 5️⃣ 填寫【交班紀錄單】")


# ==========================================
# 分頁 6：通用文本轉 Checklist 工具
# ==========================================
with tab6:
    st.header("📝 貼上 SOP，自動轉成 Checklist")
    raw_text = st.text_area("請在此貼上 SOP 文字：", height=200)
    if st.button("✨ 瞬間轉換成 Checklist"):
        if raw_text:
            st.divider()
            st.subheader("✅ 您的專屬核對表：")
            lines = raw_text.split('\n')
            for line in lines:
                if line.strip():
                    st.checkbox(line.strip(), key=line.strip())
            st.success("轉換完成！")
