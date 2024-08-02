
def test_function(string):
    result = string
    def inner_function(string):
        result = string
        print(result)

    inner_function('I in scope view test_function')
    return result

result = test_function('Local result from "test_function" to global result')
print(result)
test_function(1)
print(test_function(1))

print(inner_function)  # an error message appears, because function has enclosing data type

# LEGB rule: local -> enclosing -> global -> built-in
# From less to more