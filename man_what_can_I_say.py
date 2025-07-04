import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python man_what_can_I_say.py <command>")
        sys.exit(1)
    command = sys.argv[1]
    if command == "hello":
        print("Hello, world!")
    elif command == "goodbye":              
        print("Goodbye, world!")
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()