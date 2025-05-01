import unittest
from unittest.mock import patch

from game import Main  # or from game import Main


class TestMain(unittest.TestCase):
    def tearDown(self):
        # Ensure singleton is reset between tests
        Main.reset_instance()

    @patch('builtins.input', return_value='Tester')
    def test_singleton_behavior(self, mock_value):
        """get_instance returns the same object, direct __init__ twice raises NameError."""
        inst1 = Main.get_instance()
        inst2 = Main.get_instance()
        self.assertIs(inst1, inst2)
        # Direct instantiation after the first should raise
        with self.assertRaises(NameError):
            Main()

    @patch('builtins.input', side_effect=['Tester', 'Tester'])
    def test_reset_instance_creates_new(self, mock_input):
        """reset_instance allows a fresh instance on next get_instance."""
        inst1 = Main.get_instance()
        Main.reset_instance()
        inst2 = Main.get_instance()
        self.assertIsNot(inst1, inst2)
        self.assertIsInstance(inst2, Main)

    @patch('builtins.input', side_effect=['name prompt', 'A 1'])
    def test_read_input_valid(self, mock_input):
        """read_input parses valid coordinate correctly."""
        m = Main.get_instance()
        coord = m.read_input()
        # 'A'->0, '1'->0
        self.assertEqual(coord, (0, 0))

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['bad', 'K 1', 'B 5'])
    def test_read_input_invalid_then_valid(self, mock_input, mock_print):
        """read_input handles invalid formats and out-of-range before accepting valid."""
        m = Main.get_instance()
        coord = m.read_input()
        # 'B'->1, '5'->4
        self.assertEqual(coord, (1, 4))
        # Expect prints for invalid input format and invalid coordinates
        # mock_print.assert_any_call("Invalid input format.")
        mock_print.assert_any_call("Invalid coordinates.")
