# Structure of Equations Describing Adaptive Systems

Consider a process controlled by an indirect adaptive controller as shown in Fig. 3.1. We will first consider the case in which parameters of a continuous-time model are estimated by using a gradient procedure. Assume that the system to be controlled is linear. Let $\vartheta$ denote the controller parameters and $\nu$ the external driving signals. The signal $\nu$ is typically composed of the command signal $u_{c}$ and nonmeasurable disturbances acting on the process. With constant controller parameters the closed-loop system can be written as

$$\frac {d \xi}{d t} = A (\vartheta) \xi + B (\vartheta) v \tag {6.1}\eta = \binom{e}{\varphi} = C (\vartheta) \xi + D (\vartheta) \nu$$

The state vector $\xi$ includes the states of the system, the reference model, the data filter, and the auxiliary state variables that may have to be introduced to calculate the error e and the regression vector $\varphi$ used in the parameter adjustment mechanism. The vector $\eta$ consists of the error and the regression vector that are used by the parameter estimator.

Furthermore, let $\theta$ denote the process parameters. A normalized gradient scheme for estimating the parameters can be described by

$$\frac {d \hat {\theta}}{d t} = \gamma \frac {\varphi (\vartheta , \xi) e (\vartheta , \xi)}{\alpha + \varphi (\vartheta , \xi) ^ {T} \varphi (\vartheta , \xi)} \tag {6.2}$$

The control design can be represented by a nonlinear function $\vartheta = \chi(\hat{\theta})$ , which maps the estimated parameters into controller parameters. This map becomes the identity for direct algorithms.

For constant $\vartheta$ the system (6.1) is linear. The solution can then also be characterized by the operators $G_{e\nu}$ and $G_{\varphi\nu}$ , which relate $e$ and $\varphi$ to $\nu$ . These operators depend on the controller parameters $\vartheta$ . Equation (6.2) can then be written as

$$\frac {d \hat {\theta}}{d t} = \gamma \frac {(G _ {\varphi \nu} v) (G _ {e \nu} v)}{\alpha + (G _ {\varphi \nu} v) ^ {T} G _ {\varphi \nu} v}$$
