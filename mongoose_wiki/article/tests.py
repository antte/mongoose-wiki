"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from mongoose_wiki.article.models import Article, TranslationPattern

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

class ArticleTest(TestCase):
    
    def test_escape_html_entities(self):
        body = "<a href=\"\">&'</a>"
        expected = "&lt;a href=&quot;&quot;&gt;&amp;&apos;&lt;/a&gt;"
        article = Article()
        actual = article.escapeHtmlEntities(body)
        self.failUnlessEqual(actual, expected)