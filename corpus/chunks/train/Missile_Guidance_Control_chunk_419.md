# 5.6.2 Unguided Free-Fall Weapon Delivery

For unguided weapons (see also Section 5.6), such as free-fall bombs, delivery accuracy is affected by two categories of error sources: human errors and aircraft system errors. Their relationship is illustrated in Table 5.1. As shown, aircraft off-parameters error and aiming errors are both human-related, while platform error and weapon separation error are aircraft related. For computed deliveries, the aircraft off-parameters error is absent.

If the weapon is a free-fall bomb, a flat Earth approximation can be used to compute the time from launch to impact. The initial velocity of the weapon is assumed to be the velocity of the aircraft at launch of the bomb. The time required for the weapon to fall to the target’s altitude is computed based on the initial velocity and the force of gravity acting on the weapon. If the weapon is unable to traverse the distance in the horizontal plane to the target in the time required for the weapon to impact the target in the vertical plane, the weapon will fall short of the target. Once the weapon will at least reach the target, the launch will occur. The launch action will be performed on the target.

Table 5.1. Sources of Delivery Accuracy Errors

<table><tr><td>Delivery</td><td colspan="2">Human Errors</td><td colspan="2">Aircraft Errors</td></tr><tr><td>Manual</td><td>AircraftOff-Parameters</td><td>Aiming</td><td>Platform</td><td>WeaponSeparation</td></tr><tr><td>Computed</td><td></td><td>Aiming</td><td>Platform</td><td>WeaponSeparation</td></tr></table>

The time of impact with the target is computed as the time required for the weapon to traverse the distance to the target along a straight-line path. The velocity specified for the weapon is oriented directly along the straight-line path and is assumed constant. The intercept phase is scheduled at the computed intercept time.
