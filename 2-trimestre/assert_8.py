def pode_votar(idade): 
    if idade > 16:
        print("pode votar")
assert pode_votar(30) is True
assert pode_votar(15) is False  
assert pode_votar(16) is True   
assert pode_votar(17) is True   
