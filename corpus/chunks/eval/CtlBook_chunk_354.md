$$K _ {m a x} = r K _ {m i n} \tag {10.1}$$

This method is illustrated below with respect to the nominal (center) value.

![](image/621971dcfd424fe62c82775327c96a990e3e978199607f15f96f04b588328bf1.jpg)

<details>
<summary>text_image</summary>

P_{2MAX}
P_2
SEARCH
REGION
P_{2MIN}
Best
Search Result
True Optimum
P_{1MAX}
P_{1}
</details>

Figure 10.2: Search range does not contain the true optimum of the function and nds a minimum in one corner.

![](image/daa067a79fb791951a8fce6c1c0466bcaa09717e11fb79a11768e6b836adc642.jpg)

<details>
<summary>text_image</summary>

factor of r
NOM.
Nominal
√r(Nom)
</details>

Other search range methods are possible but note that this approach will never generate negative gain values (which are not allowed for PID controllers anyway).

It can be tricky to know a good initial value for the gains $K _ { p } , K _ { i } , K _ { D }$ . Depending on the problem they can range from much less than 1 to hundreds. One computer-only approach, is to start your search over a wide range and then narrow it down on subsequent searches. However this takes many optimization runs to nd a good answer. A better approach is to do a rough manual PID design (Section 9.5.1). The result of your manual design is a good starting point.

Search size Next we choose how many discrete values we will try within the search range for each of the three gains, N vals. The number of simulations we must run is then $N v a l s ^ { 3 } .$ . My computer can do about 500-1000 simulations per minute in python.
