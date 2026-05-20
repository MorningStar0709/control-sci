# 14.11 Problems

Problem 14.1 Figure 14.9 shows a single-loop analog feedback system. The plant is

![](image/754d664ef94fb6498c4eebad784f0598c3a0ee0e920245266081197ac5bc5f36.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    w1 --> o(( ))
    o --> e --> F --> o --> y --> K --> u --> P --> end
    w2 --> e2 --> F --> o --> K --> P
    z1 --> W
    w2 --> ε2 --> K --> u --> P
    z2 --> ε1 --> P
    end
    w1 --> o
    e --> o
    y --> o
    u --> o
```
</details>

Figure 14.9: Analog feedback system

P and the controller $K ; F$ is an antialiasing filter for future digital implementation of the controller (it is a good idea to include $F$ at the start of the analog design so that there are no surprises later due to additional phase lag). The basic control specification is to get good tracking over a certain frequency range, say $[ 0 , \omega _ { 1 } ]$ ; that is, to make the magnitude of the transfer function from $w _ { 1 }$ to e small over this frequency range. The weighted tracking error is $z _ { 1 }$ in the figure, where the weight W is selected to be a lowpass filter with bandwidth $\omega _ { 1 }$ . We could attempt to minimize the $\mathcal { H } _ { \infty }$ norm from w1 to $z _ { 1 }$ , but this problem is not regular. To regularize it, another input, $w _ { 2 } .$ , is added and another signal, $z _ { 2 } ,$ is penalized. The two weights $\epsilon _ { 1 }$ and $\epsilon _ { 2 }$ are small positive scalars. The design problem is to minimize the $\mathcal { H } _ { \infty }$ norm

$$
\text {   from   } w = \left[ \begin{array}{l} w _ {1} \\ w _ {2} \end{array} \right] \text {   to   } z = \left[ \begin{array}{l} z _ {1} \\ z _ {2} \end{array} \right].
$$

Figure 14.9 can then be converted to the standard setup by stacking the states of $P , F ,$ and W to form the state of $G .$

The plant transfer function is taken to be

$$P (s) = \frac {2 0 - s}{(s + 0 . 0 1) (s + 2 0)}.$$

With a view toward subsequent digital control with $h = 0 . 5$ , the filter $F$ is taken to have bandwidth $\pi / 0 . 5$ , and Nyquist frequency $\omega _ { N } \mathbf { \Omega }$ :

$$F (s) = \frac {1}{(0 . 5 / \pi) s + 1}.$$

The weight W is then taken to have bandwidth one-fifth the Nyquist frequency:

$$W (s) = \left[ \frac {1}{(2 . 5 / \pi) s + 1} \right] ^ {2}.$$

Finally, $\epsilon _ { 1 }$ and $\epsilon _ { 2 }$ are both set to 0.01.

Run hinfsyn and show your plots of the closed-loop frequency responses.
