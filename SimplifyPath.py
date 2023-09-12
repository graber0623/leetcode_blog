path1 = "/home/"
path2 = "/../"
path3 = "/home//foo/"

# print(path1.split("/"))
# print(path2.split("/"))
# print(path3.split("/"))

def simplifyPath(path):
    path_list = path.split("/")
    print(path_list)
    remover = ["",".",".."]
    for dirname in path_list:
        if dirname in remover:
            path_list.remove(dirname)
    print(path_list)
    res = "/" + "/".join(path_list)
    print("========")
    return res

print(simplifyPath(path1))
print(simplifyPath(path2))
print(simplifyPath(path3))

a = [".."]

