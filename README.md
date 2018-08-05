# runtastic data plotter
## What is this?
A python-scripts that parses your runtastic-data into an easy accesible format and lets you create cool and customizable </br>
diagrams! You feed it your runtastic-data, tell it what to use and voilà, a custom diagram!
## How does it work?
When you export your runtastic data it comes in JSON-files, each for one session. The script parses the the data into python. </br>
Then it uses the plot.ly python library to create a diagram with the data you want. The `Plotter.py` class wraps the plotly </Br>
functions into a simple to use format, combining them with your runtastic-data.
## How do I set it up?
At first you need to get your runtastic data! Therefore you go on the runtastic-website, log-in, go to settings and export your data.
Because this script uses plotly, you need to install the plotly-python-library (https://plot.ly/d3-js-for-python-and-pandas-charts/) </br>
## How do I use it?
Take a look into the `ExampleMain.py`! 
* If you create an own script, make sure you dont forget the imports!
* Create a new Parser with `parser = Parser("/Path/to/the/Sport-sessions/directory")` with giving it the path to the directory
where the Sport-sessions directory lies. If the script lies in the same directory as 'Sport-sessions' you can leave the path empty 
like 'parser = Parser()'
* initialize the parser with `parser.initialize_sport_sessions()`
* create a new plotter with `plotter = Plotter(parser)`
* create a new bar-graph with `my_bar_graph = plotter.bar_graph("my_data")`
* create a new line-graph with `my_line_graph = plotter.line_graph("my_data")`
##### make sure to check out the next paragraph on what to put into `"my_data"` !
* if you want to create a diagram you need to call `plotter.plot(my_list_of_graphs, "Title of My Plot", "X-Axis-Title", "Y-Axis-Title")`
As you see, the function takes a **List** of Graphs, not a single graph! That means you can put as many graphs as you want in 
one diagram! Of course you can also just put one graph into the list:-)
* Now just run `ExampleMain.py` (or your script) with `python3 ExampleMain.py` in your console!
#### If you didn't mess up, now a `plot.html` will have appereared in your browser and in your directory containing your diagram!
But don't worry, if you made a mistake just check the console, there might be printed what exactly you did wrong!
## What do I put into `plotter.bar_graph("my_data")`?
the functions `line_graph()` `and bar_graph()` take one or two strings as arguments:
* putting only one argument in `line_graph("calories")` will create a diagram mapping the **calories** on the y-Axis and each
sport-session on x-Axis
* putting two arguments in `line_graph("duration", "calories")` will create a diagramm with the first argument (**duration**)
as y-Axis and the second argument (**duration**) as x-Axis </br>
As you can see, that leaves it completely open, what correlations between your runtastic data you want to display! 
Cool, isn't it? </br>
## But what is this data, you're talking about all the time?
When you create a graph with `plotter.bar_graph("my_data")` you need to give the data you want to use. This data is all
about your sport-session, like you see them in the runtastic-app. This means the "my_data" string can be:
* date
* start_time 
* end_time 
* distance 
* duration
* elevation_gain
* elevation_loss
* average_speed
* calories
* longitude
* latitude
* max_speed
* pause_duration
* pulse_avg
* pulse_max
* avg_cadence
* max_cadence
* manual
* edited
* completed
* indoor
* session_id
* sport_type_id
## It's not working!
Make sure to check the console as most activity and occuring errors will pop up there! Make sure to take a look at the 
`ExampleMain.py` and check if your syntax follows the given examples or my explanation here!
## Contact me!
If you cant find your mistake, want to suggest improvements, found mistakes, or want to chat a bit feel free to write me a mail
or a message! I'm still new to coding so any feedback is appreciated;-)
