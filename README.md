# fund_analysis

Research workspace for the AlphaPai OpenPai API.

## Environment setup

- Python 3.12 or later.
- Supply `ALPHAPAI_API_KEY` through the cloud environment's personal secret configuration.
- Allow HTTPS access to `open-api.rabyte.cn`.
- Do not store credentials in this repository.

## Verify access

```sh
python3 scripts/check_alphapai.py
```

The check reports only whether the credential is available and whether authentication succeeds. It does not print the credential or retrieve paid research content.

For research requests, use the installed `alphapai-research` skill after authentication is verified.
