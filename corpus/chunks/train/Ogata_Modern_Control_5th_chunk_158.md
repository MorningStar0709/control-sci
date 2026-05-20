A block diagram for this system is shown in Figure 4–25. The transfer function $Y ( s ) / E ( s )$ can be obtained as

$$\frac {Y (s)}{E (s)} = \frac {b}{a + b} \frac {\frac {K}{s}}{1 + \frac {a}{a + b} \frac {K}{s} \frac {T _ {1} s}{T _ {1} T _ {2} s ^ {2} + (T _ {1} + 2 T _ {2}) s + 1}}$$

Under normal circumstances we design the system such that

$$\left| \frac {a}{a + b} \frac {K}{s} \frac {T _ {1} s}{T _ {1} T _ {2} s ^ {2} + (T _ {1} + 2 T _ {2}) s + 1} \right| \gg 1$$

then

$$
\begin{array}{l} \frac {Y (s)}{E (s)} = \frac {b}{a} \frac {T _ {1} T _ {2} s ^ {2} + \left(T _ {1} + 2 T _ {2}\right) s + 1}{T _ {1} s} \\ = K _ {p} + \frac {K _ {i}}{s} + K _ {d} s \\ \end{array}
$$

where

$$K _ {p} = \frac {b}{a} \frac {T _ {1} + 2 T _ {2}}{T _ {1}}, \quad K _ {i} = \frac {b}{a} \frac {1}{T _ {1}}, \quad K _ {d} = \frac {b}{a} T _ {2}$$

Thus, the controller shown in Figure 4–24 is a proportional-plus-integral-plus-derivative controller (PID controller).
