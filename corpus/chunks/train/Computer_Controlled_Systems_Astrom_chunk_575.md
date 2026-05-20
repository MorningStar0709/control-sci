# Example 9.8 Double integrator in $\delta$ -form

Consider the double integrator $G(s) = 1 / s^2$ . Then

$$H (q) = \frac {h ^ {2} (q + 1)}{2 (q - 1) ^ {2}} = \frac {h ^ {2} (\delta h + 2)}{2 h ^ {2} \delta^ {2}} = \frac {1 + \delta h / 2}{\delta^ {2}} = \bar {H} (\delta)$$

When $h$ goes to zero we get

$$\lim _ {h \rightarrow 0} \bar {H} (\delta) = \frac {1}{\delta^ {2}} = G (\delta)$$

Notice that the $\delta$ -form also has "sampling zeros," $\delta = -2/h$ . This zero will approach $-\infty$ when $h \to 0$ .

Heuristically we can interpret the $\delta$ -operator as a shift of origin and scaling. This is a common trick in numerical analysis and has the consequence that the $\delta$ -form can obtain better numerical properties than the shift operator. A controller in $\delta$ -form can be described by the state equations

$$\delta x (k h) = \bar {F} x (k h) + \bar {G} y (k h) = d (k h) \tag {9.24}u (k h) = C x (k h) + D y (k h)$$

The shift operator and its inverse are implemented exactly using an assignment statement. To make a realization in $\delta$ -form we must implement the operator $\delta^{-1}$ . Solving (9.24) for $x(kh)$ gives

$$x (k h) = \delta^ {- 1} d (k h) = x (k h - h) + h d (k h)$$

The extra amount of computations compared to the shift form is marginal. One extra vector addition is necessary. Notice that because $hd(kh)$ is normally much smaller than $x(kh - h)$ , it is necessary to represent $x(kh - h)$ with a sufficient word length.
