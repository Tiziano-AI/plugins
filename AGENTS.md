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

Preserve concurrent changes and stage exact owned files. The public repository
is `Tiziano-AI/plugins`. Public pushes and additional plugin listings require
the user's authority for that change; an earlier release is not standing
authority for the next one. No other remote or collaborator is authorized.

## Release convention

For every listed product, a release is one immutable annotated Git tag named
`v<version>` at its qualified release commit. The version in every shipped
native plugin manifest and the same product's package metadata must agree.
Both catalogs pin the tag's **peeled commit SHA**, never the annotated tag
object, a branch or a moving tag. Products that ship several plugins together
use one version and one release tag for that commit; host support stays explicit.
GitHub Release pages are optional, not another release authority.

Prepare and qualify the product at an exact commit through its own release
gate. Publish that commit and tag with the required authority, then publish
the catalog pin. Finally update each intended installation through its owner's
native route and check its selected version and source commit against the pin.
A separate CLI or application follows its product's install route too; installing
the plugin does not update it. Release readiness, catalog availability, installed
files and loading in an already-open session are separate claims.

Once published, a version and its tag are spent. Never move or replace the tag,
or publish different product bytes under that version. A release with changed
shipped payload needs a new version, including changed plugin instructions.
Commits after the pinned release are **unreleased development**, even if a
development manifest still carries the last version. Documentation-only or
guide-only commits do not force a new release or a catalog change. Do not
promote HEAD merely because its version string matches the pin; qualify and
version the next release deliberately. Development work must not replace an
accepted installed release under its old version.

When backfilling a missing tag, resolve the version from the existing catalog's
exact commit, verify that commit's identity and that the tag is absent locally
and remotely, and annotate that commit. This records already-published bytes;
it does not retroactively establish product acceptance or qualify a later HEAD.
Keep older valid tags unchanged.

The agent home's existing surface doctor owns local release-chain checks:
catalog agreement, pinned manifests, release tags and declared installed
provenance. Its offline result is a snapshot, not proof of remote publication
or session loading. At publication, read the remote commit and peeled tag back
explicitly. A deliberately absent plugin is not an installation gap, and a
new release never grants access to another host or account.

Use English for source, documentation and commit messages. Keep private account
identities, local workstation paths, credentials and runtime captures out of
this repository.
