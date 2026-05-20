# Exercise 1.50: Some smoothing

One of the problems with asking you to derive the Kalman filter is that the derivation is in so many textbooks that it is difficult to tell if you are thinking independently. So here’s a variation on the theme that should help you evaluate your level of understanding of these ideas. Let’s calculate a smoothed rather than filtered estimate and covariance. Here’s the problem.

We have the usual setup with a prior on $x ( 0 )$

$$x (0) \sim N (\overline {{x}} (0), Q _ {0})$$

and we receive data from the following system

$$x (k + 1) = A x (k) + w (k)\mathcal {Y} (k) = C x (k) + \nu (k)$$

in which the random variables $w ( k )$ and $\nu ( k )$ are independent, identically distributed normals, $w ( k ) \sim N ( 0 , Q ) , \nu ( k ) \sim N ( 0 , R )$ .

(a) Calculate the standard density for the filtering problem, $p _ { x ( 0 ) , y ( 0 ) } ( x ( 0 ) | y ( 0 ) )$

(b) Now calculate the density for the smoothing problem

$$p _ {x (0) | y (0), y (1)} (x (0) | y (0), y (1))$$

that is, not the usual $p _ { x ( 1 ) | y ( 0 ) , y ( 1 ) } ( x ( 1 ) | y ( 0 ) , y ( 1 ) )$ .
