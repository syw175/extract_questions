def find_questions(questions_list, topic):
    desired_questions = []
    for question in questions_list:
        if topic in question:
            desired_questions.append(question)
    return desired_questions

# COPY and PASTE contents of word file into text file
# Change 'Ch11.txt' into 'filename.txt', LEAVE THE APOSTROPHES
# Make sure first line of file is question #1 or else it won't work
file_name = 'Ch10.txt'

# CHANGE i_want_this_topic to the desired topic or header
# ENSURE capitalization is correct, otherwise it won't work
# ENSURE that it is an actual topic, NOT a SUB-TOPIC
# EXAMPLE: "Common Sources Of Risk On IT Projects"
# Project Phases and the Project Life Cycle

i_want_these_topics = ['The Importance Of Project Communications Management',
                       'Keys To Good Communications',
                       'Planning Communications Management',
                       'Managing Communications',
                       'Suggestions For Improving Project Communications',
                       'Using Software To Assist In Project Communications']


f = open(file_name, 'r')
# Initialize list of question numbers
num_list = []
for k in range(1, 99):
    string = str(k) + "."
    num_list.append(string)


# Append ALL questions in file to list
question_list = []
question_count = -1
for line in f:
    if line[0:3].strip() in num_list:
        question_list.append(line)
        question_count += 1
    else:
        question_list[question_count] += line


# Print out desired test bank questions
for elem in i_want_these_topics:
    exam_questions = find_questions(question_list, elem)
    for questions in exam_questions:
        print(questions)