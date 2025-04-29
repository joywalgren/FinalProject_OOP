import unittest
from unittest.mock import patch, MagicMock
from opponent import AIPlayer
from dumb_strategy import DumbStrategy


class TestAIPlayer(unittest.TestCase):
    def setUp(self) -> None:
        """Setup an AIPlayer instance for testing."""
        self.ai = AIPlayer(DumbStrategy())

    @patch("attack.BasicAttack.execute", return_value="Hit!")
    def test_attack_player_hit(self, mock_execute):
        """Test AI attacking the player and hitting."""

        mock_board = MagicMock()
        mock_board._board = [[MagicMock() for _ in range(10)] for _ in range(10)]
        result = self.ai.attack_player(mock_board)

        # check that the result is true (hit)
        self.assertTrue(result)

    @patch("attack.BasicAttack.execute", return_value="Miss!")
    def test_attack_player_miss(self, mock_execute):
        """Test AI attacking the player and hitting."""

        mock_board = MagicMock()
        mock_board._board = [[MagicMock() for _ in range(10)] for _ in range(10)]
        result = self.ai.attack_player(mock_board)

        # check that the result is False (miss)
        self.assertFalse(result)
