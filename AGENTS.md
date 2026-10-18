# Working on the Tiziano AI plugin catalog

This repository owns the public `tiziano-ai` marketplace for native Codex and
Claude Code clients. It is a catalog, not a plugin monorepo: each plugin keeps
its code, guide, version and releases in its own repository.

## Keep the catalog thin

- Maintain native manifests at `.agents/plugins/marketplace.json` for Codex
  and `.claude-plugin/marketplace.json` for Claude Code. Both use the permanent
  marketplace name `tiziano-ai`.
- Point entries at their actual source repositories. Do not copy skills,
  credentials, MCP configuration or plugin version metadata into this catalog.
- List a plugin only for hosts it supports. Preserve matching plugin identity
  and repository across the two catalogs when it supports both hosts.
- A catalog entry makes source eligible for installation; it does not prove
  installed behavior, authenticate services or authorize live qualification.
- Do not publish private projects or list another plugin without the user's
  authority. This catalog is public even when a local consumer has private
  accounts or configuration.

Read the current native marketplace contracts before changing source types or
install policy. Test catalog structure and perform isolated native installation
when it can settle a real packaging question. Never modify live user homes,
grant access or launch agents as a catalog test.

## Publication

Preserve concurrent changes and stage exact owned files. The current commission
authorizes creating and initially publishing `Tiziano-AI/plugins`, with T3 Workers
as its only entry. Further public pushes and additional plugin listings need
the user's authorization. No other remote or collaborator is authorized.

Use English for source, documentation and commit messages. Keep private account
identities, local workstation paths, credentials and runtime captures out of
this repository.
