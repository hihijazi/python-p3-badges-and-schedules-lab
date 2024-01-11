def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    # list_names = []
    # for name in names:
    #     list_names.append(badge_maker(name))
    # return list_names
    names= [badge_maker(name) for name in names]
    return names

def assign_rooms(names):
    list = []
    for i in range(len(names)):
        list.append(f'Hello, {names[i]}! You\'ll be assigned to room {i + 1}!')
    return list

def printer(names):
    list_badge= batch_badge_creator(names)
    for name in list_badge:
        print (name)
    list_rooms = assign_rooms(names)  
    for name in list_rooms:
        print(name)