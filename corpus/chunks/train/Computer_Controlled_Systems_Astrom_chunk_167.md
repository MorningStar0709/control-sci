# Jury's Stability Criterion

The following test is useful for determining if Eq. (3.4) has all its zeros inside the unit disc. Form the table

$$
\begin{array}{c c c c c} a _ {0} & a _ {1} & \dots & a _ {n - 1} & a _ {n} \\ a _ {n} & a _ {n - 1} & \dots & a _ {1} & a _ {0} \\ \hline a _ {0} ^ {n - 1} & a _ {1} ^ {n - 1} & \dots & a _ {n - 1} ^ {n - 1} \\ a _ {n - 1} ^ {n - 1} & a _ {n - 2} ^ {n - 1} & \dots & a _ {0} ^ {n - 1} \\ \hline \vdots & & & & \\ a _ {0} ^ {0} & & & & \end{array} \quad \alpha_ {n} = \frac {a _ {n}}{a _ {0}} \quad \alpha_ {n - 1} = \frac {a _ {n - 1} ^ {n - 1}}{a _ {0} ^ {n - 1}}
$$

where

$$a _ {i} ^ {k - 1} = a _ {i} ^ {k} - \alpha_ {k} a _ {k - i} ^ {k}\alpha_ {k} = a _ {k} ^ {k} / a _ {0} ^ {k}$$

The first and second rows are the coefficients in (3.4) in forward and reverse order, respectively. The third row is obtained by multiplying the second row by $\alpha_{n}=a_{n}/a_{0}$ and subtracting this from the first row. The last element in the third row is thus zero. The fourth row is the third row in reverse order. The scheme is then repeated until there are $2n+1$ rows. The last row consists of only one element. The following theorem results.

THEOREM 3.3 JURY'S STABILITY TEST If $a_0 > 0$ , then Eq. (3.4) has all roots inside the unit disc if and only if all $a_0^k$ , $k = 0, 1, \ldots, n - 1$ are positive. If no $a_0^k$ is zero, then the number of negative $a_0^k$ is equal to the number of roots outside the unit disc.

Remark. If all $a_0^k$ are positive for $k = 1, 2, \ldots, n - 1$ , then the condition $a_0^0 > 0$ can be shown to be equivalent to the conditions

$$
\begin{array}{l} A (1) > 0 \\ (- 1) ^ {n} A (- 1) > 0 \\ \end{array}
$$

These conditions constitute necessary conditions for stability and hence can be used before forming the table.

![](image/5731955c081159c9f81c4bee883ea99dc3acd6b5920f608b80bc0972fa390767.jpg)

<details>
<summary>text_image</summary>

a₂
1
-2 -1 1 2 a₁
-1
</details>

Figure 3.2 The stability area for the second-order equation (3.5) as a function of the coefficients $\alpha_{1}$ and $\alpha_{2}$ .
