import unittest
from unittest.mock import patch
from menu import Menu


class TestMenu(unittest.TestCase):
    @patch("builtins.input", side_effect=["1"])
    def test_menu_option_1(self, mock_input):
        """Test selecting option 1 from the menu."""
        option = Menu.menu()
        self.assertEqual(option, 1)

    @patch("builtins.input", side_effect=["2"])
    def test_menu_option_2(self, mock_input):
        """Test selecting option 2 from the menu."""
        option = Menu.menu()
        self.assertEqual(option, 2)

    @patch("builtins.input", side_effect=["3"])
    def test_menu_option_3(self, mock_input):
        """Test selecting option 3 from the menu."""
        option = Menu.menu()
        self.assertEqual(option, 3)
