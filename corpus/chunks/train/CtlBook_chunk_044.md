# Example 1.11

Consider the system of Example 1.7. The equations were:

$$f _ {1} (x) = 0. 4 x ^ {2} - 0. 1 x ^ {3} + 3 \sin (x)$$

linearized twice, once about x = −6 radians, and again about x = 1 radian.

$$\hat {f} _ {1 a} = - 3 9. 4 8 - 1 2. 7 2 x \quad \hat {f} _ {1 b} = 0. 7 0 3 + 2. 1 2 1 x$$

If the accuracy requirement is $5 \% ,$ which linearization a or b has a bigger neighborhood?

Our approach will be to compute numerically values of $f ( x )$ and ˆf(x) and look for the error dropping below 5% We'll dene our error percentage as:

$$E _ {j} = \left| \frac {f (x) - f _ {j} (x)}{f (x)} \right|$$

Let's make a spreadsheet for them both. We'll generate columns as follows:

<table><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td></tr><tr><td>x</td><td> $f_1(x)$ </td><td> $f_{1a}(x)$ </td><td> $E_a$ </td><td> $f_{1b}(x)$ </td><td> $E_b$ </td></tr></table>
