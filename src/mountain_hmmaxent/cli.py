from __future__ import annotations
import argparse
import pandas as pd
from .stats import species_cluster_bootstrap
from .conservation import jaccard


def main():
    p = argparse.ArgumentParser(description="mountain-hmmaxent reproducibility utilities")
    sub = p.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("bootstrap")
    b.add_argument("csv"); b.add_argument("--value", required=True); b.add_argument("--species", default="species")
    j = sub.add_parser("jaccard")
    j.add_argument("csv"); j.add_argument("--a", required=True); j.add_argument("--b", required=True)
    args = p.parse_args()
    df = pd.read_csv(args.csv)
    if args.cmd == "bootstrap":
        print(species_cluster_bootstrap(df, args.value, args.species))
    elif args.cmd == "jaccard":
        print(jaccard(df[args.a].astype(bool), df[args.b].astype(bool)))

if __name__ == "__main__":
    main()
