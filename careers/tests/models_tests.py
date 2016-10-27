"""Tests for the models of the careers app."""
from django.test import TestCase

from mixer.backend.django import mixer


class CareerPositionTestCase(TestCase):
    """Tests for the ``CareerPosition`` model."""
    longMessage = True

    def test_model(self):
        instance = mixer.blend('careers.CareerPosition', title='Career 1',
                               position=1, )
        self.assertTrue(instance.pk, msg=('Should be able to save the obj'))

    def test_str(self):
        testTitle = 'Test Career'
        instance = mixer.blend('careers.CareerPosition', title=testTitle,
                               position=1, )
        self.assertEqual(str(instance), testTitle,
                         msg=('Should return title'))
