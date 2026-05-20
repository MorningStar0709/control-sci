# 9.6 Can AI design a PID controller? (New, Spring 2025)

This is what we all want to know right now, right?

Let's try this with the design problem of Example 14 (Page 154). We will try a series of prompts rather than drop the problem in all at once. We'll just go ahead and write out the rst part to orient Claude.ai to the fact we are using python, what modules we import, etc. We thus start with:

Prompt 1 Could you please complete the following python code to perform the Root Locus analysis? (which is followed immediately in the same prompt with the code of Listing 9.1).

Claude.ai generates additional code which produces:

![](image/cb9b781db490dbcede99816be542666866b01fce6fd504feb413626aa487ac3a.jpg)

<details>
<summary>radar</summary>

| Real Axis | Imaginary Axis |
| --- | --- |
| 0 | 0 |
| 15 | 0.34 |
| 30 | 0.50 |
| 45 | 0.64 |
| 60 | 0.77 |
| 75 | 0.87 |
| 90 | 0.94 |
</details>

Pretty cool! Let's mark this up with performance regions. The next prompt is:

Thank you. Could you revise that to add lines to the plot which indicates 10% overshoot, and settling time <= 8 sec.?

Claude.ai generates additional code which produces:

![](image/52d5f173e8ea4cee47fd55f9a6f6bde54e51c8445115430fd55431c2cc4ab0ef.jpg)

(Note the relevant poles and zeros are kind of tiny and the red-dashed settling time line is barely visible). Next we ask it to x the issues identied above:

Prompt 3 Thank you, The overshoot line looks good but there are spurious lines in the plot legend. Also, can you change the plotting axes to focus on the poles and zeros of magnitude less than 20?

Claude.ai generates additional code which produces:

![](image/ed53becd5233605ace44e3a3267cc7e1b51257697fd57c73232c7ae3f797d514.jpg)

The problem here is that our specications are equality constraints, not inequalities. We need to get our dominant poles to the interesection of the diagonal dashed line (percent overshoot) and the vertical dashed red line (Ts) and it's too hard to see.

Prompt 4 Since my performance specs are equality constraints, I want the diverging poles to go near or through the intersection of the Ts and percent overshoot lines. Can you modify the controller for that? Also, please further zoom to focus on that point.

Claude.ai generates additional code which produces:

![](image/e5c9a492e18e7a5d8a953fe46209a0da5eea58a0293efbfd7851d57400c8b270.jpg)

<details>
<summary>radar</summary>
