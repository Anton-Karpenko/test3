from factory import DjangoModelFactory, Faker

from apps.courses.models import Course


class CourseFactory(DjangoModelFactory):
    name = Faker('sentence', nb_words=2)
    description = Faker('text')
    start_date = '2019-10-27'
    end_date = '2019-11-27'

    class Meta:
        model = Course
