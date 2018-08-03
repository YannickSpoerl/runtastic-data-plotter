from Parser import Parser
from Plotter import Plotter

parser = Parser()
parser.initialize_sport_sessions()
plotter = Plotter(parser, "My runtastic plot")
plotter.line_plot("duration")
plotter.double_line_plot("duration", "average_speed")
