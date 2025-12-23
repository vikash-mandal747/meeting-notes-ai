import json
from graph.meeting_graph import build_meeting_graph


def main():
    graph = build_meeting_graph()
    result = graph.invoke({})

    output = {
        "summary": result["summary"],
        "action_items": result["action_items"]
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
