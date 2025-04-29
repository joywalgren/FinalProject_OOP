import unittest
from unittest.mock import MagicMock
from dumb_strategy import DumbStrategy
from smart_strategy import TargetedStrategy


class TestAIStrategy(unittest.TestCase):
    def test_dumb_strategy(self):
        """Test the DumbStrategy."""
        strategy = DumbStrategy()
        mock_ai = MagicMock()
        mock_ai.available_moves = [(0, 0), (1, 1)]
        move = strategy.choose_move(mock_ai)
        self.assertIn(move, [(0, 0), (1, 1)])

    def test_targeted_strategy(self):
        """Test the TargetedStrategy."""
        strategy = TargetedStrategy()

        mock_ai = MagicMock()
        mock_ai.target_stack = [(5, 5)]
        mock_ai.tried = []

        # choosing a move from the target stack
        move = strategy.choose_move(mock_ai)
        self.assertEqual(move, (5, 5))

        # make sure the spots around the hit were added to the stack
        strategy.handle_result(mock_ai, (5, 5), "Hit!")
        self.assertIn((4, 5), mock_ai.target_stack)
        self.assertIn((5, 4), mock_ai.target_stack)
        self.assertIn((5, 6), mock_ai.target_stack)
        self.assertIn((6, 5), mock_ai.target_stack)
