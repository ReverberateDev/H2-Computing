# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.5 # Or your jupytext version
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Chapter S2A: Programming Elements (H2 Computing 9569)
#
# This notebook covers fundamental programming elements including coding standards, arrays, trace tables, data validation/verification, program testing, and recursion.

# %% [markdown]
# ## 1. Coding Standards & Good Programming Style (Syllabus 2.1.1 - 2.1.3)
#
# **Coding standards** are rules and guidelines for writing code to ensure it is:
# *   Well-structured
# *   Maintainable
# *   Readable
# *   Consistent
#
# Good **programming style** enhances clarity and elegance.
#
# ### 1.1 Principles of Good Programming Style:
#
# 1.  **Use Comments Effectively:**
#     *   Include header comments (programmer name, date, description, version).
#     *   Explain the purpose of functions/algorithms (objectives, inputs, outputs).
#     *   Clarify complex logic, but avoid explaining basic syntax.
# 2.  **Use Meaningful Identifiers:**
#     *   Variable/function names should be descriptive (e.g., `total_score` instead of `ts`).
#     *   Avoid single letters unless conventional (like `i`, `j`, `k` for loop counters).
# 3.  **Apply Proper Indentation and White Space:**
#     *   Use consistent indentation (e.g., 4 spaces) to show code structure (loops, conditionals).
#     *   Use blank lines to separate logical blocks of code.
# 4.  **Adhere to Specifications:**
#     *   Ensure the program meets all requirements defined in the problem statement.
# 5.  **Avoid Deep Nesting:**
#     *   Limit nesting levels of loops and `IF` statements, as excessive nesting reduces readability and can increase execution time. Consider refactoring into functions if nesting becomes too deep.
#
# ### 1.2 Coding Standards in A-Level Practical Exams
#
# Marks are awarded for:
# *   **Indentation and White Space:** Proper and consistent use.
# *   **Meaningful Identifiers:** Clear, descriptive names for variables, constants, functions, etc.
# *   **Comments:** Inclusion of comments to clarify code logic or purpose.

# %% [markdown]
# ## 2. Arrays (Syllabus 2.2.1)
#
# An **array** is a data structure that stores a **finite**, **ordered** collection of elements of the **same data type**.
#
# *   **Finite:** Fixed number of elements, determined at declaration.
# *   **Ordered:** Each element has a specific position (index).
# *   **Same Data Type:** All elements must be integers, reals, characters, etc.
# *   **Contiguous Memory:** Elements are typically stored next to each other in memory.
# *   **Access:** Elements are accessed using the array name and an index (e.g., `myArray[3]`).
# *   **Indexing:**
#     *   **Pseudo-code:** Often uses 1-based indexing (e.g., `ARRAY[1:10]`). Bounds (`L:U`) are inclusive. Can also use `ARRAY[<size>]`.
#     *   **Python:** Uses **0-based** indexing (first element is at index 0).

# %% [markdown]
# ### 2.1 One-dimensional (1D) Array
# A linear sequence of elements.
#
# #### Pseudo-code Declaration

# %%
# // Method 1: Using Lower and Upper Bounds (Inclusive)
# DECLARE StudentID : ARRAY[1:10] OF INTEGER
#
# // Method 2: Using Size (Often implies 0-based or 1-based depending on context,
# // but Cambridge often assumes 1-based if size is used like this unless specified)
# DECLARE Scores : ARRAY[30] OF REAL

# %% [markdown]
# #### Python Implementation (using Lists)
# Python lists are dynamic but often used to implement array concepts. For fixed-type arrays, libraries like NumPy are common, but standard lists suffice for basic A-Level concepts.

# %%
# Python list acting as an array (0-based index)
# Simulating DECLARE Scores : ARRAY[1:5] OF INTEGER
scores = [0] * 5 # Creates a list of 5 zeros -> indices 0, 1, 2, 3, 4

# Accessing elements (remember 0-based)
scores[0] = 95 # Accessing the first element
scores[4] = 78 # Accessing the fifth (last) element

print(f"Scores array (list): {scores}")
print(f"First score: {scores[0]}")

try:
    print(scores[5]) # This would cause an IndexError
except IndexError as e:
    print(f"Error accessing index 5: {e}")

# %% [markdown]
# ### 2.2 Two-dimensional (2D) Array
# An array of arrays, representing a grid or table structure (rows and columns).
#
# #### Pseudo-code Declaration

# %%
# DECLARE Attendance : ARRAY[1:5, 1:4] OF CHAR
# // Represents a 5x4 grid (5 rows, 4 columns)
# // Indices are [row, column]

# %% [markdown]
# #### Accessing 2D Array Elements (Pseudo-code)

# %%
# // Accessing element at Row 3, Column 2
# someVar ← Attendance[3, 2]
#
# // Assigning to element at Row 5, Column 3
# Attendance[5, 3] ← 'N'

# %% [markdown]
# #### Python Implementation (using Lists of Lists)

# %%
# Simulating DECLARE Attendance : ARRAY[1:5, 1:4] OF CHAR
# Using 0-based indexing for both dimensions

rows = 5
cols = 4

# Create a 5x4 grid initialized with spaces
attendance = [[' ' for _ in range(cols)] for _ in range(rows)]

# Accessing elements (remember 0-based)
# Corresponds to pseudo-code Attendance[3, 2] -> Python attendance[2][1]
attendance[2][1] = 'Y'

# Corresponds to pseudo-code Attendance[5, 3] -> Python attendance[4][2]
attendance[4][2] = 'N'

print("Attendance grid (list of lists):")
for row_index in range(rows):
    print(attendance[row_index])

print(f"\nElement at Row 3, Col 2 (Python index [2][1]): {attendance[2][1]}")
print(f"Element at Row 5, Col 3 (Python index [4][2]): {attendance[4][2]}")


# %% [markdown]
# ### 2.3 Assigning a Group of Elements into an Array
# Often done using a loop to initialize or populate the array.
#
# #### Pseudo-code Example: Initializing an array

# %%
# DECLARE SpellingTest : ARRAY[1:30] OF INTEGER
# DECLARE index : INTEGER
#
# FOR index ← 1 TO 30
#   SpellingTest[index] ← -1 // Initialize each element to -1
# ENDFOR

# %% [markdown]
# #### Python Implementation

# %%
# Initialize a list of 30 elements to -1
spelling_test = [-1] * 30
print(f"Initialized spelling_test (first 10 elements): {spelling_test[:10]}...")

# Alternative using a loop (more verbose for simple initialization)
spelling_test_loop = []
for _ in range(30):
    spelling_test_loop.append(-1)
# print(spelling_test_loop)


# %% [markdown]
# ## 3. Trace Table (Syllabus 2.2.6)
#
# A **trace table** is a technique used to test algorithms by manually simulating the execution step-by-step on paper. It helps track the values of variables, conditions, and outputs to understand the algorithm's flow and detect logic errors (**dry run**).
#
# *   **Structure:** Columns for relevant variables, conditions being tested, and any output produced.
# *   **Process:** Go through the algorithm line by line, updating the table entry for any variable that changes or recording condition results and outputs at each step.
# *   **Purpose:** Debugging, verifying logic, understanding algorithm behavior with specific inputs.
# *   **Clarity:** If a variable doesn't change in a step, the cell can be left blank in that row for clarity.
#
# *(See PDF Page 4 for examples of trace tables for a simple loop and nested loops).*

# %% [markdown]
# #### Example: Trace Table for Simple Loop (from PDF, Input = 4)
#
# **Pseudo-code:**
# ```pseudocode
# num ← USERINPUT
# WHILE num < 100 DO
#   num ← num * 2
# ENDWHILE
# OUTPUT num
# ```
#
# **Trace Table:**
#
# | Step        | Line Executed         | num | num < 100 | OUTPUT | Notes                     |
# |-------------|-----------------------|-----|-----------|--------|---------------------------|
# | 1           | `num ← USERINPUT`     | 4   |           |        | Initial input             |
# | 2           | `WHILE num < 100 DO`  | 4   | TRUE      |        | Condition met             |
# | 3           | `num ← num * 2`       | 8   | TRUE      |        | num updated               |
# | 4           | `WHILE num < 100 DO`  | 8   | TRUE      |        | Loop continues            |
# | 5           | `num ← num * 2`       | 16  | TRUE      |        | num updated               |
# | 6           | `WHILE num < 100 DO`  | 16  | TRUE      |        | Loop continues            |
# | 7           | `num ← num * 2`       | 32  | TRUE      |        | num updated               |
# | 8           | `WHILE num < 100 DO`  | 32  | TRUE      |        | Loop continues            |
# | 9           | `num ← num * 2`       | 64  | TRUE      |        | num updated               |
# | 10          | `WHILE num < 100 DO`  | 64  | TRUE      |        | Loop continues            |
# | 11          | `num ← num * 2`       | 128 | TRUE      |        | num updated               |
# | 12          | `WHILE num < 100 DO`  | 128 | FALSE     |        | Condition fails, loop exits |
# | 13          | `OUTPUT num`          | 128 | FALSE     | 128    | Final output              |

# %% [markdown]
# ## 4. Data Validation and Verification (Syllabus 2.4.1 - 2.4.2)
#
# These are processes to ensure data integrity, but they check different things.
#
# ### 4.1 Data Verification
#
# **Verification** confirms that data has been transferred accurately from one source/medium to another without errors introduced during the transfer (e.g., typing, copying). **It does not check if the original data was correct.**
#
# *   **Purpose:** Detect errors during data entry or transmission.
# *   **Types of Errors Detected:**
#     *   **Transcription errors:** Mistakes made when copying data (e.g., misreading handwriting, OCR errors).
#     *   **Transposition errors:** Accidentally swapping adjacent characters (e.g., typing `132` instead of `123`).
# *   **Techniques:**
#     *   **Double Entry:** Entering the data twice; the system compares the two entries and flags discrepancies (e.g., password confirmation fields).
#     *   **Visual Check:** A human compares the entered data on the screen with the original source document.
#
# ### 4.2 Data Validation
#
# **Validation** is an **automated** check performed by the software to ensure that input data is **sensible, reasonable, complete, and within acceptable boundaries** according to predefined rules. **It does not guarantee accuracy** (e.g., a valid date might still be the *wrong* date).
#
# *   **Purpose:** Prevent garbage data from being processed.
# *   **When:** Typically performed *before* data is processed.
# *   **Common Validation Checks:**
#
# | Check Type     | Description                                       | Example                                                                     |
# |----------------|---------------------------------------------------|-----------------------------------------------------------------------------|
# | **Range Check**  | Ensures data falls within a defined min/max range. | Month must be between 1 and 12. Score must be between 0 and 100.            |
# | **Format Check** | Ensures data follows a specific pattern/structure.  | Email address must match pattern `x@y.z`. Postcode must be 6 digits. NRIC format. |
# | **Length Check** | Ensures data has the correct number of characters. | Password must be at least 8 characters. Phone number must be 8 digits.      |
# | **Presence Check**| Ensures a required field is not left empty.       | Name field cannot be blank. Email address must be provided.                 |
# | **Type Check**   | Ensures data is of the correct data type.         | Age must be an integer. Name must be a string.                              |
# | **Check Digit**  | An extra digit calculated from the data digits, used for self-checking. | Last character of Singapore NRIC/FIN. Last digit of ISBN/barcode. (See Modulus-11 example in PDF p.7). |

# %% [markdown]
# #### Check Digit Example: Modulus-11
# (Algorithm needs to be understood/memorised if required for exams).
#
# **General Steps (for product code 1234):**
# 1.  Assign weights starting from 2 for the rightmost digit, increasing leftwards (4->2, 3->3, 2->4, 1->5).
# 2.  Multiply each digit by its weight: (1\*5), (2\*4), (3\*3), (4\*2).
# 3.  Sum the products: 5 + 8 + 9 + 8 = 30.
# 4.  Find the remainder when the sum is divided by 11: 30 % 11 = 8.
# 5.  Subtract the remainder from 11: 11 - 8 = 3.
# 6.  The result is the check digit (3). If the result is 10, use 'X'. If 11, use 0 (check specific rules).
# 7.  Complete code: 1234**3**.
#
# *(Note: NRIC uses a different specific weighting and letter conversion, also detailed in PDF p.7)*

# %% [markdown]
# ## 5. Program Testing (Syllabus 2.4.3 - 2.4.4)
#
# **Program testing** is the process of executing a program with the intent of finding errors. It's crucial for ensuring software quality and correctness.
#
# ### Types of Errors:
#
# 1.  **Syntax Errors:**
#     *   Violation of the programming language's grammar rules (e.g., misspelt keywords `pritn`, missing colons, mismatched brackets).
#     *   Detected by the compiler or interpreter during translation.
#     *   Program **cannot run** until syntax errors are fixed.
#
# 2.  **Runtime Errors:**
#     *   Errors that occur **during program execution**.
#     *   Detected by the operating system or runtime environment.
#     *   Often cause the program to crash or terminate abnormally.
#     *   **Examples:**
#         *   Division by zero.
#         *   Trying to access an array index out of bounds.
#         *   Input errors (e.g., entering text when a number is expected, if not handled).
#         *   File I/O errors (e.g., file not found).
#         *   Running out of memory (e.g., memory leak).
#         *   Stack overflow (often due to infinite recursion).
#         *   Type mismatch during an operation (if not caught by syntax check).
#         *   Overflow/Underflow (value exceeds data type limits).
#
# 3.  **Logic Errors:**
#     *   Errors in the program's design or algorithm.
#     *   The program runs without crashing but produces **incorrect or unexpected results**.
#     *   **Most difficult to detect** as there are no error messages.
#     *   Requires careful testing with various inputs and comparing actual output to expected output.
#     *   **Examples:** Using the wrong formula (`area = length + width`), incorrect loop condition (`<` instead of `<=`), flawed algorithm steps.

# %% [markdown]
# ### 5.4 Designing Test Cases
#
# A **test case** specifies inputs, execution conditions, testing procedures, and expected results for a single test objective.
#
# *   **Atomic:** Should ideally test only one specific feature or condition at a time.
# *   **Goal:** Validate testing coverage and identify defects.
# *   **Types of Test Data:** Test cases should use a variety of data to ensure robustness:
#     *   **Normal Data:** Sensible, typical inputs that should be accepted. (e.g., age = 25, score = 70).
#     *   **Abnormal/Invalid Data:** Inputs that should be rejected by validation rules. (e.g., age = -5, score = 110, month = 13, non-numeric input for age).
#     *   **Extreme Data:** Valid data at the limits of acceptable ranges. (e.g., score = 0, score = 100, minimum/maximum length strings).
#     *   **Boundary Data:** Data points just inside and just outside the valid range boundaries. Includes extreme data and the first invalid values. (e.g., if valid range is 0-100, test -1, 0, 100, 101).
#
# ### 5.5 Designing Test Plan
#
# A **test plan** is a document outlining the scope, approach, resources, and schedule of intended test activities. It typically includes a comprehensive set of test cases.
#
# A simple test plan table might include:
#
# | Test Case ID | Input(s)        | Purpose / Data Type | Expected Output | Actual Output | Pass/Fail |
# |--------------|-----------------|---------------------|-----------------|---------------|-----------|
# | TC01         | 50              | Normal              | Accepted        |               |           |
# | TC02         | -10             | Abnormal            | Rejected        |               |           |
# | TC03         | 0               | Extreme/Boundary    | Accepted        |               |           |
# | TC04         | 100             | Extreme/Boundary    | Accepted        |               |           |
# | TC05         | -1              | Boundary            | Rejected        |               |           |
# | TC06         | 101             | Boundary            | Rejected        |               |           |
# | TC07         | "abc"           | Abnormal (Type)     | Rejected/Error  |               |           |
#
# *(The 'Actual Output' and 'Pass/Fail' columns are filled in during actual testing).*

# %% [markdown]
# ## 6. Recursion (Syllabus 2.2.5 - 2.2.7)
#
# **Recursion** is a programming technique where a function calls itself, either directly or indirectly, to solve a problem.
#
# ### Features of a Recursive Function:
#
# 1.  **Base Case(s):** One or more stopping conditions that do not involve a recursive call. This prevents infinite recursion and provides a known result to start the "unwinding".
# 2.  **Recursive Step:** The function calls itself with modified arguments that move closer to the base case.
# 3.  **Definition:** Defined in terms of itself (e.g., factorial `Fac(N) = N * Fac(N-1)`).
# 4.  **Finite Calls:** The sequence of calls must eventually reach a base case.
#
# ### Examples:
#
# #### Factorial (N!)

# %% [markdown]
# ##### Pseudo-code (Recursive Factorial)

# %%
# FUNCTION Fac(N: INTEGER) RETURNS INTEGER
#   // Base Case
#   IF N = 0 THEN
#     RETURN 1
#   // Recursive Step
#   ELSE
#     RETURN N * Fac(N - 1)
#   ENDIF
# ENDFUNCTION

# %% [markdown]
# ##### Python (Recursive Factorial)

# %%
def factorial_recursive(n):
  if n < 0:
    return "Factorial not defined for negative numbers"
  elif n == 0: # Base case
    return 1
  else: # Recursive step
    return n * factorial_recursive(n - 1)

print(f"Factorial(3) = {factorial_recursive(3)}")
print(f"Factorial(0) = {factorial_recursive(0)}")
print(f"Factorial(5) = {factorial_recursive(5)}")

# %% [markdown]
# #### Fibonacci Sequence

# %% [markdown]
# ##### Pseudo-code (Recursive Fibonacci)

# %%
# FUNCTION Fibonacci(n: INTEGER) RETURNS INTEGER
#   // Base Case 1
#   IF n = 0 THEN
#     RETURN 0
#   // Base Case 2
#   ELSE IF n = 1 THEN
#     RETURN 1
#   // Recursive Step
#   ELSE
#     RETURN Fibonacci(n - 1) + Fibonacci(n - 2)
#   ENDIF
# ENDFUNCTION

# %% [markdown]
# ##### Pseudo-code (Iterative Fibonacci)

# %%
# FUNCTION Fibonacci_Iterative(n: INTEGER) RETURNS INTEGER
#   DECLARE num1, num2, num3, i : INTEGER
#
#   IF n = 0 THEN
#     RETURN 0
#   ELSE IF n = 1 THEN
#     RETURN 1
#   ELSE
#     num1 ← 0
#     num2 ← 1
#     // Loop starts from 2 because cases 0 and 1 are handled
#     FOR i ← 2 TO n
#       num3 ← num1 + num2
#       num1 ← num2       // Shift values for next iteration
#       num2 ← num3
#     ENDFOR
#     RETURN num3 // The nth Fibonacci number
#   ENDIF
# ENDFUNCTION

# %% [markdown]
# ##### Python (Recursive Fibonacci - often inefficient for larger n)

# %%
def fibonacci_recursive(n):
  if n < 0:
    return "Invalid input"
  elif n == 0: # Base case 1
    return 0
  elif n == 1: # Base case 2
    return 1
  else: # Recursive step
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# print(f"Fibonacci(5) = {fibonacci_recursive(5)}")
# print(f"Fibonacci(10) = {fibonacci_recursive(10)}")
# Note: This becomes very slow for n > ~35 due to repeated calculations

# %% [markdown]
# ##### Python (Iterative Fibonacci - more efficient)

# %%
def fibonacci_iterative(n):
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        num1 = 0
        num2 = 1
        for _ in range(2, n + 1):
            num3 = num1 + num2
            num1 = num2
            num2 = num3
        return num3

print(f"Iterative Fibonacci(5) = {fibonacci_iterative(5)}")
print(f"Iterative Fibonacci(10) = {fibonacci_iterative(10)}")
print(f"Iterative Fibonacci(40) = {fibonacci_iterative(40)}") # Much faster

# %% [markdown]
# ### 6.1 Comparing Recursion and Iteration
#
# | Feature         | Recursion                                          | Iteration (Loops)                                    |
# |-----------------|----------------------------------------------------|------------------------------------------------------|
# | **Simplicity**    | Often more elegant/simpler code for problems with naturally recursive structures (trees, divide & conquer). | Can be more complex for recursive patterns, simpler for linear tasks. |
# | **Memory Usage**| Uses call stack memory for each call; risk of **stack overflow** with deep recursion. | Uses fixed memory (loop variables); no stack overflow risk from iteration itself. |
# | **Exec Speed**  | Can be slower due to function call overhead.       | Generally faster due to less overhead.               |
# | **Debugging**   | Harder to trace due to multiple function contexts. | Easier to trace loop execution flow.                 |
# | **Proof**       | Often easier to prove correctness using mathematical induction. | May use loop invariants for proofs.                 |
# | **Use Cases**   | Tree traversals, divide & conquer (Binary Search, Merge Sort), Factorial, Fibonacci (though inefficiently). | Tasks involving repetition over a sequence/range (summing lists, linear search). |
# | **Time Complex**| Can sometimes be less efficient (e.g., basic recursive Fibonacci is O(2^n)). | Often more straightforward to analyze; iterative Fibonacci is O(n). |

# %% [markdown]
# ### 6.2 Use of Call Stack
#
# The **call stack** (or execution stack) is a data structure used by the runtime system to manage function calls.
#
# *   **Stack Frames:** When a function is called, a **stack frame** (or activation record) is pushed onto the stack. This frame contains:
#     *   **Return Address:** Where to resume execution in the calling function after the current function finishes.
#     *   **Parameters:** Copies of arguments passed to the function (or references).
#     *   **Local Variables:** Variables declared inside the function.
#     *   (Sometimes) Saved state of the calling function.
# *   **Pushing:** Calling a function pushes a new frame.
# *   **Popping:** When a function returns, its stack frame is popped off the stack, and control returns to the return address stored in the frame below it.
# *   **Recursion & Stack:** Each recursive call pushes a new stack frame. Deep recursion can lead to many frames.
# *   **Stack Overflow:** If the call stack runs out of memory (exceeds its maximum size) due to too many nested or recursive calls without returning (e.g., infinite recursion), a **stack overflow error** occurs, crashing the program.
# *   **Unwinding:** The process of returning from recursive calls and popping frames off the stack after the base case is reached.
#
# *(See PDF Page 14 for a diagram illustrating stack frames).*

# %% [markdown]
# ## 7. Video References (from PDF)
#
# *   **7.1 Trace Tables:** [https://www.youtube.com/watch?v=jqegERorXPI](https://www.youtube.com/watch?v=jqegERorXPI)
# *   **7.2 Validation/Verification:** [https://www.youtube.com/watch?v=NmwtF0fAUfI](https://www.youtube.com/watch?v=NmwtF0fAUfI)
# *   **7.3 Errors (Syntax, Runtime, Logic):** [https://www.youtube.com/watch?v=ToPP5UGgJUM](https://www.youtube.com/watch?v=ToPP5UGgJUM)
# *   **7.4 Test Data:** [https://www.youtube.com/watch?v=tWwcefljMAQ](https://www.youtube.com/watch?v=tWwcefljMAQ)
# *   **7.5 Recursion (CS50):** [https://www.youtube.com/watch?v=mz6tAJMVmfM](https://www.youtube.com/watch?v=mz6tAJMVmfM)
# *   **7.6 Call Stack:** [https://www.youtube.com/watch?v=Q2sFmqvpBe0](https://www.youtube.com/watch?v=Q2sFmqvpBe0)

# %% [markdown]
# ---
# *End of Summary for Chapter S2A: Programming Elements*
# ---