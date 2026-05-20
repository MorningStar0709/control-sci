# 8.5 Digital PID-Controllers

Many practical control problems are solved by PID-controllers. The "textbook" version of the PID-controller can be described by the equation

$$u (t) = K \left(e (t) + \frac {1}{T _ {i}} \int^ {t} e (s) d s + T _ {d} \frac {d e (t)}{d t}\right) \tag {8.21}$$

where error e is the difference between command signals $u_{c}$ (the set point) and process output y (the measured variable). K is the gain or proportional gain of the controller, $T_{t}$ the integration time or reset time, and $T_{d}$ the derivative time. The PID-controller was originally implemented using analog technology that went through several development stages, that is, pneumatic valves, relays and motors, transistors, and integrated circuits. In this development much know-how was accumulated that was embedded into the analog design. Today virtually all PID-controllers are implemented digitally. Early implementations were often a pure translation of (8.21), which left out many of the extra features that were incorporated in the analog design. In this section we will discuss the digital PID-controller in some detail. This is a good demonstration that a good controller is not just an implementation of a “textbook” algorithm. It is also a good way to introduce some of the implementation issues that will be discussed in depth in Chapter 9.
