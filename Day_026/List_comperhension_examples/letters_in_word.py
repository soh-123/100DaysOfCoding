sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

sentence_list = sentence.split()
# new_dict = {new_key:new_value for (key, value) in list if test}
result = {word:len(word) for (word) in sentence_list}

print(result)

