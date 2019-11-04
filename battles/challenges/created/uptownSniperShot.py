draft2 = """

*Credits: @kov -- original challenge idea*
*@danielhong35 -- graphics and reference solution*

The *Freedom Fighting Force* armed and enlisted you to take out the corrupt, pro-*surreptitious surveillance* senator who has been unlawfully receiving benefits from big corporations in order to pass a controversial new law.

The senator will be giving a speech tomorrow at 1100 hours in Central Park. The *FFF* has satellites and drones at its disposal, and will provide you all the required intel for you to successfully assassinate the senator using a sniper rifle.

FFF intel defined the origin, `(x = 0, y = 0, z = 0)`, of the three-dimensional space around the senator as the point on the ground between his feet. In this coordinate system, `+x` is the direction pointing East, `+y` points North, and `+z` points up to the sky.

The senator is 2 meters and a few centimeters tall and standing on a platform 3 meters tall, so your target is the point `(0, 0, 5)`.

The owner of the nearby luxury *Hermetian Hotel* secretly supports your cause and is granting you access to a room on **any floor above the `4`th floor** (where you're less likely to get caught). Each floor of the hotel is `5` meters tall (ignoring the thickness of each floor's ground material).

Being an American building, the floor at street level is called the first floor (number `1`), occupying heights from `0` up to but not including `5` meters. The z-coordinates `5` &le; `z` &lt; `10` are on floor `2`, and so on. At first glance, the hotel appears to be the tallest building of the city.

FFF will provide you the satellite data for the hotel building and every nearby building that might block the sniper shot.

Every building in the vicinity is a rectangular prism, whose walls are all parallel to the `x` and `y` axes. In addition, the planes formed by their roofs are all parallel to the ground plane.

For the hotel, you will be given an array of floats `[x, y, length, width]`, where `x` and `y` are the coordinates of the **center of its perimeter rectangle**, `length` is the size of the wall parallel to the `x`-axis, and `width` the size parallel to the `y`-axis. Satellite data for its height is fuzzy.

For the remaining buildings, the intel is a matrix of floats `[x, y, length, width, height]`, where the first four variables are the same as those described for the hotel, and the `height` is how tall it is.

The hotel's rooms have ample windows and you may adjust the rifle's position so that effectively you have a clear shot from anywhere in the hotel's perimeter. 

In addition, the sniper rifle is so powerful that at the given distances, effects of gravity and air resistance are negligible. 

What is the lowest floor you can be in and still assassinate the senator? 

__Example__

"""

draft = """

PRIVATE
https://app.codesignal.com/challenge/LmSw5tHnCZS4JmhCz 

*Credits: @kov -- original challenge idea*
*@danielhong35 -- graphics and reference solution*

The *Freedom Fighting Force* armed and enlisted you to take out the corrupt, pro-*surreptitious surveillance* senator who has been unlawfully receiving benefits from big corporations in order to pass a controversial new law.

The senator will be giving a speech tomorrow at 1100 hours in Central Park. The *FFF* has satellites and drones at its disposal, and will provide you all the required intel for you to successfully assassinate the senator using a sniper rifle.

FFF intel defined the origin, `(x = 0, y = 0, z = 0)`, of the three-dimensional space around the senator as the point on the ground between his feet. In this coordinate system, `+x` is the direction pointing East, `+y` points North, and `+z` points up to the sky.

The senator is 2 meters and a few centimeters tall and standing on a platform 3 meters tall, so your target is the point `(0, 0, 5)`.

The owner of the nearby luxury *Hermetian Hotel* secretly supports your cause and is granting you access to a room on **any floor above the fourth floor** (where you're less likely to get caught). Each floor of the hotel is `5` meters tall (ignoring the thickness of each floor's ground material).

Being an American building, the floor at street level is called the first floor (number `1`), occupying heights from `0` up to but not including `5` meters. The z-coordinates `5` &le; `z` &lt; `10` are on floor `2`, and so on. At first glance, the hotel appears to be the tallest building of the city.

FFF will provide you the satellite data for the hotel building and every nearby building that might block the sniper shot.

Every building in the vicinity is a rectangular prism, whose walls are all parallel to the `x` an `y` axes. In addition, the planes formed by their roofs are all parallel to the ground plane.

For the hotel, you will be given an array of floats `[x, y, length, width]`, where `x` and `y` are the coordinates of the **center of its perimeter rectangle**, `length` is the size of the wall parallel to the `x`-axis, and `width` the size parallel to the `y`-axis. Satellite data for its height is fuzzy.

For the remaining buildings, the intel is a matrix of floats `[x, y, length, width, height]`, where the first four variables are the same as those described for the hotel, and the `height` is how tall it is.

The hotel's rooms have ample windows and you may assume the corner's size is negligible. The sniper rifle is so powerful that at the given distances, effects of gravity and air resistance are negligible.

You may pick any spot from any window to shoot from. What is the lowest floor you can be in and still assassinate the senator?


__Example__

"""

description = """

*Credits: @kov -- original challenge idea*
*@danielhong35 -- graphics and reference solution*

The *Freedom Fighting Force* armed and enlisted you to take out the corrupt, pro-*surreptitious surveillance* senator who has been unlawfully receiving benefits from big corporations in order to pass a controversial new law.

The senator will be giving a speech tomorrow at 1100 hours in Central Park. The *FFF* has satellites and drones at its disposal, and will provide you all the required intel for you to successfully assassinate the senator using a sniper rifle.

FFF intel defined the origin, `(x = 0, y = 0, z = 0)`, of the three-dimensional space around the senator as the point on the ground between his feet. In this coordinate system, `+x` is the direction pointing East, `+y` points North, and `+z` points up to the sky.

The senator is 2 meters and a few centimeters tall and standing on a platform 3 meters tall, so your target is the point `(0, 0, 5)`.

The owner of the nearby luxury *Hermetian Hotel* secretly supports your cause and is granting you access to a room on **any floor above the fourth floor** (where you're less likely to get caught). Each floor of the hotel is `5` meters tall (ignoring the thickness of each floor's ground material).

Being an American building, the floor at street level is called the first floor (number `1`), occupying heights from `0` up to but not including `5` meters. The z-coordinates `5` &le; `z` &lt; `10` are on floor `2`, and so on. At first glance, the hotel appears to be the tallest building of the city.

FFF will provide you the satellite data for the hotel building and every nearby building that might block the sniper shot.

Every building in the vicinity is rectangular, whose walls are all parallel to the `x` an `y` axes. In addition, the planes formed by their roofs are all parallel to the ground plane.

For the hotel, you will be given an array of floats `[x, y, length, width]`, where `x` and `y` are the coordinates of the **center of its perimeter rectangle**, `length` is the size of the wall parallel to the `x`-axis, and `width` the dimension parallel to the `y`-axis. Satellite data for its height is fuzzy.

For the remaining buildings, the intel is a matrix of floats `[x, y, length, width, height]`, where the first four variables are the same as those described for the hotel, and the `height` is how tall it is.

The hotel's rooms have ample windows and you may assume the walls corner's width is negligible. Given that you may pick any spot from any window to shoot from, what is the lowest floor you can be in and still assassinate the senator?

__Example__

"""

def uptownSniperShot(hotel, buildings):
    pass
