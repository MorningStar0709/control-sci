# Parameterization and Parameter Changes

In conventional process controllers, the operator can manipulate the set point and the parameters in the control law (gain, integration time, and derivative time). With computer control, there are many other interesting alternatives. Because of the simplicity of computing, it is possible to use one parameterization in the control algorithm and another in the operator communication. The parameters displayed to the operator may then be related to the performance of the system rather than to the details of the control algorithm. The conversion between the parameters is made by an algorithm in the computer.

To illustrate the idea of performance-related parameters, consider design of a servo using the pole-placement method described in Chapter 5. The closed-loop properties may be specified in terms of the relative damping $\zeta$ and the bandwidth $\omega_{B}$ . To perform the design, it is also necessary to have a model of the open-loop dynamics. One possibility is to have the process engineer enter the desired bandwidth and damping and a continuous-time model. The computer can then make the necessary conversions in order to obtain the control law. If the computer also has a recursive estimation algorithm, it is not necessary to introduce the model. Clearly, there are many interesting possibilities if estimation and design algorithms are included in the controller.

There are two operational problems with on-line parameter changes. One problem is related to real-time programming. Data representing parameters are shared among different programs. It is then necessary to make sure that one program is not using data that are being changed by another program. This is discussed in Sec. 9.8.

The other problem is algorithmic. There may be switching transients when the parameters are changed in a control algorithm. To get some insight into what can happen, consider the simple PI-algorithm

```txt
e:=uc-y
u:=k*(e+i/ti)
i:=i+e*h 
```

It is clear that a change of the integration time ti will cause a step in the control signal unless the integral part, i, is zero. The problem can be avoided by changing the state from i to i\*ti/ti', where ti' is the new value of the integration time. Another simpler way is to write the algorithm as

```autohotkey
e:=uc-y
u:=k*e+i
i:=i+k*e*h/ti 
```
