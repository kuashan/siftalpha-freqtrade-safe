import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SafetyGate(unittest.TestCase):
    def test_nontrading_private_ready(self):
        compose = (ROOT / "docker-compose.yml").read_text(encoding="utf-8")
        config = json.loads((ROOT / "user_data" / "config.json").read_text(encoding="utf-8"))

        self.assertIn("freqtradeorg/freqtrade:stable", compose)
        self.assertIn("webserver", compose)
        self.assertNotIn("\n      - trade\n", compose)
        self.assertIn('expose:\n      - "8080"', compose)
        self.assertNotIn("\n    ports:", compose)

        self.assertTrue(config["dry_run"])
        self.assertEqual(config["initial_state"], "stopped")
        self.assertFalse(config["force_entry_enable"])
        self.assertEqual(config["exchange"]["api_key"], "")
        self.assertEqual(config["exchange"]["secret"], "")
        self.assertTrue(config["api_server"]["enabled"])
        self.assertEqual(config["api_server"]["listen_ip_address"], "0.0.0.0")
        self.assertEqual(config["api_server"]["listen_port"], 8080)

    def test_config_is_delivered_as_an_inline_read_only_file_mount(self):
        compose = (ROOT / "docker-compose.yml").read_text(encoding="utf-8")

        self.assertIn("type: bind", compose)
        self.assertIn("source: ./user_data/config.json", compose)
        self.assertIn("target: /freqtrade/user_data/config.json", compose)
        self.assertIn("read_only: true", compose)
        self.assertIn("content: |", compose)
        self.assertNotIn("- ./user_data:/freqtrade/user_data", compose)


if __name__ == "__main__":
    unittest.main()
