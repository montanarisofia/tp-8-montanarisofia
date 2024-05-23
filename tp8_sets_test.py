import unittest

# pylint: disable=deprecated-module
from sets import (clean_ingredients,
                  check_drinks)

from sets_test_data import (recipes_with_duplicates,
                            recipes_without_duplicates,
                            all_drinks,
                            drink_names)


class SetsTest(unittest.TestCase):

    def test_clean_ingredients(self):
        test_data = zip(recipes_with_duplicates[::3], recipes_without_duplicates[::3])

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", inputs="recipes with duplicated ingredients",
                              result="recipe ingredients de-duped"):
                error_msg = (f"Expected a cleaned ingredient list for {item[0]}, "
                             "but the ingredients aren't cleaned as expected.")

                self.assertEqual(clean_ingredients(item[0], item[1]), (result[1], result[2]), msg=error_msg)

    def test_check_drinks(self):
        test_data = zip(all_drinks[::2], drink_names[::2])

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", iputs="all drinks", results="drinks classified"):
                error_msg = f"Expected {result} for {item}, but got something else instead."
                self.assertEqual(check_drinks(item[0], item[1]), (result), msg=error_msg)
