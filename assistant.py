class PersonalAssistant:
    def __init__(self):
        self.income = 0    # 이번 달 수입
        self.expense = 0   # 이번 달 지출

    def respond(self, message: str) -> str:
        # 수입 추가
        if "수입" in message and "추가" in message:
            try:
                amount = int(message.replace("수입", "").replace("추가", "").strip())
                self.income += amount
                return f"수입 {amount}원이 추가되었습니다. 이번 달 총 수입: {self.income}원"
            except:
                return "숫자를 입력하세요. 예: 수입 5000 추가"

        # 지출 추가
        elif "지출" in message and "추가" in message:
            try:
                amount = int(message.replace("지출", "").replace("추가", "").strip())
                self.expense += amount
                return f"지출 {amount}원이 추가되었습니다. 이번 달 총 지출: {self.expense}원"
            except:
                return "숫자를 입력하세요. 예: 지출 3000 추가"

        # 이번 달 결산
        elif "결산" in message or "남은 돈" in message or "이번 달 요약" in message:
            remaining = self.income - self.expense
            return f"이번 달 수입: {self.income}원, 지출: {self.expense}원, 남은 돈: {remaining}원"

        # 수입 확인
        elif "수입" in message and ("얼마" in message or "총" in message):
            return f"이번 달 총 수입: {self.income}원"

        # 지출 확인
        elif "지출" in message and ("얼마" in message or "총" in message):
            return f"이번 달 총 지출: {self.expense}원"

        # 인사
        elif "안녕" in message:
            return "안녕하세요! 이번 달 수입과 지출을 기록해 드립니다. 예: 수입 5000 추가, 지출 3000 추가, 결산"

        # 기본 응답
        else:
            return f"사용 가능한 명령어: 수입 [금액] 추가, 지출 [금액] 추가, 결산, 수입 얼마, 지출 얼마, 안녕"
