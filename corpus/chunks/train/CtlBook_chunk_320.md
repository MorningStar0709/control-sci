# Deriving $K _ { P } , K _ { I } , K _ { D }$ from controller zeros

Using the root locus technique we'll get insights about where to place the two poles of the PID controller. We'll outline the procedure below without a specic plant and we'll repeat the procedure with a specic plant in the upcoming examples.

There are several identical forms of the PID controller including:

$$C _ {P I D} (s) = K _ {D} \left(s ^ {2} + \frac {K _ {P}}{K _ {D}} s + \frac {K _ {I}}{K _ {D}}\right) \frac {1}{s}$$

which is also

$$C _ {P I D} (s) = K _ {D} \left(s + \frac {K _ {P}}{K _ {D}} + \frac {K _ {I}}{K _ {D}} \frac {1}{s}\right) = K _ {D} s + K _ {P} + \frac {K _ {I}}{s} \tag {9.10}$$

First, in the design process, from our specications we must dene the regions of the s-plane where second order response satises our requirements (Section 9.3.1). Recall that the performance target could be a region (inequality requirements) or a point (equality requirements).

Assuming that we use a PID controller, we can place two zeros in the s-plane to get the plant's root locus to move where we want it (we also add the PID controller's required pole at $( s = 0 )$ . Thus we focus on the form:

$$C _ {P I D} = \frac {K _ {D} (s + z _ {1}) (s + z _ {2})}{s}$$

At the end, our design will consist of numerical values for the three parameters, $K , z _ { 1 } , z _ { 2 }$

For the two zeros, we will initially guess places for them based on the intuition (developed in this chapter's exercises and examples) that zeros will pull the closed-loop poles towards themselves (often helpfully to the left on the complex plane).

Once we have chosen the zeros (two real zeros or a pair of CC zeros), and we place the required pole at $s = 0 ,$ we rely on Root Locus analysis to choose K.

To start o, let's assume we studied a plant and that zero locations we like are

$$z _ {i} = (s + 1. 7 \pm 0. 5 j)$$

(again, we'll develop intuition on this shortly).

Now we plot the root locus and plot the performance regions by hand or using software. Assuming the root locus goes through at least one location inside our performance region, 1) choosing a point, $p _ { d }$ on the root locus we like, 2) nding $K = K _ { D }$ by solving the magnitude condition:

$$\left| K C P H (s) \right| _ {s = p _ {d}} = 1$$

We solve this by either: 2a) plugging in and using

$$K = \frac {1}{| C P H (s) | _ {s = p _ {d}}}$$

or 2b) plotting by computer and clicking on the desired point in the root locus graph to read o K.

Suppose solving or clicking as above gives $K _ { D } = 1 . 8 5$ . Multiplying out the two CC PID zeros gives

$$C (s) = \frac {K _ {D} (s + 1 . 7 + 0 . 5 j) (s + 1 . 7 - 0 . 5 j)}{s} = \frac {1 . 8 5 (s ^ {2} + 3 . 4 s + 3 . 1 4)}{s}$$

Multiplying and rearranging,

$$C _ {P I D} (s) = 1. 8 5 s + 6. 2 9 + \frac {5 . 8 0 9}{s} = 6. 2 9 + \frac {5 . 8 0 9}{s} + 1. 8 5 s$$

Matching coecients with Equation 9.10 gives us

$$K _ {P} = 6. 2 9 \quad K _ {I} = 5. 8 0 9 \quad K _ {D} = 1. 8 5$$
