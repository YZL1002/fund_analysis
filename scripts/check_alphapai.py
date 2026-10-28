#!/usr/bin/env python3
"""Check OpenPai authentication without displaying credentials."""
import json
import os
import sys
import urllib.error
import urllib.request

def main():
    key = os.environ.get("ALPHAPAI_API_KEY", "").strip()
    if not key:
        print("ALPHAPAI_API_KEY is not available to this task. Configure it in the cloud environment.")
        return 2
    print("ALPHAPAI_API_KEY is available (value hidden).")
    request = urllib.request.Request(
        "https://open-api.rabyte.cn/alpha/open-api/v1/sync/auth/hello",
        data=b"{}",
        headers={"app-agent": key, "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            result = json.load(response)
    except urllib.error.HTTPError as error:
        print(f"Authentication check failed: HTTP {error.code}.")
        return 1
    except (urllib.error.URLError, TimeoutError):
        print("Connection failed. Check the environment network access.")
        return 1
    except (ValueError, UnicodeError):
        print("Authentication check failed: response was not valid JSON.")
        return 1
    if isinstance(result, dict) and result.get("code") == 200000:
        print("OpenPai authentication succeeded.")
        return 0
    print("Authentication check failed: API did not report success.")
    return 1

if __name__ == "__main__":
    sys.exit(main())
