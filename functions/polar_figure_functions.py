import plotly.graph_objects as go



def create_polar_plot(sequence: List[int]):
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r = [3] * len(sequence),
        theta = [x+(360/len(sequence)) for x in range(len(sequence))],
        mode = 'lines',
        name = 'Test',
        line_color = 'violet'
    ))
    fig.update_layout(rotation = 90)

