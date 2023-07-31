from django.test import SimpleTestCase
from accounts.forms import LoginForms, SignupForms


class TestAccountsForms(SimpleTestCase):

    def test_login_form_valid_data(self):
        form = LoginForms(data={
            'name_or_email_login': 'resh',
            'password': '123456',
        })

        self.assertTrue(form.is_valid())

    def test_login_form_valid_no_data(self):
        form = LoginForms(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_signup_form_valid_data(self):
        form = SignupForms(data={
            'name_signup': 'resh defense',
            'username_signup': 'resh',
            'email': 'resh@gmail.com',
            'password': '123456',
            'confirm_password': '123456',
        })

        self.assertTrue(form.is_valid())

    def test_signup_form_valid_no_data(self):
        form = SignupForms(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)

    def test_signup_form_valid_data_with_password_no_equals(self):
        form = SignupForms(data={
            'name_signup': 'resh defense',
            'username_signup': 'resh',
            'email': 'resh@gmail.com',
            'password': '123456',
            'confirm_password': '12345678',
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertEquals(form.errors['confirm_password'][0], 'The passwords are not the same!')

    def test_signup_form_valid_data_with_password_no_less_6_characters(self):
        form = SignupForms(data={
            'name_signup': 'resh defense',
            'username_signup': 'resh',
            'email': 'resh@gmail.com',
            'password': '123456',
            'confirm_password': '1234',
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertEquals(form.errors['confirm_password'][0], 'Certifique-se de que o valor tenha no mínimo 6 caracteres (ele possui 4).')