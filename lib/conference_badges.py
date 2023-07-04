def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_list = []
    for name in names:
        badge_list.append(f"Hello, my name is {name}.")
    return badge_list

def assign_rooms(names):
    rooms_list = []
    index = 1
    for name in names:
        rooms_list.append(f"Hello, {name}! You'll be assigned to room {index}!")
        index += 1
    return rooms_list

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for room in assign_rooms(names):
        print(room)
