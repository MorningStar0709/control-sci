![](image/a50967e596b7e7fef4c94416a722a1823ce906c390495b54d8cf68a938545902.jpg)

<details>
<summary>line</summary>

| Time, t = kT_s | e(k-2) | e(k-1) | e(k) | e(k+1) |
| --- | --- | --- | --- | --- |
| k-2 |  |  |  |  |
| k-1 |  |  |  |  |
| k |  |  |  |  |
| k+1 |  |  |  |  |
</details>

Figure 10.59 Numerical integration using the rectangle rule.

As a second example, consider the PID control logic

$$u (t) = K _ {P} e (t) + K _ {I} \int e (t) d t + K _ {D} \dot {e} (t) \tag {10.61}$$

Now we must develop a discrete-time equation for the derivative of the error signal ė (t). The simplest technique is to use the backward finite-difference equation

$$v (k) = \frac {e (k) - e (k - 1)}{T _ {s}} \tag {10.62}$$

where digital signal v(k) is the numerical derivative of the error signal. Using Eqs. (10.62) and (10.60), the digital PID control algorithm is

$$u (k) = K _ {P} e (k) + K _ {I} w (k) + K _ {D} v (k) \tag {10.63}$$

Implementing the PID controller requires three lines of computer code: Eq. (10.60) computes the numerical integral of the digital error e(k), Eq. (10.62) computes the numerical derivative of e(k), and Eq. (10.63) computes the digital control signal u(k) using the PID gains. This particular PID algorithm is called a first-order recursive method because it requires the computer memory to only store the integral signal w(k − 1) and error signal e(k − 1) from the previous sample time.

Computing the derivative using the finite-difference equation (10.62) may produce very poor results if the signal e(k) is corrupted by noise. This issue was briefly discussed in a previous section, and the simplest remedy is to replace the PD controller with a lead controller. For example, consider the continuous-time PD controller with gains $K _ { P } = 1 2$ and $K _ { D } = 4$ :

$$\text { PD control: } \quad u (t) = 1 2 e (t) + 4 \dot {e} (t) \tag {10.64}$$

The PD controller transfer function is

$$\text { PD controller: } \quad G _ {\mathrm{PD}} (s) = 1 2 + 4 s = 4 (s + 3) = \frac {U (s)}{E (s)} \tag {10.65}$$

This PD controller has a low-frequency (DC) gain of 12. We can replace the pure differentiation by inserting a low-pass filter in series with the original PD controller to yield a lead controller. For example, let us add a low-pass filter with a corner frequency of 20 rad/s

$$\text { Lead controller: } \quad G _ {\mathrm{LF}} (s) = \frac {8 0 (s + 3)}{s + 2 0} = \frac {U (s)}{E (s)} \tag {10.66}$$
