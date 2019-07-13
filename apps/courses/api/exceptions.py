from django.utils.translation import ugettext as _
from rest_framework.exceptions import APIException


class AlreadyAssigned(APIException):
    status_code = 400
    default_detail = _('This student is already assigned to the course')
    default_code = 'already_assigned'
