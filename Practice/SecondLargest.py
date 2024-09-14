def Second_largest(List):
    if len(List) < 2:
        return None
    else:
        List.sort(reverse=True)
        return List[1]

print("Enter List:")
List = map(int , input().split())
List = list(set(List))


print(Second_largest(List))