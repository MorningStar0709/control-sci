$K _ { p }$ is called the proportional gain, $T _ { i }$ is called the integral time, and $T _ { d }$ is called the derivative time. From Equation (3–37) we obtain the proportional gain $K _ { p }$ , integral time $T _ { i }$ and derivative time, $T _ { d }$ to be

$$K _ {p} = \frac {R _ {4} \left(R _ {1} C _ {1} + R _ {2} C _ {2}\right)}{R _ {3} R _ {1} C _ {2}}T _ {i} = \frac {1}{R _ {1} C _ {1} + R _ {2} C _ {2}}T _ {d} = \frac {R _ {1} C _ {1} R _ {2} C _ {2}}{R _ {1} C _ {1} + R _ {2} C _ {2}}$$

When a PID controller is expressed as

$$\frac {E _ {o} (s)}{E _ {i} (s)} = K _ {p} + \frac {K _ {i}}{s} + K _ {d} s$$

$K _ { p }$ is called the proportional gain, $K _ { i }$ is called the integral gain, and $K _ { d }$ is called the derivative gain. For this controller

$$K _ {p} = \frac {R _ {4} \left(R _ {1} C _ {1} + R _ {2} C _ {2}\right)}{R _ {3} R _ {1} C _ {2}}K _ {i} = \frac {R _ {4}}{R _ {3} R _ {1} C _ {2}}K _ {d} = \frac {R _ {4} R _ {2} C _ {1}}{R _ {3}}$$

Table 3–1 shows a list of operational-amplifier circuits that may be used as controllers or compensators.

Table 3–1 Operational-Amplifier Circuits That May Be Used as Compensators
