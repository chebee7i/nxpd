from nxpd.nx_pydot import to_pydot
def install_repr_png():
    import networkx as nx
    import StringIO 
    def getsvg(graph):
        G2 = to_pydot(graph)
        buf = StringIO.StringIO()
        G2.write(buf, prog='dot', format='png')
        return buf.getvalue()
    nx.Graph._repr_png_ = getsvg
    
install_repr_png()
