import plotly.plotly


class Plotter:

    def __init__(self, parser):
        self.parser = parser

    def plot(self, data):
        x_list = []
        y_list = []
        for session in self.parser.sessions:
            x_list.append(session.startTime.strftime("%d.%m."))
            y_list.append(session.)


    def duration_per_session(self):
        print("Plotting...")
        x_list = []
        y_list = []
        for session in self.parser.sessions:
            x_list.append(session.startTime.strftime("%d.%m."))
            y_list.append(round(session.duration/60))
        data = [plotly.graph_objs.Bar(
            x=x_list,
            y=y_list)]
        plotly.offline.plot(data, filename="plot.html")
        print("Plotting successful")

