# 3.5.1 Introduction

To introduce the concept of observability, consider the system of Example 3.4 (with zero input), and suppose there is a sensor that measures y, the height of the center of gravity referred to equilibrium. Let there be an initial angular displacement but no vertical displacement or velocity. As was shown in Example 3.4, the motion for t > 0 will have a pitch (angular) component but no heave (vertical) component. The sensor will read zero and will provide no information at all about the motion in the system.

Example 3.2 provides another case of an uninformative sensor, if the sensor is a voltmeter across the two top resistances of value R. For $i_{s}=0$ and an initial state $x_{1}=x_{2}$ , the two voltages $x_{1}$ and $x_{2}$ remain equal for t>0, so that the voltmeter constantly reads zero.

The concept of observability addresses the issue of sensing and the ability of the sensors to capture the dynamical behavior of the system. The C matrix describes how the sensed outputs are generated from the states, i.e., the way in which the sensors “couple into” the states. The relationship between the C and A matrices will turn out to be crucial.
