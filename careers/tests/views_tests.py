"""Tests for the views of the careers app."""
from django.test import RequestFactory, TestCase
from django.core.urlresolvers import reverse

from .. import views


class CareersViewTestCase(TestCase):
    """Tests for the ``CareersView`` view class."""
    longMessage = True

    def test_url_reverse(self):
        url = reverse('careers')
        self.assertEqual(url, '/careers/')

    def test_view(self):
        req = RequestFactory().get('/')
        resp = views.CareersView.as_view()(req)
        self.assertEqual(resp.status_code, 200, msg='View should be callable')
