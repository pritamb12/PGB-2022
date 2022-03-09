#!//usr/bin/python3

class Day1:
    def __init__(self):
        # Define variables for each data type and store respective data
        self.Dict = {"key1": "Value1", "key2": "Value2"}
        self.List = [1, 2, 3, 4, 5, 6, "seven"]
        self.Integer = 1
        self.String = "hello"
        self.Set = {"value1", "value2", "value3"}
        self.Tuple = 1, 2, 3, 4, 5, 7, 7
        self.FrozenSet = frozenset(self.Tuple)
        print("\nInitialized Datatypes : \n")
        print(f"Dictionary : {self.Dict}")
        print(f"List : {self.List}")
        print(f"Integer : {self.Integer}")
        print(f"String : {self.String}")
        print(f"Set : {self.Set}")
        print(f"Tuple : {self.Tuple}")
        print(f"FrozenSet : {self.FrozenSet}")

    def override(self):
        print("\nOverriding Datatypes : \n")
        over = 1
        print("Initialized variable 'over' as Integer : ")
        print(over)
        over = "Override to String"
        print("Override Integer to String")
        print(over)
        over = [1, 2]
        print("Override String to List")
        print(over)
        over = {"key": "value"}
        print("Override List to Dictionary")
        print(over)
        over = {1, 2, 3}
        print("Override Dictionary to Set")
        print(over)
        over = 4, 5, 6
        print("Override Set to Tuple")
        print(over)

    def datatypes_add(self):
        print("\nAdding Datatypes : \n")
        try:
            a = 1 + "String"
        except Exception as e:
            print("Can't add Integer to String : 1 + 'String'")
        try:
            b = "String" + True
        except Exception as e:
            print("Can't add String to Boolean : 'String' + True")
        try:
            c = [1, 2] + (3, 4)
        except Exception as e:
            print("Can't add List to Tuple : [1, 2] + (3, 4)")

    def mutable_immutable(self):
        # Updating Datatypes
        print("\nList Mutable and Immutable Datatypes : \n")
        self.Dict["key1"] = "Value3"
        print(self.Dict)
        print("Dictionary is Mutable")
        self.List.append("eight")
        print(self.List)
        print("List is Mutable")
        print(self.Integer)
        self.Integer += 2
        print("Integer is Immutable")
        print(self.String)
        self.String += " world"
        print(self.String)
        print("String is Immutable")
        print(self.Set)
        self.Set.add("value4")
        print(self.Set)
        print("Set is Mutable")
        try:
            self.Tuple.append("9")
        except:
            print("Tuple Is Immutable")
        finally:
            print(self.Tuple)
        try:
            self.FrozenSet.append(2)
        except:
            print("FrozenSet Is Immutable")

    def list_operations(self):
        print("\nList Operations : \n")
        fruits = ['apple', 'banana', 'cherry']
        cars = ['Ford', 'BMW', 'Volvo']
        print(f"Fruits : {fruits}, Cars : {cars}")
        fruits.append("orange")
        print(f"Appended Fruits : {fruits}")
        fruits_copy = fruits.copy()
        print(f"Copied Fruits to new list : {fruits_copy}")
        fruits_copy.clear()
        print(f"Deleted elements in Fruits list : {fruits_copy}")
        print(f"DCount of cherry in Fruits list : {fruits.count('cherry')}")
        fruits.extend(cars)
        print(f"Added elements in cars list into fruits list : {fruits}")
        fruits.insert(1, "orange")
        print(f"Added 'orange' as second element in fruits list : {fruits}")
        del fruits[1]
        print(f"Deleted 2nd element in fruits list : {fruits}")
        fruits.remove("banana")
        print(f"Removed 'banana' from fruits list : {fruits}")
        fruits = fruits[::-1]
        print(f"Reversed elements in fruits list : {fruits}")
        cars.sort()
        print(f"Sorted cars list : {cars}")

    def string_operations(self):
        print("\nSet Operations : \n")
        print(f"String : {self.String}")
        String = self.String.upper()
        print(f"Converted string to uppercase : {self.String}")
        String = self.String.lower()
        print(f"Converted string to lowercase : {self.String}")
        print(f"Count of letter 'o' in string : {String.count('o')}")
        print(f"Check if string ends with 'd' : {String.endswith('d')}")
        print(f"Check if all characters in string is alphabet : {self.String.isalpha()}")
        print(String.title())
        print(f"Convert the first character of each word to upper case : {String}")
        print(self.String.capitalize())
        print(f"Convert the first character to upper case : {self.String}")
        print(String.find("l"))
        print(String[::-1])

    def tuple_operations(self):
        print("\nTuple Operations : \n")
        print(f"Count of value 7 in Tuple : {self.Tuple.count(7)}")
        print(f"Get index of value 3 in Tuple : {self.Tuple.index(3)}")

    def dictionary_operations(self):
        print("\nDictionary Operations : \n")
        dict_list = "key1", "key2", "key3"
        print("Create a dictionary with 3 different keys, all with the value '5' using inbuilt method")
        Dict1 = dict.fromkeys(dict_list, 5)
        print(Dict1)
        print(f"Return the value of the specified key : {Dict1['key1']}")
        print(f"Print all key, value pairs : {Dict1.items()}")
        print("Remove the element with the specified key : ")
        del Dict1["key2"]
        Dict1["key4"] = 6
        print(Dict1)
        print("Remove the last inserted key-value pair")
        Dict1.popitem()
        print(Dict1)

    def set_operations(self):
        print("\nSet Operations  : \n")
        print(self.Set)
        self.Set.add(10)
        print(f"Added an element to the set : {self.Set}")
        self.Set.remove(10)
        print(f"Remove specific element from the set : {self.Set}")

    def two_sets_operations(self):
        print("\nTwo Sets Operations : \n")
        print("create 2 sets x and y : ")
        x = {1, 2, 3, 4, 5, 7}
        y = {6, 7, 8, 9, 10, 11}
        print(f"Return a set that contains the items that only exist in set x, and not in set y : {x.difference(y)}")
        print("Remove the items that exist in both sets : ")
        x.difference_update(y)
        print(x)
        print(f"Items that exist in both sets : {x.intersection(y)}")
        print(f"Return True if no items in set x is present in set y : {x.isdisjoint(y)}")
        print(f"Return True if all items in set x are present in set y : {x.issubset(y)}")
        print(f"Return True if all items set y are present in set x : {y.issubset(x)}")
        print(f"Return a set that contains all items from both sets, except items that are present in both sets : {x.symmetric_difference(y)}")
        print(f"Remove the items that are present in both sets, AND insert the items that is not present in both sets : ")
        x.symmetric_difference_update(y)
        print(x)
        print(f"Return a set that contains all items from both sets, duplicates are excluded : {x.union(y)}")
        print("Insert the items from set y into set x : ")
        x.update(y)
        print(x)


main = Day1()
main.override()
main.datatypes_add()
main.mutable_immutable()
main.list_operations()
main.string_operations()
main.tuple_operations()
main.dictionary_operations()
main.set_operations()
main.two_sets_operations()