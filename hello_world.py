import argparse

def main():
    parser = argparse.ArgumentParser(description="Hello world script")
    parser.add_argument('--name', '-n', default='World', help='Name to greet')
    args = parser.parse_args()
    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()
