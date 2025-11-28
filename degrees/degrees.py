import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
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

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    # TODO

    """We can frame this as a search problem: our states are people. 
        Our actions are movies, which take us from one actor to another 
        (it's true that a movie could take us to multiple different actors, but that's okay for this problem).
        Our initial state and goal state are defined by the two people we're trying to connect. 
        By using breadth-first search, we can find the shortest path from one actor to another. """

    # I need to figure out if i can use the self attribute here 
    # I need to figure out where to use source and target in the following code (goal == target)
    # I need to FO if it is of to use the queue stack for the following code (YES)
    # I need to think about the data structures involved
    

    # shortest_path should return a list of tuples of strings [(1, 2), (3, 4)], where each item is (movie_id, person_id)
    # given a source, select the source in the people dictionary and add each film in the movie set to the frontier
    # using a queue, loop for the stars in each movie in search of target, exempting the explored
    # for each non-match, add the movie to the explored set
    # if target found, break and return result
    # else add the movies for that star to the frontier 


    # Keep track of number of states explored
    num_explored = 0

    # Initialize the frontier to the starting position
    start = Node(state=source, parent=None, action=None)
    frontier = QueueFrontier()
    frontier.add(start)

    # Initialize an empty explored set
    explored = set()

    # Keep looping until solution found
    while True:

        # If nothing left in frontier, then no path
        if frontier.empty():
            return None
        
        # Choose a node from the frontier
        node = frontier.remove()
        num_explored += 1

        # If node is in the goal, we have a solution
        if node.state == target:
            actions = []
            cells = []
        
            # Follow parent node to find solution
            while node.parent is not None:
                actions.append(node.action)
                cells.append(node.state)
                node = node.parent
            actions.reverse() #i need to reverse it because as of now i've appended them from the target to the source 
            cells.reverse()

            solutions = []
            length = len(actions) 
            for i in range(length):
                pair = (actions[i], cells[i])
                solutions.append(pair)
            return solutions

        # Mark node as explored
        explored.add(node.state)

        # Add neighours to frontier
        for action, state in neighbors_for_person(node.state):
            if not frontier.contains_state(state) and state not in explored:
                child = Node(state=state, parent=node, action=action)
                frontier.add(child)


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
