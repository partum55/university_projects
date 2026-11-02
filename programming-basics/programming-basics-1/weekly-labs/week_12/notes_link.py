"""
notes_link.py

This module provides functionality to build a directed graph of connections between notes
based on their links. Notes are assumed to be markdown files located in the same directory
where this script is executed. A link is denoted by `[[note]]`, representing a reference
to the file `note.md`.

The module consists of:
1. build_graph_from_note(note_path, graph=None): Constructs a graph of connections between notes.
2. convert_to_dot(graph): Saves the graph as a DOT file for visualization.

Example:
    If "note.md" contains `[[note4]]`, "note4.md" contains `[[note]]`, and there are no
    other connections, calling `build_graph_from_note("notes/note.md")` will return:
    {"note": ["note4"], "note4": ["note"]}.
"""

import re


def build_graph_from_note(note_path: str, graph = None) -> dict:
    """
    Recursively builds a directed graph of note connections.

    Args:
        note_path (str): The relative path to the note file (e.g., "notes/note.md").
        graph (dict, optional): A pre-existing graph to extend. Defaults to None.

    Returns:
        dict: A dictionary representing the graph of note connections.
              Keys are note names without file extensions.
              Values are sorted lists of directly linked note names.

    Raises:
        FileNotFoundError: If the note file specified in `note_path` does not exist.
        UnicodeDecodeError: If the file cannot be read with UTF-8 encoding.

    Example:
        Suppose the following structure of notes:
        - note.md: Contains '[[note4]]'
        - note4.md: Contains '[[note]]'

        Calling build_graph_from_note("notes/note.md") will return:
        {"note": ["note4"], "note4": ["note"]}
    """
    if graph is None:
        graph = {}
    with open(note_path, "r", encoding="utf-8") as file:
        content = file.read()
        pattern = r"\[\[(.*?)\]\]"
        matches = re.findall(pattern, content)
        curr_dir, curr_note = note_path[:-3].split("/")
        graph[curr_note] = sorted(set(matches)) if matches else []
        for match in matches:
            linked_note_path = f"{curr_dir}/{match}.md"
            if match not in graph:
                build_graph_from_note(linked_note_path, graph)
        if not graph[curr_note]:
            del graph[curr_note]
        return graph


def convert_to_dot(graph: dict) -> None:
    """
    Converts a graph of note connections into a DOT file for visualization.

    Args:
        graph (dict): A dictionary representing the graph of note connections.
                      Keys are note names, and values are lists of connected note names.

    Returns:
        None: Writes the DOT representation of the graph to a file named 'graph.dot'.

    Example:
        Given the graph {"note": ["note4"], "note4": ["note"]}, the generated DOT file
        will contain:
        digraph {
        "note" -> "note4"
        "note4" -> "note"
        }
    """
    with open ("graph.dot", "w", encoding="utf-8") as file:
        file.write("digraph {\n")
        for key, value in sorted(graph.items()):
            for elem in value:
                file.write(f'{key} -> {elem}\n')
        file.write("}")


if __name__ == "__main__":
    # e = build_graph_from_note("notes/note3.md")
    # print(e)
    t = build_graph_from_note("notes/note.md")
    print(t)
    convert_to_dot(t)
    # convert_to_dot(e)
