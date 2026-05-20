# Example 6.8

Illustrate how a non-linear spring could be broken down into a linear spring plus a disturbance. Suppose our spring obeys

$$f (x) = K x + 0. 1 K x ^ {2}$$

Notice that this can be broken down into a linear part (Kx) and nonlinear part (0.1Kx2). One approach might be simply to separate the linear from the non linear terms above. As shown in the plot below, a dierent split gives a higher stiness to the linear term in such a way as to make a smaller non-linear term.

![](image/8fa3349e63c8c5c7a0d4d179d1afa6a60ffe22b4ccea63609953ff024f5d8e14.jpg)

<details>
<summary>line</summary>

| x | Blue Line | Green Line | Red Line |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 1 | 2 | 3 | -1 |
| 2 | 4 | 6 | -2 |
| 3 | 6 | 9 | -2.5 |
| 4 | 8 | 12 | -2.5 |
| 5 | 10 | 15 | -2.5 |
| 6 | 12 | 18 | -1 |
| 7 | 15 | 21 | -0.5 |
| 8 | 18 | 24 | 0 |
| 9 | 22 | 27 | 1 |
| 10 | 30 | 27 | 3 |
</details>

This computer plot shows the nonlinear spring given by the equation above and K = 1.5 and also a linear t (in green):

$$f (x) = 2. 7 x$$

The dierence

$$f _ {N L} = K x + 0. 1 K x ^ {2} - 2. 7 x$$

is shown in red. Note that we have linearized the spring function with a dierent approach to that of Chapter 1. Using Chapter 1's method, we will get a better t to one specic point on the curve (the point at which we compute linearization), but the green line above gives us a dierent kind of linearization which works over a broad range of x values (and itersects at two points). Such a line could be computed, for example, by linear regression.

Suppose the system goes through a trajectory,

$$x (t) = 5 + 5 \sin (5 t)$$

Then this nonlinear spring would generate the following forces:

![](image/9c669bbc910a19e27463845365393c6044f52cd66740f3d705c34fd20652934d.jpg)

<details>
<summary>line</summary>

| x | Blue Line | Green Line | Red Line |
| --- | --- | --- | --- |
| 0.0 | 12.0 | 14.0 | -2.0 |
| 0.5 | 28.0 | 26.0 | 3.0 |
| 1.0 | 30.0 | 27.0 | 3.0 |
| 1.5 | 28.0 | 26.0 | 2.0 |
| 2.0 | 20.0 | 18.0 | -2.0 |
| 2.5 | 12.0 | 14.0 | -2.0 |
| 3.0 | 0.0 | 12.0 | -2.0 |
| 3.5 | 12.0 | 18.0 | -2.0 |
| 4.0 | 28.0 | 26.0 | 3.0 |
| 4.5 | 30.0 | 27.0 | 3.0 |
| 5.0 | 28.0 | 26.0 | 2.0 |
| 5.5 | 20.0 | 18.0 | -2.0 |
| 6.0 | 12.0 | 14.0 | -2.0 |
| 6.5 | 0.0 | 12.0 | -2.0 |
| 7.0 | 12.0 | 18.0 | -2.0 |
| 7.5 | 28.0 | 26.0 | -2.0 |
| 8.0 | 30.0 | 27.0 | -2.0 |
| 8.5 | 28.0 | 26.0 | -2.0 |
| 9.0 | 20.0 | 18.0 | -2.0 |
| 9.5 | 12.0 | 14.0 | -2.0 |
| 10.0 | 12.0 | 14.0 | -2.0 |
</details>

Here the sinusoidal force output is nonlinear (blue) but can be broken down into a linear part (green) and a non-linear part (red). The linear approximation is pretty good (for this system at least) and the non-linear forces (red) can be treated as a disturbance (which is then attenuated by Equation 6.4).
