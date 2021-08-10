def create_file_name(name):
  words = name.split(" ")
  new_words = list(map(lambda word : word.lower(), words))
  return f"{'_'.join(new_words)}.py"

print(create_file_name("Sorted Squared Array"))