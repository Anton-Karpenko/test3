from .models import CourseParticipant
from .api.exceptions import AlreadyAssigned


class AssignToCourse:
    def __init__(self, course, validated_data):
        self.course = course
        self.student = validated_data['student']

    def execute(self):
        obj, created = CourseParticipant.objects.get_or_create(course=self.course, student=self.student)
        if not created:
            raise AlreadyAssigned()


class UnAssignFromCourse:
    def __init__(self, course, validated_data):
        self.course = course
        self.student = validated_data['student']

    def execute(self):
        CourseParticipant.objects.filter(course=self.course, student=self.student).delete()
