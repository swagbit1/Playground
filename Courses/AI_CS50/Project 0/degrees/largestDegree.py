import csv
import sys
import random

from util import Node, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}

SAMPLE_SIZE = 3


def load_data(directory):
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def shortest_path(source, target):
    start = Node(state=source, parent=None, action=None)
    frontier = QueueFrontier()
    frontier.add(start)
    explored = set()

    while True:
        if frontier.empty():
            return None

        node = frontier.remove()

        if node.state == target:
            actions = []
            cells = []
            while node.parent is not None:
                actions.append(node.action)
                cells.append(node.state)
                node = node.parent
            actions.reverse()
            cells.reverse()
            return list(zip(actions, cells))

        explored.add(node.state)

        for action, state in neighbors_for_person(node.state):
            if not frontier.contains_state(state) and state not in explored:
                child = Node(state=state, parent=node, action=action)
                frontier.add(child)


def neighbors_for_person(person_id):
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


def main():
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    print("Loading data...")
    load_data(directory)
    print(f"Data loaded. {len(people)} people found.")
    print(f"Sampling {SAMPLE_SIZE:,} random pairs...\n")

    all_ids = list(people.keys())
    top10 = []  # list of (degree, path, id1, id2)
    checked = 0
    skipped = 0

    for i in range(SAMPLE_SIZE):
        id1, id2 = random.sample(all_ids, 2)

        checked += 1
        print(f"  Checked {checked:,}/{SAMPLE_SIZE:,} | Skipped (no path): {skipped:,} | Top degree so far: {top10[0][0] if top10 else 0}")

        path = shortest_path(id1, id2)
        if path is None:
            skipped += 1
            continue

        degree = len(path)

        if len(top10) < 10:
            top10.append((degree, path, id1, id2))
            top10.sort(key=lambda x: x[0], reverse=True)
        elif degree > top10[-1][0]:
            top10[-1] = (degree, path, id1, id2)
            top10.sort(key=lambda x: x[0], reverse=True)

    print("\n===== TOP 10 MOST SEPARATED PAIRS =====\n")
    for rank, (degree, path, id1, id2) in enumerate(top10, 1):
        name1 = people[id1]["name"]
        name2 = people[id2]["name"]
        print(f"#{rank}: {name1} <-> {name2} — {degree} degrees of separation")
        full_path = [(None, id1)] + path
        for i in range(degree):
            p1 = people[full_path[i][1]]["name"]
            p2 = people[full_path[i + 1][1]]["name"]
            movie = movies[full_path[i + 1][0]]["title"]
            print(f"   {i + 1}: {p1} and {p2} starred in {movie}")
        print()


if __name__ == "__main__":
    main()