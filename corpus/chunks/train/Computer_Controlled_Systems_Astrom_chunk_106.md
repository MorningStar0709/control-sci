# Sampling a System with Time Delay

Time delays are common in mathematical models of industrial processes. The theory of continuous-time systems with time delays is complicated because the systems are infinite-dimensional.

It is, however, easy to sample systems with time delays because the control signal is constant between sampling instants, which makes the sampled-data system finite-dimensional. Let the system be described by

$$\frac {d x (t)}{d t} = A x (t) + B u (t - \tau) \tag {2.8}$$

It is assumed initially that the time delay $\tau$ is less than or equal to the sampling period. The zero-order-hold sampling of the system (2.8) will now be calculated. Integration of (2.8) over one sampling period gives

$$x (k h + h) = e ^ {A h} x (k h) + \int_ {k h} ^ {k h + h} e ^ {A (k h + h - s ^ {\prime})} B u (s ^ {\prime} - \tau) d s ^ {\prime} \tag {2.9}$$

Because the signal $u(t)$ is piecewise constant over the sampling interval, the delayed signal $u(t-\tau)$ is also piecewise constant. The delayed signal will, however, change between the sampling instants (see Fig. 2.2). To evaluate the integral of (2.9), it is then convenient to split the integration interval into two parts so that $u(t - \tau)$ is constant in each part. Hence

![](image/08ae074471347c3555e1c22293fc82e9cba5878eaae65412361ae2f40a4d1874.jpg)

<details>
<summary>line</summary>

| Time Interval | Delayed Signal (u(t)) | Delayed Signal (t) |
| --- | --- | --- |
| kh - h | Low | 0 |
| kh | High | 0 |
| kh + h | High | 0 |
| kh + 2h | High | 0 |
</details>

Figure 2.2 The relationship among $u(t)$ , the delayed signal $u(t - \tau)$ , and the sampling instants.

$$
\begin{array}{l} \int_ {k h} ^ {k h + h} e ^ {A (k h + h - s ^ {\prime})} B u \left(s ^ {\prime} - \tau\right) d s ^ {\prime} \\ = \int_ {k h} ^ {k h + \tau} e ^ {A (k h + h - s ^ {\prime})} B d s ^ {\prime} u (k h - h) + \int_ {k h + \tau} ^ {k h + h} e ^ {A (k h + h - s ^ {\prime})} B d s ^ {\prime} u (k h) \\ = \Gamma_ {1} u (k h - h) + \Gamma_ {0} u (k h) \\ \end{array}
$$

Sampling the continuous-time system (2.8) thus gives

$$x (k h + h) = \Phi x (k h) + \Gamma_ {0} u (k h) + \Gamma_ {1} u (k h - h) \tag {2.10}$$

where

$$
\begin{array}{l} \Phi = e ^ {A h} \\ \Gamma_ {0} = \int_ {0} ^ {h - \tau} e ^ {A s} d s B \tag {2.11} \\ \Gamma_ {1} = e ^ {A (h - \tau)} \int_ {0} ^ {\tau} e ^ {A s} d s B \\ \end{array}
$$

A state-space model of (2.10) is given by

$$
\binom {x (k h + h)} {u (k h)} = \left( \begin{array}{c c} \Phi & \Gamma_ {1} \\ 0 & 0 \end{array} \right) \binom {x (k h)} {u (k h - h)} + \binom {\Gamma_ {0}} {I} u (k h)
$$

Notice that r extra state variables $u(kh - h)$ , which represent the past values of the control signal, are introduced. The continuous-time system of (2.8) is infinite dimensional; the corresponding sampled system, however, is a finite-dimensional system. Thus time delays are considerably simpler to handle if the system is sampled, for the following reason: To specify the state of the system, it is necessary to store the input over a time interval equal to the time delay. With zero-order-hold reconstruction, the input signal can be represented always by a finite number of values.
