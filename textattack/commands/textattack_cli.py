#!/usr/bin/env python
import argparse
import os
import sys

from textattack.commands.attack import AttackCommand, AttackResumeCommand
from textattack.commands.augment import AugmentCommand
from textattack.commands.benchmark_model import BenchmarkModelCommand
from textattack.commands.benchmark_recipe import BenchmarkRecipeCommand
from textattack.commands.list_things import ListThingsCommand
from textattack.commands.train_model import TrainModelCommand


def main():
    parser = argparse.ArgumentParser(
        "TextAttack CLI",
        usage="[python -m] texattack <command> [<args>]",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    subparsers = parser.add_subparsers(help="textattack command helpers")

    # Register commands
    AttackCommand.register_subcommand(subparsers)
    AttackResumeCommand.register_subcommand(subparsers)
    AugmentCommand.register_subcommand(subparsers)
    BenchmarkModelCommand.register_subcommand(subparsers)
    BenchmarkRecipeCommand.register_subcommand(subparsers)
    ListThingsCommand.register_subcommand(subparsers)
    TrainModelCommand.register_subcommand(subparsers)

    # Let's go
    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        exit(1)

    # Run
    args.func.run(args)


if __name__ == "__main__":
    main()
