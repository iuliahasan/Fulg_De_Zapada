import random

from Database.database import get_connection

def _fetch_modules_from_db(topic_filter):
    connection = get_connection()
    cursor = connection.cursor()
    modules = []

    try:
        query = '''SELECT module_id, topic, title, difficulty, duration_minutes
            FROM Study_Modules WHERE LOWER(topic) LIKE :1 or LOWER(title) LIKE :1'''
        cursor.execute(query, [f"%{topic_filter}%"])

        for row in cursor.fetchall():
            modules.append(
                {'module_id': row[0],
                 'topic': row[1],
                 'title': row[2],
                 'difficulty': row[3],
                 'duration_minutes': row[4]
                }
            )

        if not modules:
            cursor.execute('''SELECT module_it, topic, title, 
            difficulty, duration_minutes FROM Study_Modules''')

            for row in cursor.fetchall():
                modules.append(
                    {'module_id': row[0],
                     'topic': row[1],
                     'title': row[2],
                     'difficulty': row[3],
                     'duration_minutes': row[4]
                    }
                )

            return modules
    finally:
        cursor.close()
        connection.close()

def generate_optimal_study(question, current_level='beginner', max_time=90):
    topic = ''
    for word in ['python', 'sql', 'oracle', 'retele', 'algoritmi']:
        if word in question.lower():
            topic = word
            break

    modules = _fetch_modules_from_db(topic)

    if not modules:
        return 'Nu exista module de studiu dispnibile in baza de date'

    num_modules = len(modules)
    target_difficulty_map = {
        'beginner': 5,
        'intermediate': 10,
        'advanced': 15
    }
    target_difficulty = target_difficulty_map.get(current_level.lower(), 9)

    def fitness(chromosome):
        total_time = 0
        total_difficulty = 0
        selected_count = 0

        for i, gene in enumerate(chromosome):
            if gene == 1:
                total_time += modules[i]['duration_minutes']
                total_difficulty += modules[i]['difficulty']
                selected_count += 1

        if selected_count == 0 or total_time > max_time:
            return 0

        difficulty_penalty = abs(target_difficulty - total_difficulty)

        return max(1, 100 - (difficulty_penalty * 5))

    population_size = 20
    generations = 15
    population = [[random.randint(0,1) for _ in range(num_modules)] for _ in range(population_size)]

    for _ in range(generations):
        population = sorted(population, key=fitness, reverse=True)
        parents = population[:population_size // 2]
        next_generation = parents.copy()

        while len(next_generation) < population_size:
            p1, p2 = random.sample(parents, 2)

            if num_modules > 1:
                cut = random.randint(1, num_modules - 1)
                child = p1[:cut] + p2[cut:]
            else:
                child = p1.copy()

            if random.random() < 0.1:
                index = random.randint(0, num_modules - 1)
                child[index] = 1 - child[index]

            next_generation.append(child)

        population = next_generation

    best_chromosome = max(population, key=fitness)
    selected_modules = [modules[i] for i, gene in enumerate(best_chromosome) if gene == 1]

    if not selected_modules:
        return 'Nu am putut genera un plan optimizat pentru parametrii ceruti'

    total_time = sum(m['duration_minutes'] for m in selected_modules)
    result = f'Plan de studiu optimizat (Nivel: {current_level}, durata: {total_time}/{max_time} minute)\n'

    for index, module in enumerate(selected_modules,1):
        result += (f'{index}. {module["topic"].upper()} {module["title"]} '
                   f'{module["difficulty"]} /10 {module['duration_minutes']} minutes)\n')

    return result.strip()