# 9.10 Problems

9.1 Consider control of a double integrator with a sampling period of 1 s. Calculate the deadbeat control for the system obtained using an antialiasing filter with the transfer function

$$G (s) = \frac {1}{s ^ {2} + 1 . 4 s + 1}$$

Compare the deadbeat strategy obtained with the deadbeat strategy for the pure double-integrator using simulation.

9.2 Write a program for computing the scalar product of two arrays

```txt
begin
s:=0
for i:=1 to n do
s:=s+a[i]*b[i]
end 
```

in each case.

(a) s: integer, a, b: arrays of integers.   
(b) s: double-precision integer, a, b: arrays of integers.   
(c) s: real, a, b: arrays of reals.   
(d) s: double-precision real, a, b: arrays of reals.

Compare the computing times and precision. Try to find computers that have floating-point calculations in software, as well as in hardware.

9.3 Consider Example 9.9. Discuss the possibilities of using two loops with different sampling periods in order to improve the precision in the calculation.

9.4 Write a code for a digital PI-controller where the antiwindup is implemented as an observer with the time constant $T_{0}$ .

9.5 Write a code for a digital PID-controller where the antiwindup is implemented as a deadbeat observer.

9.6 Write a code in your favorite high-level language for a digital PID-algorithm where antiwindup is implemented as an observer with time constant $T_{0}$ . Determine the number of operations required for one iteration. Compile the program. Determine how many memory calls it requires. Time the program. How do the measured computing times relate to the number of operations and the computing times given in the computer manual?

9.7 Consider the control algorithm of (9.1), where $x_{m}$ is considered to be an input. Assume that the state, the control variable, and the process output have dimensions $n_{x}, n_{u}$ , and $n_{y}$ , respectively, and that the matrices are full. Determine the number of additions, multiplications, and divisions required for one iteration.

9.8 Consider the control algorithm of (9.2). Write a code that implements the control algorithm in your favorite high-level language. Compile the code, determine how much memory space the code occupies, and determine the execution time. Try to find a good simple formula for determining the execution time.
