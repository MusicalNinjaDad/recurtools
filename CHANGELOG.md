# Changelog: recurtools

- rename chainanything to starchain
- standardised on keywork argument `preserve`

## v0.4.0 - update to flatten (BREAKING)
- **new keyword-only argument** `dontflatten` (optional): type which will not be flattened. Default: `(str, bytes)`.
- `preservestrings` argument **removed**.
- **Default behaviour changed**: Strings will no longer be flattened by default, if you want to flatten strings then use `dontflatten=None`.

## v0.3.1 - Migrate to GitHub
- Repository is now located on GitHub (previously ADO).
- All future code changes will be linted by ruff following most of the full rule set. Rule exclusions are documented in `pyproject.toml`; existing code base will be migrated over time.
- Test coverage is visible on https://codecov.io
- Initial preparation for mkdocs / mkdocstring based documentation