import plotly.plotly


class Plotter:

    number_of_plots = 0

    def __init__(self, parser):
        self.parser = parser
        self.sessions = parser.sessions

    def match_data(self, y_data, x_data):
        x_list = []
        y_list = []
        for session in self.sessions:
            if y_data not in session.data:
                print("'" + y_data + "' is no property of session! ")
                return None, None
            elif x_data not in session.data:
                print("'" + x_data + "' is no property of session!")
                return None, None
            x_list.append(session.data[x_data])
            y_list.append(session.data[y_data])
        return x_list, y_list

    def plot(self, graphs, title, x_axis, y_axis):
        print("Plotting " + title + " ...")
        i = 0
        for graph in graphs:
            i += 1
            if graph is None:
                istr = str(i)
                print("Couldn't plot " + title + "! Object number " + istr + " in the list is not valid! Possible "
                                                 "Errors: \n-It is not a graph. \n-It is 'None'. \n-It was not "
                                                 "successfully created. Check for any other Errors in the console!")
                return
        layout = plotly.graph_objs.Layout(
            title=title,
            xaxis=dict(title=x_axis),
            yaxis=dict(title=y_axis)
        )
        figure = plotly.graph_objs.Figure(data=graphs, layout=layout)
        plotly.offline.plot(figure, filename="plot" + str(Plotter.number_of_plots) + ".html")
        Plotter.number_of_plots += 1
        print("Plotted " + title)

    def line_graph(self, y_data, x_data="date"):
        print("Creating new Line-Graph...")
        x_list, y_list = self.match_data(y_data, x_data)
        if x_list is None or y_list is None:
            print("Couldn't create Line-Graph.")
            return None
        print("Created new Line-Graph")
        return plotly.graph_objs.Scatter(x=x_list, y=y_list)

    def bar_graph(self, y_data, x_data="date"):
        print("Creating new Bar-Graph...")
        x_list, y_list = self.match_data(y_data, x_data)
        if x_list is None or y_list is None:
            print("Couldn't create Bar-Graph")
            return None
        print("Created new Bar-Graph")
        return plotly.graph_objs.Bar(x=x_list, y=y_list)



