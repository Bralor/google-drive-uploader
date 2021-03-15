import argparse


def main():
    print("Running main...")
    print(f"File: {args.upload}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--upload", action="store",
                        metavar="PATH", help="upload existing file to GDrive")
    args = parser.parse_args()

    if args.upload:
        main()
    elif args:
        parser.print_help()

