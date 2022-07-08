/* 
Previously, we have provided a straightforward but inefficient implementation of queue.
A more efficient way is to use a circular queue. Specifically, we may use a fixed-size array 
and two pointers to indicate the starting position and the ending position. And 
the goal is to reuse the wasted storage we mentioned previously.
Let's take a look at an example to see how a circular queue works. 
You should pay attention to the strategy we use to enqueue or dequeue an element. 
*/