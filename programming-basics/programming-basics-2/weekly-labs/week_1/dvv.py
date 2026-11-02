from copy import deepcopy

CAPACITY = {'Responsible AI': 25,
            'AI, Decision Making, and Society': 10,
            'Representation, Inference, and Reasoning in AI': 15}


PREREQUISITES = {
    'Responsible AI': {
        'Fundamentals of Programming': 40,
        'Linear Algebra': 30,
        'Probability and Statistics': 30},
    'AI, Decision Making, and Society': {
        'Worldview core': 40,
        'Decision Making': 40,
        'Fundamentals of Programming': 20},
    'Representation, Inference, and Reasoning in AI': {
        'Introduction to Algorithms': 40,
        'Probability and Statistics': 40,
        'Data Visualisation': 20}}


def read_file(filename):
    '''
    Reads file with registrations and
    return this information as a dictionary.
    'Number' is the ordinal number at the moment of registration.
    For our file, Robert Wilson was the first, and James Davis
    was the last (therefore, it has number 50).
    'Scores' are the scores of students for corresponding
    prerequisites.
    'Prioritization' is a prioritization of the corresponding students.
    >>> read_file('registrations.txt')['James Davis']
    {'Number': 50, 'Scores': {'Fundamentals of Programming': 70, \
'Linear Algebra': 63, 'Probability and Statistics': 71, 'Worldview core': 65, \
'Decision Making': 82, 'Introduction to Algorithms': 72, 'Data Visualisation': 93}, \
'Prioritization': {'AI, Decision Making, and Society': 1, \
'Representation, Inference, and Reasoning in AI': 2, 'Responsible AI': 3}}
    '''
    output = {}
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.readlines()
        for i, line in enumerate(content):
            if 'Name' in line:
                name = line.split(':')[1].strip()
                output[name] = {'Number': i//12+1, 'Scores':{}}
            if 'Prioritization' in line:
                info = line.split(':')[1:][0].strip().split(';')
                info = {subject[3:].strip(): i+1 for i, subject in enumerate(info)}
                output[name].update({'Prioritization': info})
            if line.strip().startswith('-'):
                score = line.strip().split(':')
                score = {score[0][2:]: int(score[1].strip())}
                output[name]['Scores'].update(score)
    return output


def selection_priority(registration, priority, subject, capacity):
    '''
    select prior
    >>> selection_priority(read_file('registrations.txt'), 1, \
'Responsible AI', CAPACITY['Responsible AI'])[1][:3]
    [('Linda Wilson', (91.6, 1)), ('Robert Rodriguez', (85.3, 2)), \
('William Wilson', (85.3, 9))]
    '''
    registrations = deepcopy(registration)
    ranking = {}
    for student, data in registrations.items():
        if subject in data['Prioritization'] and data['Prioritization'][subject] == priority:
            score = sum(data['Scores'][subjects] * PREREQUISITES[subject][subjects]/100 for subjects in PREREQUISITES[subject])
            ranking[student] = (round(score, 1), data['Number'])
    final = sorted(ranking.items(), key=lambda x: (x[1][0], -x[1][1]), reverse=True)[:capacity]
    for student in final:
        del registrations[student[0]]
    return registrations, final


def selection(registration):
    '''
    Makes a selection of students based on
    the registration information (please read the
    corresponding algorithm on CMS).
    Returns the dictionary, where the keys are subjects to choose
    and values are lists of tuples with students' name and ranking score
    sorted by ranking score in descending order.
    >>> selection(read_file('registrations.txt'))['Responsible AI']
    [('Robert Davis', 92.0), ('Linda Wilson', 91.6), \
('Patricia Williams', 89.5), ('Mary Brown', 85.8), \
('Robert Rodriguez', 85.3), ('William Wilson', 85.3), \
('Michael Davis', 83.4), ('Elizabeth Miller', 82.3), \
('Elizabeth Jones', 81.4), ('James Miller', 80.7), \
('Jennifer Johnson', 80.4), ('James Jones', 79.5), \
('Robert Williams', 79.3), ('John Williams', 77.3), \
('Mary Jones', 75.9), ('William Williams', 75.8), \
('Elizabeth Wilson', 74.0), ('Linda Johnson', 73.7), \
('Robert Miller', 71.5), ('Robert Wilson', 69.5), \
('William Rodriguez', 69.4), ('Jennifer Rodriguez', 69.0), \
('Patricia Johnson', 68.6), ('James Davis', 68.2), ('Jennifer Jones', 65.1)]
    '''
    output = {'Responsible AI': [],
              'AI, Decision Making, and Society': [],
              'Representation, Inference, and Reasoning in AI': []}
    registrations = deepcopy(registration)
    for priority in [1, 2, 3]:
        for subject, students in output.items():
            count = CAPACITY[subject]-len(students)
            if count > 0:
                registrations, ranking = selection_priority(registrations,
                                                            priority,
                                                            subject,
                                                            count)
                students.extend(ranking)
    for subject in output:
        output[subject] = sorted([(stud[0], stud[1][0]) for stud in
                                  output[subject]],
                                  reverse=True, key=lambda x: x[1])
    return output


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())