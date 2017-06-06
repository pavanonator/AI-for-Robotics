Project 1: Search in Pacman
===========================

Introduction
------------

In this project, you will implement generic search algorithms applicable to wide classes of problems. The course staff
has supplied an autograder which includes test cases based on small graphs to help you debug your implementations.
Once you have debugged on the graph based test cases, you can apply your search algorithm implementations to pacman to
help him find paths through his maze world.

The autograder can be invoked locally for you to grade your answers on your machine. This can be run with the command:

    python autograder.py

Questions
---------

**Question 1: Depth First Search (2 points)**

In this question, you will implement the depth-first search (DFS) algorithm in the depthFirstSearch function in search.py.

**Question 2: Breadth First Search (2 points)**

Implement the breadth-first search (BFS) algorithm in the breadthFirstSearch function in search.py.

**Question 3: Uniform Cost Search (2 points)**

While BFS will find a fewest-actions path to the goal, we might want to find paths that are "best" in other senses.
Uniform-cost graph search achieves this by allowing us to find optimal solutions while associating a distinct cost with
each action.

**Question 4: A* (3 points)**

Implement A* graph search in the empty function aStarSearch in search.py.

**Question 5: Corners (2 points)**

The real power of A* will only be apparent with a more challenging search problem. Like heuristics, search problem
implementations are not generic but are (or course) specific to the problem you are solving. Now, it's time to formulate
a new problem and design a heuristic for it.

Implement the CornersProblem search problem in searchAgents.py.

**Question 6: Heuristics (3 points)**

Implement a non-trivial, consistent heuristic for the CornersProblem in cornersHeuristic.

**Question 7: Eating All The Dots (4 points)**

Now we'll solve a hard search problem: eating all the Pacman food in as few steps as possible.

Fill in foodHeuristic in searchAgents.py with a consistent heuristic for the FoodSearchProblem. Depending on how few
nodes your heuristic expands, you'll get additional points.

**Question 8: Replanning (2 points)**

Sometimes, even with A* and a good heuristic, finding the optimal path through all the dots is hard. In these cases,
we'd still like to find a reasonably good path, quickly. In this section, you'll write an agent that always greedily
eats the closest dot. Implement the function findPathToClosestDot in searchAgents.py.

**Extra Credit (up to 2 points)**

Implement an ApproximateSearchAgent in searchAgents.py that finds a short path through the bigSearch layout.

Grades
------


    Question q1: 2/2
    Question q2: 2/2
    Question q3: 2/2
    Question q4: 3/3
    Question q5: 2/2
    Question q6: 3/3
    Question q7: 5/4
    Question q8: 2/2
    Question extra: 0/0
    -------------------
    Total: 21/20