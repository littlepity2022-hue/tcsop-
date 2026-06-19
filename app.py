import streamlit as st

# 設定網頁標題與寬度
st.set_page_config(page_title="SOP 智能核對系統", page_icon="📋", layout="centered")

st.title("⚡ 極速 SOP 智能核對系統")
st.caption("把複雜的長篇大論，變成 5 秒內能完成的互動防呆表單")

# 建立分頁
tab1, tab2 = st.tabs(["🌟 頂級 SOP 示範 (首日量審核)", "📝 貼上新 SOP 自動轉換"])

# ==========================================
# 分頁 1：針對你提供的「首日量審核」客製化的頂級介面
# ==========================================
with tab1:
    st.header("📋 主題：首日量審核")
    
    # 模塊 1：基礎流程
    st.subheader("1️⃣ 基礎流程")
    step1 = st.checkbox("✅ 刷取藥袋/餐包上 QR code")
    
    if step1:
        # 模塊 2：動態情境判斷
        st.subheader("2️⃣ 處方退藥流程")
        
        # --- 新增：系統退藥操作步驟 (使用折疊面板，保持畫面乾淨) ---
        with st.expander("💻 點此查看：系統退藥操作步驟 (步驟 1~3)", expanded=False):
            st.info("💡 依照以下路徑於系統操作：")
            st.markdown("""
            **步驟 1：一般退藥收藥**
            👉 路徑：`住院調劑` ➔ `退藥-收藥作業`
            * 刷取藥袋條碼，輸入實收量並暫存。
            
            **步驟 2：特殊藥品退藥**
            👉 路徑：`特殊藥品系統` ➔ `特殊藥品系統-退藥`
            * 勾選欲退藥之品項 (如：UD過檔、首日量等)。
            
            **步驟 3：入庫**
            * 實體藥品入 ADC。
            """)
        # --------------------------------------------------------

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

        # --- 新增：模塊 5 - 8C中繼站 (結合防呆邏輯) ---
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
        # -----------------------------------------------

        st.divider()

        # 模塊 4：冷藏藥品
        st.subheader("4️⃣ ❄️ 冷藏藥品處理")
        col1, col2 = st.columns(2)
        with col1:
            st.checkbox("將藥品放置於冰箱")
        with col2:
            st.checkbox("於護理站貼『有冷藏藥』磁鐵提醒")

        st.divider()

        # 模塊 5：管制藥品 
        st.subheader("5️⃣ 🚨 管制藥 1-3 級")
        st.checkbox("紀錄單放藥袋內，簽收單釘藥袋上，放於『管制藥待領』籃")
        st.checkbox("確認傳送/護理端領藥紀錄時間並繳回，歸於『管單』籃")
        
        with st.expander("👉 點此展開：管制藥貼片 (Fentanyl) 嚴格核發流程", expanded=False):
            st.write("非 New pt 需有廢片及使用紀錄表才可核發：")
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
# 分頁 2：通用文本轉 Checklist 工具
# ==========================================
with tab2:
    st.header("📝 貼上 SOP，自動轉成 Checklist")
    st.write("未來遇到新 SOP，貼在下方，系統會依據換行自動生成核對表。")
    
    raw_text = st.text_area("請在此貼上 SOP 文字：", height=200)
    
    if st.button("✨ 瞬間轉換成 Checklist"):
        if raw_text:
            st.divider()
            st.subheader("✅ 您的專屬核對表：")
            lines = raw_text.split('\n')
            for line in lines:
                clean_line = line.strip()
                if clean_line:
                    st.checkbox(clean_line, key=clean_line)
            st.success("轉換完成！您可以直接開始點擊核對。")
        else:
            st.warning("請先貼上文字！")
