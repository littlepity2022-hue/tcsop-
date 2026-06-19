import streamlit as st
import datetime

# 1. 設定網頁標題與寬度
st.set_page_config(page_title="SOP核對系統", page_icon="📋", layout="centered")


st.caption("互動防呆表單")

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
    
    # 🌟 已改回 Radio 攤開模式
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
            "🔍 住院病人(自備藥)藥物辨識",
            "🏠 HAH 居家在宅醫療", 
            "🏢 輕安居作業"        
        ],
        horizontal=True
    )
    
    st.divider()

    # ---------------- 既有選項邏輯 ----------------

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
        st.subheader("💉 Home TPN 門診處方核發")
        st.error("🚨 **【極重要限制】請務必確認：必須至【急診藥局】領取；且限【星期一、三、五 下午 2:00 後】**")
        tpn_step1 = st.checkbox("確認目前時間與地點符合上述規定")
        tpn_step2 = st.checkbox("請病人出示紙本【居家 TPN 領取紀錄表】")
        if tpn_step1 and tpn_step2:
            st.checkbox("核對處方內容：日期、乘載數量是否吻合")
            tpn_step4 = st.checkbox("🖊️ 藥師親自於紀錄表上【蓋章】")
            if tpn_step4:
                st.success("🎉 核對無誤，可將 Home TPN 交予病人。")

    elif dispense_type == "🩸 骨髓捐贈藥品":
        st.subheader("🩸 骨髓捐贈藥品核發")
        st.info("💡 **事前準備位置：** 藥品已由藥庫提前放置於【首日量單門冰箱】 (內含：好幾天份藥 + 綠聯 + 白聯)")
        st.markdown("#### ✅ 病人來領 Checklist")
        st.checkbox("❄️ 【註2】確認給藥時是否需附帶【冰桶】")
        st.checkbox("📅 【步驟 b】僅給予【當日藥品】(務必核對編碼與日期！)")
        st.checkbox("✍️ 【步驟 a】綠聯、白聯：【發藥藥師】與【領受人】皆已簽名")
        st.divider()
        dose_status = st.radio("請問此劑為最後一劑嗎？", ["請選擇...", "➡️ 否，病人後續還需續領", "🛑 是，此為最後一劑"], horizontal=True)
        if dose_status == "➡️ 否，病人後續還需續領":
            st.success("✅ 【步驟 c】請將【綠聯】歸還給病人帶回續用。")
            st.checkbox("已將綠聯歸還病人")
        elif dose_status == "🛑 是，此為最後一劑":
            st.warning("⚠️ 【註1】最後一劑特殊處理：")
            st.checkbox("將綠、白 2 聯【皆收下】不退還")
            st.checkbox("將 2 聯交給【線上主管】(若為值班時段，則放置於交班資料夾)")

    elif dispense_type == "⚕️ Thyrogen":
        st.subheader("⚕️ Thyrogen 處理流程")
        thyrogen_task = st.radio("🎯 請問您目前要執行哪項任務？", ["請選擇...", "🛠️ 前期：藥品調劑與準備", "📦 後期：急診藥局核發(領藥)"], horizontal=True)
        if thyrogen_task == "🛠️ 前期：藥品調劑與準備":
            st.markdown("#### 1️⃣ 調劑準備 Checklist")
            pt_type = st.radio("請問是哪種處方？", ["請選擇...", "🏥 住院處方", "🏥 門診處方"], horizontal=True)
            if pt_type == "🏥 住院處方":
                st.info("💡 住院處理原則")
                st.checkbox("首日量藥袋請【直接調劑】(直接從藥庫拿)")
                st.checkbox("首日量直接上病房")
            elif pt_type == "🏥 門診處方":
                st.info("💡 門診處理原則 (有交接動作)")
                st.checkbox("專用藥師依照藥袋調劑")
                st.checkbox("調劑完畢後，交給【主管】")
                st.success("✅ 後續由主管統一放置於【首日量單門冰箱】")
        elif thyrogen_task == "📦 後期：急診藥局核發(領藥)":
            st.markdown("#### 2️⃣ 急診核發 Checklist")
            st.info("🔄 給藥原則：比照骨捐流程，單次給藥。")
            st.checkbox("確認核醫科人員已出示【病患注射卡】")
            st.checkbox("至【首日量單門冰箱】拿取已備好之 Thyrogen 藥袋")
            with st.expander("🚨 異常狀況處理：當下未找到該病患藥袋？", expanded=False):
                st.warning("遇到找不到病患藥袋時，請值班藥師執行以下動作：")
                st.checkbox("✍️ 值班藥師【手寫藥袋】給藥")
                st.checkbox("💻 後續於【電子交班單】交班給藥庫")

    elif dispense_type == "👶 嬰兒室公費疫苗/血液製劑":
        st.subheader("👶 住院24小時內新生兒施打 (公費) 疫苗/血液製劑")
        st.error("🚨 **【地點限定】本流程僅限至【急診藥局】請領！**")
        with st.expander("ℹ️ 點此查看：目前開放請領之兩項品項", expanded=False):
            st.markdown("1. **(疫苗)** Hepatitis B Vaccine 10mcg `[冷藏][公費]`\n2. **(血液製劑)** Hepatitis B Immune Globulin 100IU `[冷藏][公費]`")
        st.divider()
        st.warning("⚠️ **【冷鏈防呆限制】** 請務必等傳送將專用冰桶拿來後，再開始後續動作！")
        cooler_arrived = st.checkbox("✅ 傳送已將【專用冰桶】與【請領單】送達藥局")
        if cooler_arrived:
            st.markdown("#### 1️⃣ 內容物核對")
            col_v1, col_v2 = st.columns(2)
            with col_v1:
                st.checkbox("冰桶內：溫度計、監視卡、冰寶、查檢表")
            with col_v2:
                st.checkbox("請領單：名字床號、蓋章、領取量")
            st.divider()
            st.markdown("#### 2️⃣ 調劑與單據處理")
            st.checkbox("✍️ 依照藥袋調劑，並於【帳卡】寫上床號")
            st.checkbox("📝 於比對欄位填寫『公費』")
            slip_handled = st.radio("是否已正確分拆請領單？", ["尚未處理...", "✅ 將上聯留著夾冰箱旁，下聯還給傳送"], horizontal=False)
            if slip_handled == "✅ 將上聯留著夾冰箱旁，下聯還給傳送":
                st.checkbox("🎉 完成首日量核對")

    elif dispense_type == "🏠 門診居家照護(管制針劑)":
        st.subheader("🏠 門診居家照護管制藥針劑流程")
        role = st.radio("🧑‍⚕️ 請問您目前是哪一站的藥師？", ["請選擇...", "👁️ 核對藥師", "💊 門診發藥藥師", "🚑 急診發藥藥師"], horizontal=True)
        st.divider()
        if role == "👁️ 核對藥師":
            st.error("🚨 **【強制防呆】管 1 - 管 4 針劑先【不調劑】！**")
            st.markdown("#### ✅ 您的專屬任務：")
            st.checkbox("將其他藥品核對完畢")
            st.checkbox("將【空藥袋】一併夾好送出")
            st.success("✅ 核對藥師任務結束。")
        elif role == "💊 門診發藥藥師":
            st.info("💡 居家護理師後續會去急診藥局領針劑，門診只需處理以下事項：")
            st.markdown("#### ✅ 您的專屬任務：")
            st.checkbox("發給病人『其他藥品』")
            st.checkbox("將【管箋】及【空藥袋】交給『調一藥師』")
            st.markdown("#### ⚠️ 特殊狀況檢查")
            mix_rx = st.radio("管箋上是否『同時有口服跟針劑』？", ["請確認...", "🟢 否，純針劑", "🔴 是，有口服也有針劑"], horizontal=True)
            if mix_rx == "🔴 是，有口服也有針劑":
                st.warning("⚠️ 記得在管箋上【備註口服是誰發的】！")
                st.checkbox("已備註口服發藥藥師")
        elif role == "🚑 急診發藥藥師":
            st.markdown("#### ✅ 您的專屬任務：分為領藥當下與回收空瓶")
            er_task = st.radio("目前進度是？", ["請選擇...", "📦 護理師正要領藥", "♻️ 護理師拿空瓶來回收 (需結案)"], horizontal=True)
            if er_task == "📦 護理師正要領藥":
                st.checkbox("✍️ 核發時，填寫【追蹤本子】")
                st.success("護理給藥紀錄會由系統直接帶入，當下處理完成！")
            elif er_task == "♻️ 護理師拿空瓶來回收 (需結案)":
                st.markdown("**💻 回收空瓶需操作系統【管藥結案】：**")
                with st.expander("👉 點此查看系統結案操作步驟", expanded=True):
                    st.markdown("1. 進入路徑：`特殊藥品系統` ➔ `特殊藥品系統-管藥結案`\n2. 篩選條件設定為：**[已結案] = [否]**\n3. 勾選欲結案之品項，點擊上方【結案】按鈕。")
                st.checkbox("✅ 已完成系統管藥結案")
                st.checkbox("✅ 將此紀錄交班給【藥庫】")

    elif dispense_type == "🚑 急診發藥注意事項":
        st.subheader("🚑 急診發藥注意事項")
        er_pt_status = st.radio("請選擇急診病人狀態：", ["請選擇...", "🛏️ 急診在院", "🚶 急診出院"], horizontal=True)
        if er_pt_status == "🛏️ 急診在院":
            st.info("💡 流程：調劑 ➔ 審核 ➔ 傳送領取")
            st.checkbox("完成調劑")
            st.checkbox("完成審核")
            st.checkbox("交由傳送領取")
        elif er_pt_status == "🚶 急診出院":
            st.info("💡 流程：比照【門診發藥模式】")
        st.divider()
        st.error("🚨 **【重大異常防呆：漏發部份品項】**")
        st.write("注意：急診病人處方易頻繁修改。發藥藥師務必查看系統【有效處方明細】，確認各處方是否標示『已發藥』！")

    # ---------------- 整併進來的 HAH 邏輯 ----------------
    elif dispense_type == "🏠 HAH 居家在宅醫療":
        st.subheader("🏠 HAH 居家在宅醫療：二院區 B1 領藥")
        
        opd_time = st.radio(
            "🕒 請確認當前時段：",
            ["平日正常門診 (09:00 - 21:00)", "週六半日/週日/國定假日 (含停診時段)"],
            horizontal=True
        )

        st.divider()

        if opd_time == "平日正常門診 (09:00 - 21:00)":
            st.info("📦 處理方式：一院區轉送二院區 (第一院區主管派人送藥 ➔ 二院區中藥局核發)")
            
            st.checkbox("1. 確認一院區傳送已將藥品送達二院區")
            st.checkbox("2. 點收完畢，將藥品放置於【HAH 居家在宅醫療專用藥盒】內")
            
            st.markdown("#### 🚪 領藥窗口分配 (B1 窗口)")
            now_time = datetime.datetime.now().time()
            st.write(f"🕘 目前系統時間：{now_time.strftime('%H:%M')}")

            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.warning("🌅 白班 (12:30前)")
                st.checkbox("至 **A4 窗口** 發藥")
            with col_b:
                st.warning("⛅ 白班 (12:30後)")
                st.checkbox("至 **D8 窗口** 發藥")
            with col_c:
                st.warning("🌃 夜班 (13:30-22:00)")
                st.checkbox("至 **E 窗口** 發藥")

        else:
            st.error("🚨 🚑 假日/停診處理：此時段統一由『急診藥局』辦理核發！")
            st.checkbox("1. 單位人員需憑【處方箋】至急診藥局領藥")
            
            with st.expander("🏃‍♂️ 急診發藥藥師操作指南", expanded=True):
                st.markdown("""
                * **步驟 A：** 依照處方箋號碼，前往【門診區】拿取藥品。
                * **步驟 B：** 執行核發作業 (比照一般門診發藥流程)。
                * **步驟 C：** 核發完成需在【處方箋】上蓋章。
                """)
            
            st.checkbox("2. 將【處方箋】&【總張】放入『急診交班透明夾』")
            st.success("✅ 完成假日/夜間核發交班作業")

        st.divider()
        st.caption("❓ 若有任何疑問，請立即詢問【線上主管】")

    # ---------------- 整併進來的 輕安居 邏輯 ----------------
    elif dispense_type == "🏢 輕安居作業":
        st.subheader("🏢 輕安居作業 SOP")
        st.caption("依照平假日原則、處方類型與站點角色進行防呆核對")

        day_type = st.radio(
            "📅 請問今天是平日還是假日？", 
            ["請選擇...", "🌞 平日", "🎉 週六/國定假日", "🚨 假日/無門診 (值班急領)"], 
            horizontal=True
        )

        st.divider()

        if day_type == "🌞 平日":
            st.markdown("#### 📝 輕安居 - 平日列印與作業原則")
            
            med_type = st.radio("💉 處方是否包含針劑？", ["請選擇...", "包含針劑", "無針劑 (下午餐包作業)"], horizontal=True)

            if med_type == "包含針劑":
                st.info("💡 【含針劑】處方處理原則")
                st.checkbox("由『門診調劑藥師』負責調劑 (總包)")
                st.checkbox("病人領藥後，請引導至『注射室』給藥")

            elif med_type == "無針劑 (下午餐包作業)":
                st.info("💡 【無針劑】下午餐包流程：NH7 調劑 ➔ NH4 審核 ➔ F1 核發 ➔ 傳送至二院區")
                
                # 🌟 輕安居站點角色也改回 Radio
                role_task = st.radio(
                    "👩‍⚕️ 您目前負責的崗位是？", 
                    ["請選擇...", "1️⃣ 調劑 (輕安居7)", "2️⃣ 書記", "3️⃣ 審核 (輕安居4)", "4️⃣ 傳送 (DU4)", "5️⃣ 核發 (F1)"],
                    horizontal=True
                )

                if role_task == "1️⃣ 調劑 (輕安居7)":
                    st.warning("⏰ 建議作業時間：11:30-13:00 / 13:30-16:30")
                    st.checkbox("負責調劑捲餐包")
                    st.checkbox("確認完成『16:00 前』之處方")
                elif role_task == "2️⃣ 書記":
                    st.warning("⏰ 建議作業時間：12:00-13:00")
                    st.checkbox("執行書記轉餐包作業")
                elif role_task == "3️⃣ 審核 (輕安居4)":
                    st.warning("⏰ 建議作業時間：13:30-17:30")
                    st.checkbox("審核當日『16:00 前』之處方")
                elif role_task == "4️⃣ 傳送 (DU4)":
                    st.warning("⏰ 建議作業時間：14:00-15:00")
                    st.checkbox("傳送將藥車推至『急診藥局』 (DU4 & 13-22C)")
                    st.checkbox("急診藥師主動告知發藥藥師")
                elif role_task == "5️⃣ 核發 (F1)":
                    st.warning("⏰ 建議作業時間：15:30-17:00")
                    st.checkbox("依照收付之處方箋給藥")
                    st.error("🚨 注意：總張勿撕！依照護理單位置於臺車上")
                    st.checkbox("未領之藥品：依照單位，分別置於『小寶後方輕安居籃』內")

        elif day_type == "🎉 週六/國定假日":
            st.markdown("#### 📝 輕安居 - 週六/國定假日作業原則")
            st.info("💡 流程重點：門診總包 ➔ 暫放 ➔ 傳送二院區")
            st.checkbox("一律由『門診調劑藥師』負責調劑 (總包)")
            st.checkbox("核對後，放置於『小寶旁輕安區藥品暫放籃』")
            st.checkbox("注意：週六依然會進行核發 ➔ 傳送推至二院區")

        elif day_type == "🚨 假日/無門診 (值班急領)":
            st.error("🚨 🚑 假日(W6/W7)無門診時段：值班時段輕安局急領")
            st.checkbox("1️⃣ 先查詢 HIS5 藥品狀態是否完成")
            st.caption("*(未完成定義：窗邊長籃內無藥品，且藥品狀態未開立)*")
            st.checkbox("2️⃣ 於輕安居籃內拿取藥袋調劑，並以『總包給藥』")
            st.checkbox("3️⃣ 調劑、審核、核發皆完成後，收處方箋並留『電子交班單』")


# ==========================================
# 分頁 3：ADC 特殊狀況處理流程 
# ==========================================
with tab3:
    st.header("🚨 主題 3：ADC 特殊狀況處理流程")
    st.caption("依照異常類型進行分流防呆處置")

    # 第一層防呆：判斷 ADC 異常類型
    adc_issue_type = st.radio(
        "🔍 請問您目前遇到什麼類型的 ADC 異常？",
        [
            "請選擇...",
            "🛠️ (1) 操作上問題 (醫囑取藥/盤點等操作相關)",
            "💻 (2) 資訊異常 (醫囑後已審核，但正常流程無法開櫃)",
            "📦 (3) 庫存量不一致 (實際庫存與電腦畫面不符)",
            "💥 (4) ADC 當機或無法審核 (導致無法給藥)",
            "📉 (5) ADC 內藥品庫存不足" 
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

    # 情境 4：大當機 / 無法給藥
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

    # 情境 5：ADC 內藥品庫存不足
    elif adc_issue_type == "📉 (5) ADC 內藥品庫存不足":
        st.subheader("📉 ADC 內藥品庫存不足處置流程")
        
        out_of_stock_shift = st.radio(
            "🕒 請問目前的時段是？",
            ["請選擇...", "🌞 平日白天", "🌙 假日 / 夜間 / 春節值班時段"],
            horizontal=True
        )

        if out_of_stock_shift == "🌞 平日白天":
            st.success("📞 平日處理非常簡單：直接【電聯藥庫】處理即可！")
            st.checkbox("✅ 已電聯通知藥庫補藥")

        elif out_of_stock_shift == "🌙 假日 / 夜間 / 春節值班時段":
            st.warning("⚠️ 注意核心原則：填寫交接班紀錄單，**【無須】**打給 oncall 主管詢問！")
            st.checkbox("✍️ 已確認填寫交接班紀錄單")
            st.divider()

            med_class = st.radio(
                "💊 請問不足的藥品是哪一類？",
                ["請選擇...", "📦 一般藥品", "💉 管藥 (針劑)"],
                horizontal=True
            )

            if med_class == "📦 一般藥品":
                st.info("💡 流程：單位填單 ➔ 急診發藥 ➔ 單位盤入ADC ➔ 留單交班給藥庫")
                st.checkbox("請單位填寫【藥品處理單】給急診藥局 (原因請寫：ADC 藥品不足量)")
                st.checkbox("急診藥局進行發藥")
                st.checkbox("請單位以盤點方式入 ADC")
                st.checkbox("將「藥品處理單藥局聯」放置於【交班文件夾】中 (藥庫上班日會重新評估)")

            elif med_class == "💉 管藥 (針劑)":
                st.info("💡 流程：走換發流程 ➔ 急診發藥 (限單位領取) ➔ 單位盤入ADC")
                st.checkbox("請單位送出申請量與病人使用紀錄，並將【空瓶】送回急診藥局")
                st.checkbox("急診藥局於 ADC 調劑換發，空瓶確認無誤後可直接丟棄")
                st.error("🚨 【強制防呆】須由【單位人員】親自到急診藥局領藥，**不可由傳送領取**！")
                st.checkbox("確認由單位人員親自領走藥品")
                st.checkbox("請單位以盤點方式入 ADC，並到 HIS5 進行簽收")
                st.caption("*(後續由藥庫上班日重新評估增量)*")
# ==========================================
# 分頁 4：一般異常處理 (含藥包機切換邏輯)
# ==========================================
with tab4:
    st.header("⚠️ 主題 4：其他異常事件處理流程")
    st.caption("針對缺藥、單據異常、藥包機故障之處置")

    # 第一層：選擇異常事件
    abnormal_event = st.radio(
        "🚨 發生了什麼異常事件？",
        [
            "請選擇...", 
            "💊 缺藥 (線上/UD 找不到藥)", 
            "📄 藥袋或藥包異常 (破損/印錯/內容誤)", 
            "🤖 藥包機異常 (大小寶當機/落藥補包)"
        ],
        horizontal=True, key="main_task_4"
    )

    st.divider()

    if abnormal_event == "💊 缺藥 (線上/UD 找不到藥)":
        shift_time = st.radio("🕒 時段：", ["🌞 平日", "🌙 值班"], horizontal=True, key="short_shift")
        if shift_time == "🌞 平日":
            st.checkbox("1. 確認線上與 UD 確實無藥")
            st.checkbox("2. 告知【線上主管】")
        else:
            st.error("🚨 值班需自行至藥庫取藥")
            st.info("💡 查詢母庫儲位：請看【網頁版藥典】")
            st.checkbox("1. 至藥庫取藥並填寫【實體帳卡】")
            st.checkbox("2. 帳卡放於庫管理員桌上或待作帳盒")

    elif abnormal_event == "📄 藥袋或藥包異常 (破損/印錯/內容誤)":
        shift_time = st.radio("🕒 時段：", ["🌞 平日", "🌙 值班"], horizontal=True, key="paper_shift")
        if shift_time == "🌞 平日":
            st.checkbox("1. 告知【線上主管】")
        else:
            st.error("🚨 值班補印與通報")
            st.checkbox("1. 補印藥袋/藥包")
            st.checkbox("2. 電聯 On-call 主管")
            st.checkbox("3. 留取處方箋/總張並落實交班")

    elif abnormal_event == "🤖 藥包機異常 (大小寶當機/落藥補包)":
        machine_issue = st.radio(
            "🔍 具體狀況：",
            ["請選擇...", "💥 當機 (需切換機台)", "⚠️ 落藥 (需補包)"],
            horizontal=True, key="machine_sub"
        )
        
        if machine_issue == "💥 當機 (需切換機台)":
            st.error("🚨 **第一動作：切換機台設定 (1改2)**")
            with st.expander("🖥️ TOSHO 系統切換步驟 (大寶轉小寶)", expanded=True):
                st.markdown("""
                1. 接收系統點 **[停止接收]**
                2. 進入 **[參數設定]** -> **[資料接收]**
                3. 將 **[門診]、[首日出院]、[急診]** 從 **1 改為 2**
                4. **存檔** 並重新點 **[資料接收]** 開啟
                """)
            st.warning("🔄 **機台重啟位置**")
            st.write("🐘 **大寶**: 撕單區電腦下方櫃子主機旁")
            st.write("🐕 **小寶**: 小寶顯示面板下方")
            st.checkbox("已完成切換並嘗試重啟")

        elif machine_issue == "⚠️ 落藥 (需補包)":
            st.info("💡 **處理路徑**")
            st.code("門急診作業 ➔ 作業停止 ➔ 領藥號查詢 ➔ 補包點選")
            st.checkbox("1. 掉落藥品已清空並檢查機器")
            st.checkbox("2. 已完成填寫【補包登記表】")
# --- 邏輯 D：系統補印操作路徑手冊 (註1) ---
    st.divider()
    with st.expander("📑 系統補印與管藥紀錄表操作路徑 (註1)", expanded=False):
        st.markdown("當需要手動補印藥袋或紀錄表時，請參考以下系統設定：")
        
        print_cate = st.selectbox(
            "🔍 請選擇欲補印的處方類別：",
            [
                "請選擇...", 
                "🏥 門診、預約藥袋 / 急診 MBD", 
                "🚑 急診在院中", 
                "📦 住院出院帶藥", 
                "🛌 住院首日量", 
                "🚨 管藥使用紀錄表 (Fentanyl 貼片等)"
            ],
            key="reprint_tool"
        )
        
        if print_cate == "🏥 門診、預約藥袋 / 急診 MBD":
            st.info("**系統路徑：** 門/急診工作清單 ➔ 點入處方 ➔ 查找領藥單號")
            st.markdown("**報表名稱：** `門/急診MBD總張+藥袋-台中版` \n\n *(預約慢箋適用)*")
            
        elif print_cate == "🚑 急診在院中":
            st.info("**系統路徑：** 急診工作清單 ➔ 點入處方 ➔ 查找領藥單號")
            st.markdown("**報表名稱：** `急診總張+藥袋(在院中)-台中版`")
            
        elif print_cate == "📦 住院出院帶藥":
            st.info("**系統路診：** 住院工作清單 ➔ 輸入床號 ➔ 類別：[出院帶藥] ➔ 篩選")
            st.markdown("**報表名稱：** `住院MBD藥袋-台中版`")
            
        elif print_cate == "🛌 住院首日量":
            st.info("**系統路徑：** 住院工作清單 ➔ 輸入床號")
            st.markdown("**報表名稱：** `住院ON-LINE藥袋(大)-台中版-多藥一袋`")
            
        elif print_cate == "🚨 管藥使用紀錄表 (Fentanyl 貼片等)":
            st.warning("⚠️ 平日時段請洽【線上主管】；值班時段若無自動列印才執行補印。")
            st.info("**路徑：** 共用服務 ➔ 報表 ➔ 選擇欲印項目")
            st.markdown("""
            1. **住院出院：** `管制貼片劑使用紀錄表(出院)`
            2. **在院中/門診：** `管制貼片劑使用紀錄表`
            """)
            st.error("🚨 **列印重點：** 輸出 PDF 後，列印地點務必選擇 **[Pbag 8]** (急診藥局管制藥印表機)")
# 這裡接原本的頁尾 (st.sidebar...)

st.sidebar.info(f"📅 系統執行日：{datetime.date.today()}")
st.sidebar.caption("⚡ 本系統僅供 SOP 快速核對使用，實際操作請依醫院規範為準。")
