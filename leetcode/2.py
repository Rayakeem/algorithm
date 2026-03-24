#node 구현
class Node:
  def __init__(self, value=0, next=None):
    self.value = value
    self.next = next

#연결리스트 구현
class LinkedList(object):
  def __init__(self):
    self.head = None

  def append(self, value) :
    new_node = Node(value)

    if self.head is None:
      self.head = new_node

    else:
      current = self.head
      while(current.next):
        current = current.next
      current.next = new_node

#연결리스트 중간에 노드 추가 insertAt(idx, value)

  def insert(self, idx, value):
    new_node = Node(value)

    #맨 앞에 넣는 경우
    if(idx == 0):
      new_node.next = self.head
      self.head = new_node
      return
    
    #중간에 넣는 경우
    current = self.head
    current_idx = 0

    while current and current_idx < idx-1 :
      current = current.next
      current_idx += 1

      if current:
        new_node.next = current.next
        current.next= new_node

      else:
            print("인덱스가 리스트 범위를 벗어났습니다.")