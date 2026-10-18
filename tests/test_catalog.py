"""Offline checks for the two native views of the publisher catalog."""

import json
from pathlib import Path
import unittest
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]


def load(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.codex = load(".agents/plugins/marketplace.json")
        self.claude = load(".claude-plugin/marketplace.json")

    def test_marketplace_identity_and_unique_plugin_names(self):
        for catalog in (self.codex, self.claude):
            self.assertEqual(catalog["name"], "tiziano-ai")
            names = [entry["name"] for entry in catalog["plugins"]]
            self.assertTrue(names)
            self.assertEqual(len(names), len(set(names)))

    def test_shared_entries_resolve_the_same_repository(self):
        codex = {entry["name"]: entry for entry in self.codex["plugins"]}
        claude = {entry["name"]: entry for entry in self.claude["plugins"]}
        self.assertIn("t3-workers", codex)
        self.assertIn("t3-workers", claude)
        for name in codex.keys() & claude.keys():
            with self.subTest(plugin=name):
                left = codex[name]["source"]
                right = claude[name]["source"]
                self.assertEqual(left["source"], "url")
                self.assertEqual(right["source"], "github")
                parsed = urlsplit(left["url"])
                self.assertEqual(parsed.scheme, "https")
                self.assertEqual(parsed.netloc, "github.com")
                self.assertFalse(parsed.query or parsed.fragment)
                self.assertEqual(parsed.path.removesuffix(".git").strip("/"), right["repo"])

    def test_codex_entries_have_explicit_install_policy(self):
        for entry in self.codex["plugins"]:
            with self.subTest(plugin=entry["name"]):
                self.assertIn(entry["policy"]["installation"],
                              ("AVAILABLE", "INSTALLED_BY_DEFAULT", "NOT_AVAILABLE"))
                self.assertIn(entry["policy"]["authentication"], ("ON_INSTALL", "ON_USE"))
                self.assertTrue(entry["category"])


if __name__ == "__main__":
    unittest.main()
