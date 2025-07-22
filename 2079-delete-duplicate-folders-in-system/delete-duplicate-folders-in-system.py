from collections import defaultdict

class Node:
    def __init__(self, val=""):
        self.val = val
        self.subFolder = ""
        self.children = {}

class Solution:
    def getNode(self, val):
        return Node(val)

    def insert(self, root, path):
        for folder in path:
            if folder not in root.children:
                root.children[folder] = self.getNode(folder)
            root = root.children[folder]

    def populateNodes(self, root, subFolderMap):
        subFolderPaths = []

        for childName, child in root.children.items():
            subFolderResult = self.populateNodes(child, subFolderMap)
            subFolderPaths.append((childName, subFolderResult))

        subFolderPaths.sort()
        completePath = "".join(f"({name}{path})" for name, path in subFolderPaths)

        root.subFolder = completePath
        if completePath:
            subFolderMap[completePath] += 1

        return completePath

    def removeDuplicates(self, root, subFolderMap):
        to_delete = []
        for childName, child in root.children.items():
            if child.subFolder and subFolderMap[child.subFolder] > 1:
                to_delete.append(childName)
            else:
                self.removeDuplicates(child, subFolderMap)

        for name in to_delete:
            del root.children[name]

    def constructResult(self, root, path, result):
        for childName, child in root.children.items():
            path.append(childName)
            result.append(list(path))
            self.constructResult(child, path, result)
            path.pop()

    def deleteDuplicateFolder(self, paths):
        root = self.getNode("/")
        for path in paths:
            self.insert(root, path)

        subFolderMap = defaultdict(int)
        self.populateNodes(root, subFolderMap)
        self.removeDuplicates(root, subFolderMap)

        result = []
        self.constructResult(root, [], result)
        return result

        