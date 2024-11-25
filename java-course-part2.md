# Part 2: Strings and Methods

## 1. String Class Methods

String is a special class in Java that helps us work with text. Unlike primitive types, String is a reference type, but it can be created using string literals (text in double quotes).

### Key String Methods

#### 1. charAt(int index)
Returns the character at the specified index (position) in a string.
- Index starts at 0
- Returns a char value

**Example:**
```java
String s = "Go_Sun_Devils";
char result = s.charAt(3);  // Returns '_'
```

Position breakdown:
```
Index: 0  1  2  3  4  5  6  7  8  9  10 11 12
Value: G  o  _  S  u  n  _  D  e  v  i  l  s
```

#### 2. compareTo(String anotherString)
Compares two strings lexicographically (dictionary order).
- Returns negative if calling string comes before parameter
- Returns positive if calling string comes after parameter
- Returns 0 if strings are equal

**Example:**
```java
String s1 = "a banana";
String s2 = "banana";
boolean result = s1.compareTo(s2) < 0;  // Returns true
```
Solution: true because "a banana" comes before "banana" in dictionary order

#### 3. equals(Object anObject)
Compares two strings for exact content match.
- Returns true if strings have identical content
- Returns false otherwise
- Always use equals() for String comparison, not ==

**Example:**
```java
String s1 = "carrot";
String s2 = "carrot";
boolean result = s2.equals(s1);  // Returns true
```

#### 4. indexOf(String str)
Finds the first occurrence of a substring.
- Returns the index of first occurrence
- Returns -1 if substring not found
- Case sensitive

**Examples:**
```java
String s = "Red and Blue are my favorite colors.";
int result = s.indexOf("a");  // Returns 4

String s2 = "Bananas and apples are yummy.";
int result2 = s2.indexOf("A");  // Returns -1 (not found)
```

#### 5. length()
Returns the number of characters in the string.

**Example:**
```java
String s = "7 birds and 12 cats";
int length = s.length();  // Returns 19
```

#### 6. substring(int beginIndex, int endIndex)
Extracts a portion of the string.
- beginIndex: inclusive (included)
- endIndex: exclusive (not included)
- Returns a new string

**Example:**
```java
String s = "Apples and bananas are yummy.";
String result = s.substring(1, 3);  // Returns "pp"
```

## 2. Methods and Method Calls

### Understanding Method Scope and Variables

Methods in Java have their own scope, meaning variables declared inside a method are only accessible within that method.

**Example:**
```java
class Main {
    private static void foo() {
        int x = 11;    // Local variable
    }

    private static int x = 5;    // Class variable

    public static void main(String[] args) {
        foo();
        System.out.println(x);    // Prints 5
    }
}
```

**Output: 5**

Explanation:
- The x inside foo() is different from the class variable x
- Changes to local variables don't affect variables outside the method
- Each method has its own scope

### Method Call Flow

Understanding how methods call each other and how values are passed is crucial.

**Example 1:**
```java
class Driver {
  public static void main(String[] args) {
    fop(8);
    baz(4);
  }

  static void fop(int a) {
    System.out.print(a);    // Prints 8
    baz(a + 1);            // Calls baz(9)
  }

  static void baz(int a) {
    System.out.print(a);    // Prints 9, then later 4
  }
}
```

**Output: 894**

Execution flow:
1. main calls fop(8)
2. fop prints 8
3. fop calls baz(9)
4. baz prints 9
5. main calls baz(4)
6. baz prints 4

**Example 2:**
```java
class Driver {
  public static void main(String[] args) {
    int a = fop(3);
    int b = baz(3);
  }

  static int fop(int a) {
    a = baz(a + 4);    // a = 7
    System.out.print(a);    // Prints 7
    return a;
  }

  static int baz(int a) {
    System.out.print(a);    // Prints 7, then 3
    return a - 0;
  }
}
```

**Output: 73**

### Key Concepts in Method Usage:

1. **Method Scope**
   - Variables declared in a method are local to that method
   - Local variables "hide" class variables of the same name
   - Each method call creates new local variables

2. **Method Parameters**
   - Parameters are local variables
   - Changes to parameters don't affect the original values
   - Parameters can have the same names as variables in other methods

3. **Return Values**
   - void methods don't return anything
   - Return type must match method declaration
   - Return statement exits the method immediately

### Common Pitfalls to Avoid:

1. Don't confuse local variables with class variables
2. Remember that each method call creates new variable spaces
3. Don't try to access local variables from other methods
4. Don't forget to use the return value if the method returns one
5. Don't rely on variable values persisting between method calls

### Practice Tips:

1. Draw method call diagrams
2. Track variable values in each scope
3. Write out the execution sequence
4. Practice tracing code with different inputs
5. Pay attention to return values and how they're used