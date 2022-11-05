opelObj = {
    "marka": "Opel",
    "model": "Astra",
    "yil": 2022
}
#-> dictioanry listesi oluşturacaksan listsedeki elemanlaar arasına virgül koymayı unutma.

sonuc = opelObj["marka"]
sonuc = opelObj.get("marka")
#->.get()şeklinde yaptığımızı köşeli parantezle yapabiliriz.
print(sonuc)

for x in opelObj:
    print(x)

#Böyle yazdığımızda opelObj içindeki açıklanan terimleri bize verir(marka,model,yil)

for x in opelObj:
    print(opelObj[x])
#Böyle yazdığımızda bize value değerlerini verir(opel,astra,2022)

for x in opelObj.values():
    print(x)    

#Böyle de aynı value değerlerini bize verir.

for x,y in opelObj.items():
    print(x,y)

#->dictionary içindeki bütün itemleri görebiliriz.

opelObj.pop("marka")
print(opelObj) 
#-> opelObj içinden silmek istediğin itemi bu şekilde pop komutuyla silebilirsin.

opelObj.clear()
print(opelObj)
#-> opelObj içindeki her şeyi temizler.

opelObj.update({
    "marka": "Honda"
})
print(opelObj)
#-> update komutuyla dictionary içindeki bilgileri güncellleyebiliriz.

opelObj.update({
    "marka": "Honda",
    "renk": "Pembe"
})
print(opelObj)
#-> update komutuyla yeni bilgi de ekleyebiliriz.


