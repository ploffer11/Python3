import abc 
import uuid 

class IntroToPython:
    def lesson(self):
        return f"""
            Hello {self.student}. define two variables,
            an integer named a with value 1
            and a string named b with value 'hello'
        """ 

    def check(self, code):
        return code == "a = 1\nb = 'hello'"

class Assignment(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def lesson(self, student):
        pass
    
    @abc.abstractmethod
    def check(self, code):
        pass 

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Assignment:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented

class Statistics(Assignment):
    def lesson(self):
        return (
            "Good work so far, "
            + self.student
            + ". Now calculate the average of the numbers "
            + " 1, 5, 18, -3 and assign to a variable named 'avg'"
        )

    def check(self, code):
        import statistics

        code = "import statistics\n" + code

        local_vars = {}
        global_vars = {}
        exec(code, global_vars, local_vars) 

        return local_vars.get("avg") == statistics.mean([1, 5, 18, -3])

class AssignmentGrader:
    def __init__(self, student, AssignmentClass):
        self.assignment, self.assignment.student, self.attempts, self.correct_attempts = (
            AssignmentClass(), student, 0, 0
        )
    
    def check(self, code):
        self.attempts += 1
        result = self.assignment.check(code)
        if result:
            self.correct_attempts += 1
        
        return result

    def lesson(self):
        return self.assignment.lesson()

class Grader:
    
    def __init__(self):
        self.student_graders, self.assignment_classes = (
            {}, {}
        )

    def register(self, assignment_class):
        """
        # Role 
        dictionary : assignment_classes
        key : id (uuid4)
        value : assignment_class (class)

        # Args 
        assignment_class (class)

        # Return
        unique id (uuid4) 
        """
        if not issubclass(assignment_class, Assignment):
            raise RuntimeError(
                "Your class does not have the right methods"
            )
        id = uuid.uuid4()
        self.assignment_classes[id] = assignment_class
        return id

    def start_assignment(self, student, id):
        """
        # Role
        dictionary : student_graders
        key : student(str) 
        value : AssignmentGrader(student, assignment_classes[id])(class)  

        # Args
        student (str) : name of student
        id (uuid4) : id of student

        # No return value
        """
        self.student_graders[student] = AssignmentGrader(
            student, self.assignment_classes[id]
        )

    def get_lesson(self, student):
        """
        # Role
        dictionary : student_graders
        key : student (str)
        value : AssignmentGrader (class)

        # Args
        student (str) : name of student

        # Return
        AssignmentGrader.lesson()

        """
        assignment = self.student_graders[student]
        return assignment.lesson()
    
    def check_assignment(self, student, code):
        assignment = self.student_graders[student]
        return assignment.check(code)
    
    def assignment_summary(self, student):
        grader = self.student_graders[student]
        return f""" 
        {student}'s attempts at {grader.assignment.__class__.__name__}:

        attempts : {grader.attempts}
        correct : {grader.correct_attempts}
        passed : {grader.correct_attempts > 0}
        """


grader = Grader()
itp_id = grader.register(IntroToPython)
stat_id = grader.register(Statistics)

grader.start_assignment("Tammy", itp_id)

print("Tammy's Lesson :", grader.get_lesson("Tammy"))

print(
    "Tammy's check :",
    grader.check_assignment("Tammy", "a = 1 ; b = 'hello'"),
)

print(
    "Tammy's other check :",
    grader.check_assignment("Tammy", "a = 1\nb = 'hello'"),
)

print(grader.assignment_summary("Tammy"))

grader.start_assignment("Tammy", stat_id)

print("Tammy's Lesson :", grader.get_lesson("Tammy"))

print("Tammy's check :", grader.check_assignment("Tammy", "avg = 5.25"))

print(
    "Tammy's other check :",
    grader.check_assignment(
        "Tammy", "avg = statistics.mean([1, 5, 18, -3])"
    ),
)

print(grader.assignment_summary("Tammy"))
