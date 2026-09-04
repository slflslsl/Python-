#%%
#키오스크
window_width = 40
store_name = input("   안녕하세요 업주님😎\n     여기에 업소명을 입력해주세요!: ").strip()
welcome_message = f"반갑습니다 고객님!\n      행복을 드리는 {store_name}입니다💕"
print("-" * window_width)
print(welcome_message.center(window_width))
print("-" * window_width)

customer_name = input("상품이 준비되면 저희 스태프가 고객님의 성함을 불러드립니다🔊\n 성함을 입력해주세요!(닉네임 가능): ").strip()
print(f"{customer_name} 님이군요?!\n 기억할게요👌")

menu_name = input("📌주문할 메뉴를 선택해주세요!: ").strip()
size = input("📌사이즈를 선택해주세요!\n (저희는 middle, big, ultra 세 사이즈가 있어요!: ").strip()
quantity = int(input("📌상품의 갯수를 골라주세요!\n (현재 +1 행사중입니다!: "))

event_quantity = quantity + 1

print(f"{customer_name} 님!\n주문이 완료되었습니다🎉")
print(f"{customer_name} 님의 주문 내역은 아래와 같습니다.")
print(f"{menu_name}의 {size}사이즈를 {quantity}개 주문하셨습니다.")
print(f"현재 +1 행사 중이라 {menu_name}의 {size}사이즈를 {event_quantity}개 준비하겠습니다.")
print("편하신 곳에서 잠시만 기다려주세요⌛")

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