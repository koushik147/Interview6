class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = [] # creating the resultant array
        hashmap= defaultdict(list) # creating the default hashmap of list
        q = deque() # creating a deque
        q.append((root,0)) # append the deque with root

        while q: # run until the q
            size=len(q) # assinging the size with length of q
            level=[] # creating the level array
            for _ in range(size): # run until the size popping the q and store it in node and v
                node,v = q.popleft()
                hashmap[v].append(node.val) # append the node value in the hashmap
                if node.left: # if left then append to node left 
                    level.append((node.left,v-1)) 
                if node.right: # if right then append to node right
                    level.append((node.right,v+1))
            level.sort(key = lambda x: (x[1], x[0].val)) # sorting the level with the node's value
            q = deque(level) # assigning the deque level
        hashmap = OrderedDict(sorted(hashmap.items())) # assigning the ordereddict of sorted hashmap items
        for k,v in hashmap.items():
            result.append(v) # run until the dictionary and append the result

        return result # returning the result