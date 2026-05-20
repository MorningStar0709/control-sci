![](image/d1cbaf6d8e03b344afda1c19ddc973750c04ade655089eb42c0570d53ef8ca5f.jpg)

<details>
<summary>contour</summary>

| Region | u1 | u2 |
| --- | --- | --- |
| ① | 0.0 | 0.0 |
| ② | 2.5 | 0.0 |
| ③ | 0.0 | 2.5 |
| ④ | 1.5 | 1.5 |
</details>

Figure 6.7: Cost contours for a two-player, nonconvex game; cost increases for the convex combination of the two players’ optimal points.

in which $a = 1 . 1$ and $\beta = 0 . 4$ . Each player optimizes the cooperative objective starting at ➀ and produces the points, $( u _ { 1 } ^ { 0 } , u _ { 2 } ^ { p } )$ , denoted ➁ and $( u _ { 1 } ^ { p } , u _ { 2 } ^ { 0 } )$ , denoted ➂. Consider taking a convex combination of the two players’ optimal points for the next iterate

$$(u _ {1} ^ {p + 1}, u _ {2} ^ {p + 1}) = w _ {1} (u _ {1} ^ {0}, u _ {2} ^ {p}) + w _ {2} (u _ {1} ^ {p}, u _ {2} ^ {0}) \qquad w _ {1} + w _ {2} = 1, \quad w _ {1}, w _ {2} \geq 0$$

We see in Figure 6.7 that this iterate causes the objective function to increase rather than decrease for most values of w1, w2. For $w _ { 1 } = w _ { 2 } =$ $1 / 2$ , we see clearly from the contours that V at point ➃ is greater than V at point ➀. The values of the four points are given in the following table

<table><tr><td>Point</td><td> $u_1$ </td><td> $u_2$ </td><td> $V(u)$ </td></tr><tr><td>1</td><td>0</td><td>0</td><td>-0.93</td></tr><tr><td>2</td><td>2.62</td><td>0</td><td>-1.10</td></tr><tr><td>3</td><td>0</td><td>2.62</td><td>-1.10</td></tr><tr><td>4</td><td>1.31</td><td>1.31</td><td>-0.76</td></tr></table>

The possibility of a cost increase leads to the possibility of closedloop instability and precludes developing even a nominal control theory for this situation. In the centralized MPC problem, this nonconvexity issue can be addressed in the optimizer, which can move both inputs simultaneously and always avoid a cost increase. In the distributed case, the required information to avoid a cost increase is by design unavailable to the players.

One can of course consider adding another player to the game who has access to more systemwide information. This player takes the optimization results of the individual players and determines a search direction and step length that achieve a cost decrease for the overall system. This player is often known as a coordinator. The main challenge of this approach is that the design of the coordinator may not be significantly simpler than the design of the centralized controller. This issue remains a topic of current research.
