x = 10
y = 0

try:
    result = x / y
except ZeroDivisionError as ex:
    print("Exception occurred:", ex)
except ValueError:
    print("Another exception")
else:
    print("No exception occurred")
finally:
    print("Close the context")
