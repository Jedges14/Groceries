#real time API keys can be used to 
INVENTORY = {
    
    'cheese': 15, 'rice': 23, 'skimmed milk': 5, 'pie': 7.5, 'egg': 2.5, 'wheat': 4.75, 'salmon': 6.0,'spice': 1.65, 'honey': 4.8, 'oil': 15, 'lean meat': 35.75
}

# -----  CHECKOUT FUNCTIONS  ----- #



W={}
 
def clerk_checkout():
    '''Reutrns input in subtotals and gives a final receipt of all inputs'''
    subtotal=0
    while True:
        B=input('>').lower()
        if B=='end cart':
            break
        
        if B in INVENTORY:
            inventory_value=INVENTORY[B]
            subtotal +=inventory_value
            print(f'subtotal: ${subtotal:.2f}')
            if B in W:    #CHECKING IF INPUT ALREADY EXISTS IN THE DICTIONARY WE ARE CREATING
                W[B]+=1 
            else:
                W[B]=1 
        else:
            pass
            #print(f'Sorry we do not have your item: {B}')
            
    print('-----------RECEIPT-----------')
    
    for r,q in W.items():
        T=float(INVENTORY[r])
        quantity=q*T
        print(f' {r}   {q}   ${quantity:.2f}')

    print(f'Total ${subtotal:.2f}')
    
    return
        

F={}      
def express_checkout():
    '''returns a receipt after all list have been entered'''
    grocery=input('>').lower()
    L=grocery.split(", ") #splits input after a comma. There should be whitespace after the comma.
    
    if len(L)>10:
        L=L[:10]           
    for item in L:
        if item not in INVENTORY:
            pass
        else:
            F[item]=L.count(item)
    print('--------------RECEIPT--------------')
    count=0
    for s,k in F.items():
        Y=float(INVENTORY[s])
        qt=k*Y
        count+=qt
        print(f' {s}   {k}   ${qt:.2f}')
     

    
    print(f'Total: ${count:.2f}')
    
    return    
    

# MAIN CODE

def main():
    Entery_question= input('Hello, dear customer, which method of checkout would you like? [clerk or express]: ').lower()
    while True:
        if Entery_question=='clerk':
            clerk_checkout()
            
        if Entery_question=='express':
            express_checkout()
            
        else:
            print('Sorry we only do "express" and "clerk" checkouts')
        
        return



# calls the main function
if __name__ == "__main__":
    main()