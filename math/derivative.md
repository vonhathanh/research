- Not a instantaneous rate of change because it requires multiple points in time (at least 2)
- Let s(t) = distance traveled at t where t is time in seconds
- let v(t) = velocity at time t
- What is the relationship between v(t) and s(t)? How does velocity depend on a distance function
- Velocity at a single momment doen't make sense
- Velocity = change in distance / change in time = (s(t+x) - s(t)) / dt = ds / dt
- We want to associate a single point in time with a velocity but actually compute it requires atleast two points in time
- The speedometer measure how far the car goes in a very small amount of time to has enough information to derive the velocity
- In pure math, the derivate is not a specific dt like 0.01, 0.0001
- ds(t)/dt = (s(t+dt) - s(t)) / dt, it's what ever approaches zero
- As dt approaches zero, the two points approach each other, the slope the line approach the tangent line of the graph at a single point
- dt is not infinitely small, not 0, it's just approaches zero
- derivative is best constant approximation for a rate of change around a point
- Let say s(t) = t^3, we have ds(t)/dt = ((t + dt)^3 - (t)^3) / dt
- Expend the term we got: 3t^2 -> this is derivative of s(t) around a point t in time 
- So the derivative of a function is just another function that represent the approximate rate of change of it's output at specific point. let's start with a simple example: f(x) = x^2, f'(x) = 2x the derivative of f(x) is telling us that rate of change of f(x) = y is a function g(x) = 2x. So when we make a tiny change to x, y will be
increased/decreased by 2x*dx. Let's test with x = 2 and dx = 0.01, rate of change of y = 2x = 4, dx = 0.01 -> 
dy = 4*0.01 = 0.04. This is fuckin true: f(x+dx) = f(2.01) = 4.0401
