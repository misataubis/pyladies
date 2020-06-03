retezec = input('Napiš řetězec.')
pozice = int(input('Napiš pozici, kde se máznak vyměnit.'))
znak = input ('Napiš znak, který se má změnit.')
cast_pred_znakem = retezec[:pozice]
cast_po_znaku = retezec[pozice+1:]

novy_retezec = cast_pred_znakem + znak + cast_po_znaku
print(novy_retezec)