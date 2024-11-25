# Part 1: Java Basics

## 1. Variables and Assignment

### Understanding Variable Assignment
Variables in Java are like containers that hold values. When we assign values between variables, we're copying the value from one container to another.

#### Example Problem:
```java
int x = 17;
int y = 5;
int a = y;
y = x;
x = a;
```

**Solution: x will print 5**

Let's trace this step by step:
1. x is assigned 17
2. y is assigned 5
3. a is assigned y's value (5)
4. y is assigned x's value (17)
5. x is assigned a's value (5)

This is a common pattern for swapping values using a temporary variable (a).

## 2. Java Identifiers

Java identifiers are names given to variables, methods, classes, etc. They must follow specific rules.

### Rules for Valid Identifiers:
1. Must begin with a letter, underscore (_), or dollar sign ($)
2. Cannot begin with a number
3. Can only contain letters, numbers, underscores, and dollar signs
4. Cannot be a Java keyword
5. Cannot contain spaces

### Practice Problem Solutions:
Valid identifiers:
- ✅ My_vAlUe
- ✅ Tax
- ✅ a123b
- ✅ name1
- ✅ _hi_world_
- ✅ vairabel
- ✅ max_of_array
- ✅ Code123
- ✅ SpEcIaL_vAlUe_1

Invalid identifiers:
- ❌ 1NAME (starts with number)
- ❌ a-bonus (contains hyphen)
- ❌ in_&_out (contains &)
- ❌ sum and difference (contains spaces)
- ❌ Test Variable (contains space)
- ❌ 00xGOLD (starts with number)
- ❌ My Variable (contains space)
- ❌ 2_Tax (starts with number)
- ❌ !age (contains !)
- ❌ x & y (contains space and &)

## 3. Basic Expressions

### Math Expressions
When evaluating mathematical expressions, remember the order of operations (PEMDAS):
1. Parentheses
2. Exponents
3. Multiplication and Division (left to right)
4. Addition and Subtraction (left to right)

#### Example:
```java
a + b % c * d
```
Given: a = 11, b = 37, c = 3, d = 5

Solution: 36
1. First: 37 % 3 = 1 (remainder)
2. Then: 1 * 5 = 5
3. Finally: 11 + 5 = 36

### Logical Expressions
Logical operators:
- && (AND)
- || (OR)
- ! (NOT)

Example: `false || false`
Solution: `false`
(false OR false is false)

### Relational Expressions
Compare values using:
- == (equal to)
- != (not equal to)
- > (greater than)
- < (less than)
- >= (greater than or equal to)
- <= (less than or equal to)

Example: `3 == 1`
Solution: `false`
(3 is not equal to 1)

## 4. Primitive Data Types

Java has eight primitive data types:

1. **boolean**
   - Stores true/false values
   - Size: 1 bit

2. **byte**
   - Stores whole numbers from -128 to 127
   - Size: 8 bits

3. **short**
   - Stores whole numbers from -32,768 to 32,767
   - Size: 16 bits

4. **int**
   - Stores whole numbers from -2^31 to 2^31-1
   - Size: 32 bits

5. **long**
   - Stores whole numbers from -2^63 to 2^63-1
   - Size: 64 bits

6. **float**
   - Stores fractional numbers up to 7 decimal digits
   - Size: 32 bits
   - Must end with 'f' or 'F'

7. **double**
   - Stores fractional numbers up to 15 decimal digits
   - Size: 64 bits

8. **char**
   - Stores a single character/letter
   - Size: 16 bits

### Practice Questions Solutions:

#### Float Literals:
- ✅ 5.25f
- ✅ 5f
- ❌ 5.25 (double)
- ❌ '\n' (char)
- ❌ '5' (char)
- ❌ "5.0" (String)

#### Char Literals:
- ✅ '\n'
- ✅ '5'
- ❌ 5.25 (double)
- ❌ "true" (String)
- ❌ 123 (int)
- ❌ "5.0" (String)

## Practice Exercise

Write a line of Java code that declares a double variable named x initialized to 90.24.

**Solution:**
```java
double x = 90.24;
```

### Common Pitfalls to Avoid:
1. Don't forget to initialize variables before using them
2. Don't confuse = (assignment) with == (comparison)
3. Don't use reserved keywords as identifiers
4. Don't forget type suffixes (f for float)
5. Don't mix up primitive types with their wrapper classes

### Key Takeaways:
1. Java is a strongly-typed language - every variable must have a declared type
2. Primitive types are the building blocks of Java programs
3. Understanding identifier rules is crucial for naming variables
4. Type conversion rules are important for avoiding errors
5. Expression evaluation follows strict order of operations