# main.py
from query_handler import handle_query

def main():
    while True:
        nl_query = input("Enter your query: ")
        if nl_query.lower() == 'exit':
            break
        result = handle_query(nl_query)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
