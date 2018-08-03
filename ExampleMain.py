from Parser import Parser
from Plotter import Plotter

parser = Parser()
parser.initialize_sport_sessions()
plotter = Plotter(parser)
plotter.duration_per_session()
