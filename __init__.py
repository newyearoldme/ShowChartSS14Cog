from .showchartss14cog import ChartCog

def setup(client):
    client.add_cog(ChartCog(client))