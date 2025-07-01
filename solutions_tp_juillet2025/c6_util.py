def traduire_rgb_fr_en(s):
    match(s):
        case "rouge" :
            return "red"
        case "vert" : 
            return "green"
        case "bleu" : 
            return "blue"
        case _ : 
            return "?"
        
def traduire_rgb_en_fr(s):
    match(s):
        case "red" :
            return "rouge"
        case "green" : 
            return "vert"
        case "blue" : 
            return "bleu"
        case _ : 
            return "?"        

