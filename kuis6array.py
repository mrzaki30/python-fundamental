# - Variabel array bernama "var_array" dengan nilai dari 0 hingga 100.
# - Hitung nilai rata-rata dari elemen array tersebut.
# - Simpan hasil perhitungan dalam variabel bernama "result".


var_array = [i for i in range(101)]
# var_array.append(i)
# print(var_array)

result = sum(var_array) / len(var_array)

print(result)
