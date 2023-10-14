import altair as alt
from datetime import datetime
import streamlit as st


# TODO: get from env variables
conn = st.experimental_connection("postgresql", type="sql")

date_range = st.date_input(label="Filter date range", value=(
    datetime.fromisoformat("2023-09-01T00:00:00Z"),
    datetime.fromisoformat("2023-10-15T00:00:00Z"),
))

versions_df = conn.query(
    'SELECT DISTINCT(version) as version FROM measurements WHERE timestamp BETWEEN :start AND :end;',
    ttl="60s",
    params={
        "start": date_range[0],
        "end": date_range[1],
    }
)
version_filter = st.multiselect("Filter versions in selected time range", versions_df.version)


def get_data(start_date, end_date, versions):
    sql = 'SELECT * FROM measurements WHERE timestamp BETWEEN :start AND :end'
    params = {
        "start": start_date,
        "end": end_date,
    }

    if versions:
        sql += " AND version IN :versions"
        params["versions"] = tuple(versions)

    return conn.query(
        sql,
        ttl="30s",
        params=params,
    )


df = get_data(date_range[0], date_range[1], version_filter)

st.title("Performance by version (bar chart) [ms]")
st.bar_chart(df, x="version", y="value", color="value")

st.title("Performance by version (line chart) [ms]")
line_chart = alt.Chart(df).mark_line().encode(
    x='version',
    y='value',
)

scatter_chart = alt.Chart(df).mark_circle(size=150, opacity=0.7).encode(
    x='version',
    y='value',
    tooltip=('timestamp', 'value', 'version'),
)

chart = (line_chart + scatter_chart).properties(
    width=600,
    height=400
)
st.altair_chart(chart, use_container_width=True)

