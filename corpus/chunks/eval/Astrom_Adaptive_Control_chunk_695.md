# Algorithm Skeleton

All adaptive algorithms discussed in this chapter have the following form:

```txt
1 Analog_Digital_conversion
2 Compute_control_signal
3 Digital_Analog_conversion
4 If estimate then
5 begin{estimate}
6 Covariance_update
7 Parameter_update
8 If tune then
9 begin{tune}
th_design:=th_estimated
10 Design_calculations
11 end{tune}
12 end{estimate}
13 Organize_data
14 Compute_as_much_as_possible_of_control_signal 
```

Row 1 implements the conversion of the measured output signal, the reference signal, and possible feedforward signal. All the converted signals are supposed to be filtered through appropriate anti-aliasing filters, as discussed in Section 11.2. Row 3 sets the control signal to the process. Rows 14 and 2 contain the calculations of the control signal, which are independent of whether the parameters are estimated or not. Notice the division of the calculations of the control signal to avoid overly long computation times. All calculations that are possible to do in advance are done in Row 14. Only calculations that contain the last measurements are done in Row 2.

Rows 4–13 contain calculations that are specific for an adaptive algorithm. There are two logical variables, estimate and tune, which control whether the parameters are going to be estimated and whether the controller is going to be redesigned, respectively. The estimation is done in Rows 5–7, and the design calculations are done in Row 10. Row 13 organizes the data such that the algorithm is always ready to start estimation when the operator wishes.

The various adaptive algorithms discussed in this section differ only in the design calculations. The estimator part can be the same for all algorithms. One important part of the algorithms that will not be discussed here is the operator interface. This is usually a significant part of an adaptive control system, but it is very hardware-dependent, so it is difficult to discuss in general terms. We now discuss the calculations in Rows 4–13 in more detail.
