# mengenal type data pada python

# integer
data_integer = 5
print("data : ", data_integer, "bertipe", type(data_integer))

# float
data_float = 2.5
print("data : ", data_float, "bertipe", type(data_float))

# string
data_string = "Ujang"
print("data : ", data_string, "bertipe", type(data_string))

# string
data_bool = True
print("data : ", data_bool, "bertipe", type(data_bool))

# type data kompleks
data_kompleks = complex(5,6)
print("data : ", data_kompleks, "bertipe", type(data_kompleks))

# type data C
from ctypes import c_double, c_char

data_double = c_double(2.2513)
print("data : ", data_double, "bertipe", type(data_double))