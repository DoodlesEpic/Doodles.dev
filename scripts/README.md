# Scripts

This directory contains Python scripts used to maintain the website data.

## `generate_projects.py`

`generate_projects.py` fetches public repositories from the GitHub API for
`DoodlesEpic` and writes them to a YAML file for the Projects page.

The generated entries include the repository name, URL, description, creation
and update dates, main language, license data, and topics. Forked repositories
and the profile README repository are skipped by default.

## Run locally

The script dependencies are managed with [uv](https://docs.astral.sh/uv/) in
this directory. The required Python and uv versions are pinned in the project's
`.mise.toml`, so install the local toolchain first from the repository root:

```bash
mise install
```

Run the script from `_data` so it updates the file used by Jekyll:

```bash
cd _data
uv --project ../scripts run python ../scripts/generate_projects.py
```

This overwrites `_data/projects.yml`.

If mise is not activated in your shell, prefix the uv command with
`mise exec --`:

```bash
cd _data
mise exec -- uv --project ../scripts run python ../scripts/generate_projects.py
```

## Configuration

The script has a few constants near the top of the file:

- `GITHUB_USERNAME`: the GitHub user whose repositories are fetched.
- `OUTPUT_FILENAME`: the YAML filename written in the current directory.
- `INCLUDE_FORKS`: whether forked repositories should be included.
