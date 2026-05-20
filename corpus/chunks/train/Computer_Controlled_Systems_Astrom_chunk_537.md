# Outliers and Measurement Malfunctions

The linear filtering theory that will be discussed in Chapter 11 is very useful in reducing the influence of measurement noise. However, there may also be other types of errors, such as instrument malfunction and conversion errors. These are typically characterized by large deviations, which occur with low probabilities. It is very important to try to eliminate such errors so that they do not enter into the control-law calculations. There are many good ways to achieve this when using computer control.

The errors may be detected at the source. In systems with high-reliability requirements, this is done by duplication of the sensors. Two sensors are then combined with a simple logic, which gives an alarm if the difference between the sensor signals is larger than a threshold. A pair of redundant sensors may be regarded as one sensor that gives either a reliable measurement or a signal that it does not work.

Three sensors may be used in more extreme cases. A measurement is then accepted as long as two out of the three sensors agree (two-out-of-three logic). It is also possible to use even more elaborate combinations of sensors and filters.

An observer can also be used for error detection. For example, consider the control algorithm of (9.1) with an explicit observer. Notice that the one-step prediction error

$$\varepsilon (k) = y (k) - \hat {y} (k | k - 1) = y (k) - C \hat {x} (k | k - 1) \tag {9.4}$$

appears explicitly in the algorithm. This error can be used for diagnosis and to detect if the measurements are reasonable. This will be further discussed in connection with the Kalman filter in Chapter 11.

In computer control there are also many other possibilities for detecting different types of hardware and software errors. A few extra channels in the A-D converter, which are connected to fixed voltages, may be used for testing and calibration. By connecting a D-A channel to an A-D channel, the D-A converter may also be tested and calibrated.
