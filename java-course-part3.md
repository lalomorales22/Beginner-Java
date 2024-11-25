# Part 3: Control Flow

## 1. Decision Logic

Decision logic allows your program to make choices based on conditions. Java provides several structures for implementing decision logic.

### Simple If Statements

The basic form of decision making. Code inside the if block executes only if the condition is true.

```java
if (condition) {
    // code to execute if condition is true
}
```

**Example 1:**
```java
class Driver {
  public static void main(String[] args) {
    int a = 40;
    int b = 8;

    if (a > 73 && b < 8) {
      System.out.print(a);
    }
    System.out.print(b);
  }
}
```
**Output: 8**

Explanation:
- Condition `a > 73 && b < 8` is false (40 is not > 73)
- If block is skipped
- Program prints only b's value (8)

### Multiple If Statements

Multiple independent conditions can be checked using separate if statements.

**Example 2:**
```java
class Driver {
  public static void main(String[] args) {
    int a = 7;
    int b = 3;
    int c = 5;
    int x = 1;

    if (a < 3) {
      x = x + 700;
    }
    if (b < 7) {
      x = x + 30;
    }
    if (c < 2) {
      x = x + 5;
    }

    System.out.print(x);
  }
}
```
**Output: 31**

Explanation:
1. First if: false (7 is not < 3), x stays 1
2. Second if: true (3 < 7), x becomes 31
3. Third if: false (5 is not < 2), x stays 31

### If-Else Statements

Provides alternative code to execute when the condition is false.

**Example 3:**
```java
int a = 5;
int b = 17;
int c = 6;
int x = 17;
 
if (c >= b - a) {
    x = 1;
} else {
    x = 3;
}
 
System.out.print(x);
```
**Output: 3**

Explanation:
- b - a = 17 - 5 = 12
- c >= 12 is false (6 is not >= 12)
- else block executes, setting x to 3

### Nested If Statements

If statements can be placed inside other if statements.

**Example 4:**
```java
class Driver {
  public static void main(String[] args) {
    int a = 40;
    int b = 40;

    if (a > 26)
      if (b < 31)
        System.out.print(a);
      else
        System.out.print(b);
    else
      System.out.print(a + b);
  }
}
```
**Output: 40**

Explanation:
1. Outer if: true (40 > 26)
2. Inner if: false (40 is not < 31)
3. Inner else executes, printing b (40)

### If-Else If Chains

For multiple mutually exclusive conditions.

**Example 5:**
```java
int a = 3;
int b = 1;
int c = 7;
int x = 10;
 
if (a <= b) {
    x = 15;
} else if (a <= c) {
    x = 13;
} else if (b <= c) {
    x = 17;
} else {
    x = 12;
}
 
System.out.print(x);
```
**Output: 13**

Explanation:
1. First if: false (3 is not <= 1)
2. First else if: true (3 <= 7)
3. x becomes 13
4. Remaining conditions are not checked

## 2. Loops

Loops allow you to execute code repeatedly. Java provides several types of loops.

### While Loops

Executes code while a condition remains true.

**Example 1:**
```java
class Driver {
  public static void main(String[] args) {
    int a = 15;
    int b = a + 12;  // b = 27

    while (a < b) {
      a = a + 2;     // a increases by 2
      b = b - 1;     // b decreases by 1
    }

    System.out.print(a + b);
  }
}
```
**Output: 47**

Trace table:
```
Initial: a=15, b=27
Loop 1:  a=17, b=26
Loop 2:  a=19, b=25
Loop 3:  a=21, b=24
Loop 4:  a=23, b=23
End:     a=23, b=24 (23 + 24 = 47)
```

### For Loops

Used when you know how many iterations you need.

**Example 2:**
```java
class Driver {
  public static void main(String[] args) {
    int a = 90;

    for (int i = 6; i > 1; i--) {
      a = a - i;
    }

    System.out.print(a);
  }
}
```
**Output: 75**

Trace table:
```
Start:  a=90, i=6    a=90-6=84
Loop 1: a=84, i=5    a=84-5=79
Loop 2: a=79, i=4    a=79-4=75
Loop 3: a=75, i=3    a=75-3=72
Loop 4: a=72, i=2    a=72-2=70
End:    a=70
```

### Nested Loops

Loops inside other loops for more complex iterations.

**Example 3:**
```java
class Driver {
  public static void main(String[] args) {
    int a = 15;
    int b = 0;

    for (int c = 6; c > 3; c--) {
      b = 0;
      while (b < c) {
        b = b + 1;
        a = a + b;
      }
      b = b + a;
    }
    System.out.print(b);
  }
}
```

### Key Concepts in Control Flow:

1. **Decision Making**
   - Conditions must evaluate to boolean
   - Multiple conditions can be combined with && (AND) and || (OR)
   - Code blocks determine scope of if/else statements

2. **Loop Control**
   - Loop condition must eventually become false
   - Variables modified in the loop affect the condition
   - Break and continue can alter loop flow

3. **Nested Structures**
   - If statements and loops can be nested
   - Each level of nesting increases complexity
   - Inner structures complete before outer ones continue

### Common Pitfalls to Avoid:

1. Infinite loops (condition never becomes false)
2. Off-by-one errors in loop counters
3. Forgetting curly braces for multi-line blocks
4. Mismatched if-else pairs in nested statements
5. Complex conditions that are hard to understand

### Practice Tips:

1. Draw flow diagrams for complex logic
2. Create trace tables for loops
3. Test boundary conditions
4. Use meaningful variable names
5. Keep conditions simple and readable