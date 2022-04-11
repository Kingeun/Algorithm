# 트리 만들기
class TreeNode() :
	def __init__ (self) :
		self.left = None
		self.data = None
		self.right = None


# 전위 순회
def preorder(node):
  print(node.data, end='')
  if node.left != '.':
    preorder(tree[node.left])
    #print(tree[node.left])
  if node.right != '.':
    preorder(tree[node.right])

# 중위
def inorder(node):
  if node.left != '.':
    inorder(tree[node.left])
  print(node.data, end='')
  if node.right != '.':
    inorder(tree[node.right])

def postorder(node):
  if node.left != '.':
    postorder(tree[node.left])
  if node.right != '.':
    postorder(tree[node.right])
  print(node.data, end='')

n = int(input())
tree = {}
#트리 생성하는 과정
for _ in range(n):
  node,left,right=input().split()
  tree[node]=TreeNode()

  tree[node].data=node
  tree[node].left = left
  tree[node].right = right


preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
