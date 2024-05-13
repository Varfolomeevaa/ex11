class Group:
    """
    A class used to represent a Group of students.
    """
    all_groups = []

    def __init__(self, info):
        """
        Initialize the Group instance.

        Parameters:
        info (str): A semicolon-separated string containing group number, name, graduation year, and semester.
        """
        info = info.split(';')
        self.number_group = info[0]
        self.name = info[1]
        self.year_grad = info[2]
        self.sem = info[3]
        Group.all_groups.append(self)

    def __str__(self):
        """
        Return a string representation of the group's information.
        """
        return (f'Номер группы: {self.number_group}.Специальность: {self.name}.Год выпуска: {self.year_grad}.'
                f'Семестр: {self.sem}.')

    def __repr__(self):
        """
        Return an unambiguous string representation of the group.
        """
        return self.__str__()


class Teacher:
    """
    A class used to represent a Teacher.
    """
    all_teachers = []

    def __init__(self, info):
        """
        Initialize the Teacher instance.

        Parameters:
        info (str): A semicolon-separated string containing subject name, type, teacher's name,
        semester, and group number.
        """
        info = info.split(';')
        self.name_sub = info[0]
        self.type = info[1]
        self.name_teach = info[2]
        self.sem = info[3]
        self.num_group = info[4]
        Teacher.all_teachers.append(self)

    def __str__(self):
        """
        Return a string representation of the teacher's information.
        """
        return f'{self.name_sub} {self.type} {self.name_teach} {self.num_group}'

    def __repr__(self):
        """
        Return an unambiguous string representation of the teacher.
        """
        return self.__str__()


class Subject:
    """
    A class used to represent a Subject.
    """
    all_subjects = []

    def __init__(self, info):
        """
        Initialize the Subject instance.

        Parameters:
        info (str): A semicolon-separated string containing subject name, type, day, lesson time,
        room, week type, group number, and semester.
        """
        info = info.split(';')
        self.name = info[0]
        self.type = info[1]
        self.day = info[2]
        self.lesson = info[3]
        self.room = info[4]
        self.week = info[5]
        self.num_group = info[6]
        self.sem = info[7]
        self.teacher = ''
        Subject.sub_teacher(self)
        Subject.all_subjects.append(self)

    def sub_teacher(self):
        """
        Associate a teacher with the subject if they match the subject name, type, group number, and semester.
        """
        for i in Teacher.all_teachers:
            if i.name_sub == self.name and i.type == self.type and i.num_group == self.num_group and i.sem == self.sem:
                self.teacher = i.name_teach

    def __str__(self):
        """
        Return a string representation of the subject's schedule information.
        """
        return f'{self.lesson} {self.name} {self.type} {self.teacher} {self.room}'

    def __repr__(self):
        """
        Return an unambiguous string representation of the subject.
        """
        return self.__str__()


class Schedule:
    """
    A class used to represent a Schedule.
    """
    sched_even = []
    sched_not_even = []

    def __init__(self, day, week, group, sem):
        """
        Initialize the Schedule instance.

        Parameters:
        day (str): The day of the week.
        week (str): The type of week ('even' or 'odd').
        group (str): The group number.
        sem (str): The semester
        """
        self.day = day
        self.week = week
        self.all_sub = []
        self.group = group
        self.sem = sem
        self.inf_gr = Schedule.info_about_group(self)
        if week == 'чет':
            Schedule.sched_even.append(self)
        else:
            Schedule.sched_not_even.append(self)

    @staticmethod
    def forming_sch():
        """
        Form the schedule by associating subjects with the appropriate day, group, and semester.
        """
        for sub in Subject.all_subjects:
            if sub.week == 'чет':
                for i in Schedule.sched_even:
                    if sub not in i.all_sub and sub.day == i.day and sub.num_group == i.group and sub.sem == i.sem:
                        i.all_sub.append(sub)
            else:
                for i in Schedule.sched_not_even:
                    if sub not in i.all_sub and sub.day == i.day and sub.num_group == i.group and sub.sem == i.sem:
                        i.all_sub.append(sub)

    def info_about_group(self):
        """
        Return information about the group associated with the schedule.
        """
        for i in Group.all_groups:
            if i.number_group == self.group and i.sem == self.sem:
                return i

    def __str__(self):
        """
        Return a string representation of the schedule for a particular day.
        """
        return (f'{self.day}\n'
                f'{"\n".join([str(i) for i in self.all_sub])} \n')

    def __repr__(self):
        """
        Return an unambiguous string representation of the schedule.
        """
        return self.__str__()
