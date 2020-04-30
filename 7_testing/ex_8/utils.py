def send_mail(email: str, subject: str, body: str):
    print(email, subject, body)


def concat_name(f_name: str, l_name: str):
    return f'{f_name} {l_name}'


def set_user_meta(instance, value: dict):
    instance.meta = value
