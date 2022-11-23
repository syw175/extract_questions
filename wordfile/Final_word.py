# Program: Test bank question extractor
# Author: Steven Wong
# Date: April 26, 2022
# Description: Extracts questions from test bank with the desired topics
# Instructions: Copy contains of test bank chapter into a textfile. Change file_name variable below
# Change i_want_these_topics to desired topic questions to extract


def find_questions(questions_list, topic):
    desired_questions = []
    for question in questions_list:
        if topic in question:
            desired_questions.append(question)
    return desired_questions

# CHANGE 'sample.txt' into 'your_textfile_name.txt'
# EXAMPLE: 'sample.txt' -> 'Ch2.txt'
file_name = 'sample.txt'


# CHANGE i_want_this_topic to the desired topics
# EXAMPLE: "Common Sources Of Risk On IT Projects"
i_want_these_topics = ['Project Phases and the Project Life Cycle',
                       'The Context of Information Technology Projects',
                       'Recent Trends Affecting Information Technology Project Management']


new_file = open("your_topic.txt", 'w')
f = open(file_name, 'r')

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
        new_file.write(questions)
        print(questions)