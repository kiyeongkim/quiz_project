from openai import OpenAI
import json

client = OpenAI()


def generate_quiz(topic, num_questions, max_length=40):
    prompt = f"주제: {topic}\n\n상식 퀴즈 문제와 답을 {num_questions}개 작성해 주세요. 각 문제의 글자 수는 {max_length}자를 넘지 않게 해 주세요. 각 문제에는 답변도 포함되어야 합니다. 형식은 다음과 같습니다.\n문제: [문제 내용]\n답변: [답변 내용]\n"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    # 응답에서 퀴즈 추출
    quiz_text = response.choices[0].message.content.strip()
    questions = []
    for qa_pair in quiz_text.split("\n문제: "):
        if qa_pair.strip():  # 빈 문자열 방지
            qa_pair = "문제: " + qa_pair.strip()  # 포맷 맞추기
            try:
                question = qa_pair.split("답변: ")[0].replace("문제: ", "").strip()
                answer = qa_pair.split("답변: ")[1].strip()
                questions.append({"question": question, "answer": answer})
            except IndexError:
                print(f"Skipping invalid pair: {qa_pair}")

    return {"topic": topic, "quiz": questions}


def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def openai_quiz():
    topic = input("퀴즈 주제를 선택하세요 (문화&예술, 역사, 과학, 정치&경제): ")
    num_questions = input("생성할 퀴즈 갯수를 입력하세요: ")
    quiz = generate_quiz(topic, num_questions)
    save_to_json(quiz, "./assets/quiz.json")
    print(f"{topic} 주제의 퀴즈 {num_questions}개 생성 완료했습니다")
