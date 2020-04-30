import uuid
from utils import send_mail

SUBJECT_REGISTRATION = 'Welcome, {name}'
BODY_REGISTRATION = 'You are welcome!'


class User:

    def __init__(self, email, f_name, l_name, uid=None):
        self.email = email
        self.f_name = f_name
        self.l_name = l_name
        self.id = uid or uuid.uuid4()

    def get_full_name(self):
        return f'{self.f_name} {self.l_name}'

    def send_mail(self):
        send_mail(self.email,
                  SUBJECT_REGISTRATION.format(name=self.get_full_name()),
                  BODY_REGISTRATION
                  )

    def __str__(self):
        return f'User: <{self.id}: {self.get_full_name()}>'

send_mail("asd", "fas", "fas")