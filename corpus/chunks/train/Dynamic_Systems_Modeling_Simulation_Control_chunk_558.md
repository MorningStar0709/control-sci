# PID Tuning Rules

The previous examples demonstrate the basic attributes of the PID controller: increasing the proportional gain $K _ { P }$ tends to speed up the response (reduce the peak time) but may increase the overshoot; increasing the integral gain $K _ { I }$ tends to reduce the steady-state error but may slow down the response; increasing the derivative gain $K _ { D }$ tends to reduce the overshoot and the settling time. It is clear that implementing a PID controller requires selecting three independent gains in order to achieve a good balance in the closed-loop performance criteria such as response time, overshoot, settling time, and steady-state error. In the early 1940s, Ziegler and Nichols [1] developed two methods for selecting “good” PID gains. These “PID tuning rules” were based on heuristic trials conducted by Ziegler and Nichols and they provide control engineers with a good starting point for selecting the PID gains that provide satisfactory closed-loop performance.

In the first method, Ziegler and Nichols noted that the open-loop step response of many dynamic systems exhibits an “S-shaped” curve with no overshoot. Figure 10.21 shows the characteristics of a general S-shaped open-loop response, which Ziegler and Nichols called the reaction curve. In practice, the reaction curve could be obtained experimentally by applying a step input and measuring the system output in an open-loop manner. The key parameters of the reaction curve are the delay time $T _ { d }$ and slope R shown in Fig. 10.21. Both parameters are obtained by drawing a line tangent to the inflection point of the S-curve (see Fig. 10.21), where the reaction curve has the steepest slope R. Ziegler and Nichols used these two parameters to develop PID gains that produced a closed-loop response that exhibited a one-quarter decay ratio, meaning that the transient response decays to one-quarter its peak value in one period of oscillation. Table 10.1 presents the Ziegler–Nichols rules for selecting the PID gains using the reaction-curve parameters delay time $T _ { d }$ and slope R. Note that Ziegler and Nichols present gain-tuning rules for P, PI, and PID controllers.

![](image/287ea62322e4425e381ad3e89cce563aeeb2ebcfe63f86c73c43ef6bfeb0cb8e.jpg)

<details>
<summary>line</summary>

| Time, t | y(t) |
| --- | --- |
| Td | 0 |
| T | >T |
| >T | A |
</details>

Figure 10.21 Reaction curve from an open-loop step input.
