# Chaos_Game
A simple implementation of the chaos game in pygame.

# How Does Chaos Game work?
1. **Choose Starting Points:**
   - Decide on a set number of starting points and place them within a chosen geometric shape. Commonly, a triangle is used as the initial shape.

2. **Initialize a New Point:**
   - Add a new point to the canvas. In the traditional Chaos Game, this point is often placed randomly, but in this implementation, it is initially set to the center of the screen.

3. **Randomly Select a Starting Point:**
   - Randomly choose one of the starting points.

4. **Move the New Point:**
   - Move the newly added point towards the randomly selected starting point by a certain percentage. The usual percentage is 50%, which means moving halfway towards the chosen starting point.

5. **Repeat:**
   - Repeat last 2 steps.
