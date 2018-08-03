import plotly.plotly


class Plotter:

    number_of_plots = 0

    def __init__(self, parser, title="MyPlot"):
        self.parser = parser
        self.sessions = parser.sessions
        self.title = title

    def bar_plot(self, data, data2="date"):
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
        plot = [plotly.graph_objs.Bar(
            x=x_list,
            y=y_list)]
        layout = plotly.graph_objs.Layout(
            title=self.title,
            xaxis=dict(title=data2),
            yaxis=dict(title=data)
        )
        figure = plotly.graph_objs.Figure(data=plot, layout=layout)
        plotly.offline.plot(figure, filename="plot" + str(Plotter.number_of_plots) + ".html")
        Plotter.number_of_plots += 1

    def double_bar_plot(self, data, data2, data3="date"):
        x_list = []
        y_list_1 = []
        y_list_2 = []
        for session in self.sessions:
            if data not in session.data:
                print("Error: " + data + " is no property of session!")
                return
            elif data2 not in session.data:
                print("Error: " + data2 + " is no property of session!")
            elif data3 not in session.data:
                print("Error: " + data3 + " is no property of session!")
            x_list.append(session.data[data3])
            y_list_1.append(session.data[data])
            y_list_2.append(session.data[data2])
        plot = [plotly.graph_objs.Bar(
            x=x_list,
            y=y_list_1,
            name=data),
                plotly.graph_objs.Bar(
                    x=x_list,
                    y=y_list_2,
                    name=data2
                )]
        layout = plotly.graph_objs.Layout(
            title=self.title,
            xaxis=dict(title=data3),
            yaxis=dict(title=data + "/ " + data2)
        )
        figure = plotly.graph_objs.Figure(data=plot, layout=layout)
        plotly.offline.plot(figure, filename="plot" + str(Plotter.number_of_plots) + ".html")
        Plotter.number_of_plots += 1

    def line_plot(self, data, data2="date"):
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
        plot = [plotly.graph_objs.Scatter(
            x=x_list,
            y=y_list,
            mode="lines+markers",
            name=data
            )]
        layout = plotly.graph_objs.Layout(
            title=self.title,
            xaxis=dict(title=data2),
            yaxis=dict(title=data)
        )
        figure = plotly.graph_objs.Figure(data=plot, layout=layout)
        plotly.offline.plot(figure, filename="plot" + str(Plotter.number_of_plots) + ".html")
        Plotter.number_of_plots += 1

    def double_line_plot(self, data, data2, data3="date"):
        x_list = []
        y_list_1 = []
        y_list_2 = []
        for session in self.sessions:
            if data not in session.data:
                print("Error: " + data + " is no property of session!")
                return
            elif data2 not in session.data:
                print("Error: " + data2 + " is no property of session!")
            elif data3 not in session.data:
                print("Error: " + data3 + " is no property of session!")
            x_list.append(session.data[data3])
            y_list_1.append(session.data[data])
            y_list_2.append(session.data[data2])
        plot = [plotly.graph_objs.Scatter(
            x=x_list,
            y=y_list_1,
            mode="lines+markers",
            name=data),
                plotly.graph_objs.Scatter(
                    x=x_list,
                    y=y_list_2,
                    mode="lines+markers",
                    name=data2
                )]
        layout = plotly.graph_objs.Layout(
            title=self.title,
            xaxis=dict(title=data3),
            yaxis=dict(title=data + "/ " + data2)
        )
        figure = plotly.graph_objs.Figure(data=plot, layout=layout)
        plotly.offline.plot(figure, filename="plot" + str(Plotter.number_of_plots) + ".html")
        Plotter.number_of_plots += 1


