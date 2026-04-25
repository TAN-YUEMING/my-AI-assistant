from assistant import PersonalAssistant

def main():
    print("안녕하세요! 나만의 맞춤형 AI 비서입니다")
    assistant = PersonalAssistant()
    
    while True:
        user_input = input("\n말씀해주세요: ")
        if user_input.lower() in ["종료", "exit", "quit"]:
            print("안녕히 가세요!")
            break
        response = assistant.respond(user_input)
        print(f"비서: {response}")

if __name__ == "__main__":
    main()
