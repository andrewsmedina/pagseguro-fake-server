from django.test import TestCase
from django.core.urlresolvers import reverse


class ApiTestCase(TestCase):

    def test_checkout(self):
        response = self.client.get(reverse("checkout"))
        expected = """
<?xml version="1.0" encoding="ISO-8859-1"?>
<checkout>
<code>8CF4BE7DCECEF0F004A6DFA0A8243412</code>
<date>2010-12-02T10:11:28.000-02:00</date>
</checkout>
"""
        self.assertEqual(expected, response.content)
