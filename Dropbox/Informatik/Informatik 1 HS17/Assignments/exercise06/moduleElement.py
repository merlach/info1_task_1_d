
# @Tutor IMPORTANT: scroll down until you find the comment that announces each exercise!
"""
ects_earned = 138
points_earned = 44
points_max = 60
ects_required_for_ba = 180
ects_missing = ects_required_for_ba - ects_earned
num6_ects_courses = ects_missing//6
grade = round(points_earned/points_max*5+1, 2)

print("So far you have earned", ects_earned, "ECTS points.")
print("You still need", ects_missing, "ECTS points to finish you BA.")
print("This means you should take", num6_ects_courses, "6 ECTS courses.")
print("In the exam you got", points_earned, "of", points_max ,"points.")
print("You have achieved a grade of", grade,"in this exam.")
"""
# addenda from exercise 02 Assignment 4.1a):
def percentage_completed(a,b):
    c = round(a/b*100,2)
    c = str(c)
    c = c+'%'
    return c
"""
print('You have completed',percentage_completed(ects_earned,ects_required_for_ba),'of the ETCS required for your BA')
"""
def calculate_grade(a,b):
    """Input: points earned and maximum of points
    Output: grade"""
    return round(a / b * 5 + 1, 2)

"""
exam2 = calculate_grade(67,90)
print("You have achieved a grade of", exam2,"in your second exam.")
"""
def multiple_of(a,b):
    """Input: Two numbers
    Output: Boolean whether first number is a multiple of the second one."""
    if a%b == 0:
        return True
    else:
        return False
"""
print('The missing ECTS points can be achieved by a multiple of 3 ECTS courses only:',str(multiple_of(ects_missing,3))+'.')
"""
#Exercise 02 Assignment 4.1c) function variant:

def percentage_completed_calc(a,b):
    c = round(a/b*100,2)
    c = int(c)
    return c


def new_ects(n):
    global ects_earned
    global ects_missing

    def ope(n):
        global ects_earned
        if n == -1:
            print('Invalid entry!')
            pass
        else:
            ects_earned += n
            print('You have earned ', ects_earned, ' ECTS points.')
            ects_missing = 180 - ects_earned
            if ects_missing <= 0:
                print('You have completed', percentage_completed(ects_earned, 180),
                      'of the ETCS required for your BA.')
                print('Congratulations! You have finished your BA!')
                pass
            elif ects_missing < 30:
                print('You lucky dog! There are less than 30 points necessary to finish your degree!')
            else:
                print(
                    'Too bad! You still need to earn more than 30 points. Looks like we\'ll have to endure you some more semesters.')
            checkq()

    def checkq():
        more_points_question = input('Do you have any more points to add?')
        if more_points_question == 'yes' or more_points_question == 'Yes':
            new_ects_earned = int(input('Please enter newly earned ECTS points:'))
            new_ects(new_ects_earned)
        else:
            pass

    ope(n)
"""
new_ects_earned = int(input('Please enter newly earned ECTS points:'))
new_ects(new_ects_earned)
"""
#addition for exercise 03 assignment 7.1a)

def add_grade(filename,mode='w'):

    """
    First argument should be the filename.
    Second argument defaults to 'w', i. e. the file will be created.
    If an existing file needs to be altered, choose 'a'.
    Function asks user to input name of lecture, ECTS points for it,
    and the points achieved and the maximum of achieveable points.
    It calculates the grade.
    Into the file a line for each course is generated with ECTS points,
    grade, and name of the lecture.
    """

    if filename[-4:] != '.txt':
        filename+='.txt'

    if mode=='a':
        file=open(filename,'a')
    elif mode == 'w':
        file = open(filename, 'w')
        file.write('ECTS\tgrade\tlecture\tsemester')
    else:
        print('Invaild argument. Choose either \'w\' or \'a\' as mode argument')

    new_data = ''
    while True:
        answer = input('Do you want to add new course data?\n')
        if answer == 'no' or answer == 'No':
            break
        elif answer == 'yes' or answer == 'Yes':
            course_name = input('Please enter the name of the lecture:\n')
            ECTS = input('How many ECTS points are assigned for this course?\n')
            points_max = int(input('How many points could have maximally been achieved in'\
                               +' the course?\n'))
            points_ach = int(input('How many points did the student achieve?\n'))
            semester = input('In which semester was this course held?\n')
            grade = calculate_grade(points_ach,points_max)
            extra = '\n'+ECTS+'\t'+str(grade)+'\t'+course_name+'\t'+semester
            new_data+=extra
            continue
        else:
            print('Please enter either \'yes\' or \'no\'.')
            continue
        break
    file.write(new_data)
    file.close()
"""
add_grade('Uni_Exam_Ex03_7_1_a')
"""
# Exercise 3 Assignment 7.1b)

def get_study_overview(filename):

    """
    Input: File originally created with add_grade(x)
    prints passed lectures, achieved ECTS, grades, percentage of BA finished, and average
    grade.
    """

    if filename[-4:] != '.txt':
        filename+='.txt'

    lectures =''
    ECTS_achieved = 0
    grades = 'The grades you have earned are:'
    interim_grade = 0
    text = open(filename,'r')
    a = text.readlines()
    cop_a = a[1:]
    for n in a[1:]:
        if n == '\n':
            cop_a.remove('\n')
    for n in cop_a:
        line = n.split("\t")
        ects =float(line[0])
        grade =float(line[1])
        lecture = line[2]
        if grade < 4.0:
            continue
        else:
            lectures+=lecture
            ECTS_achieved+=ects
            grades += str('\n')+str(grade)+str('(')+str(ects)+str(' ECTS)')
            if interim_grade == 0:
                interim_grade = ects*grade
            else:
                interim_grade += ects*grade
            final_grade = round(interim_grade/ECTS_achieved,2)
    print('You have passed the following lectures:\n{}'.format(lectures))
    print('You have achieved {} ECTS so far'. format(ECTS_achieved))
    print(grades)
    print('You have completed', percentage_completed(ECTS_achieved, 180),
          'of the ETCS required for your BA.')
    print('Your average grade is {}.'.format(final_grade))
    text.close()
"""
get_study_overview('Uni_Exam_Ex03_7_1_a.txt')
"""

# Exercise 03 Task 7.1c)
"""
add_grade('my_studies.txt')
add_grade('my_studies.txt','a')
get_study_overview('my_studies.txt')
"""

#Exercise 04 Task4_a: for redefined function see lines 93ff
"""
add_grade('Test_Uni_Exam_Ex03_7_1_a')
"""

#Exercise 04 Task_4b

def get_list_lectures(file,lect='passed'):
    """
    Takes two arguments. First argument is a file name. Second defaults to 'passed',
    but may be changed to 'failed'.
    Returns a list of passed or failed lectures. File should have been created with
    add_grade(filename).
    """
    if isinstance(file,str):

        if file[-4:] != '.txt':
            file += '.txt'

        data = open(file,'r')
        a = data.readlines()
        cop_a = a[1:]
        for n in a[1:]:
            if n == '\n':
                cop_a.remove('\n')
        lectures = []

        if lect == 'passed':
            for n in cop_a:
                line = n.split("\t")
                grade = float(line[1])
                lecture = line[2]
                if grade < 4.0:
                    continue
                else:
                    lectures.append(lecture)
            return lectures
        elif lect == 'failed':
            for n in cop_a:
                line = n.split("\t")
                grade = float(line[1])
                lecture = line[2]
                if grade > 3.9:
                    continue
                else:
                    lectures.append(lecture)
            return lectures
        else:
            print('Error. Second argument needs to be a string. Either "passed" \
                  or "failed"')

    else:
        print('Error. The first argument should be a string.')

# Test:
"""
print(get_list_lectures('Test_Uni_Exam_Ex03_7_1_a.txt'))
print(get_list_lectures('Test_Uni_Exam_Ex03_7_1_a.txt','failed'))
"""

# Exercise 04 Task_4c:

def get_lectures_by_semeseter(file):
    """
    input: filename created with add_grade(filename). returns a dictionary with semesters
    as keys and respective lectures that have been booked.
    """
    if file[-4:] != '.txt':
        file += '.txt'

    data = open(file, 'r')
    a = data.readlines()
    cop_a = a[1:]
    for n in a[1:]:
        if n == '\n':
            cop_a.remove('\n')
    semdict = {}
    for n in cop_a:
        line = n.split("\t")
        lecture = line[2]
        semester = line[3]
        if '\n' in semester:
            semester = semester.replace('\n','')
        if semester not in semdict.keys():
            semdict[semester] = [lecture]
        else:
            semdict[semester] += [lecture]
    return semdict

def get_ects_by_semester(file):
    """
    input: filename created with add_grade(filename). returns a dictionary with semesters
    as keys and earned ECTS points in each semester.
    """
    if file[-4:] != '.txt':
        file += '.txt'

    data = open(file, 'r')
    a = data.readlines()
    cop_a = a[1:]
    for n in a[1:]:
        if n == '\n':
            cop_a.remove('\n')
    semdict = {}

    for n in cop_a:
        line = n.split("\t")
        grade = float(line[1])
        semester = line[3]
        if '\n' in semester:
            semester = semester.replace('\n','')
        ects = float(line[0])
        if grade < 4.0:
            continue
        else:
            if semester not in semdict.keys():
                semdict[semester] = ects
            else:
                semdict[semester]+=ects

    return semdict
"""
add_grade('Test_Uni_Exam_Ex03_7_1_a.txt','a')
print(get_lectures_by_semeseter('Test_Uni_Exam_Ex03_7_1_a.txt'))
print(get_ects_by_semester('Test_Uni_Exam_Ex03_7_1_a.txt'))


add_grade('my_studies.txt')
print(get_list_lectures('my_studies.txt'))
print(get_lectures_by_semeseter('my_studies.txt'))
print(get_ects_by_semester('my_studies.txt'))
"""

# exercise 5
"""
class Module:

    def __init__(self, ects, title, semester, grade=None):
        self.ects = ects
        self.title = title
        self.semester = semester
        self.grade = grade
        self.dates = []
        self.elements = []

    def get_important_dates_overview(self):
        sublst = []
        for i in self.dates:
            for b in i:
                sublst.append(b)
        print('{}:\t{}'.format(sublst[0],sublst[1]))

    def set_grade(self,ngrade):
        self.grade = ngrade


    def add_module_element(self,sdate,sclass,module, ects, title, semester, grade=None):
        self.object = sclass(module, ects, title, semester, grade)
        sclass.add_important_date(self, sdate, datekind=None)
        self.elements += self.object


class ModuleElement(Module):

    def __init__(self, module, ects, title, semester, grade=None):
        self.module = module
        Module.__init__(self, ects, title, semester, grade)

    def add_important_date(self,date,datekind=None):
        self.dates.append((datekind,date))

################################################################################

class Lecture(ModuleElement):

    def __init__(self, module, ects, title, semester, grade=None):
        self.module = module
        Module.__init__(self, ects, title, semester, grade)

    def add_important_date(self,date):
        ModuleElement.add_important_date(self,date,"Lesson")

class Lab(ModuleElement):

    def __init__(self, module, ects, title, semester, grade=None):
        self.module = module
        Module.__init__(self, ects, title, semester, grade)

    def add_important_date(self,date):
        ModuleElement.add_important_date(self,date,"Lab session")


class Midterm(ModuleElement):

    def __init__(self, module, ects, title, semester, grade=None):
        self.module = module
        Module.__init__(self, ects, title, semester, grade)

    def add_important_date(self,date):
        ModuleElement.add_important_date(self,date,"Midterm")

class FinaleExam(ModuleElement):

    def __init__(self, module, ects, title, semester, grade=None):
        self.module = module
        Module.__init__(self, ects, title, semester, grade)

    def add_important_date(self,date):
        ModuleElement.add_important_date(self,date,"FinalExam")


################################################################################

### implement class Thesis here ### nothing in exercise about that

################################################################################

### implement class Seminar here ### nothing in exercise about that

################################################################################

### test cases ###

info1 = Lecture(6,"Info 1",1,"Harald Gall")
info1.add_important_date("11-11-2017") #statt folgendem Code eingeführt
#info1.set_exam_date("11-11-2017") #code not in exercise
info1.get_important_dates_overview()
# none of the following codes in the exercise

internet_economics = Seminar(3,"Internet Economics",5,"Burkhardt Stiller")
internet_economics.set_presentation_date("12-12-2019")
internet_economics.set_deadline_date("1-1-2020")
internet_economics.get_important_dates_overview()
"""

# Exercise 06

class Module(object):

    ############################################################################

    def __init__(self,ects,title,semester,grade=None):
        "constructor for class module"

        # store everything as instance variables
        self.ects = ects
        self.grade = grade
        self.title = title
        self.semester = semester

        # create a list to store all important dates
        self.dates = []

        # create a list to store all module elements
        self.elements = []

    ############################################################################

    def get_important_dates_overview(self):
        "prints all the important dates for a module"

        print("Important dates for {0:s}:".format(self.title))

        for kind,date in self.dates:
            print("\t{0:s} on {1:s}".format(kind,date))

    ############################################################################

    def set_grade(self,grade):
        "set the grade to a given value"

        self.grade = grade

    ############################################################################

    def add_module_element(self,other_class,date):
        "add a new module element to the elements list"

        obj = other_class(self)
        obj.add_important_date(date)
        self.elements.append((obj))

################################################################################

class ModuleElement(object):

    ############################################################################

    def __init__(self,module):
        "constructor for class module element"

        # store module as instance variable
        self.module = module

    ############################################################################

    def add_important_date(self,kind,date):
        "add a date to the module's date dictionary"

        self.module.dates.append((kind,date))


################################################################################

class Lesson(ModuleElement):

    ############################################################################

    def __init__(self,module):
        "constructor for class lesson"

        # call super class constructor
        ModuleElement.__init__(self,module)

    ############################################################################

    def add_important_date(self,date):
        "add a lesson to the date dictionary"

        ModuleElement.add_important_date(self,"Lesson",date)

################################################################################

class Lab(ModuleElement):

    ############################################################################

    def __init__(self,module):
        "constructor for class lab"

        # call super class constructor
        ModuleElement.__init__(self,module)

    ############################################################################

    def add_important_date(self,date):
        "add a lab session to the date dictionary"

        ModuleElement.add_important_date(self,"Lab Session",date)

################################################################################

class Midterm(ModuleElement):

    ############################################################################

    def __init__(self,module):
        "constructor for class midterm"

        # call super class constructor
        ModuleElement.__init__(self,module)

    ############################################################################

    def add_important_date(self,date):
        "add a midterm to the date dictionary"

        ModuleElement.add_important_date(self,"Midterm",date)

################################################################################

class FinalExam(ModuleElement):

    ############################################################################

    def __init__(self,module):
        "constructor for class final exam"

        # call super class constructor
        ModuleElement.__init__(self,module)

    ############################################################################

    def add_important_date(self,date):
        "add a final exam to the date dictionary"

        ModuleElement.add_important_date(self,"Final Exam",date)

################################################################################


### test cases ###

# info1 = Module(6,"Info 1",1)
# info1.add_module_element(Midterm,"31.10.2017")
# info1.add_module_element(FinalExam,"20.12.2017")
# info1.get_important_dates_overview()


