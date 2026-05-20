# Example 2.7 Double integrator with delay

The double integrator in Example 2.2 with a time delay $0 \leq \tau \leq h$ gives

$$
\begin{array}{l} \Phi = e ^ {A h} = \left( \begin{array}{c c} 1 & h \\ 0 & 1 \end{array} \right) \\ \Gamma_ {1} = e ^ {A (h - \tau)} \int_ {0} ^ {\tau} e ^ {A s} d s B = \left( \begin{array}{c c} 1 & h - \tau \\ 0 & 1 \end{array} \right) \binom{\frac {\tau^ {2}}{2}}{\tau} = \binom{\tau \left(h - \frac {\tau}{2}\right)}{\tau} \\ \Gamma_ {0} = \int_ {0} ^ {h - \tau} e ^ {A s} d s B = \left(\frac {(h - \tau) ^ {2}}{2} h - \tau\right) \\ \end{array}
$$
