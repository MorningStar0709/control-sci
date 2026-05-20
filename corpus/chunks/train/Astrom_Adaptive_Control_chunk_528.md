# EXAMPLE 7.4 Optimal dual controller

The first example is a numerically solved dual control problem from Åström and Helmersson (1982). Consider the integrator in Example 7.2. The gain is assumed to be constant but unknown, that is, $\varphi_{b} = 1$ and $R_{1} = 0$ . It is assumed that the parameter $b$ is a random variable with a Gaussian prior distribution; the conditional distribution of $b$ , given inputs and outputs up to time $t$ , is Gaussian with mean $\hat{b}(t)$ and covariance $P(t)$ . The hyperstate can then be characterized by the triple $(y(t), \hat{b}(t), P(t))$ . The equations for updating the hyperstate are given by Eqs. (7.9).

Define the loss function

$$V _ {N} = \min _ {u} E \left\{\sum_ {k = t + 1} ^ {t + N} y ^ {2} (k) \mid \mathcal {Y} _ {t} \right\}$$

where $Y_{t}$ denotes the data available at time t, that is, $\{y(t), y(t-1), \ldots\}$ . By introducing the normalized variables

$$\eta = y / \sqrt {R _ {2}} \quad \beta = \hat {b} / \sqrt {P} \quad \mu = - u \hat {b} / y$$

it can be shown that $V_{N}$ depends on $\eta$ and $\beta$ only. Further introduce the normalized innovation

$$\varepsilon (t) = \frac {y (t + 1) - y (t) - \hat {b} (t) u (t)}{R _ {2} + u (t) ^ {2} P (t)}$$

For $R_{2} = 1$ the Bellman equation for the problem can be written as

$$V _ {N} (\eta , \beta) = \min _ {\mu} U _ {N} (\eta , \beta , \mu)$$

where

$$V _ {0} (\eta , \beta) = 0$$

and

$$U _ {N} (\eta , \beta , \mu) = 1 + \eta^ {2} (1 - \mu) ^ {2} + \frac {\mu^ {2} \eta^ {2}}{\beta^ {2}} - \int_ {- \infty} ^ {\infty} V _ {N - 1} (\eta_ {p}, \beta_ {p}) \phi (s) d s$$

where $\phi$ is the normal probability density with zero mean and unit variance and

$$\eta_ {p} = \eta - \mu \eta + s \sqrt {1 + \frac {\mu^ {2} \eta^ {2}}{\beta^ {2}}}\beta_ {p} = \beta \sqrt {1 + \frac {\mu^ {2} \eta^ {2}}{\beta^ {2}}} - \frac {\mu \eta}{\beta} s$$

Notice that $\eta_{p}$ and $\beta_{p}$ are the one-step-ahead predicted values of $\eta$ and $\beta$ . When the minimization is performed, the control law is obtained as

$$\mu_ {N} (\eta , \beta) = \arg \min _ {\mu} U _ {N} (\eta , \beta , \mu)$$

![](image/03001e47651dd7f584a7c1b2d66c01e4a538fe61780e80030b336b1621324e1d.jpg)  
Figure 7.5 Illustration of the cautious control and dual control laws when (a) N = 1; (b) N = 3; (c) N = 6; and (d) N = 31. The control signal is shown as a function of $\eta' = \eta/(1 + \eta)$ and $\beta' = \beta^{2}/(1 + \beta^{2})$ . The control signal is limited, which explains the plateaus.
