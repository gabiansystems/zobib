import sys
import argparse

from . import zobib_export

commands = {
    'export': zobib_export,
}


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('command', type=str,
                        choices=commands.keys())
    args, unknown = parser.parse_known_args()
    sys.argv = [f'zobib_{args.command}'] + sys.argv[2:]
    return commands[args.command].main()
