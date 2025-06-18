from app.graph import graph


def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chatbot. Goodbye!")
            break

        # Simulate a chat interaction with the graph
        response = graph.invoke({"messages": [{"role": "user", "content": user_input}]})
        print(response["messages"][1])


if __name__ == "__main__":
    main()
