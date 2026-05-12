from django.test import TestCase

from .rectangle import Rectangle


class RectangleTestCase(TestCase):

    def test_rectangle_iteration(self):

        rect = Rectangle(10, 5)

        result = list(rect)

        expected = [
            {"length": 10},
            {"width": 5}
        ]

        self.assertEqual(result, expected)