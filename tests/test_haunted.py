import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import haunted


class HauntedTerminalTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.root = Path(self.tempdir.name)
        self.lore_file = self.root / "lore.json"

        self.data_patch = patch.object(haunted, "DATA_DIR", self.root)
        self.file_patch = patch.object(haunted, "LORE_FILE", self.lore_file)
        self.data_patch.start()
        self.file_patch.start()
        self.addCleanup(self.data_patch.stop)
        self.addCleanup(self.file_patch.stop)

    def test_lore_round_trip(self):
        notes = [
            "The ghost awakened on Halloween.",
            "The crypt remembers.",
        ]
        haunted.save_lore(notes)
        self.assertEqual(haunted.load_lore(), notes)

    def test_missing_lore_returns_empty_list(self):
        self.assertEqual(haunted.load_lore(), [])

    def test_invalid_lore_returns_empty_list(self):
        self.lore_file.parent.mkdir(parents=True, exist_ok=True)
        self.lore_file.write_text("{invalid json", encoding="utf-8")
        self.assertEqual(haunted.load_lore(), [])

    def test_lore_file_has_restricted_permissions(self):
        haunted.save_lore(["A private note"])
        mode = self.lore_file.stat().st_mode & 0o777
        self.assertEqual(mode, 0o600)

    def test_personalities_are_available(self):
        self.assertEqual(
            set(haunted.PERSONAS),
            {"ghost", "oracle", "cryptkeeper"},
        )

    def test_endpoint_is_local(self):
        self.assertTrue(haunted.API.startswith("http://127.0.0.1:"))

    def test_lore_is_valid_json(self):
        haunted.save_lore(["Remember the crypt"])
        data = json.loads(self.lore_file.read_text(encoding="utf-8"))
        self.assertIsInstance(data, list)


if __name__ == "__main__":
    unittest.main()
