from Repository.conversation_repository import save_conversation, get_conversations_by_user
from Services.genetic_algorithm_service import generate_optimal_study
from Database.database import get_connection

# MAPEK Diagram

# Knowledge (K)
def _update_user_level_in_db(username, new_level):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("UPDATE Utilizatori SET current_level = :1 WHERE username = :2",
                       [new_level, username])
        connection.commit()
    finally:
        cursor.close()
        connection.close()

# Monitor (M)
def monitor_interaction(username, question):
    history = get_conversations_by_user(username)

    return {
        'username' : username,
        'question' : question,
        'no_of_interactions' : len(history),
        'history' : history
    }

# Analyze (A)
def analyze_progress(monitored_data, current_level):
    total = monitored_data['no_of_interactions']
    new_level = current_level

    if total >= 10 and current_level == 'intermediate':
        new_level = 'advanced'
    elif total >= 5 and current_level == 'beginner':
        new_level = 'intermediate'

    level_changed = (new_level != current_level)

    return {
        'recommended_level' : new_level,
        'level_changed' : level_changed,
        'question' : monitored_data['question']
    }

# Plan (P)
def plan_response(analysis_result):
    question = analysis_result['question']
    target_level = analysis_result['recommended_level']
    planned_content = generate_optimal_study(question, target_level)

    if analysis_result['level_changed']:
        prefix = f'Felicitari! Ai avansat la nivelul {target_level.upper()}\n\n'
        return prefix + planned_content

    return planned_content

# Execute (E)
def execute_action(username, question, planned_answer, analysis_result):
    if analysis_result['level_changed']:
        _update_user_level_in_db(username, analysis_result['recommended_level'])

    save_conversation(username, question, planned_answer)

    return planned_answer

def generate_answer(question, current_level='beginner'):
    question = question.strip().lower()

    return generate_optimal_study(question, current_level)

def process_question(username, question, current_level='beginner'):
    monitored_data = monitor_interaction(username, question)
    analysis_result = analyze_progress(monitored_data, current_level)
    planned_answer = plan_response(analysis_result)
    final_answer = execute_action(username, question, planned_answer, analysis_result)

def get_user_history(username):
    return get_conversations_by_user(username)