# A Simple Dedicated Control System

Consider a simple control loop that has a few measured signals, a few outputs, and limited operator communication. Information may be displayed to the operator, and the operator may have a few buttons and a few dials. The programming of such a system is very simple. If a real-time clock is available, the code is in essence given by Listing 9.7.

The first line is simply a procedure that halts execution until a clock-interrupt occurs. The procedure Regulate is the code required to implement the desired control algorithm.

The procedure Display in Listing 9.7 computes some variables and displays them in analog or digital form. Notice that it is straightforward to introduce facilities for the operator to change parameters simply by introducing them as analog inputs.

The program in Listing 9.7 is fairly easy to debug. The procedures Regulate and Display are simple sequential procedures that can be tested off-line. It is also easy to check that the wait procedure gives an interrupt every sampling period. It will fail only if the time required to execute the procedures is longer than one sampling period. This may be tested by timing.

Listing 9.7 Computer code skeleton for a simple control loop.   
```txt
repeat
Wait for clock interrupt
Regulate
Display
forever 
```

![](image/81a612d12fa29ba34036e9e96faa7b29c845bdafc54a197fd9691d3f08efd7d3.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    Clock --> P0["P0"]
    P0 --> i{i}
    i --> True1["P1"]
    i --> False1["False"]
    False1 --> j{j}
    j --> True2["P2"]
    j --> False2["False"]
    True2 --> P2
    True2 --> False2
    P2 --> j2["j = false"]
    P2 --> P3["P3"]
    P3 --> iJ[i}j{true}
    iJ --> P3
```
</details>

Figure 9.20 Flow chart for a multiloop control law with two sampling rates.
