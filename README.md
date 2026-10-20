# Tiziano AI plugins

One **`tiziano-ai`** marketplace for native Codex and Claude Code clients.
Add the catalog once, then choose the plugins you want. Each plugin remains
in its own repository with its own version and release lifecycle.

## Available plugins

| Plugin | Hosts | Purpose |
| --- | --- | --- |
| [T3 Workers](https://github.com/Tiziano-AI/t3-workers) | Codex, Claude Code | Orchestrate persistent, visible T3 workers across providers and accounts from your native chief. |
| [Cloudflare Publish](https://github.com/Tiziano-AI/cloudflare-publish) | Codex, Claude Code | Give local Mac HTTP(S) or pinned machine-only SSH services stable hostnames through your own Cloudflare account. Requires a separately installed CLI, cloudflared and your own DNS zone; installs no infrastructure automatically. |
| [Charter Skills](https://github.com/Tiziano-AI/charter-skills) | Codex, Claude Code | Mac-first specialist methods for product decisions, design, engineering, research and creative production. Adds on-demand expertise, not standing instructions or a deployment engine. |
| [Grokpair](https://github.com/Tiziano-AI/grokpair) | Codex, Claude Code | Delegate bounded work to a detached Grok Build collaborator, then inspect its replies and files. Requires Grok Build and its own authentication; installing the plugin starts no collaborator. |
| [Voices](https://github.com/Tiziano-AI/voices) | Codex, Claude Code | Create reusable voices and exact speech performances on your Apple Silicon Mac. Guidance requires your separately installed local Voices CLI and models; installing it starts no service. |
| [Deck Studio](https://github.com/Tiziano-AI/deck-studio) | Codex, Claude Code | Create and revise local HTML decks and screenshot PDFs. Requires local Node.js, npm, Python and explicit package-local Chromium setup; installation publishes nothing. |

Only explicitly listed plugins are distributed here. A project's existence in
the Tiziano AI organization does not make it part of this catalog.

## Install

### Codex

```sh
codex plugin marketplace add Tiziano-AI/plugins
codex plugin add t3-workers@tiziano-ai
```

Use the CLI belonging to your intended installation; a desktop app's bundled
runtime can differ from `codex` on your PATH. You can also select the plugin
in the supported desktop plugin directory after adding the marketplace.
Start a fresh local chat and verify that the plugin's skill is available.

### Claude Code

```sh
claude plugin marketplace add Tiziano-AI/plugins
claude plugin install t3-workers@tiziano-ai --scope user
```

Run `/reload-plugins` where supported, or start a new session. T3 Workers can
then be invoked explicitly as `/t3-workers:t3-workers`.

Adding this marketplace does not install every plugin. Installing T3 Workers
does not install T3, configure providers or approve MCP OAuth. Follow the
[plugin's setup guide](https://github.com/Tiziano-AI/t3-workers#connect-your-t3-environment)
and reuse an existing native connection when available.

For Cloudflare Publish, use `cloudflare-publish@tiziano-ai` in the install
command instead. Follow its [setup guide](https://github.com/Tiziano-AI/cloudflare-publish#install-the-cli-and-plugin)
for the separate macOS CLI and Cloudflare prerequisites. Installing its
guidance creates no tunnel, credentials, DNS, Access policy or background job;
removing it does not stop existing publications.

For another plugin, substitute its catalog name in the same command:
`charter-skills@tiziano-ai`, `grokpair@tiziano-ai`, `voices@tiziano-ai` or
`deck-studio@tiziano-ai`. Follow the selected repository's setup guide for
its prerequisites and first use. Catalog installation does not install a
separate application, CLI, model or service, or grant provider access.

## Update or remove

Refresh the catalog and update the selected plugin through the native client:

```sh
# Codex
codex plugin marketplace upgrade tiziano-ai
codex plugin add t3-workers@tiziano-ai

# Claude Code
claude plugin marketplace update tiziano-ai
claude plugin update t3-workers@tiziano-ai --scope user
```

Reload the supported host or start a new session, then check the selected
version. Remove only the plugin when that is what you intend:

```sh
codex plugin remove t3-workers@tiziano-ai
# OR
claude plugin uninstall t3-workers@tiziano-ai --scope user
```

Removing a whole marketplace is a different action and can affect its installed
plugins. Plugin removal does not automatically stop work, delete user data or
revoke separately configured connections; each plugin's guide owns that boundary.

## Catalog maintenance

The two small native manifests reference plugin repositories directly:

- `.agents/plugins/marketplace.json` uses Codex Git URL and Git-subdirectory sources.
- `.claude-plugin/marketplace.json` uses Claude GitHub and Git-subdirectory sources.

There are no copied plugins, build step, daemon or bundled credentials. Add an
entry only for supported hosts and keep version details with the plugin.
Pinned entries select the same reviewed source commit in both hosts;
promoting a replacement changes that pin explicitly. Charter Skills and
Grokpair select their plugin subdirectories through native `git-subdir`
sources. The other entries select repository roots. The catalog copies
neither implementation nor skill content.

```sh
python3 -m unittest discover -s tests -v
claude plugin validate --strict .
```

These checks validate the catalog, not remote plugin installation or behavior.
Before publishing a source change, exercise native installation in an isolated
home without inference, OAuth or live user configuration changes.

Native contracts: [OpenAI marketplace metadata](https://developers.openai.com/plugins/build/plugins#marketplace-metadata)
and [Claude marketplace sources](https://code.claude.com/docs/en/plugin-marketplaces#choose-a-plugin-source).

MIT licensed. Individual plugins keep their own licenses and support boundaries.
