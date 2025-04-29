import unittest
from unittest.mock import patch, mock_open
from player import Player
from io import StringIO


class TestPlayer(unittest.TestCase):
    @patch("builtins.input", side_effect=["test_player"])
    def setUp(self, mock_input) -> None:
        """Setup a Player instance for testing."""
        self.player = Player()
        self.player._name = "test_player"
        self.player._data_dict = {"test_player": [5, 3]}

    @patch("builtins.input", side_effect=["test_player"])
    def test_get_name(self, mock_input):
        """Test getting the player's name."""
        name = Player.get_name()
        self.assertEqual(name, "test_player")

    @patch("builtins.input", side_effect=["h"])
    def test_get_difficulty(self, mock_input):
        """Test getting the difficulty level."""
        difficulty = Player.get_difficulty()
        self.assertEqual(difficulty, "h")

    @patch("builtins.open", new_callable=mock_open, read_data="test_player,5,3\n")
    def test_create_dict_from_file(self, mock_file):
        """Test creating a dictionary from a file."""
        data_dict = self.player.create_dict_from_file("data.txt", ",")
        self.assertEqual(data_dict, {"test_player": [5, 3]})

    @patch("builtins.open", new_callable=mock_open)
    def test_save_dict_to_file(self, mock_file):
        """Test saving the dictionary to a file."""
        self.player.save_dict_to_file("data.txt", self.player._data_dict, ",")
        mock_file.assert_called_once_with("data.txt", "w", encoding="utf-8")
        mock_file().write.assert_called_with("test_player,5,3\n")

    def test_update_player_stats(self):
        """Test updating player stats."""
        self.player.update_player_stats(2, 1)
        self.assertEqual(self.player._data_dict["test_player"], [7, 4])

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_player_stats(self, mock_stdout):
        """Test displaying player stats."""
        self.player.display_player_stats()
        self.assertEqual(
            mock_stdout.getvalue().strip(),
            "Test_player, you have won 5 times and lost 3 times.",
        )
