# Streamlit + Jupyter + Postgres

Very simple demonstration on how to set up a dashboard using `streamlit` by reading data from a Postgres database. It also provides another service that allows using Jupyter notebooks with the `%sql` magic to query the database and manipulate the output.

**Note:** This is just a demonstration (a very rough PoC), it is not intended to be used in production.

## Usage

```bash
docker-compose up
```

Then open http://localhost:8501/ to see the dashboard and http://localhost:8888/lab/workspaces/auto-S/tree/example.ipynb to see the example notebook.
