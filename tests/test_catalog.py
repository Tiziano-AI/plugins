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
                parsed = urlsplit(left["url"])
                self.assertEqual(parsed.scheme, "https")
                self.assertEqual(parsed.netloc, "github.com")
                self.assertFalse(parsed.query or parsed.fragment)
                if left["source"] == "git-subdir":
                    self.assertEqual(right["source"], "git-subdir")
                    self.assertEqual(left["url"], right["url"])
                    left_path = left["path"].removeprefix("./")
                    right_path = right["path"].removeprefix("./")
                    self.assertEqual(left_path, right_path)
                    self.assertTrue(left_path)
                    self.assertFalse(left_path.startswith("/"))
                    self.assertNotIn("..", left_path.split("/"))
                    self.assertIn("sha", left)
                else:
                    self.assertEqual(left["source"], "url")
                    self.assertEqual(right["source"], "github")
                    self.assertEqual(parsed.path.removesuffix(".git").strip("/"), right["repo"])
                if "sha" in left or "sha" in right:
                    self.assertEqual(left["sha"], right["sha"])
                    self.assertRegex(left["sha"], r"\A[0-9a-f]{40}\Z")
                    self.assertNotIn("ref", left)
                    self.assertNotIn("ref", right)

    def test_codex_entries_have_explicit_install_policy(self):
        for entry in self.codex["plugins"]:
            with self.subTest(plugin=entry["name"]):
                self.assertIn(entry["policy"]["installation"],
                              ("AVAILABLE", "INSTALLED_BY_DEFAULT", "NOT_AVAILABLE"))
                self.assertIn(entry["policy"]["authentication"], ("ON_INSTALL", "ON_USE"))
                self.assertTrue(entry["category"])

    def test_cloudflare_publish_pins_one_canonical_public_source_commit(self):
        codex = {entry["name"]: entry for entry in self.codex["plugins"]}
        claude = {entry["name"]: entry for entry in self.claude["plugins"]}
        left = codex["cloudflare-publish"]
        right = claude["cloudflare-publish"]
        self.assertEqual(right["source"]["repo"], "Tiziano-AI/cloudflare-publish")
        self.assertEqual(left["source"]["sha"], right["source"]["sha"])
        self.assertRegex(left["source"]["sha"], r"\A[0-9a-f]{40}\Z")
        self.assertNotIn("ref", left["source"])
        self.assertNotIn("ref", right["source"])
        self.assertEqual(left["policy"]["authentication"], "ON_USE")

    def test_codex_remote_entries_provide_native_preview_metadata(self):
        for entry in self.codex["plugins"]:
            if entry["source"]["source"] not in ("url", "git-subdir"):
                continue
            with self.subTest(plugin=entry["name"]):
                preview = entry["interface"]
                for key in ("displayName", "shortDescription", "developerName"):
                    self.assertTrue(preview[key].strip())
                website = urlsplit(preview["websiteUrl"])
                self.assertEqual(website.scheme, "https")
                self.assertTrue(website.netloc)


if __name__ == "__main__":
    unittest.main()
