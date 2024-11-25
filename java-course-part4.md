# Part 4: Arrays and Objects

## 1. Arrays

Arrays in Java are objects that store multiple values of the same type. The size of an array is fixed when it's created.

### Array Declarations and Instantiation

#### One-Dimensional Arrays

There are several ways to declare and instantiate arrays:

```java
// Declaration and instantiation in separate steps
int[] values;           // Declaration
values = new int[5];    // Instantiation

// Declaration and instantiation in one step
int[] values = new int[5];

// Declaration, instantiation, and initialization
int[] values = {4, 60, 19, 57, 80};
```

**Valid Array Declarations:**
```java
// ✅ These are correct:
float[] values = new float[5];    // Creates array of 5 floats
float[] values = new float[4];    // Creates array of 4 floats
float[6] values = new float[6];   // Creates array of 6 floats
```

**Invalid Array Declarations:**
```java
// ❌ These are incorrect:
float[5] values = new float[];    // Size missing in instantiation
float[] values = float[5];        // Wrong syntax
float[4] values = new float[6];   // Sizes don't match
```

#### Two-Dimensional Arrays

2D arrays are arrays of arrays, useful for representing tables or matrices.

**Valid 2D Array Declarations:**
```java
// ✅ These are correct:
float[][] values = new float[8][6];   // 8 rows, 6 columns (48 elements)
float[][] values = new float[6][8];   // 6 rows, 8 columns (48 elements)
float[][] values = new float[4][12];  // 4 rows, 12 columns (48 elements)
```

**Invalid 2D Array Declarations:**
```java
// ❌ These are incorrect:
float[,] values = float[4,8];     // Wrong syntax
float[48] values = new float[48]; // Not a 2D array
float[][] values = new float[48]; // Second dimension missing
```

### Array Access and Manipulation

Arrays use zero-based indexing, meaning the first element is at index 0.

**Example:**
```java
int[] values = {4, 60, 19, 57, 80, 97, 65, 9, 14, 78};
System.out.println(values[1]);    // Prints 60

int[][] grid = {
    {4, 71, 26, 63},
    {18, 91, 45, 49},
    {79, 34, 85, 98}
};
System.out.println(grid[1][2]);   // Prints 45
```

### Array Iteration

There are several ways to iterate over arrays. Here are the correct ways:

```java
// ✅ Correct forward iteration
for (int j = 0; j < values.length; j++) {
    values[j]--;
}

// ✅ Correct backward iteration
for (int j = values.length - 1; j >= 0; j--) {
    values[j]--;
}
```

**Common Iteration Errors:**
```java
// ❌ Incorrect (ArrayIndexOutOfBoundsException)
for (int j = values.length; j > 0; j--)  // Starts at invalid index
    values[j]--;

// ❌ Incorrect (Misses last element)
for (int j = 0; j < values.length - 1; j++)
    values[j]--;
```

## 2. Object-Oriented Programming Basics

### Classes and Objects

A class is a blueprint for objects. Objects are instances of classes.

**Example Class Definition:**
```java
public class Box {
    // Instance variables (attributes)
    private double height;
    private double width;
    private double length;
    
    // Constructor
    public Box(double height, double width, double length) {
        this.height = height;
        this.width = width;
        this.length = length;
    }
    
    // Method
    public boolean isTall() {
        return height > width && height > length;
    }
}
```

### Object Instantiation

Creating objects from a class using constructors.

**Valid Object Creation:**
```java
// ✅ These are correct:
Pet myPet = new Pet();                    // Default constructor
Pet yourPet = new Pet(3, "Cat");         // Parameterized constructor
```

**Invalid Object Creation:**
```java
// ❌ These are incorrect:
new Pet myPet = Pet();                    // Wrong syntax
Pet myPet = new Pet("Cat");              // Wrong number of parameters
String yourPet = new Pet(3, "Dog");      // Wrong reference type
```

## 3. Binary Search

Binary search is an efficient algorithm for finding elements in a sorted array.

### Example:
```java
int[] list = {2, 6, 13, 19, 22, 26, 32, 39, 44, 48, 51, 57, 61, 69, 73};
// Searching for 11
```

**Binary Search Process:**
1. Compare middle element (32)
2. 11 < 32, so search left half
3. Compare middle of left half (13)

The third comparison would be with 6.

## 4. Practice Programming Problems

### Problem 1: Min Plus Max Method
Write a method that finds the sum of the minimum and maximum values in an array.

```java
public static int minPlusMax(int[] arr) {
    if (arr == null || arr.length == 0) {
        throw new IllegalArgumentException("Array cannot be null or empty");
    }
    
    int min = arr[0];
    int max = arr[0];
    
    for (int i = 1; i < arr.length; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    
    return min + max;
}
```

### Problem 2: Box Class Implementation
Complete implementation of the Box class.

```java
public class Box {
    // Instance variables
    private double height;
    private double width;
    private double length;
    
    // Constructor
    public Box(double height, double width, double length) {
        this.height = height;
        this.width = width;
        this.length = length;
    }
    
    // Method to check if box is tall
    public boolean isTall() {
        return height > width && height > length;
    }
}
```

### Key Concepts:

1. **Array Fundamentals**
   - Fixed size
   - Zero-based indexing
   - Type safety
   - Length property

2. **Object-Oriented Principles**
   - Encapsulation
   - Constructor usage
   - Method implementation
   - Instance variables

3. **Algorithm Implementation**
   - Loop control
   - Decision making
   - Array manipulation
   - Error handling

### Common Pitfalls to Avoid:

1. Array index out of bounds errors
2. Forgetting to initialize arrays
3. Incorrect loop boundaries
4. Missing private modifiers for instance variables
5. Not handling null or empty arrays

### Practice Tips:

1. Always test boundary conditions
2. Consider edge cases (null, empty arrays)
3. Test with different array sizes
4. Verify object state after operations
5. Use meaningful variable names