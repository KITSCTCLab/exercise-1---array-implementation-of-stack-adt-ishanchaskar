# Problem
Perform the operations on stack.

You have an empty sequence, and you will be given  queries. Each query is one of these two types.

1 &nbsp; x  -Push the element x into the stack.<br/>
2 &nbsp; &nbsp;   -Delete the element present from the top of the stack.<br/>


# Function Description
Complete the functions, push, pop, is_empty, is_full, and status. They must perform the actions as described above. The function, status displays the current available elements of stack, if it is not empty.


# Constraints
The size of the stack may range from 1 to 100.<br/>
The number of queries may range from 1 to 100.<br/>


# Input Format
The first line contains two integers. First integer represents maximum capacity of stack and second integer represents number of queries. Each of the next q lines contains a single query in the form described in the problem statement above. All queries start with an integer denoting the query type, but only query 1 is followed by an additional space-separated value, x, denoting the value to be enqueued.

# Sample Input with explaination
5 &nbsp; 4 &nbsp; &nbsp; _# size is 5 and number of queries are 4_<br />
1 &nbsp; 10 &nbsp;    _# Push 10_<br />
2 &nbsp; &nbsp; &nbsp; &nbsp;   _# Perform pop_<br />
1 &nbsp; 13 &nbsp;   _# Push 13_<br />
1 &nbsp; 11 &nbsp;   _# Push 11_<br />

# Sample Output
13<br/>
11


# Sample Input-1
3 &nbsp; 1<br/>
1 &nbsp; 22


# Sample Output-1
22

# Sample Input-2
5 &nbsp; 5<br/>
1 &nbsp; 10<br/>
1 &nbsp; 20<br/>
1 &nbsp; 30<br/>
1 &nbsp; 40<br/>
1 &nbsp; 50<br/>


# Sample Output-2
10<br/>
20<br/>
30<br/>
40<br/>
50<br/>
