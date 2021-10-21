# Logic - simple, quick to generate first and last names.
# code:
def _genName():
    import random
    
    # Girl - 1
    class F:
        names = ["marillia", "marine", "ana", "vitoria", "vivi", "surtada", "marcia", "juju", "karol", "karoline", "coralline", "sophia", "emily", "sofia", "sara", "alice", "jessica", "irelia", "issabella", "leticia", "isadora", "laura", "manu", "manuela", "luisa", "maria", "joselli"]
        subnames  = ["silva", "alckerman", "mendonca", "carlo", "uzumaki", "oliveira", "santos", "souza", "ferreira", "alves", "lima", "gomes", "ribeiro", "martins", "carvalho", "aumeida", "lopes", "soares", "fernandes", "vieira", "barbosa", "rocha", "dias", "naicimento", "nunes", "machado", "cardoso", "teixeira"]

    # Boy - 2
    class H:
        names = ["marcos", "mello", "adriel", "vitin", "victor", "surtado", "marcelo", "juliano", "klepsom", "carlao", "alisom", "sergio", "elo", "felipe", "diego", "renan", "kevim", "cass", "andre", "sueth", "jhon", "mayke", "diegao", "travis", "luis", "daniel", "otavio"]
        subnames  = ["silva", "alckerman", "mendonca", "carlo", "uzumaki", "oliveira", "santos", "souza", "ferreira", "alves", "lima", "gomes", "ribeiro", "martins", "carvalho", "aumeida", "lopes", "soares", "fernandes", "vieira", "barbosa", "rocha", "dias", "naicimento", "nunes", "machado", "cardoso", "teixeira"]

    # select
    if random.randint(1, 2) == 1:
        name = F.names[random.randint(0, len( F.names) - 1)]
        subname =  F.subnames[random.randint(0, len( F.subnames) - 1)]
        return f"{name} {subname}"

    else:
        name = H.names[random.randint(0, len( F.names) - 1)]
        subname = H.subnames[random.randint(0, len( F.subnames) - 1)]
        return f"{name} {subname}"
        
# Return only object with function
class genName:
    def __init__(self):
        self.gen = _genName