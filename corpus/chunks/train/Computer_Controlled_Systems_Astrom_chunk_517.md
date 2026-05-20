# Selection of Sampling Interval

When DDC-control was first introduced, computers were not as powerful as they are today. Long sampling intervals were needed to handle many loops. The following recommendations for the most common process variables are given for DDC-control.

<table><tr><td>Type of variable</td><td>Sampling time, s</td></tr><tr><td>Flow</td><td>1-3</td></tr><tr><td>Level</td><td>5-10</td></tr><tr><td>Pressure</td><td>1-5</td></tr><tr><td>Temperature</td><td>10-20</td></tr></table>

Commercial digital controllers for few loops often have a short fixed-sampling interval on the order of 200 ms. This implies that the controllers can be regarded as continuous-time controllers, and the continuous-time tuning rules may be used. Several rules of thumb for choosing the sampling period for a digital PID-controller are given in the literature. There is a significant difference between PI- and PID-controllers. For PI-controllers the sampling period is related to the integration time. A typical rule of thumb is

$$\frac {h}{T _ {i}} \approx 0. 1 \text { to } 0. 3$$

When Ziegler-Nichols tuning is used this implies

$$\frac {h}{L} \approx 0. 3 \text { to } 1$$

or

$$\frac {h}{T _ {u}} \approx 0. 1 \text { to } 0. 3$$

With PID-control the critical issue is that the sampling period must be so short that the phase lead is not adversely affected by the sampling. This implies that the sampling period should be chosen so that the number $hN/T_{d}$ is in the range of 0.2 to 0.6. With N = 10 this means that for Ziegler-Nichols tuning the ratio h/L is between 0.01 and 0.06. This gives

$$\frac {h N}{T _ {d}} \approx 0. 2 \text { to } 0. 6$$

Significantly shorter sampling periods are thus required for controllers with derivative action. If computer time is at a premium, it is advantageous to use the sampled-data design methods used in this book.
