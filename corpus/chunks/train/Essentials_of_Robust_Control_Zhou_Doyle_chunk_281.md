Example 10.5 Consider again the robust performance problem of a system with output multiplicative uncertainty in Chapter 8 (see Figure 8.10):

$$P _ {\Delta} = (I + W _ {1} \Delta W _ {2}) P, \| \Delta \| _ {\infty} < 1.$$

Then it is easy to show that the problem can be put in the general framework by selecting

$$
G (s) = \left[ \begin{array}{c c} - W _ {2} T _ {o} W _ {1} & - W _ {2} T _ {o} W _ {d} \\ W _ {e} S _ {o} W _ {1} & W _ {e} S _ {o} W _ {d} \end{array} \right]
$$

and that the robust performance condition is satisfied if and only if

$$\left\| W _ {2} T _ {o} W _ {1} \right\| _ {\infty} \leq 1 \tag {10.25}$$

and

$$\left\| \mathcal {F} _ {u} (G, \Delta) \right\| _ {\infty} \leq 1 \tag {10.26}$$

for all $\Delta \in \mathcal { R } \mathcal { H } _ { \infty }$ with $\| \Delta \| _ { \infty } < 1$ . But equations (10.25) and (10.26) are satisfied iff for each frequency ω

$$
\mu_ {\boldsymbol {\Delta}} (G (j \omega)) = \inf _ {d _ {\omega} \in \mathbb {R} _ {+}} \overline {{\sigma}} \left(\left[ \begin{array}{c c} - W _ {2} T _ {o} W _ {1} & - d _ {\omega} W _ {2} T _ {o} W _ {d} \\ \frac {1}{d _ {\omega}} W _ {e} S _ {o} W _ {1} & W _ {e} S _ {o} W _ {d} \end{array} \right]\right) \leq 1.
$$

Note that, in contrast to the sufficient condition obtained in Chapter $^ { 8 , }$ this condition is an exact test for robust performance. To compare the $\mu$ test with the criteria obtained in Chapter $\mathrm { 8 , }$ , some upper-bounds for $\mu$ can be derived. Let

$$d _ {\omega} = \sqrt {\frac {\| W _ {e} S _ {o} W _ {1} \|}{\| W _ {2} T _ {o} W _ {d} \|}}.$$

Then, using the first approximation for $\mu ,$ we get

$$
\begin{array}{l} \mu_ {\Delta} (G (j \omega)) \leq \sqrt {\| W _ {2} T _ {o} W _ {1} \| ^ {2} + \| W _ {e} S _ {o} W _ {d} \| ^ {2} + 2 \| W _ {2} T _ {o} W _ {d} \| \| W _ {e} S _ {o} W _ {1} \|} \\ \leq \sqrt {\left\| W _ {2} T _ {o} W _ {1} \right\| ^ {2} + \left\| W _ {e} S _ {o} W _ {d} \right\| ^ {2} + 2 \kappa (W _ {1} ^ {- 1} W _ {d}) \left\| W _ {2} T _ {o} W _ {1} \right\| \left\| W _ {e} S _ {o} W _ {d} \right\|} \\ \leq \| W _ {2} T _ {o} W _ {1} \| + \kappa (W _ {1} ^ {- 1} W _ {d}) \| W _ {e} S _ {o} W _ {d} \| \\ \end{array}
$$

where $W _ { 1 }$ is assumed to be invertible in the last two inequalities. The last term is exactly the sufficient robust performance criteria obtained in Chapter 8. It is clear that any term preceding the last forms a tighter test since $\kappa ( W _ { 1 } ^ { - 1 } W _ { d } ) \geq 1$ . Yet another alternative sufficient test can be obtained from the preceding sequence of inequalities:
