import plotly.plotly


class Plotter:

    number_of_plots = 0

    def __init__(self, parser):
        self.parser = parser
        self.sessions = parser.sessions

    def match_data(self, data, data2):
        x_list = []
        y_list = []
        for session in self.sessions:
            if data not in session.data:
                print("Error: " + data + " is no property of session!")
                return
            elif data2 not in session.data:
                print("Error: " + data2 + " is no property of session!")
            x_list.append(session.data[data2])
            y_list.append(session.data[data])
        return x_list, y_list

    def plot(self, graphs, title, x_axis, y_axis):
        layout = plotly.graph_objs.Layout(
            title=title,
            xaxis=dict(title=x_axis),
            yaxis=dict(title=y_axis)
        )
        figure = plotly.graph_objs.Figure(data=graphs, layout=layout)
        plotly.offline.plot(figure, filename="plot" + str(Plotter.number_of_plots) + ".html")
        Plotter.number_of_plots += 1

    def line_graph(self, data, data2="date"):
        x_list, y_list = self.match_data(data, data2)
        return plotly.graph_objs.Scatter(x=x_list, y=y_list)

    def bar_graph(self, data, data2="date"):
        x_list, y_list = self.match_data(data, data2)
        return plotly.graph_objs.Bar(x=x_list, y=y_list)



