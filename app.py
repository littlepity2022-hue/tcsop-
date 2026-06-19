import streamlit as st
import datetime

# 1. 設定網頁標題與寬度
st.set_page_config(page_title="SOP 智能核對系統", page_icon="📋", layout="centered")

st.title("⚡ 極速 SOP 智能核對系統")
st.caption("把複雜的長篇大論，變成 5 秒內能完成的互動防呆表單")

# 2. 建立分頁 (新增了 HAH 分頁)
tab1, tab2, tab3, tab4 = st.tabs(["1️⃣ 首日量審核", "2️⃣ 核發作業中心", "🏠 3️⃣ HAH 居家醫療", "📝 貼上新 SOP"])

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
            "🚑 急診發藥注意事項"
        ],
        horizontal=True
    )
    
    st.divider()

    if dispense_type == "💊 單位請領管制藥":
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

# ==========================================
# 分頁 3：HAH 居家在宅醫療 (本次新增內容)
# ==========================================
with tab3:
    st.header("🏠 HAH 居家在宅醫療：二院區 B1 領藥")
    
    # 區分時間段（核心防呆）
    opd_time = st.radio(
        "🕒 請確認當前時段：",
        ["平日正常門診 (09:00 - 21:00)", "週六半日/週日/國定假日 (含停診時段)"],
        horizontal=True
    )

    st.divider()

    if opd_time == "平日正常門診 (09:00 - 21:00)":
        st.subheader("📦 處理方式：一院區轉送二院區")
        st.info("💡 流程重點：第一院區主管派人送藥 ➔ 二院區中藥局核發")
        
        st.checkbox("1. 確認一院區傳送已將藥品送達二院區")
        st.checkbox("2. 點收完畢，將藥品放置於【HAH 居家在宅醫療專用藥盒】內")
        
        st.markdown("#### 🚪 領藥窗口分配 (B1 窗口)")
        # 顯示當前時間參考
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
        st.subheader("🚑 假日/停診處理：急診藥局窗口")
        st.error("🚨 注意：此時段統一由『急診藥局』辦理核發！")
        
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

# ==========================================
# 分頁 4：通用文本轉 Checklist 工具
# ==========================================
with tab4:
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
