import unittest
from app.models.tag import Tag

class TestTag(unittest.TestCase):

    def setUp(self):
        self.tag = Tag("Groceries")

    def test_tag_has_category(self):
        self.assertEqual("Groceries", self.tag.category)

    def test_tag_has_active(self):
        self.assertEqual(True, self.tag.active)