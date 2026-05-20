![](image/d0af1caa76ea8448fb9cef49e5b552be3545645db0b7e0b1b370e3cc0c6e1188.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    y_d --> Fd
    Fd --> sum((+))
    sum --> u
    y_m --> -Fd
    -Fd --> sum
```
</details>

or

![](image/bf368483b766ecfc1b5f45fc1b55c4f3ccc097db26e0d0d51451a28bd63ed335.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    y_d --> Fd
    Fd --> sum((+))
    sum --> u
    Fm --> sum
    sum --> y_m
```
</details>

(d)

![](image/f777d2cc7185ea6608e727cddf5bed7ee2af35b1def351bbeeda9a9ccebb6fe5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    y_d["y_d"] --> adder["+"]
    adder --> F_d["F_d"]
    F_d --> u["u"]
    y_m["y_m"] --> adder
    adder --> y_m
```
</details>

(c)   
Figure 4.3 Control configurations: a) Open loop; b) Feedforward; c) Feedback, one degree of freedom; d) Feedback, two degrees of freedom

![](image/83c741d5f6f26052d2d33b418f396577731e472cb51dab084bed1584c97af34d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    yd --> Fd
    Fd --> add1["+"]
    add1 --> u
    u --> P
    P --> add2["+"]
    add2 --> y
    y --> Ps
    Ps --> add3["+"]
    add3 --> ym
    ym --> Fm
    Fm --> add1
    Fw --> Pw
    Pw --> w
    w --> Fw
    Fw --> add2
    Fm --> add2
    add2 --> y
```
</details>

Figure 4.4 Block diagram for a linear control system

where

$$H _ {d} = \text { set point to output closed - loop transfer function }H _ {w} = \text { disturbance to output closed - loop transfer function }H _ {v} = \text { sensor noise to output closed - loop transfer function. }$$

The error, defined as $\mathbf{e} = \mathbf{y}_d - \mathbf{y}$ , satisfies

$$\mathbf {e} (s) = [ I - H _ {d} (s) ] \mathbf {y} _ {d} (s) - H _ {w} (s) \mathbf {w} (s) - H _ {v} (s) \mathbf {v} (s). \tag {4.6}$$

The transfer functions $H_{d}$ , $H_{w}$ , and $H_{v}$ depend on the transfer functions of Equations 4.1, 4.3, and 4.4, associated respectively with the plant, the sensors, and the controller. The functional relationship depends on the controller structure. It is precisely this dependence that makes the study of different control schemes important and interesting. The design problem is to obtain $H_{d}$ , $H_{w}$ , and $H_{v}$ with desirable properties via an appropriate controller design, i.e., by choosing the structure and dynamics of the controller.

In cases where it is convenient to work with d, the disturbance referred to the output, rather than with w, Equation 4.5 is replaced by
