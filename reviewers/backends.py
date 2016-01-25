from django.conf import settings
from reviewers.models import Reviewer
class EmailAuthBackend(object):
    def authenticate(self, email=None, password=None):
        try:
            user=Reviewer.objects.get(email=email)
            if user.check_password(password):
                return user
        except Reviewer.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user=Reviewer.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except Reviewer.DoesNotExist:
            return None