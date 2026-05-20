# Example A.5 An inventory model

An inventory is a typical example that can naturally be described as a discrete-time system. Orders and deliveries are obtained at regular intervals tied to the calendar—for example, each day or week.

Let $y(k)$ be the inventory at time $k$ before any transaction is started. The deliveries to the inventory that are ordered at time $k$ are $u(k)$ . It is assumed that there is a delay of one period from the order until the goods start coming into the inventory. Finally, the delivery from the inventory is $v(k)$ . Introduce the state variables $x_1(k) = y(k)$ and $x_2(k) = u(k - 1)$ . The inventory can be described by the following discrete-time state equations:

$$x _ {1} (k + 1) = x _ {1} (k) + x _ {2} (k) - v (k)x _ {2} (k + 1) = u (k)$$

or

$$
x (k + 1) = \left( \begin{array}{l l} 1 & 1 \\ 0 & 0 \end{array} \right) x (k) + \binom {0} {1} u (k) + \binom {- 1} {0} v (k) \tag {A.11}

y (k) = \left( \begin{array}{l l} 1 & 0 \end{array} \right) x (k)
$$

The input-output relation is given by

$$y (k) - y (k - 1) = u (k - 2) - v (k - 1) \tag {A.12}$$
