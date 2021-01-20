def about(name, age likes):
    sentence = "Meet {}! They are {} years old and they like {}.".format(name, age, likes)
    return sentence

dictionary = {"name": "Ryan", "age":23, "likes":"Python"}
about(**dictionary)



def war_type(**kwargs):
	for key, value in kwargs.items():
		print("call sign - {}: warrior type - {}".format(key, value))

