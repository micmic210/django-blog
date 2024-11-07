from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'test',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for the 'name' field"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Name was not provided, but the form is valid")

class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for the 'email' field"""
        form = CollaborateForm({
            'name': 'Matt',
            'email': '',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Email was not provided, but the form is valid")

class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for the 'message' field"""
        form = CollaborateForm({
            'name': 'Matt',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertTrue(form.is_valid(), msg="Message was not provided, but the form is valid")