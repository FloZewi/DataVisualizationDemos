import plotly.graph_objects as go

fig = go.Figure(go.Sankey(
    arrangement = "fixed",
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["A", "B", "C", "D", "E", "F"],
      color = ["blue", "green", "red", "cyan", "magenta", "yellow"]
    ),
    link = dict(
      source = [0, 1, 1, 2, 3, 4, 5, 5, 4, 3], # indices correspond to labels
      target = [1, 2, 3, 3, 4, 5, 4, 2, 0, 1],
      value = [8, 4, 2, 8, 4, 2, 4, 4, 6, 4]
  )))

fig.update_layout(title_text="Chord Diagram (Sankey)", font_size=10)
fig.show()
