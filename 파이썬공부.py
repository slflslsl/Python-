#%%
# 키오스크
# 1. 초기 데이터 및 메시지 설정
PRICE_DICT = {'아메리카노': 2000, '라떼': 2500, '주스': 3000}
INVENTORY_DICT = {'아메리카노': 10, '라떼': 5, '주스': 7}
MENU_NAMES = list(PRICE_DICT.keys())
SALES = 0

MSG_ENTER = "* 엔터를 누르면 장바구니로 이동합니다."
MSG_INPUT_MENU = "주문할 메뉴 번호 입력 >> "
MSG_INPUT_COUNT = "수량 입력 >> "

# 2. 키오스크 전체 메인 루프 (재고가 1개라도 남아있는 동안 실행)
while sum(INVENTORY_DICT.values()) > 0:
    print("\n안녕하세요! 카페입니다.")
    print("=== 메뉴판 ===")
    for i, menu in enumerate(MENU_NAMES):
        print(f"{i+1}. {menu} : {PRICE_DICT[menu]}원 (재고: {INVENTORY_DICT[menu]}개)")

    # 손님별 장바구니 생성
    cart = {menu: 0 for menu in MENU_NAMES}

    # 3. 주문 입력 루프
    while True:
        print(MSG_ENTER)
        menu_num = input(MSG_INPUT_MENU)

        # 엔터 입력 시 주문 선택 종료 -> 결제/처리 단계로 이동
        if menu_num == "":
            break

        # 숫자 변환 및 인덱스 계산
        menu_idx = int(menu_num) - 1
        selected_menu = MENU_NAMES[menu_idx]

        # 수량 입력 루프
        while True:
            count = int(input(MSG_INPUT_COUNT))
            if count <= INVENTORY_DICT[selected_menu]:
                cart[selected_menu] += count
                break
            else:
                print("재고가 부족합니다. 다시 입력해 주세요.")

    # 4. 주문 처리 및 재고/매출 업데이트
    print("\n[주문 접수 중...]")
    for menu in MENU_NAMES:
        order_qty = cart[menu]
        INVENTORY_DICT[menu] -= order_qty
        SALES += order_qty * PRICE_DICT[menu]

    print("주문이 성공적으로 완료되었습니다!")
    del cart  # 장바구니 초기화/삭제

# 5. 영업 종료
print("\n모든 재고가 소진되어 영업을 종료합니다.")
print(f"오늘의 총 매출: {SALES}원")

#%%
#사전
print("指す : 가리키다, 示す : 보여주다, 나타내다, 表す : 표현하다")
vocab = {
    "指す": {
        "reading": "さす(sasu) = 사스",
        "meaning": "가리키다",
        "example": "彼は地図を指して、道を教えた。(그는 지도를 가리키며 길을 알려줬다.)"
    },
    "示す": {
        "reading": "しめす(shimesu) = 시메스",
        "meaning": "보여주다, 나타내다",
        "example": "データは改善を示している。(데이터는 개선을 보여주고 있다.)"
    },
    "表す": {
        "reading": "あらわす(arawasu) = 아라와스",
        "meaning": "표현하다",
        "example": "彼女は感情を言葉で表した。(그녀는 감정을 말로 표현했다.)"
    }
}

search_word = input("🔍 자세히 볼 일본어 단어를 입력하세요: ")

if search_word in vocab:
    print(f"📖 '{search_word}'")
    print(f"   발음: {vocab[search_word]['reading']}") 
    print(f"   뜻: {vocab[search_word]['meaning']}")
    print(f"   예문: {vocab[search_word]['example']}")
else:
    print(f"❌ '{search_word}'는 단어장에 없습니다. 😢")