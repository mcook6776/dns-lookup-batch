"""DNS Lookup Batch — Resolve a list of hostnames and write A and AAAA records to CSV."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='dns_lookup_batch',
        description='Resolve a list of hostnames and write A and AAAA records to CSV.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('DNS Lookup Batch')
    print('Bulk DNS, one table.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
