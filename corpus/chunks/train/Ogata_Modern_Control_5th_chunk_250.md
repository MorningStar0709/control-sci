$$K _ {v} = \lim _ {s \rightarrow 0} \frac {s K (T _ {a} s + 1) (T _ {b} s + 1) \cdots}{s (T _ {1} s + 1) (T _ {2} s + 1) \cdots} = K$$

For a type 2 or higher system,

$$K _ {v} = \lim _ {s \rightarrow 0} \frac {s K (T _ {a} s + 1) (T _ {b} s + 1) \cdots}{s ^ {N} (T _ {1} s + 1) (T _ {2} s + 1) \cdots} = \infty , \quad \text { for } N \geq 2$$

The steady-state error $e _ { \mathrm { s s } }$ for the unit-ramp input can be summarized as follows:

$$e _ {\mathrm{ss}} = \frac {1}{K _ {v}} = \infty , \quad \text { for type 0 systems }e _ {\mathrm{ss}} = \frac {1}{K _ {v}} = \frac {1}{K}, \quad \text { for type 1 systems }e _ {\mathrm{ss}} = \frac {1}{K _ {v}} = 0, \quad \text { for type 2 or higher systems }$$

The foregoing analysis indicates that a type 0 system is incapable of following a ramp input in the steady state.The type 1 system with unity feedback can follow the ramp input with a finite error. In steady-state operation, the output velocity is exactly the same as the input velocity, but there is a positional error. This error is proportional to the velocity of the input and is inversely proportional to the gain K. Figure 5–47 shows an example of the response of a type 1 system with unity feedback to a ramp input. The type 2 or higher system can follow a ramp input with zero error at steady state.

Static Acceleration Error Constant $K _ { a } .$ The steady-state error of the system with a unit-parabolic input (acceleration input), which is defined by

$$r (t) = \frac {t ^ {2}}{2}, \quad \text { for } t \geq 0= 0, \quad \text { for } t < 0$$

is given by

$$
\begin{array}{l} e _ {\mathrm{ss}} = \lim _ {s \rightarrow 0} \frac {s}{1 + G (s)} \frac {1}{s ^ {3}} \\ = \frac {1}{\lim _ {s \to 0} s ^ {2} G (s)} \\ \end{array}
$$

The static acceleration error constant $K _ { a }$ is defined by the equation

$$K _ {a} = \lim _ {s \rightarrow 0} s ^ {2} G (s)$$

The steady-state error is then

$$e _ {\mathrm{ss}} = \frac {1}{K _ {a}}$$

Note that the acceleration error, the steady-state error due to a parabolic input, is an error in position.

The values of $K _ { a }$ are obtained as follows:

For a type 0 system,

$$K _ {a} = \lim _ {s \rightarrow 0} \frac {s ^ {2} K (T _ {a} s + 1) (T _ {b} s + 1) \cdots}{(T _ {1} s + 1) (T _ {2} s + 1) \cdots} = 0$$

For a type 1 system,

$$K _ {a} = \lim _ {s \rightarrow 0} \frac {s ^ {2} K (T _ {a} s + 1) (T _ {b} s + 1) \cdots}{s (T _ {1} s + 1) (T _ {2} s + 1) \cdots} = 0$$

For a type 2 system,

$$K _ {a} = \lim _ {s \rightarrow 0} \frac {s ^ {2} K (T _ {a} s + 1) (T _ {b} s + 1) \cdots}{s ^ {2} (T _ {1} s + 1) (T _ {2} s + 1) \cdots} = K$$

For a type 3 or higher system,
