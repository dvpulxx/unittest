import unittest
from qautils.slugify import slugify

class TestsSlugify(unittest.TestCase):

    def test_basic_slug(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_special_characters(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_multiple_spaces_and_underscores(self):
        self.assertEqual(slugify(" multiple spaces _ "), "multiple-spaces")

    def test_dashes_trimming(self):
        self.assertEqual(slugify("---A---B---"), "a-b")

    def test_empty_result(self):
        self.assertEqual(slugify("!!!"), "")

    def test_extra_whitespace(self):
        # проверка на табы и переносы строк
        self.assertEqual(slugify("Line\twith\nTabs"), "line-with-tabs")

if __name__ == "__main__":
    unittest.main()