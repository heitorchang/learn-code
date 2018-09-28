description = """

NEW IDEA: You have to optimize sleep/alertness with time studied

Instead of coffee, you are taking an experimental drug that has different effects based on the minute 

Tomorrow's the dreaded *Algorithms 151* final exam! It's 2 AM and you're nearly falling asleep, but you have some coffee and candy bars to keep you awake.

You rate your alertness level from `0` (fallen asleep) to `100` (can take on any 4000+ coin challenge without breaking a sweat).

For every minute that passes, your alertness level drops by `1` point.

**Drinking coffee:**

* Raises your alertness level by `15` points 

* Takes `20` minutes to have its effect. Your machine needs to brew a fresh cup and the caffeine needs to hit your brain.

**Eating a candy bar:**

* Boosts your alertness level by `10` points

* Takes `15` minutes to have its effect. You have to eat it and digest it to get the sugar rush.

**Metabolic Behavior**

* You may eat candy and drink coffee at the same time, but consuming the same item before the previous one takes effect is ineffective.

* The effect of consuming coffee or candy is instantaneous once the required number of minutes have passed. However, if you fall asleep before the effect kicks in, you will not wake up.

* If your alertness level would have reached `0` at the exact minute a food's boost is supposed to take effect, you will remain awake with that food's (or combination's) boost level.

Given your **initial alertness level**, the number of coffee cups available and the number of candy bars you have, output the total number of minutes you can stay awake studying.

"""

constraints = """
How you rate your Alertness level, from 0 to 100

*Guaranteed constraints*

<code>0 &lt; initialAlertness &le; 100</code>
"""
