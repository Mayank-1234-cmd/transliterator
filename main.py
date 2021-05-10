import f1
def transliterate(lang1,lang2,text):
  #all use hindi unicode as name
  table=f1.jsondct()
  for i in range(0,len(table[lang1]["names"])):
    try:
      replsfrom=table[lang1]["symbols"][i]
      replsto=table[lang2]["symbols"][i]
      text=text.replace(replsfrom,replsto)
    except Exception as e:
      pass
  return text
print(transliterate("Devanagari","Sinhala","कख"))#return क2ख2
# works


