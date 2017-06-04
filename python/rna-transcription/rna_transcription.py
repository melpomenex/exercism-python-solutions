def to_rna(dna):
    return "".join([{"G":"C","C":"G","T":"A","A":"U"}.get(a,a) for a in dna])
