#Namų darbas
#Duoti trys kintamieji
skaicius = 5
trupmeninis_skaicius = 5.8
tekstas = "\"Labas rytas\""

#Taikant type() ir id() funkcijas galima atspausdinti šių kintamųjų vertes, tipus ir adresus atmintyje
print(f'Kintamojo "skaicius" vertė = "{skaicius}", tipas = "{type(skaicius)}", o adresas = "{id(skaicius)}"')
print("*" * 80)
print(f'Kintamojo "trupmeninis_skaicius" vertė = "{trupmeninis_skaicius}", tipas = "{type(trupmeninis_skaicius)}", o adresas = "{id(trupmeninis_skaicius)}"')
print("*" * 80)
print(f'Kintamojo "tekstas" vertė = {tekstas}, tipas = "{type(tekstas)}", o adresas = "{id(tekstas)}"')
print("*" * 80)

#Patobulinkite pateiktą kodo atkarpą taip, kad šie duomnys būtų spausdinami pateikiant aiškų ir rišlų tekstą
#(atkreipkite dėmesį, kad norint atspausdint sibolį ", jis nurodomas su pasvyruoju brūkšneliu \")
#rezultatas tururėtų atrodyti taip:"

"""
Kintamojo "skaičius" vertė = "5", tipas = "<class 'int'>", o adresas = "140722714909240"
********************************************************************************
Kintamojo "trupmeninis_skaicius" vertė = "5.8", tipas = "<class 'float'>", o adresas = "2458351086704"
********************************************************************************
Kintamojo "tekstas" vertė = "Labas rytas", tipas = "<class 'str'>", o adresas = "2458355027056"
********************************************************************************
"""