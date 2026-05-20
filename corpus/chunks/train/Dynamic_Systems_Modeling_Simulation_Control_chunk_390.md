where $t _ { 2 } = t _ { 1 } + T _ { \mathrm { p e r i o d } }$ . The same cancellation occurs if we use the ratio of relative peaks for the impulse response. Therefore, the ratio of relative peak values involves only the ratio of the exponential envelope terms

$$\frac {x _ {1}}{x _ {2}} = \frac {e ^ {- \zeta \omega_ {n} t _ {1}}}{e ^ {- \zeta \omega_ {n} t _ {2}}} = \frac {e ^ {- \zeta \omega_ {n} t _ {1}}}{e ^ {- \zeta \omega_ {n} (t _ {1} + T _ {\text { period }})}} = \frac {1}{e ^ {- \zeta \omega_ {n} T _ {\text { period }}}} = e ^ {\zeta \omega_ {n} T _ {\text { period }}} \tag {7.85}$$

Taking the natural logarithm of the ratio of relative peaks yields

$$\ln \frac {x _ {1}}{x _ {2}} = \zeta \omega_ {n} T _ {\text { period }} \tag {7.86}$$

Substituting for the period of the underdamped response, $T _ { \mathrm { p e r i o d } } = 2 \pi / \omega _ { n } \sqrt { 1 - \zeta ^ { 2 } }$ , in Eq. (7.86) results in the cancellation of undamped natural frequency and yields

$$\ln \frac {x _ {1}}{x _ {2}} = \frac {2 \pi \zeta}{\sqrt {1 - \zeta^ {2}}} \tag {7.87}$$

Finally, we can solve Eq. (7.87) for $\zeta$ to obtain an expression for damping ratio

$$\zeta = \frac {\delta}{\sqrt {4 \pi^ {2} + \delta^ {2}}} \tag {7.88}$$

where the symbol ?? is the natural logarithm of the ratio of relative peaks, or log decrement

$$\text { Log decrement: } \quad \delta = \ln \frac {x _ {1}}{x _ {2}}$$

Hence, Eq. (7.88) can be used to estimate damping ratio $\zeta$ from the log decrement $\delta ,$ which may be obtained from either a step or impulse response. The reader should note that the peak values $x _ { 1 }$ and $x _ { 2 }$ must be computed relative to the respective steady-state value, as shown in Fig. 7.22. In addition, the reader should note that the log decrement method is difficult to apply to systems with “moderate to large” damping ratios, such as $0 . 4 <$ < $\zeta < 1$ , because the second peak response is difficult to discern from the steady-state response. Therefore, this method has practical use only for lightly damped systems.
