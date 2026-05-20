9.9 Repeat Problem 9.8 but now use a subroutine to perform a scalar product. Discuss how computing time and storage requirements are influenced by the restructuring of the program.

9.10 Consider the control algorithm with rejection of outliers given by Eqs. (9.1) and (9.4). Make an estimate of the number of computations required for one iteration. (Hint: A matrix multiplication of an $n \times p$ matrix by a $p \times r$ matrix requires N = npr operations, where an operation corresponds to one addition and one multiplication. Solution of the equation

$$\boldsymbol {A} \boldsymbol {x} = \boldsymbol {B}$$

where A is $n \times n$ and B is $n \times p$ , requires approximately

$$N = \frac {1}{3} n ^ {3} + \frac {1}{2} n ^ {2} p$$

operations, where the major part of the calculations is the triangulation of the matrix A.)

9.11 Consider a discrete-time system characterized by the pulse-transfer function

$$H (z) = \frac {1}{(z - a) ^ {n}}$$

Calculate the sensitivity of the poles with respect to the parameters using Eq. (9.18) in each case.

(a) The filter is in companion form.   
(b) The filter is in Jordan canonical form.

9.12 Make a flow chart similar to Fig. 9.20 for a system with loops having sampling periods of 1, 2, 5, and 60 s.

9.13 Consider a system with the transfer function

$$H (z) = \frac {1}{z ^ {n} + a _ {1} z ^ {n - 1} + \cdots + a _ {n}}$$

Assume that the system is realized with fixed-point arithmetic. Let the roundoff be described as normal rounding to integers. Show that the condition for a steady-state error k with no inputs is given by

$$k + \sum_ {i = 1} ^ {n} Q (a _ {i} k) = 0$$

Furthermore, show that the condition for a limit-cycle oscillation with a period of two sampling periods is

$$k + \sum_ {i = 1} ^ {n} (- 1) ^ {i} Q (a _ {i} k) = 0$$

9.14 Consider the following algorithm for a PI-controller:

```autohotkey
Adin uc y
e:=uc-y
v:=k*e+i
u:=max(min(512,v),0)
Daout u
i:=u+k*h*e/ti 
```

Assume that the A-D and D-A converters have a resolution of 8 bits and that all calculations are made using integers. What is the word length required to represent variable i if overflow should be avoided? Use k = 50 and (a) h = 1, ti = 300 or (b) h = 0.01, ti = 1500.

Discuss how the result is influenced by the sampling period.
