zero_dim_pt = """
You're Romanaldo, the Brazilian soccer star famous for the ability to kick impossible curve balls into the goal. In front of you are Armando, the giant Argentinian goalie, and several defenders forming a wall. Can you score your free kick? The fans will go wild!

![pitch diagram](https://i.imgur.com/eAkw0Xb.png)

(Note: the diagram is NOT to the scale of the actual problem)

After watching dozens of replay videos, you and your coach noticed that the curve of your free kicks may be closely modeled as an arc of an ellipse.

### Modeling the kick

* for simplicity, the ball is represented as a zero-dimensional point

* Armando will block anything to your left that's not covered by the wall (in other words, the segment of the goal line between the left goal post, from your point of view, and the point directly above the wall's left endpoint)

* the kick will count as a goal if the ball touches the segment of the goal line not covered by Armando. It is not required to surpass this line segment (in real soccer, the entire ball must cross the goal line, but we are only estimating, for simplicity)

* the initial ball position will always be located at the lowermost point (vertex) of an ellipse

* your body will face the goal straight on, so the long axis of the ellipse is perfectly perpendicular to the goal line

* your kick will make the ball initially move to the right, then curve to the left

### The defense

* The defenders' wall will always stand perfectly horizontally and may be modeled as a line segment. If the ball touches any point of the wall, it is deflected up and above the goal, going out of bounds (and disappointing the fans).

### Given measurements (all distances in meters)

* The open width of the goal is `7.3 meters` wide. 

* the coordinates `ballLocation`, is given as an array of floats `[x, y]`

* where `x` is the perpendicular horizontal distance between the ball and the imaginary vertical line extending from the goal's left post (from your point of view)

* and where `y` is perpendicular vertical distance between the ball and the goal line

* the coordinates `wallLeftEnd` marking the defenders' wall left endpoint is given as an array of floats `[x, y]`

* where `x` is the perpendicular horizontal distance from the goal's left post (as described above)

* and where `y` is the perpendicular vertical distance from the goal line.

* the length `wallLength` indicates how long the wall is

Your task is to determine whether there's at least one possible kick to score a goal. You should output `true` or `false`.

__Input / Output__
"""

first_submission = """
You are Romanaldo, the star Brazilian soccer player famous for your uncanny ability to kick curveballs. In front of you are Armando, the giant Argentinian goalie, and several defenders forming a wall. Can you score your free kick?

![pitch diagram](https://i.imgur.com/eAkw0Xb.png)

(Note: the diagram is NOT to the scale of the actual problem)

After watching dozens of replay videos, you and your coach noticed that the curve of your free kicks may be closely modeled as an arc of an ellipse.

### Modeling the kick

* the initial ball position will always be located at the lowermost point (vertex) of the ellipse. 

* you kick best when facing the goal straight on, so the long axis of the ellipse is perfectly perpendicular to the goal line. 

* your kick will make the ball move to the right at first then curve towards the left.

### The defense

* The goalie is a beast and will block anything on his side of the goal (to the left of the wall).

* The defenders' wall will always stand perfectly horizontally and may be modeled as a line segment. They can only jump up, but will deflect any ball that touches them.

### Scoring

* The entire ball must cross the goal line between the goal posts for it to count.

* The ball's edge must clear the defenders' wall completely to enter the goal. A deflected ball is assumed to fly up above the goal and out.

### Given measurements (all distances in meters)

* Regulation requires the ball to have a diameter of `0.2 meters`, and the open width of the goal to be `7.3 meters` wide. 

* the coordinates `ballLocation`, as the array of floats `[x, y]`

* where `x` is the perpendicular horizontal distance between the ball's center and the imaginary vertical line extending from the goal's left post

* where `y` is perpendicular vertical distance between the ball's center and the goal line

* the coordinates `wallLeftEnd` marking the defenders' wall left endpoint, as the array of floats `[x, y]`

* where `x` is the perpendicular horizontal distance from the goal's left post 

* where `y` is the perpendicular vertical distance from the goal line.

* the length `wallLength` indicating how long the wall is

Your task is to determine whether there's at least one possible curve to score a goal. You should output `true` or `false`.


Input/Output

output: Whether Romanaldo can score a clean goal from his curveball kick


"""

first_draft_description = """

You are Romanaldo, the star Brazilian soccer player famous for your uncanny ability to curve your free kicks.

goal
+-----------+
|           |
 ____    \
 goalie   \
           \
      ----  |
    defense |
           /
          / 
         /
      (R)

After watching dozens of replay videos, you and your coach noticed that the curve of your free kicks may be closely modeled as an arc of an ellipsoid.

Assume the ball has a diameter of 0.2 meters, and that the entire ball must cross the goal line for it to count. Your kick starts at one extreme of an ellipsoid. The axis may be slanted. The ball is represented as a zero-dimensional point, and the goalie range and defender wall as line segments.

Given the range of the goalie and the position of the defenders (as line segments), determine whether there is a possible curved free kick that will score a goal. 
"""
