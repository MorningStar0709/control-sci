$$
\begin{array}{l} J = \int_ {0} ^ {\infty} \left\{\sum_ {i = 1} ^ {5} \left(\frac {K \Delta x _ {i}}{7 5 , 0 0 0}\right) ^ {2} + \sum_ {i = 1} ^ {5} \left(\frac {D (\Delta v _ {i - 1} - \Delta v _ {i})}{5 0 , 0 0 0}\right) ^ {2} + \left(\frac {\Delta v _ {1} + z}{2}\right) ^ {2} + \left(\frac {F _ {1}}{1 2 0}\right) ^ {2} \right] d t \\ = \int_ {0} ^ {\infty} \left[ \sum_ {i = 2} ^ {5} [ 3. 3 4 \Delta x _ {i} ] ^ {2} + \sum_ {i = 2} ^ {5} [ 3 (\Delta v _ {i - 1} - \Delta v _ {i}) ] ^ {2} + [. 5 (\Delta v _ {1} + z) ] ^ {2} + \left(\frac {F _ {1}}{1 2 0}\right) ^ {2} \right\} d t. \\ \end{array}
$$

To generate the $Q$ matrix, we note that the state-dependent part of the integrand is the Euclidean length of a vector $\mathbf{v}$ , where

$$\mathbf {v} ^ {T} = \left[ 3. 3 4 \Delta x _ {2} \dots 3. 3 4 \Delta x _ {5} \quad 3 (\Delta v _ {1} - \Delta v _ {2}) \quad \dots \quad 3 (\Delta v _ {4} - \Delta v _ {5}) \quad . 5 (\Delta v _ {1} + z) \right].$$

This vector is expressed as

$$
\mathbf {v} = V \left[ \begin{array}{c} \Delta x _ {2} \\ \vdots \\ \Delta x _ {5} \\ \dots \\ \Delta v _ {1} \\ \vdots \\ \Delta v _ {5} \\ \dots \\ z \end{array} \right] = \left[ \begin{array}{c c c c} & & & \\ 3. 3 4 I & & & \\ & & & \\ \hline & 3 - 3 & & \\ & 3 - 3 & & \\ & \dots & \dots & \\ & & 3 - 3 & \\ \hline & . 5 0 & & . 5 \end{array} \right] \left[ \begin{array}{c} \Delta x _ {2} \\ \vdots \\ \Delta x _ {5} \\ \dots \\ \Delta v _ {1} \\ \vdots \\ \Delta v _ {5} \\ \dots \\ z \end{array} \right]
$$

Since $v^{T}v = x^{T}V^{T}Vx$ , where x is the state vector, we have $Q = V^{T}V$ . This index yields the optimal gain (MATLAB lqr)

$$
\begin{array}{l} K = [ 5 4. 5 3 \quad 1 7. 2 8 \quad - 1. 3 0 3 \quad - 4. 3 6 1 \quad 1 9 1. 7 \\ - 4 0. 4 8 \quad - 3 4. 2 1 \quad - 2 9. 7 0 \quad - 2 7. 3 4 \quad - 2 7. 3 4 \quad 5 2. 0 9 ] \\ \end{array}
$$

Figure 7.18 shows the results. The velocity error is well within the desired 2-m/s magnitude, and the coupler forces are well below the limits; unfortunately, the traction force goes well above the 120-kN limit.

![](image/d051f38820ec3163fb621c4f6804b7d6b0015c643cd999f5a4a7be3e43b682ae.jpg)

<details>
<summary>line</summary>

| Time (s) | Force (kN) |
| --- | --- |
| 0 | 200 |
| 5 | 190 |
| 10 | 170 |
| 15 | 150 |
| 20 | 130 |
| 25 | 115 |
| 30 | 105 |
</details>

![](image/4daf53f7f073bdae3bd9c5b5d9935397fe8f18dcccf07af1e381cc7822d62581.jpg)

<details>
<summary>line</summary>
