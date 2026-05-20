# Implementation of a Predictive First-Order Hold

The predictive first-order hold is described by Eq. (7.9). The system can be implemented by switched operational amplifiers. It is, however, often more convenient to implement an approximation with a multirate sampled system. The time interval $(t_{k}, t_{k+1})$ is then subdivided into a N equal parts of length $\Delta_{t} = (t_{k+1} - t_{k})$ and the output of the hold circuit is incremented by

$$\Delta_ {u} = \frac {f (t _ {k + 1}) - f (t _ {k})}{N (t _ {k + 1} - t _ {k})}$$

at each time increment $\Delta_{t}$ . If $N$ is large, the output from the hold circuit is then a staircase function with very small steps, which is very close to the output given by Eq. (7.9). If necessary the output can also be filtered.
