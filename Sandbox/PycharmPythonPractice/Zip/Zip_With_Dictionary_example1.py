id = [1,2,3,4]
leaders = ["Elon Mask", "Tim Cook","Bill Gates", "Jack Ma"]

# Create dict by dict comprehension
leader_dict = {i: name for i, name in zip(id, leaders)}
print(leader_dict)

# Create dict by dict function
leader_dict2 = dict(zip(id, leaders))
print(leader_dict2)

# Update
other_id = [5, 6]
other_leaders = ["Sim Wong Foo", "Tan Ming Liang"]
leader_dict.update(zip(other_id, other_leaders))
print(leader_dict)
