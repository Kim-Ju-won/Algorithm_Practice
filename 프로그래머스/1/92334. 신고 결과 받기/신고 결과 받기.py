def solution(id_list, report, k):
    id_dict= dict()
    for Id in id_list : 
        id_dict[Id] = {
            "report":set(),
            "suspend":set(),
            "out":0
        }
    
    for case in report : 
        a, b = case.split()
        if b not in id_dict[a]["report"] :
            id_dict[a]["report"].add(b)
            id_dict[b]["out"] += 1
            
    for key in id_dict.keys():
        if id_dict[key]["out"] >= k : 
            for key2 in id_dict.keys():
                if key in id_dict[key2]["report"]:
                    id_dict[key2]["suspend"].add(key)
                    
    return [ len(id_dict[key]["suspend"]) for key in id_dict.keys()]