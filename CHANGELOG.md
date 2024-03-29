# Changelog: recurtools

## v1.0.0 - simplified interface around nested & flatten
- documentation published to https://musicalninjadad.github.io/recurtools/
- removed `sumrecursive()`see [Issue 11](https://github.com/MusicalNinjaDad/recurtools/issues/11)
- removed `chainanything()` - some of the functionality may later be incorporated into `in nested.something()`
- removed `indexrecursive()` function in preference for `nested.index()`.
- removed `countrecursive()` function in preference for `nested.count()`.
- removed `inrecursive()` function in preference for `in nested()`.
- removed `lenrecursive()` function in preference for `len(nested())`. `countcontainers` not implemented in new version.
- standardised on keywork argument `preserve` for flatten. Will later be integrated into nested

## v0.4.0 - update to flatten (BREAKING)
- **new keyword-only argument** `dontflatten` (optional): type which will not be flattened. Default: `(str, bytes)`.
- `preservestrings` argument **removed**.
- **Default behaviour changed**: Strings will no longer be flattened by default, if you want to flatten strings then use `dontflatten=None`.

## v0.3.1 - Migrate to GitHub
- Repository is now located on GitHub (previously ADO).
- All future code changes will be linted by ruff following most of the full rule set. Rule exclusions are documented in `pyproject.toml`; existing code base will be migrated over time.
- Test coverage is visible on https://codecov.io
- Initial preparation for mkdocs / mkdocstring based documentation