def chop(set):
    del set[0]
    del set[-1]
    
def middle(set):
    newSet = set[1:-1]
    return newSet

orgSet = [2, 4, 6, 8, 10, 12]
dupeSet = [2, 4, 6, 8, 10, 12]
chopSet = chop(orgSet)
midSet = middle(dupeSet)

print(orgSet)
print(chopSet)
print(dupeSet)
print(midSet)