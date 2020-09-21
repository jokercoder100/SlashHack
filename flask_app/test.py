import pydgraph

client_stub = pydgraph.DgraphClientStub('https://shaky-vacation.us-west-2.aws.cloud.dgraph.io/graphql')
client = pydgraph.DgraphClient(client_stub)
schema = 'name: string @index(exact) .'
op = pydgraph.Operation(schema=schema)
client.alter(op)