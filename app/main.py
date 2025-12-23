from graph.meeting_graph import build_meeting_graph


def main():
    print("🤖 Running Multi-Agent Meeting Notes System...\n")

    graph = build_meeting_graph()
    result = graph.invoke({})

    print("📄 FINAL OUTPUT\n")
    print("Summary:\n", result["summary"])
    print("\nAction Items:")
    for item in result["action_items"]:
        print("-", item)


if __name__ == "__main__":
    main()
