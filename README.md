# Sequence Visualizer
Click [here](https://sequence-visualizer-caf8d1d828df.herokuapp.com/) to to to the dashboard.


### So, what is this?
This is a personal project I built simply because I was curious about the repreating patterns hidden within known numerical sequences.


### And, what am I seeing?
You are seeing a visualization of the repeating patterns that arise when dividing every number of a series by an integer and then taking the remainder. For example, if we look at the fibonacci sequence:
```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, ...
```
and divide each number by `3` and capture the remainder, we get :
```
0, 1, 1, 2, 0, 2, 2, 1, 0, 1, 1, 2, 0, 2, 2, 1, 0, 1, 1, 2, 0, 2, 2, 1, ...
```
The repeating sequence here is `0, 1, 1, 2, 0, 2, 2, 1`.

The polar figure will then display this pattern by drawing a line between each of the numbers. In this case it will place the `0` at the `0,360` position on the circle, and `1` at the `120` position and the `2` at the `240` position. All equidistant from eachother.


## Deployment
Used [these](https://dash.plotly.com/deployment?_gl=1*1wwiu1a*_gcl_au*NDE5NTAwNjcuMTcxODQ3ODM4MA..*_ga*MTM1MzkwODUzMC4xNzE4NDc4Mzgx*_ga_6G7EE0JNSC*MTcxODY1NDgyNS4yLjEuMTcxODY1NDg2OC4xNy4wLjA.) instructions for deployment using Heroku.
