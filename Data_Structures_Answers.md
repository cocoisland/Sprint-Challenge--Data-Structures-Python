Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method
    O(1)
2. What is the space complexity of your ring buffer's `append` function?
    O(1)

3. What is the runtime complexity of your ring buffer's `get` method?
    O(n)

4. What is the space complexity of your ring buffer's `get` method?
    O(n)

5. What is the runtime complexity of the provided code in `names.py`?
    for loop names_1 in for loop names_2 = O(n^2)

6. What is the space complexity of the provided code in `names.py`?
    names_1, names_2, duplicate = O(3n)

7. What is the runtime complexity of your optimized code in `names.py`?
    nameDict.py - insert names_1 into a set - O(n)
                  lookup names_2 against names_1 set/dictionary - O(n)
    Therefore runtime = O(2n)

8. What is the space complexity of your optimized code in `names.py`?
    nameDict.py - names_1, names_2, uniqName, duplicate = O(4n)