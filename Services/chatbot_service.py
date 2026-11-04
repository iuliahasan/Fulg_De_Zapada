from Repository.conversation_repository import save_conversation

def process_question(user_id, question):
 answer = generate_answer(question)
 save_conversation(user_id, question, answer)

 return answer

def generate_answer(question):
    question = question.lower().strip()

