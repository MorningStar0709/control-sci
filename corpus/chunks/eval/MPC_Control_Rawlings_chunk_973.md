# C.1 Dynamic Programming

The name dynamic programming dates from the 1950s when it was coined by Richard Bellman for a technique for solving dynamic optimization problems, i.e., optimization problems associated with deterministic or stochastic systems whose behavior is governed by differential or difference equations. Here we review some of the basic ideas behind dynamic programming (DP) Bellman (1957); Bertsekas, Nedic, and Ozdaglar (2001).

To introduce the topic in its simplest form, consider the simple routing problem illustrated in Figure C.1. To maintain connection with optimal control, each node in the graph can be regarded as a point $( x , t )$ in a subset S of $X \times T$ where both the state space $X = \{ a , b , c , \ldots , g \}$ and the set of times $T = \{ 0 , 1 , 2 , 3 \}$ are discrete. The set of permissible control actions is $\mathbb { U } = \{ U , D \}$ , i.e., to go “up” or “down.” The control problem is to choose the lowest cost path from event $( d , 0 )$ (state d at $t ~ = ~ 0 )$ to any of the states at $t \ = \ 3$ ; the cost of going from one event to the next is indicated on the graph. This problem is equivalent to choosing an open-loop control, i.e., a sequence $\{ u ( 0 ) , u ( 1 ) , u ( 2 ) \}$ of admissible control actions. There are $2 ^ { N }$ controls where N is the number of stages, 3 in this example. The cost of each control can, in this simple example, be evaluated and is given in Table C.1.

There are two different open-loop optimal controls, namely {U,D,U} and $^ { \{ \mathrm { ~ D , D , D } \} }$ , each incurring a cost of 16. The corresponding state trajectories are $\{ d , e , d , e \}$ and $\{ d , c , b , a \}$ .

<table><tr><td>control</td><td>UUU</td><td>UUD</td><td>UDU</td><td>UDD</td><td>DUU</td><td>DUD</td><td>DDU</td><td>DDD</td></tr><tr><td>cost</td><td>20</td><td>24</td><td>16</td><td>24</td><td>24</td><td>32</td><td>20</td><td>16</td></tr></table>

Table C.1: Control Cost.

![](image/07f55bcdb8e7c717e7758d23a92250c6d4b2b7622fc64aca1270034a97c12a16.jpg)

<details>
<summary>radar</summary>

| i | a | b | c | d | e | f | g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 8 | 4 | 8 | 0 | 8 | 16 | 4 |
| 1 | 8 | 4 | 8 | 0 | 8 | 16 | 4 |
| 2 | 8 | 4 | 8 | 0 | 8 | 16 | 4 |
| 3 | 4 | 4 | 8 | 0 | 8 | 16 | 4 |
</details>

Figure C.1: Routing problem.
