from Repository.conversation_repository import save_conversation, get_conversations_by_user
from Services.genetic_algorithm_service import generate_optimal_study

def generate_answer(question, current_level='beginner'):
    question = question.strip().lower()

    return generate_optimal_study(question, current_level)

def process_question(username, question, current_level='beginner'):
    answer = generate_answer(question, current_level)
    save_conversation(username, question, answer)

    return answer

def get_user_history(username):
    return get_conversations_by_user(username).history()