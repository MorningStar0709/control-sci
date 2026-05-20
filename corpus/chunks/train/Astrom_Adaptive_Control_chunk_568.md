# EXAMPLE 9.3 Concentration control

Consider the concentration control problem in Example 1.5. The process is described by Eq. (1.3). Assume that we are interested in manipulating the concentration in the tank, c, by changing the inlet concentration, $c_{in}$ . For a fixed flow the dynamics can be described by the transfer function

$$G (s) = \frac {1}{1 + s T} e ^ {- s \tau}$$

where

$$T = V _ {m} / q \quad \tau = V _ {d} / q$$

If $\tau < T$ , then it is straightforward to determine a PI controller that performs well when $q$ is constant. However, it is difficult to find universal values of the controller parameters that will work well for wide ranges of $q$ . This is illustrated in Fig. 1.11, which shows the step responses of a fixed-gain controller for varying flows. Since the process has a time delay, it is natural to look for sampled data controllers. Sampling of the model with sampling period $h = V_d / (dq)$ , where $d$ is an integer, gives

$$c (k h + h) = a c (k h) + (1 - a) u (k h - d h)$$

where

$$a = e ^ {q h / V _ {m}} = e ^ {- V _ {d} / (V _ {m} d)}$$

Notice that the sampled data model has only one parameter, a, that does not depend on q. A constant-gain controller can easily be designed for the sampled data system.

The gain scheduling is realized simply by having a controller with constant parameters, in which the sampling rate is inversely proportional to the flow rate. This will give the same response, independent of the flow, in looking at the sampling instants, but the transients will be scaled in time. Figure 9.5 shows the output concentration and the control signals for three different flows. To implement this gain-scheduling controller, it is necessary to measure not only the concentration but also the flow. Errors in the flow measurement will result in jitter in the sampling period. To avoid this, it is necessary to filter the flow measurement.

![](image/26fc482fa6d508d72d690800cf84a2eee01a1cc7963c95d49764b29cc842d25b.jpg)  
Figure 9.5 Output concentration and control signal when the process in Example 9.3 is controlled by a fixed digital controller but the sampling interval is $h = 1/(2q)$ . (a) q = 0.5; (b) q - 1; (c) q = 2.

The Ziegler-Nichols transient response method discussed in Section 8.4 is based on a model with a time delay and a first-order system. Table 8.1 gives

$$K _ {c} = \frac {0 . 9 \tau}{T} = \frac {0 . 9 V _ {d}}{V _ {m}}T _ {i} = 3 \tau = \frac {3 V _ {d}}{q}$$
