#!/usr/bin/env python3
"""
Push a private Hugging Face dataset with one config per country and a single 'test' split
from the JSON file at lm_eval/tasks/include_es/Spanish.json.

Repo ID: mariagrandury/include_es

Usage:
  python scripts/push_include_es_to_hub.py \
    --file /Users/mariagrandury/Projects/somosnlp/lm-evaluation-harness/lm_eval/tasks/include_es/Spanish.json \
    --repo-id mariagrandury/include_es \
    --private

Authentication:
  - Set the environment variable HF_TOKEN with a write token, or be logged in via `huggingface-cli login`.
"""

import argparse
import json
import os
import re
import sys
import unicodedata
from typing import Dict, Iterable, List, Optional

from datasets import Dataset, DatasetDict
from huggingface_hub import HfApi, create_repo


def slugify_config_name(text: str) -> str:
    """Create a safe config name from arbitrary text (e.g., a country name)."""
    normalized = (
        unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    )
    normalized = normalized.lower().strip()
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized).strip("-")
    return normalized or "default"


def load_examples(json_path: str) -> List[dict]:
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Expected a JSON array at the root of the file.")
    return data


def group_by_country(records: Iterable[dict]) -> Dict[str, List[dict]]:
    groups: Dict[str, List[dict]] = {}
    for rec in records:
        country = rec.get("country") or "unknown"
        groups.setdefault(country, []).append(rec)
    return groups


def ensure_repo(repo_id: str, private: bool, token: Optional[str]) -> None:
    # Create if missing; if it exists, this is a no-op
    create_repo(
        repo_id=repo_id,
        repo_type="dataset",
        private=private,
        exist_ok=True,
        token=token,
    )


def push_country_split(
    repo_id: str,
    country_name: str,
    rows: List[dict],
    private: bool,
    token: Optional[str],
) -> None:
    config_name = slugify_config_name(country_name)
    # Map options list -> option_a..option_d columns; keep original keys unchanged otherwise
    mapped_rows = []
    for r in rows:
        opts = r.get("options") or []
        mapped = dict(r)
        if isinstance(opts, list):
            mapped["option_a"] = opts[0] if len(opts) > 0 else None
            mapped["option_b"] = opts[1] if len(opts) > 1 else None
            mapped["option_c"] = opts[2] if len(opts) > 2 else None
            mapped["option_d"] = opts[3] if len(opts) > 3 else None
        mapped_rows.append(mapped)

    dataset = Dataset.from_list(mapped_rows)
    dset = DatasetDict({"test": dataset})

    # Push a single-split dataset dict, specifying config per country
    dset.push_to_hub(
        repo_id=repo_id,
        config_name=config_name,
        private=private,
        token=token,
        commit_message=f"Add/Update config '{country_name}' with test split",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Push include_es JSON to HF Hub with one config per country."
    )
    parser.add_argument(
        "--file",
        default="/Users/mariagrandury/Projects/somosnlp/lm-evaluation-harness/lm_eval/tasks/include_es/Spanish.json",
        help="Path to Spanish.json",
    )
    parser.add_argument(
        "--repo-id",
        default="mariagrandury/include_es",
        help="Target dataset repo id (e.g., user/dataset)",
    )
    parser.add_argument(
        "--private",
        action="store_true",
        help="Create the dataset repo as private if it doesn't exist.",
    )
    parser.add_argument(
        "--countries",
        nargs="*",
        default=None,
        help="Optional list of country names to include. Default: all countries present in data.",
    )
    parser.add_argument(
        "--max-countries",
        type=int,
        default=None,
        help="Optional limit for number of countries to push (useful for smoke tests).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    token = os.environ.get("HF_TOKEN")

    # Basic auth check
    try:
        HfApi(token=token).whoami()
    except Exception:
        print(
            "Warning: Not authenticated to Hugging Face Hub. Set HF_TOKEN or run 'huggingface-cli login'.",
            file=sys.stderr,
        )

    print(f"Loading examples from {args.file} ...")
    examples = load_examples(args.file)

    print("Grouping by country ...")
    grouped = group_by_country(examples)

    selected_countries: List[str]
    if args.countries:
        selected_countries = [c for c in args.countries if c in grouped]
        missing = set(args.countries) - set(selected_countries)
        if missing:
            print(f"Note: Skipping unknown countries: {sorted(missing)}")
    else:
        selected_countries = sorted(grouped.keys())

    if args.max_countries is not None:
        selected_countries = selected_countries[: args.max_countries]

    print(f"Ensuring repo {args.repo_id} exists (private={args.private}) ...")
    ensure_repo(repo_id=args.repo_id, private=args.private, token=token)

    print(f"Pushing {len(selected_countries)} configs to {args.repo_id} ...")
    for idx, country in enumerate(selected_countries, start=1):
        rows = grouped[country]
        print(
            f"[{idx}/{len(selected_countries)}] Pushing country '{country}' with {len(rows)} rows ..."
        )
        push_country_split(
            repo_id=args.repo_id,
            country_name=country,
            rows=rows,
            private=args.private,
            token=token,
        )
    print("Done.")


if __name__ == "__main__":
    main()
