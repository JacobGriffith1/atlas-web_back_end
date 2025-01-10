# Python - Variable Annotations
Project for Atlas School

## Learning Objectives
At the end of this project, understand:
- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with ```mypy```

## Tasks

## 0. Basic Annotations - Add
Write a type-annotated function ```add``` that takes a float ```a``` and a float ```b``` as arguments and returns their sum as a float.

## 1. Basic Annotations - Concat
Write a type-annotated function ```concat``` that takes a string ```str1``` and a string ```str2``` as arguments and returns a concatenated string.

## 2. Basic Annotations - Floor
Write a type-annotated function ```floor``` which takes a float ```n``` as an argument and returns the floor of the float

## 3. Basic Annotations - To String
Write a type-annotated function ```to_str``` that takes a float ```n``` as an argument and returns the string representation of the float.

## 4. Define Variables
Define and annotate the following variables with the specified values:
- ```a```, an integer with a value of 1
- ```pi```, a float with a value of 3.14
- ```i_understand_annotations```, a boolean with a value of True
- ```school```, a string with a value of "Holberton"

## 5. Complex Types - List of Floats
Write a type-annotated function ```sum_list``` which takes a list ```input_list``` of floats as an argument and returns their sum as a float.

## 6. Complex Types - Mixed List
Write a type-annotated function ```sum_mixed_list``` which takes a list ```mxd_lst``` of integers and floats and returns their sum as a float.

## 7. Complex Types - String and Int/Float to Tuple
Write a type-annotated function ```to_kv``` that takes a string ```k``` and an int OR float ```v``` as arguments and returns a tuple. The first element of the tuple is the string ```k```. The second element us the square of the int/float ```v``` and should be annotated as a float.

## 8. Complex Types - Functions
Write a type-annotated function ```make_multiplier``` that takes a float ```multiplier``` as an argument and returns a function that multiplies a float by ```multiplier```.

## 9. Let's Duck Type an Iterable Object
Annotate the below function's parameters and return values with the appropriate types.
```
def element_length(lst):
    return [(i, len(i)) for i in lst]
```
