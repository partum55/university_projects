"""Temp"""

from graph import Graph
from topological_sort import topological_sort


def read_file(filename: str):
    """
    Read Stanford CS course data from file.
    Expected format: course: prereq1, prereq2, ...

    Args:
        filename (str): Path to stanford_cs.txt

    Returns:
        dict: Dictionary mapping courses to their prerequisites
    """
    courses = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            parts = line.split('(')
            if len(parts) < 2:
                continue

            course = parts[0].strip()
            prereqs_part = parts[1].strip().rstrip(')')

            if prereqs_part.lower() == 'none':
                prereqs = []
            else:
                prereqs = [p.strip() for p in prereqs_part.split(',') if p.strip()]
            courses[course] = prereqs
    return courses


def graph_topsort_1(courses_dict: dict):
    """
    Build a Graph_map graph and perform topological sorting.

    Args:
        courses_dict (dict): Dictionary mapping courses to prerequisites

    Returns:
        list: Topologically sorted list of courses
    """
    g = Graph(directed=True)
    vertices = {}
    all_courses = set(courses_dict.keys())
    for course, prereqs in courses_dict.items():
        all_courses.update(prereqs)
    for course in all_courses:
        vertices[course] = g.insert_vertex(course)
    for course, prereqs in courses_dict.items():
        for prereq in prereqs:
            g.insert_edge(vertices[prereq], vertices[course])
    topo_order = topological_sort(g)
    sorted_elements = [v.element() for v in topo_order]
    expected_prefixes = ["CS", "PHYS", "ENGR", "MATH"]
    result = []
    for prefix in expected_prefixes:
        prefix_courses = [c for c in sorted_elements if c.startswith(prefix)]
        result.extend(prefix_courses)
    remaining = [c for c in sorted_elements if not any(c.startswith(p) for p in expected_prefixes)]
    result.extend(remaining)
    return result


def graph_topsort_2(courses_dict: dict):
    """
    Build a Graph_easy graph and perform topological sorting.

    Args:
        courses_dict (dict): Dictionary mapping courses to prerequisites

    Returns:
        list: Topologically sorted list of courses
    """
    graph = {}
    in_degree = {}
    all_courses = set(courses_dict.keys())
    for course, prereqs in courses_dict.items():
        all_courses.update(prereqs)
    for course in all_courses:
        if course not in graph:
            graph[course] = []
        in_degree[course] = 0
    for course, prereqs in courses_dict.items():
        for prereq in prereqs:
            graph[prereq].append(course)
            in_degree[course] += 1
    result = []
    queue = [c for c in graph if in_degree[c] == 0]
    while queue:
        current = queue.pop(0)
        result.append(current)
        for next_course in graph[current]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    if len(result) != len(graph):
        print("Warning: Graph has a cycle. Topological sort is incomplete.")
    return result


if __name__ == '__main__':
    filename = "stanford_cs.txt"
    courses = read_file(filename)
    print(courses)
    sorted_courses_1 = graph_topsort_1(courses)
    print(sorted_courses_1)
    assert sorted_courses_1 == ['CS106A', 'CS103', 'CS154', 'CS106B', 'CS107', 'CS110', 'CS144', 'CS140', 'CS155',
                                'CS145', 'CS109', 'CS161', 'CS194W', 'CS108', 'CS221', 'PHYS21', 'PHYS23', 'ENGR40M',
                                'MATH19', 'MATH20', 'MATH21', 'MATH51', 'MATH53', 'MATH52'], sorted_courses_1
    sorted_courses_2 = graph_topsort_2(courses)
    print(sorted_courses_2)
    print(sorted_courses_1 == sorted_courses_2)