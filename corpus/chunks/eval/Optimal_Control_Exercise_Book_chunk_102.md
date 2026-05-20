ax.set_ylabel(r'Value')
ax.set_title(r"Control input $u(t)$ plot")
fig.savefig('image/boeing_input.jpg')

![](image/7fc075221bea6d6ebe0fc0b958e9f07c683949ba72ddf0fc2d2ff3f96f413a9b.jpg)

<details>
<summary>line</summary>

| Time [s] | u(t) |
| --- | --- |
| 0.0 | 0.62 |
| 2.5 | -0.15 |
| 5.0 | -0.05 |
| 7.5 | 0.03 |
| 10.0 | 0.01 |
| 12.5 | 0.00 |
| 15.0 | 0.00 |
| 17.5 | 0.00 |
| 20.0 | 0.00 |
</details>

As we can see from the graphs, the LQR controller is able to stabilize the output and bring it to a stable state within the time span we set. Moreover, as we expected, the control input satisfies the condition that lim $\mathsf { \iota } _ { t \to \infty } u ^ { * } ( t ) = 0$ and also zeroes out the output in the steady state.
