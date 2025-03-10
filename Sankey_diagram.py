import plotly.graph_objects as go

fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=["A", "B", "C", "D", "E", "F"],
        color=["blue", "green", "red", "cyan", "magenta", "yellow"]
    ),
    link=dict(
        source=[0, 1, 0, 2, 3, 3],
        target=[2, 3, 3, 4, 4, 5],
        value=[8, 4, 2, 8, 4, 2]
    )
))

fig.update_layout(title_text="Sankey Diagram", font_size=10)
fig.show()
