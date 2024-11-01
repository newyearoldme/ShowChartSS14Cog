from .chart import ChartCog

def setup(client):
    client.add_cog(ChartCog(client))