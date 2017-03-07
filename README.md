# task

This project serves to demonstrate the ROS publisher-subscriber model. One node, the Runner, publishes its position (with error) on a sine curve to a topic. A second node, the Observer, subscribes to this topic and stores these positions. Once the Runner has published a full cycle, the Observer smooths the data and produces a plot.

## Building

*Note:* This project was built with the ROS Jade distribution, and depends on Python 2.7. 

In a [catkin workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace), clone the respository and run `catkin_make`.

```
$ cd ~/catkin_ws/src
$ git clone git@github.com:djmolo/task.git
$ cd ~/catkin_ws
$ catkin_make
$ source devel/setup.bash
```

## Testing

To start the nodes, run `rosrun task observer` and `rosrun task runner` somewhere in the workspace. The plot of the data will be saved as `graph.png` in whatever folder you ran the Observer from. If instead of saving the data you would prefer for it to be displayed as soon as it is produced, you may uncomment the relevant line in the `plot_smoothed_curve` function in `src/task/plotting.py`.

To run the included tests, in the root of the workspace where the project is located, run `catkin_make run_tests`.
