pets = {
    'brutus': {
        'species': 'labra',
        'owner': 'anna',
        'age': 3,
    },
    'bruno': {
        'species': 'sheperd',
        'owner': 'anand',
        'age': 8,
    },
    'sheru' : {
        'species' : 'pug', 
        'owner' : 'Soap',
        'age' : 5,

    }
}
for name, info in pets.items():
    print(f"\n Pet name - {name.title()}")
    jaat = f"Species-{info ['species']}"
    parent = f"Owner-{ info ['owner']}"
    umr = f"Age- {info ['age']}"
    print(jaat.title())
    print(parent.title())
    print(umr.title())
    

