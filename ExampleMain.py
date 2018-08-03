from Parser import Parser
from Plotter import Plotter

parser = Parser()
parser.initialize_sport_sessions()
plotter = Plotter(parser)
graphs = list([plotter.bar_graph("duration")])
graphs.append(plotter.line_graph("calories"))
plotter.plot(graphs, "Example-Plot", "date", "duration/ calories")
