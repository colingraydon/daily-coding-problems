# Let’s say you are an airport navigation software, and you are given a mapping of source airports and a list of destination airports that you can fly to. An example input would look like this:

# input_mapping = {

#             A: [ B ],

#             B: [ A, E ]

#             C: [ D ]

#             D: [ C, A ]

#             E: [A]

#

# }

#  Write a function given inputs (src, dst, input_mapping) that will return true if there’s a valid path from 


def find_navigation(src, dst, input_mapping):


    q = []
    visited_cities = []
    visited_cities.append(src)

    count = 0
    temp = input_mapping[src]

    for element in temp:
        q.append(element)

    while (len(q) > 0):

        current = q.pop(0)
        if current == dst:
            return True
        else:
            if (current not in visited_cities):
                visited_cities.append(current)
                temp_list = input_mapping[current]
                for element in temp_list:
                    q.append(element)

    return False


test_data = {"A": ["B"],"B": ["A", "E"],"C": ["D"],"D": ["C", "A"], "E": ["A"]}

# print(find_navigation("A", "D", test_data))

print(find_navigation("A", "C", test_data))






