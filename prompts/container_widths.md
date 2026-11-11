

\- Always replace deprecated use\_container\_width with width: use width="stretch" if use\_container\_width=True, and width="content" if use\_container\_width=False, across all Streamlit components (st.dataframe, st.data\_editor, st.image, st.pyplot, st.plotly\_chart, st.button, st.download\_button, st.link\_button, st.graphviz\_chart). For st.altair\_chart specifically, set chart sizing via Altair (e.g., chart.properties(width='container')) since st.altair\_chart does not accept width.

