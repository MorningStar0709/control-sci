# 8.3 Approximations Based on State Models

In this section we will make discrete-time approximations of controllers described by continuous-time state-space models. State-feedback controllers can be regarded as generalized P-controllers. The formulation of the problem assumes that the process is described by the equations

$$\frac {d x}{d t} = A x + B u \tag {8.11}y = C x$$

where all the states are assumed to be measurable. By using a controller of the form

$$u (t) = M u _ {c} (t) - L x (t) \tag {8.12}$$

it is possible to place the poles of the closed-loop system arbitrarily if the system is controllable. The controller in (8.12) can be implemented in digital form by sampling the states and holding the control signal constant over the sampling intervals. This is how the control is done in Example 1.2. If the sampling period is increased, then the behavior of the closed-loop system starts to deteriorate. It is, however, possible to modify the controller in order to improve the performance of the closed-loop system. Assume that the discrete-time controller is

$$u (k h) = \tilde {M} u _ {c} (k h) - \tilde {L} x (k h) \tag {8.13}$$

One way to solve the problem is to design the controller in (8.12) using sampled-data theory. This is done in Chapter 4. Here, an approximate method is used to translate the controller in (8.12) into discrete-time form.

Controlling (8.11) with the continuous-time controller in (8.12) gives the closed-loop system

$$\frac {d x}{d t} = (A - B L) x + B M u _ {c} = A _ {c} x + B M u _ {c}y = C x$$

If $u_{c}(t)$ is constant over one sampling period, then this equation can be integrated; this gives

$$x (k h + h) = \Phi_ {c} x (k h) + \Gamma_ {c} M u _ {c} (k h) \tag {8.14}$$

where

$$\Phi_ {c} = e ^ {A _ {c} h}\Gamma_ {c} = \int_ {0} ^ {h} e ^ {A _ {c} s} d s B$$

If the discrete-time controller in (8.13) is used to control (8.11), then

$$x (k h + h) = (\Phi - \Gamma \tilde {L}) x (k h) + \Gamma \tilde {M} u _ {c} (k h) \tag {8.15}$$

where $\Phi$ and $\Gamma$ are the system matrices obtained when (8.11) is sampled. It is in general not possible to choose $\bar{L}$ such that

$$\Phi_ {c} = \Phi - \Gamma \tilde {L}$$

However, we can make a series expansion and equate terms of different powers of h. Assume that

$$\tilde {L} = L _ {0} + L _ {1} h / 2$$

then

$$\Phi_ {c} \approx I + (A - B L) h + \left(A ^ {2} - B L A - A B L + (B L) ^ {2}\right) h ^ {2} / 2 + \dots$$

and

$$\Phi - \Gamma \tilde {L} \approx I + (A - B L _ {0}) h + \left(A ^ {2} - A B L _ {0} - B L _ {1}\right) h ^ {2} / 2 + \dots$$
