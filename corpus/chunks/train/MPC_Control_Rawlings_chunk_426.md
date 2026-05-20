![](image/0cc27e8e62487029593c9995c890bf92d7b3f5cf3622fa19342209351ef583b2.jpg)

<details>
<summary>line</summary>

| t | x(t) | z(t) |
| --- | --- | --- |
| 0 | 1.0 | 1.0 |
| 100 | 0.3 | 0.4 |
| 200 | 0.25 | 0.25 |
| 300 | 0.25 | 0.25 |
| 400 | 0.25 | 0.25 |
| 500 | 0.25 | 0.25 |
</details>

Figure 3.8: Concentration versus time for the ancillary controller for sample time 12 (top) and 8 (bottom).

It is also possible to tune the sample time of the ancillary controller. This feature may be useful when the disturbance frequency lies outside the pass band of the central path (nominal) controller. Figure 3.8 shows how concentration varies with time when the disturbance is $w ( t ) ~ = ~ 0 . 0 0 2 \sin ( 0 . 4 t )$ , the sample time of the central path controller is 12 whereas the sample time of the ancillary controller is 12 (top figure) and 8 (bottom figure). The central path controller employs $\ell ( z - z _ { e } , \nu - \nu _ { e } )$ , and the ancillary controller employs $\ell ( x , u )$ where $\ell ( x , u ) : = ( 1 / 2 ) ( | x | ^ { 2 } + u ^ { 2 } )$ . The ancillary controller with the smaller sample time is more effective in rejecting the disturbance. -
