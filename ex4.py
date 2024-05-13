from solution_4 import Group, Subject, Teacher, Schedule


def sch(group, sem):
    week = ['чет', 'нечет']
    day = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
    for i in day:
        for j in week:
            Schedule(i, j, group, sem)


def main():
    answer_1 = input('Здравствуйте! Расписание какой группы вы хотите посмотреть? ')
    answer_2 = input('Какой семестр? ')

    with open('groups.txt', encoding='utf-8') as f_1:
        for n in f_1:
            Group(n)
    with open('teachers.txt', encoding='utf-8') as f_2:
        for n in f_2:
            Teacher(n)
    with open('subjects.txt', encoding='utf-8') as f_3:
        for n in f_3:
            Subject(n)
    sch(answer_1, answer_2)

    Schedule.forming_sch()
    answer_3 = input('Какая неделя? ')

    if answer_3.lower() == 'чет':
        print(Schedule.sched_even[0].inf_gr)
        print(*Schedule.sched_even)
    elif answer_3.lower() == 'нечет':
        print(Schedule.sched_even[0].inf_gr)
        print(*Schedule.sched_not_even)
    else:
        print('Ошибка!')


main()
