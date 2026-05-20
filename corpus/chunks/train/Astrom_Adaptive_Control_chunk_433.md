$$\operatorname{avg} \left\{f (\hat {\theta}, \xi (\hat {\theta}, t), t) \right\} = \frac {1}{T} \int_ {0} ^ {T} f (\hat {\theta}, \xi (\hat {\theta}, t), t) d t\operatorname{avg} \left\{f (\hat {\theta}, \xi (\hat {\theta}, t), t) \right\} = \lim _ {T \rightarrow \infty} \int_ {0} ^ {T} f (\hat {\theta}, \xi (\hat {\theta}, t), t) d t\operatorname{avg} \left\{f (\hat {\theta}, \xi (\hat {\theta}, t), t) \right\} = E f (\hat {\theta}, \xi (\hat {\theta}, t), t)$$

The first alternative is applicable when $f$ is periodic with period $T$ , and the last equation applies when $\xi$ is a stationary stochastic process. Notice that the averaged equations can be calculated only when the signals are bounded. This implies that the closed-loop system must be stable if the parameters $\hat{\theta}$ are fixed. The calculation of $\xi(\vartheta(\hat{\theta}), t)$ is a straightforward exercise in linear system analysis. However, the expressions may be complex for high-order systems. Symbolic calculation is a useful tool for carrying out the calculations. The use of averaging thus results in the following averaged nonlinear differential equation for the parameters:

$$\frac {d \bar {\theta}}{d t} - \gamma \operatorname{avg} \left\{\varphi (\vartheta (\bar {\theta}), \xi (\vartheta (\bar {\theta}), t)) e (\vartheta (\bar {\theta}), \xi (\vartheta (\bar {\theta}), t)) \right\} = 0 \tag {6.49}$$

This equation can also be written as

$$\frac {d \bar {\theta}}{d t} - \gamma \operatorname{avg} \left\{\left(G _ {\varphi \nu} (\vartheta (\bar {\theta}), p) \nu\right) \left(G _ {e \nu} (\vartheta (\bar {\theta}), p) \nu\right) \right\} = 0 \tag {6.50}$$

Notice that the transfer functions $G_{ev}$ and $G_{\varphi\nu}$ depend on the averaged parameter $\bar{\theta}$ . When the averaged equations are obtained, the behavior of the state variables $\xi$ can be obtained by linear analysis.

Several averaging theorems give conditions for $\bar{\theta}$ being close to $\hat{\theta}$ . The conditions typically require smoothness of the functions involved and periodicity or near periodicity of the time functions. There are also stochastic averaging theorems. Notice that averaging analysis was used in Theorems 4.1 and 4.2.
