# Example 1.5

Find

$$\mathcal {L} ^ {- 1} \{G (s) = \frac {(s + 5)}{(s + 6) (s + 2 + j) (s + 2 - j)} \}$$

Using the techniques above we can get:

$$A _ {1} = - 1 / 1 7 = - 0. 0 5 9 \quad A _ {2} = 0. 0 2 9 + 0. 3 8 j \quad A _ {3} = 0. 0 2 9 - 0. 3 8 j$$

(note that it is not necessary to compute $A _ { 3 }$ because it will always be the case for complex conjugate poles that $A _ { n + 1 } = A _ { n } ^ { * } .$ )

$$G (s) = \frac {- 0 . 0 5 9}{(s + 6)} + \frac {0 . 0 2 9 + 0 . 3 8 j}{(s + 2 + j)} + \frac {0 . 0 2 9 - 0 . 3 8 j}{(s + 2 - j)}$$

Applying the inverse transform to each term:

$$g (t) = - 0. 0 5 9 e ^ {- 6 t} + (0. 0 2 9 + 0. 3 8 j) e ^ {(- 2 - j) t} + (0. 0 2 9 - 0. 3 8 j) e ^ {(- 2 + j) t}$$

First, let's approximate

$$0. 0 2 9 \pm 0. 3 8 j \approx 0. 3 8 e ^ {\pm j \pi / 2}$$

by 1) ignoring the small real part and 2) converting to Magnitude-Angle form (see Appendix A.8).

$$g (t) = - 0. 0 5 9 e ^ {- 6 t} + 0. 3 8 e ^ {j \pi / 2} e ^ {(- 2 - j) t} + 0. 3 8 e ^ {- j \pi / 2} e ^ {(- 2 + j) t}g (t) = - 0. 0 5 9 e ^ {- 6 t} + 0. 3 8 e ^ {- 2 t} \left(e ^ {j (- t + \pi / 2)} + e ^ {- j (- t + \pi / 2)}\right)$$

Where we used:

$$e ^ {j \pi / 2} \cdot e ^ {(- 2 - j) t} \rightarrow e ^ {(j \pi / 2 - 2 t - j t)} \rightarrow e ^ {(- 2 t + j (\pi / 2 - t))} \rightarrow e ^ {(- 2 t)} \cdot e ^ {j (\pi / 2 - t))}$$

Now we use Euler's famous equality

$$e ^ {j \theta} = \cos (\theta) + j \sin (\theta)$$

as follows:

$$g (t) = - 0. 0 5 9 e ^ {- 6 t} + 0. 3 8 e ^ {- 2 t} \left(\cos (- t + \pi / 2) + j \sin (- t + \pi / 2) + \cos (- t + \pi / 2) - j \sin (- t + \pi / 2)\right)$$

Since cos(θ) = − cos(θ), and cos $( \theta - / p i / 2 ) = \sin ( \theta )$

$$g (t) = - 0. 0 5 9 e ^ {- 6 t} + 0. 3 8 e ^ {- 2 t} \left(2 \cos (t - \pi / 2)\right)g (t) = - 0. 0 5 9 e ^ {- 6 t} + 0. 7 6 e ^ {- 2 t} \left(\cos (t - \pi / 2)\right)g (t) = - 0. 0 5 9 e ^ {- 6 t} + 0. 7 6 e ^ {- 2 t} (\sin (t))$$
