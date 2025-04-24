import argparse
parser = argparse.ArgumentParser(prog="Arg parser",description="It calculates the sqaure of number",epilog="This is help text")
parser.add_argument("square",typpe=int,help="output the square of given nmber")
parser.add_argument("--optional", help="increase verbosity of output", action="store_true")

args = parser.parse_args()
if args.optional:
    print(args.__dict__)

elif args.square:
    num=args.square
    print(args.__dict__)
    print(num**2)
