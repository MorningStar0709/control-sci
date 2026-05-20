# Hidden Oscillations

Figure 3.18 shows that the continuous-time output of the process may have oscillations that are not seen at the sampling points. These are called hidden oscillations, or intersample ripple. Simulation is an effective tool for finding hidden oscillations. The modified z-transform or (2.34) also can be used to calculate the continuous-time output between the sampling instants; however, it is also enlightening to do some analysis.

The intersample ripple is essentially determined by the open-loop dynamics because the system operates in open loop between the sampling points. Two cases can be distinguished.

\- Oscillation in the continuous-time output of an open- or closed-loop system when there is no oscillation in the control signal

\- Oscillations between the sampling points caused by an oscillation in the control signal

The first case of intersample ripple may occur if observability of the open-loop system is lost due to sampling. The pulse-transfer function then has canceled poles and zeros. The effect of the canceled modes is then not seen at the sampling instants. There may then be hidden oscillations if the continuous-time open-loop system has oscillatory modes and if the sampling period matches the frequency of these modes. This type of hidden oscillation occurs only for certain values of the sampling period. A change in the sampling interval makes the system observable and the oscillation can be seen in the sampled output. The oscillation frequency is often lower in the sampled signal than in the continuous-time signal. To detect this type of intersample ripple, it is necessary to check the observability of the sampled-data system (compare with Example 3.12).
