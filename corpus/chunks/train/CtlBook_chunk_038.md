# Example 1.7

Consider the nonlinear function

$$f _ {1} (x) = 0. 4 x ^ {2} - 0. 1 x ^ {3} + 3 \sin (x)$$

and linearize twice, once about $x = - 6 ,$ and again about $x = 1$ (we are using radians for sin(x)).

First evaluate $f _ { 1 } ( x )$ for the two linearization points:

$$f _ {1} (- 6) = 3 6. 8 4 \quad f _ {1} (1) = 2. 8 2 4$$

Then let's get the derivative:

$$\dot {f} (x) = 0. 8 x - 0. 3 x ^ {2} + 3 \cos (x)$$

and evaluate it at the two points:

$$\dot {f} (- 6) = - 1 2. 7 2 \quad \dot {f} (1) = 2. 1 2 1$$

Now we get:

$$\hat {f} _ {1 a} = 3 6. 8 4 - 1 2. 7 2 (x + 6) = - 3 9. 4 8 - 1 2. 7 2 x \quad \hat {f} _ {1 b} = 2. 8 2 4 + 2. 1 2 1 (x - 1) = 0. 7 0 3 + 2. 1 2 1 x$$

Plotting using the computer:

![](image/5b59769d41b63337ef6f9599a38f672dda10ea258fb38036089ba797d1ed5e27.jpg)

<details>
<summary>line</summary>

| x | Blue Line | Red Line | Green Line |
| --- | --- | --- | --- |
| -10 | 150 | -20 | 90 |
| -8 | 100 | -15 | 60 |
| -6 | 50 | -10 | 30 |
| -4 | 20 | -5 | 0 |
| -2 | 0 | 0 | -30 |
| 0 | -20 | 5 | -60 |
| 2 | -40 | 10 | -90 |
| 4 | -60 | 15 | -120 |
| 6 | -80 | 20 | -150 |
| 8 | -100 | 25 | -180 |
| 10 | -120 | 30 | -210 |
</details>

The blue line is $f ( x ) _ { \cdot }$ , the green line is $\hat { f } _ { 1 a } ( x )$ and the red line is ${ \hat { f } } _ { 1 b } ( x )$ . The linear approxmations are reasonably accurate in the neighborhood of their operating points $( x \stackrel { \cdot } { = } - 6 , + 1 )$ , but become very bad as we move away. The size of the neighborhood for which a degree of accuracy can be obtained depends on the function and the selected operating point.
