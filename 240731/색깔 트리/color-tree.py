Q = int(input())
tree = dict()

def cal(node):
    colors = {tree[node][2]}
    stack = []
    stack.extend(tree[node][1])
    while stack:
        if len(colors) == 5:
            break
        now = stack.pop()
        colors.add(tree[now][2])
        stack.extend(tree[now][1])
    return len(colors)**2


for i in range(Q):
    com = list(map(int, input().split()))
    if com[0] == 100:
        m_id, p_id, color, m_depth = com[1:]
        if p_id == -1:
            tree[m_id] = [-1, [], color, m_depth]
        else:
            first_par, par = p_id, p_id
            depth = 1
            while True:
                if tree[par][3] <= depth:
                    break
                if tree[par][0] == -1:
                    tree[m_id] = [first_par, [], color, m_depth]
                    tree[first_par][1].append(m_id)
                    break
                par = tree[par][0]
                depth += 1
    elif com[0] == 200:
        m_id, color = com[1:]
        stack = [m_id]
        while stack:
            now = stack.pop()
            tree[now][2] = color
            stack.extend(tree[now][1])
    elif com[0] == 300:
        m_id = com[1]
        print(tree[m_id][2])
    else:
        sum_value = 0
        for node in tree:
            sum_value += cal(node)
        print(sum_value)