# 2. PID controllers

The PID controller is a commonly used feedback controller consisting of proportional, integral, and derivative terms, hence the name. This chapter will build up the definition of a PID controller term by term while trying to provide intuition for how each of them behaves.

First, we’ll get some nomenclature for PID controllers out of the way. The reference is called the setpoint (the desired position) and the output is called the process variable (the measured position). Below are some common variable naming conventions for relevant quantities.

The error e(t) is $r ( t ) - y ( t )$ .

For those already familiar with PID control, this book’s interpretation won’t be consistent with the classical intuition of “past”, “present”, and “future” error. We will be approaching it from the viewpoint of modern control theory with proportional controllers applied to different physical quantities we care about. This will provide a more complete explanation of the derivative term’s behavior for constant and moving setpoints, and this intuition will carry over to the modern control methods covered later in this book.

The proportional term drives the position error to zero, the derivative term drives the velocity error to zero, and the integral term accumulates the area between the setpoint and output plots over time (the integral of position error) and adds the current total to the control input. We’ll go into more detail on each of these.
