import streamlit as st
import datetime

# 1. 設定網頁標題與寬度
st.set_page_config(page_title="SOP 智能核對系統", page_icon="📋", layout="centered")

st.title("⚡ 極速 SOP 智能核對系統")
st.caption("把複雜的長篇大論，變成 5 秒內能完成的互動防呆表單")

# 2. 建立分頁 (已擴充為 4 個 Tab)
tab1, tab2, tab3, tab4 = st.tabs([
    "1️⃣ 首日核對",       
    "2️⃣ 核發作業中心", 
    "🚨 3️⃣ ADC 異常處理",
    "⚠️ 4️⃣ 其他異常處理"
])

# ==========================================
# 分頁 1：首日核對
# ==========================================
with tab1:
    st.header("📋 主題 1：首日核對")
    first_day_task = st.radio(
        "🎯 請問您目前要處理哪項作業？",
        ["請選擇...", "✅ 1. 基礎流程 (刷 QR code)", "🔙 2. 處方退藥流程", "🏥 3. 8C 中繼站處理流程", "❄️ 4. 冷藏藥品處理", "🚨 5. 管制藥 1-3 級"],
        horizontal=True, key="tab1_task"
    )
    st.divider()

    if first_day_task == "✅ 1. 基礎流程 (刷 QR code)":
        st.subheader("1️⃣ 基礎流程")
        st.checkbox("✅ 刷取藥袋/餐包上 QR code")
        st.success("💡 基礎刷條碼作業完成後，請依循實際需求選擇其他異常或特殊處理流程。")
    elif first_day_task == "🔙 2. 處方退藥流程":
        st.subheader("2️⃣ 處方退藥流程")
        with st.expander("💻 點此查看：系統退藥操作步驟 (步驟 1~3)", expanded=False):
            st.info("💡 步驟 1：一般退藥收藥 | 步驟 2：特殊藥品退藥 | 步驟 3：入庫")
        patient_status = st.radio("📍 病人目前狀態：", ["請選擇...", "🏥 住院", "🚑 急診在院中", "💼 急診出院帶藥"], horizontal=True)
        if patient_status == "🏥 住院":
            st.checkbox("審核當下若已DC：確認系統自動回簽")
            st.checkbox("審核完才DC：藥品直上病房，由護理端啟退藥")
        elif patient_status == "🚑 急診在院中":
            st.warning("⚠️ 病人還在醫院 (未結帳 / 三日未領)")
            st.checkbox("醫生DC後，確認藥局印出DC總張")
            st.checkbox("若已發出，急診發藥藥師當班追回")
        elif patient_status == "💼 急診出院帶藥":
            st.success("💳 病人急診出院 (已結帳)")
            st.checkbox("急診護理端書記手退，由急診ADC補藥時一併帶回")
            st.checkbox("ADC補藥藥師輸入『實收量』並點選確認退藥退庫")
    elif first_day_task == "🏥 3. 8C 中繼站處理流程":
        st.subheader("3️⃣ 🏥 8C 中繼站處理流程")
        st.checkbox("✅ 審核完成後，蓋『中繼站』印章並放專用籃")
        bed_status = st.radio("請確認最新轉床狀態：", ["請選擇...", "🔵 已轉床", "🟡 未轉床", "🔴 異常(三日未動)"])
        if bed_status == "🔵 已轉床":
            st.success("✅ 行動：改新床號，通知傳送送藥。")
            st.checkbox("已修改新床號並通知傳送")
        elif bed_status == "🟡 未轉床":
            st.warning("⚠️ 行動：務必【留交班】。")
            st.checkbox("已確實留下交班紀錄")
        elif bed_status == "🔴 異常(三日未動)":
            st.error("🚨 警告：立刻交由【線上主管】處理！")
    elif first_day_task == "❄️ 4. 冷藏藥品處理":
        st.checkbox("將藥品放置於冰箱")
        st.checkbox("於護理站貼『有冷藏藥』磁鐵提醒")
    elif first_day_task == "🚨 5. 管制藥 1-3 級":
        st.checkbox("紀錄單放藥袋內，簽收單釘藥袋上，放於『管制藥待領』籃")
        with st.expander("👉 點此展開：管制藥貼片 (Fentanyl) 流程", expanded=False):
            st.checkbox("第一步：確認 ST 且當天換片")
            st.checkbox("第二步：貼片放於麻盒櫃暫放區，等待廢片")
            st.checkbox("第三步：填寫 Fentanyl 貼片追蹤紀錄本")

# ==========================================
# 分頁 2：核發作業中心 
# ==========================================
with tab2:
    st.header("📦 主題 2：核發作業中心")
    dispense_type = st.radio(
        "🎯 請問您目前要處理哪項作業？",
        ["請選擇...", "💊 單位請領管制藥", "💉 Home TPN", "🩸 骨髓捐贈藥品", "⚕️ Thyrogen", "👶 疫苗/血液製劑", "🏠 門診居家(管針)", "🚑 急診發藥", "🔍 自備藥辨識", "🏠 HAH 居家醫療", "🏢 輕安居作業"],
        horizontal=True, key="tab2_task"
    )
    st.divider()
    if dispense_type == "💉 Home TPN":
        st.error("🚨 限【急診藥局】領取；限【星期一、三、五 下午 2:00 後】")
        st.checkbox("確認目前時間與地點符合規定")
        st.checkbox("請病人出示紙本【領取紀錄表】")
        st.checkbox("🖊️ 藥師親自於紀錄表上【蓋章】")
    elif dispense_type == "🔍 自備藥辨識":
        duty_role = st.radio("🕒 時段狀態：", ["請選擇...", "🧑‍🏫 諮詢櫃台開櫃", "🌙 其他時段 (夜間/假日)"])
        if duty_role == "🧑‍🏫 諮詢櫃台開櫃": st.success("👉 由 DI 藥師負責")
        elif duty_role == "🌙 其他時段 (夜間/假日)": st.warning("👉 由 首日量藥師(值班) 負責")
        st.checkbox("進入路徑：藥局_主管 ➔ 入院管理 ➔ 藥學照會清單")
        st.checkbox("電聯臨床端告知辨識完成並送回藥品")
    # ... 其餘內容保持與原程式碼邏輯一致 (此處省略部分重複邏輯以求簡潔)

# ==========================================
# 分頁 3：ADC 特殊狀況處理流程 
# ==========================================
with tab3:
    st.header("🚨 主題 3：ADC 特殊狀況處理流程")
    adc_issue_type = st.radio(
        "🔍 請問您目前遇到什麼類型的 ADC 異常？",
        ["請選擇...", "🛠️ (1) 操作問題", "💻 (2) 資訊異常", "📦 (3) 庫存量不一致", "💥 (4) 當機/無法給藥", "📉 (5) 庫存不足"],
        horizontal=False, key="tab3_task"
    )
    st.divider()
    if adc_issue_type == "📦 (3) 庫存量不一致":
        st.checkbox("✅ 已依照【實際庫存量】重新輸入更新數量")
        adc_time_shift = st.radio("🕒 請問時段？", ["平日白天", "值班時段"])
        if adc_time_shift == "平日白天": st.success("🗣️ 告知【線上主管】即可。")
        else: st.error("🚨 告知【on call 主管】並填寫【交班紀錄單】。")
    elif adc_issue_type == "💥 (4) 當機/無法給藥":
        adc_location = st.radio("📍 發生站點：", ["🚑 急診 ADC", "🏥 住院 ADC"])
        if adc_location == "🚑 急診 ADC":
            st.error("🚨 請急診人員用【專用手寫處方箋】來取藥，藥師手寫藥袋")
        else:
            st.warning("⚠️ 請護理站填寫【藥品處理單】來取藥，藥師手寫藥袋")
    # ... 其餘內容保持一致

# ==========================================
# 分頁 4：其他異常處理 (🔥 新增分流邏輯)
# ==========================================
with tab4:
    st.header("⚠️ 主題 4：其他異常事件處理流程")
    st.caption("針對缺藥、藥袋/藥包異常等突發狀況之處置")

    # 第一層：選擇異常事件
    abnormal_event = st.radio(
        "🚨 發生了什麼異常事件？",
        ["請選擇...", "💊 缺藥 (線上/UD 找不到藥)", "📄 藥袋或藥包異常 (破損/印錯/內容誤)"],
        horizontal=True
    )

    st.divider()

    if abnormal_event != "請選擇...":
        # 第二層：選擇時段
        shift_time = st.radio(
            "🕒 請問目前的時段是？",
            ["🌞 平日", "🌙 值班時段 (夜間/假日)"],
            horizontal=True
        )
        
        st.divider()

        # 邏輯 A：缺藥處理
        if "💊 缺藥" in abnormal_event:
            if shift_time == "🌞 平日":
                st.info("💡 **平日缺藥處置**")
                st.checkbox("1. 再次確定『線上』及『UD』確實都沒有藥品")
                st.checkbox("2. 🗣️ 立即告知【線上主管】處理")
            else:
                st.error("🚨 **值班缺藥處置：需前往藥庫取藥**")
                with st.expander("🔍 如何查詢母庫儲位？", expanded=True):
                    st.markdown("🌐 請開啟：**網頁版藥典** 查詢藥品於母庫之位置。")
                st.checkbox("1. 前往【藥庫】拿取藥品")
                st.checkbox("2. ✍️ 務必騰寫【帳卡】(寫明數量/日期)")
                st.checkbox("3. 將帳卡置於【庫管理員桌上】或【待作帳盒子】")
                st.warning("⚠️ 提醒：待周一上班日由藥庫進行作帳。")
        
        # 邏輯 B：藥袋或藥包異常
        elif "📄 藥袋或藥包異常" in abnormal_event:
            if shift_time == "🌞 平日":
                st.info("💡 **平日單據異常處置**")
                st.checkbox("1. 🗣️ 立即告知【線上主管】")
            else:
                st.error("🚨 **值班單據異常處置：緊急補印與存證**")
                col_ab1, col_ab2 = st.columns(2)
                with col_ab1:
                    st.checkbox("1. 補印藥袋")
                with col_ab2:
                    st.checkbox("2. 補印藥包")
                st.checkbox("3. 📞 電聯當日 **On call 主管**")
                st.checkbox("4. 📄 留取該筆**異常處方箋或總張** (查核存證用)")
                st.checkbox("5. ✍️ 確實記錄於**電子交班單**，落實交班")

# 頁尾
st.sidebar.info(f"📅 系統執行日：{datetime.date.today()}")
st.sidebar.caption("⚡ 本系統僅供 SOP 快速核對使用，實際操作請依醫院規範為準。")
