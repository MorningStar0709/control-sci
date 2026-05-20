The value of the gravitational acceleration at aircraft altitude is input. In order to include the effects of gravitational variation with weapon altitude, a simple weighted-average gravity is computed for the weapon delivery solution. That is,

$$\bar {g} = g _ {h} + K _ {1} h, \tag {5.62}$$

where

$$\bar {g} = \text { weighted average gravitational acceleration },g _ {h} = \text { gravitational attraction at altitude } h,K _ {1} = \text { weighting constant } (= 5. 8 \times 1 0 ^ {- 7} \text { seconds } ^ {- 2}).$$

This computation takes place outside the integration loop as an initialization.

Manual Ballistics. Manual ballistics are used in lieu of automatic ballistics when the pilot enters values for weapon time of fall and weapon range via the fire control computer.

Predict Ahead Trajectory Integration. In order to display the 45◦ toss and level toss cues, predicted impact points are continuously computed in some modes. By predicting these release points and computing a weapon trajectory, the bomb range resulting from these predicted release points is known. Thus, the cues can be displayed when the target is within range.
