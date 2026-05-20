# 13.8 Problems

13.1 The following experiment has been made to determine the normal acceleration, g. A steel ball has been dropped without initial velocity from a high TV antenna. The position of the ball, l, has been determined at different times, giving the following measurements:

Time, s Length of fall, in meters 

<table><tr><td>1</td><td>8.49</td></tr><tr><td>2</td><td>20.05</td></tr><tr><td>3</td><td>50.65</td></tr><tr><td>4</td><td>72.19</td></tr><tr><td>5</td><td>129.85</td></tr><tr><td>6</td><td>171.56</td></tr></table>

The times of the measurements are exact, but there is an error in the measurement of the position. Determine the normal acceleration using the method of least squares from the model

$$l = \frac {g t ^ {2}}{2} + e$$

13.2 Derive recursive equations for increasing the number of parameters for the method of least squares. (Hint: Use the same idea as when making the observations recursively.)

13.3 Consider the process

$$y (k) + a y (k - 1) = b u (k - 1) + e (k) + c e (k - 1)$$

where u and e are independent white-noise processes with zero mean and unit variance. Assume that the method of least squares is used to estimate a and b, as in Example 13.2. Determine the expected values of $\hat{a}$ and $\hat{b}$ as a function of a, b, and c.

13.4 The parameters $b_{1}$ and $b_{2}$ in the system

$$y (k) = b _ {1} u (k - 1) + b _ {2} u (k - 2) + e (k)$$

are determined using the method of least squares. Let the input be a step at time k = 0. Can the parameters $b_{1}$ and $b_{2}$ be determined with arbitrary accuracy when the number of observations increases? Will there be any changes if it is known that $b_{2} = 0$
