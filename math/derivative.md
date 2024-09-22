- Not a instantaneous rate of change but require multiple points in time (at least 2)
- Let s(t) = distance traveled at t where t is time in seconds
- let v(t) = velocity at time t
- What is the relationship between v(t) and s(t)? How does velocity depend on a distance function
- Velocity at a single momment doen't make sense
- Velocity = change in distance / change in time = (s(t+x) - s(t)) / dt = ds / dt
- We want to associate a single point in time with a velocity but actually compute it requires atleast two points in time
- The speedometer measure how far the car goes in a very small amount of time to has enough information to derive the velocity
- So the derivative of a function is just another function that represent the approximate rate of change of it's output at specific point. let's start with a simple example: f(x) = x^2, f'(x) = 2x the derivative of f(x) is telling us that rate of change of f(x) = y is a function g(x) = 2x. So when we make a tiny change to x, y will be
increased/decreased by 2x*dx. Let's test with x = 2 and dx = 0.01, rate of change of y = 2x = 4, dx = 0.01 -> 
dy = 4*0.01 = 0.04. This is fuckin true: f(x+dx) = f(2.01) = 4.0401