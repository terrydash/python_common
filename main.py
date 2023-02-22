from spacy import displacy
import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("the verify code should be qxe5 and CSI ID should be  150080 ,with these params i need a ticket to verify from SCOUT.")
action=""
app=""
csi_id=""
verify_code=""
num=len(doc)
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)    
    if token.text=="verify" and token.head.text=="ticket" :
        action="verify"
    elif token.text.lower()=="scout" and (token.pos_=="NOUN" or token.pos_=="PROPN"):
        app="scout"
    elif token.text.lower()=="csi"  and token.head.text.lower()=="id":
        find_csi=False
        print(111)
        for i in range(token.i,num-1):
            if doc[i].pos_=="NUM":
                csi_id=doc[i].text
                break
    elif token.text.lower()=="verify"  and token.head.text.lower()=="code":
        for i in range(token.i,num-1):            
            if doc[i].pos_=="AUX" and doc[i+1].pos_!="AUX" :
                verify_code=doc[i+1].text
                break

print(action,app,csi_id,verify_code)