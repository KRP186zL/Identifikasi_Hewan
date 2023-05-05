data = {
    'a': 10,
    'b': 25,
    'c': 5,
    'd': 35,
    'e': 20
}

max_value = max(data.values())
result = [key for key, value in data.items() if value == max_value]

print("Nilai integer terbesar adalah:", max_value)
print("Kunci dengan nilai integer terbesar adalah:", str(result))
