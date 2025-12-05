# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.people = []

    def add(self, person: Person):
        self.people.append(person)

    def is_empty(self):
        return True if len(self.people) == 0 else False

    def print_contents(self):
        print(
            f"There are {len(self.people)} in the room, and their combined height is {sum([person.height for person in self.people])} cm"
        )
        for person in self.people:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if len(self.people) == 0:
            return None
        height_array = [person.height for person in self.people]
        shortest_index = height_array.index(min(height_array))
        return self.people[shortest_index]

    def remove_shortest(self):
        if len(self.people) == 0:
            return None
        shortest = self.shortest()
        self.people.remove(shortest)
        return shortest


if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
