# EXAMPLE 11.5 Tracking parameters of a time-varying system

Consider a process described by the differential equation

$$\frac {d y}{d t} = - y (t) + K _ {p} (t) u$$

where the process gain is time varying. The process is controlled by an indirect adaptive controller that estimates parameters of the discrete-time model

$$y (k h + h) + a y (k h) = b u (k h)$$

and designs a controller with integral action using robust pole placement with

$$A _ {m} (q) = q + a _ {m} = q - e ^ {- h / T _ {m}}$$

and

$$A _ {o} (q) = q + a _ {o} = q - e ^ {- h / T _ {1}}$$

Straightforward computations give a controller of the form

$$u (k h) = t _ {0} u _ {c} (k h) + t _ {1} u _ {c} (k h - h) - s _ {0} y (k h) - s _ {1} y (k h - h) + u (k h - h)$$

![](image/e3a503b28327722fc39ea67719e8d33a710e0a6f7a9d882fadc698a9382b3fd5.jpg)  
Figure 11.8 Tracking time-varying parameters.

where

$$t _ {0} = \frac {1 + a _ {m}}{b}t _ {1} = a _ {0} t _ {0}s _ {0} = \frac {1 + a _ {o} + a _ {m} - a}{b}s _ {1} = \frac {a _ {n} a _ {m} + a}{b}$$
