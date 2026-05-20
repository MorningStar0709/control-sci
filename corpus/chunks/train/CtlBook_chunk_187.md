# 6.6 Stability

We've seen many systems like that of Example 6.10, which contain transient solutions with exponential terms. The time coecient on the exponential terms comes from the real part of poles. As long as the poles have a negative real part (i.e. they are in the left half of the complex plane) the system will converge to a steady value. Because of the negative term, all the exponentials fade out to zero with time.

On the other hand, if the time coecient (real part of the pole) is positive, even for only one of the exponential terms arising from the partial fraction expansion, the output will grow exponentially without limit. In almost all practical systems this is unacceptable and undesirable.
