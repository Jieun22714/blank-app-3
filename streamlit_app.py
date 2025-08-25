import streamlit as st

# -------------------------------
# 앱 기본 설정
# -------------------------------
st.set_page_config(page_title="내 취향 남자 아이돌 찾기", page_icon="🎤")

st.title("🎤 내 취향 남자 아이돌 찾기")
st.write("간단한 설문을 통해 당신의 취향에 맞는 남자 아이돌을 찾아드립니다!")

# -------------------------------
# 설문 입력 UI
# -------------------------------
st.subheader("1️⃣ 얼굴 상")
face_type = st.radio(
    "어떤 얼굴 상을 선호하나요?",
    ["강아지상", "고양이상", "공룡상", "여우상"]
)

st.subheader("2️⃣ 키")
height_preference = st.radio(
    "선호하는 키는?",
    ["작은 편(170cm 이하)", "보통(171~179cm)", "큰 편(180cm 이상)"]
)

st.subheader("3️⃣ 성격")
personality = st.radio(
    "어떤 성격을 좋아하나요?",
    ["장난꾸러기", "카리스마", "다정함", "시크함", "귀여움", "리더십"]
)

# -------------------------------
# 아이돌 데이터베이스 (샘플)
# -------------------------------
idols = [
    # BTS
    {"name": "정국 (BTS)", "birth": "1997-09-01", "face": "강아지상", "height": "보통(171~179cm)", "personality": "장난꾸러기", "instagram": "https://www.instagram.com/jungkook_bighitentertainment/", "x": "https://x.com/BTS_twt"},
    {"name": "뷔 (BTS)", "birth": "1995-12-30", "face": "여우상", "height": "큰 편(180cm 이상)", "personality": "시크함", "instagram": "https://www.instagram.com/thv/", "x": "https://x.com/v_bts"},
    {"name": "RM(BTS)", "birth": "1994-09-12", "face": "공룡상", "height": "큰 편(180cm 이상)", "personality": "리더십", "instagram": "https://www.instagram.com/bumzu_official/", "x": "https://x.com/rm_bts"},
    {"name": "진 (BTS)", "birth": "1992-12-04", "face": "여우상", "height": "큰 편(180cm 이상)", "personality": "다정함", "instagram": "https://www.instagram.com/jin/", "x": "https://x.com/jin_bts"},
    {"name": "슈가 (BTS)", "birth": "1993-03-09", "face": "고양이상", "height": "보통(171~179cm)", "personality": "시크함", "instagram": "https://www.instagram.com/agustd/", "x": "https://x.com/suga_bts"},
    {"name": "제이홉 (BTS)", "birth": "1994-02-18", "face": "강아지상", "height": "보통(171~179cm)", "personality": "장난꾸러기", "instagram": "https://www.instagram.com/uhope/", "x": "https://x.com/jhope_bts"},
    {"name": "지민 (BTS)", "birth": "1995-10-13", "face": "강아지상", "height": "보통(171~179cm)", "personality": "다정함", "instagram": "https://www.instagram.com/jm/", "x": "https://x.com/jimin_bts"},



    # ASTRO
    {"name": "차은우 (ASTRO)", "birth": "1997-03-30", "face": "고양이상", "height": "큰 편(180cm 이상)", "personality": "다정함", "instagram": "https://www.instagram.com/eunwo.o_c/", "x": "https://x.com/offclASTRO"},

    # EXO
    {"name": "백현 (EXO)", "birth": "1992-05-06", "face": "여우상", "height": "보통(171~179cm)", "personality": "시크함", "instagram": "https://www.instagram.com/baekhyunee_exo/", "x": "https://x.com/weareoneEXO"},

    # ENHYPEN
    {"name": "정원 (ENHYPEN)", "birth": "2004-02-09", "face": "강아지상", "height": "보통(171~179cm)", "personality": "다정함", "instagram": "https://www.instagram.com/enhypen/", "x": "https://x.com/ENHYPEN"},
    {"name": "희승 (ENHYPEN)", "birth": "2001-10-15", "face": "여우상", "height": "큰 편(180cm 이상)", "personality": "카리스마", "instagram": "https://www.instagram.com/enhypen/", "x": "https://x.com/ENHYPEN"},
    {"name": "제이 (ENHYPEN)", "birth": "2002-04-20", "face": "고양이상", "height": "큰 편(180cm 이상)", "personality": "시크함", "instagram": "https://www.instagram.com/enhypen/", "x": "https://x.com/ENHYPEN"},
    {"name": "제이크 (ENHYPEN)", "birth": "2002-11-15", "face": "강아지상", "height": "보통(171~179cm)", "personality": "장난꾸러기", "instagram": "https://www.instagram.com/enhypen/", "x": "https://x.com/ENHYPEN"},
    {"name": "성훈 (ENHYPEN)", "birth": "2002-12-08", "face": "공룡상", "height": "큰 편(180cm 이상)", "personality": "시크함", "instagram": "https://www.instagram.com/enhypen/", "x": "https://x.com/ENHYPEN"},
    {"name": "선우 (ENHYPEN)", "birth": "2003-06-24", "face": "강아지상", "height": "보통(171~179cm)", "personality": "귀여움", "instagram": "https://www.instagram.com/enhypen/", "x": "https://x.com/ENHYPEN"},
    {"name": "니키 (ENHYPEN)", "birth": "2005-12-09", "face": "공룡상", "height": "큰 편(180cm 이상)", "personality": "카리스마", "instagram": "https://www.instagram.com/enhypen/", "x": "https://x.com/ENHYPEN"},

    # Stray Kids
    {"name": "방찬 (Stray Kids)", "birth": "1997-10-03", "face": "강아지상", "height": "보통(171~179cm)", "personality": "리더십", "instagram": "https://www.instagram.com/realstraykids/", "x": "https://x.com/Stray_Kids"},
    {"name": "리노 (Stray Kids)", "birth": "1998-10-25", "face": "고양이상", "height": "보통(171~179cm)", "personality": "시크함", "instagram": "https://www.instagram.com/realstraykids/", "x": "https://x.com/Stray_Kids"},
    {"name": "창빈 (Stray Kids)", "birth": "1999-08-11", "face": "공룡상", "height": "작은 편(170cm 이하)", "personality": "카리스마", "instagram": "https://www.instagram.com/realstraykids/", "x": "https://x.com/Stray_Kids"},
    {"name": "현진 (Stray Kids)", "birth": "2000-03-20", "face": "여우상", "height": "큰 편(180cm 이상)", "personality": "시크함", "instagram": "https://www.instagram.com/hyunjin/", "x": "https://x.com/Stray_Kids"},
    {"name": "한 (Stray Kids)", "birth": "2000-09-14", "face": "강아지상", "height": "작은 편(170cm 이하)", "personality": "장난꾸러기", "instagram": "https://www.instagram.com/realstraykids/", "x": "https://x.com/Stray_Kids"},
    {"name": "필릭스 (Stray Kids)", "birth": "2000-09-15", "face": "고양이상", "height": "보통(171~179cm)", "personality": "다정함", "instagram": "https://www.instagram.com/realstraykids/", "x": "https://x.com/Stray_Kids"},
    {"name": "승민 (Stray Kids)", "birth": "2000-09-22", "face": "강아지상", "height": "큰 편(180cm 이상)", "personality": "다정함", "instagram": "https://www.instagram.com/realstraykids/", "x": "https://x.com/Stray_Kids"},
    {"name": "아이엔 (Stray Kids)", "birth": "2001-02-08", "face": "강아지상", "height": "보통(171~179cm)", "personality": "귀여움", "instagram": "https://www.instagram.com/realstraykids/", "x": "https://x.com/Stray_Kids"},

    # POW
    {"name": "Yorch (POW)", "birth": "2002-04-28", "face": "여우상", "height": "큰 편(180cm 이상)", "personality": "시크함", "instagram": "https://www.instagram.com/pow_grid/", "x": "https://x.com/POW_grid"},
    {"name": "현빈 (POW)", "birth": "2002-01-26", "face": "강아지상", "height": "큰 편(180cm 이상)", "personality": "다정함", "instagram": "https://www.instagram.com/pow_grid/", "x": "https://x.com/POW_grid"},
    {"name": "정빈 (POW)", "birth": "2003-04-05", "face": "강아지상", "height": "보통(171~179cm)", "personality": "장난꾸러기", "instagram": "https://www.instagram.com/pow_grid/", "x": "https://x.com/POW_grid"},
    {"name": "동연 (POW)", "birth": "2003-06-01", "face": "공룡상", "height": "큰 편(180cm 이상)", "personality": "카리스마", "instagram": "https://www.instagram.com/pow_grid/", "x": "https://x.com/POW_grid"},
    {"name": "홍 (POW)", "birth": "2004-02-15", "face": "고양이상", "height": "보통(171~179cm)", "personality": "귀여움", "instagram": "https://www.instagram.com/pow_grid/", "x": "https://x.com/POW_grid"},
    

    {"name": "태용 (NCT 127)", "birth": "1995-07-01", "face": "여우상", "height": "큰 편(180cm 이상)", "personality": "카리스마", "instagram": "https://www.instagram.com/taeoxo_nct/", "x": "https://x.com/taeyong"},
    {"name": "쟈니 (NCT 127)", "birth": "1995-02-09", "face": "고양이상", "height": "보통(171~179cm)", "personality": "다정함", "instagram": "https://www.instagram.com/johnnyjsj_/", "x": "https://x.com/johnny"},
    {"name": "유타 (NCT 127)", "birth": "1995-10-26", "face": "강아지상", "height": "보통(171~179cm)", "personality": "장난꾸러기", "instagram": "https://www.instagram.com/yuu_taa_1026/", "x": "https://x.com/yuta"},
    {"name": "쿤 (Way V)", "birth": "1996-01-01", "face": "고양이상", "height": "보통(171~179cm)", "personality": "다정함", "instagram": "https://www.instagram.com/kun11xd/", "x": "https://x.com/kun"},
    {"name": "도영 (NCT 127)", "birth": "1996-02-01", "face": "여우상", "height": "보통(171~179cm)", "personality": "다정함", "instagram": "https://www.instagram.com/do0_nct/", "x": "https://x.com/doyoung"},
    {"name": "텐 (Way V)", "birth": "1996-02-27", "face": "고양이상", "height": "보통(171~179cm)", "personality": "시크함", "instagram": "https://www.instagram.com/tenlee_1001/", "x": "https://x.com/ten"},
    {"name": "재현 (NCT 127)", "birth": "1997-02-14", "face": "여우상", "height": "큰 편(180cm 이상)", "personality": "다정함", "instagram": "https://www.instagram.com/nctjaehyun_/", "x": "https://x.com/jaehyun"},
    {"name": "윈윈 (Way V)", "birth": "1997-10-28", "face": "고양이상", "height": "보통(171~179cm)", "personality": "시크함", "instagram": "https://www.instagram.com/winwin_xiaojun/", "x": "https://x.com/winwin"},
    {"name": "정우 (NCT 127)", "birth": "1998-02-19", "face": "강아지상", "height": "보통(171~179cm)", "personality": "다정함", "instagram": "https://www.instagram.com/nct_dream/", "x": "https://x.com/jungwoo"},
    {"name": "마크 (NCT Dream)", "birth": "1999-08-02", "face": "강아지상", "height": "보통(171~179cm)", "personality": "장난꾸러기", "instagram": "https://www.instagram.com/onyourm__ark/", "x": "https://x.com/mark"},
    {"name": "샤오쥔 (Way V)", "birth": "1999-08-08", "face": "고양이상", "height": "보통(171~179cm)", "personality": "다정함", "instagram": "https://www.instagram.com/xiaojun_wayv/", "x": "https://x.com/xiaojun"},
    {"name": "헨드리 (Way V)", "birth": "1999-06-28", "face": "강아지상", "height": "보통(171~179cm)", "personality": "장난꾸러기", "instagram": "https://www.instagram.com/hendery_127/", "x": "https://x.com/hendery"},
    {"name": "런쥔 (NCT Dream)", "birth": "2000-03-23", "face": "고양이상", "height": "보통(171~179cm)", "personality": "다정함", "instagram": "https://www.instagram.com/renjun_jm/", "x": "https://x.com/renjun"},
    {"name": "제노 (Jeno)", "birth": "2000-04-23", "face": "강아지상", "height": "큰 편(180cm 이상)", "personality": "장난꾸러기", "instagram": "https://www.instagram.com/jeno_nct/", "x": "https://x.com/jeno"},
    {"name": "해찬 (NCT Dream)", "birth": "2000-06-06", "face": "고양이상", "height": "보통(171~179cm)", "personality": "다정함", "instagram": "https://www.instagram.com/nct_dream/", "x": "https://x.com/haechan"},
    {"name": "재민 (NCT Dream)", "birth": "2000-08-13", "face": "여우상", "height": "보통(171~179cm)", "personality": "시크함", "instagram": "https://www.instagram.com/na.jaemin_ct/", "x": "https://x.com/jaemin"},
    {"name": "양양 (Way V)", "birth": "2000-10-10", "face": "강아지상", "height": "보통(171~179cm)", "personality": "장난꾸러기", "instagram": "https://www.instagram.com/yangyang_x2/", "x": "https://x.com/yangyang"},
    {"name": "천러 (NCT Dream)", "birth": "2001-11-22", "face": "고양이상", "height": "보통(171~179cm)", "personality": "다정함", "instagram": "https://www.instagram.com/nct_dream/", "x": "https://x.com/chenle"},
    {"name": "지성 (NCT Wish)", "birth": "2002-02-05", "face": "강아지상", "height": "보통(171~179cm)", "personality": "장난꾸러기", "instagram": "https://www.instagram.com/nct_dream/", "x": "https://x.com/jisung"},
    {"name": "시온 (NCT Wish)", "birth": "2002-03-09", "face": "고양이상", "height": "보통(171~179cm)", "personality": "다정함", "instagram": "https://www.instagram.com/nctwish_official/", "x": "https://x.com/sion"},
    {"name": "리쿠 (NCT Wish)", "birth": "2002-04-17", "face": "강아지상", "height": "보통(171~179cm)", "personality": "장난꾸러기", "instagram": "https://www.instagram.com/nctwish_official/", "x": "https://x.com/riku"},
    {"name": "유시 (NCT Wish)", "birth": "2002-05-25", "face": "고양이상", "height": "보통(171~179cm)", "personality": "시크함", "instagram": "https://www.instagram.com/nctwish_official/", "x": "https://x.com/yushi"},
    {"name": "재희 (NCT Wish)", "birth": "2002-06-10", "face": "강아지상", "height": "큰 편(180cm 이상)", "personality": "다정함", "instagram": "https://www.instagram.com/nctwish_official/", "x": "https://x.com/jaehee"},
    {"name": "료 (NCT Wish)", "birth": "2002-07-15", "face": "강아지상", "height": "보통(171~179cm)", "personality": "장난꾸러기", "instagram": "https://www.instagram.com/nctwish_official/", "x": "https://x.com/ryo"},
    {"name": "사쿠야 (NCT Wish)", "birth": "2002-08-20", "face": "고양이상", "height": "보통(171~179cm)", "personality": "시크함", "instagram": "https://www.instagram.com/nctwish_official/", "x": "https://x.com/sakuya"},

    {"name": "케이 (K)", "birth": "1997-10-21", "face": "여우상", "height": "큰 편(180cm 이상)", "personality": "시크함", "instagram": "https://www.instagram.com/andteam_official/", "x": "https://x.com/andteam_k"},
    {"name": "후마 (Fuma)", "birth": "1998-06-29", "face": "고양이상", "height": "보통(171~179cm)", "personality": "다정함", "instagram": "https://www.instagram.com/andteam_official/", "x": "https://x.com/andteam_fuma"},
    {"name": "니콜라스 (Nicolas)", "birth": "2002-07-09", "face": "강아지상", "height": "보통(171~179cm)", "personality": "장난꾸러기", "instagram": "https://www.instagram.com/andteam_official/", "x": "https://x.com/andteam_nicolas"},
    {"name": "의주 (Uijoo)", "birth": "2002-09-07", "face": "여우상", "height": "큰 편(180cm 이상)", "personality": "다정함", "instagram": "https://www.instagram.com/andteam_official/", "x": "https://x.com/andteam_uijoo"},
    {"name": "유마 (Yuma)", "birth": "2004-02-07", "face": "고양이상", "height": "보통(171~179cm)", "personality": "다정함", "instagram": "https://www.instagram.com/andteam_official/", "x": "https://x.com/andteam_yuma"},
    {"name": "조 (Jo)", "birth": "2004-07-08", "face": "강아지상", "height": "큰 편(180cm 이상)", "personality": "ekwjdgka", "instagram": "https://www.instagram.com/andteam_official/", "x": "https://x.com/andteam_jo"},
    {"name": "하루아 (Harua)", "birth": "2005-05-01", "face": "여우상", "height": "작은 편(170cm 이하)", "personality": "시크함", "instagram": "https://www.instagram.com/andteam_official/", "x": "https://x.com/andteam_harua"},
    {"name": "타키 (Taki)", "birth": "2005-05-04", "face": "고양이상", "height": "보통(171~179cm)", "personality": "다정함", "instagram": "https://www.instagram.com/andteam_official/", "x": "https://x.com/andteam_taki"},
    {"name": "마키 (Maki)", "birth": "2006-02-17", "face": "강아지상", "height": "큰 편(180cm 이상)", "personality": "장난꾸러기", "instagram": "https://www.instagram.com/andteam_official/", "x": "https://x.com/andteam_maki"},
]

# -------------------------------
# 매칭 로직 (조건에 맞는 모든 아이돌 반환)
# -------------------------------
def find_matches(face, height, personality):
    matches = []
    for idol in idols:
        face_match = idol["face"] == face
        height_match = height in idol["height"]
        personality_match = personality in idol["personality"]

        if face_match and height_match and personality_match:
            matches.append(idol)
    return matches

# -------------------------------
# 결과 버튼
# -------------------------------
if st.button("✨ 설문조사 완료! 아이돌 찾기 ✨"):
    matches = find_matches(face_type, height_preference, personality)
    
    if matches:
        st.success(f"조건에 맞는 아이돌 {len(matches)}명을 찾았어요! 🎉")
        for match in matches:
            st.write(f"👤 이름: {match['name']}")
            st.write(f"🎂 생년월일: {match['birth']}")
            st.write(f"📸 [Instagram]({match['instagram']})")
            st.write(f"🐦 [X(구 트위터)]({match['x']})")
            st.write("---")
    else:
        st.warning("아쉽게도 조건에 딱 맞는 아이돌은 없네요. 😢")
