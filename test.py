from collections import deque

from utils import Node


# def dfs(grid, row, col, visit):
#     row_len, collen = len(grid), len(grid[0])
#
#     if min(row, col) < 0 or row == row_len or col == collen or grid[row][col] == 1 or (row, col) in visit:
#         return 0
#     if row == row_len - 1 and col == collen - 1:
#         return 1
#
#     visit.add((row, col))
#
#     count = 0
#
#     count += dfs(grid, row + 1, col, visit)
#     count += dfs(grid, row, col + 1, visit)
#     count += dfs(grid, row - 1, col, visit)
#     count += dfs(grid, row, col - 1, visit)
#
#     # visit.remove((row, col))
#     return count
#
#
# a = [
#     [0, 0, 0, 0],
#     [0, 1, 0, 0],
#     [0, 1, 0, 1],
#     [1, 0, 0, 0]
# ]
# print(dfs(a, 0, 0, set()))

# def dp(rows, cols):
#     prev_row = [0] * 4
#
#     for i in range(rows - 1, -1, -1):
#         cur_row = [0] * cols
#         cur_row[cols - 1] = 1
#         for j in range(cols - 2, -1, -1):
#             cur_row[j] = cur_row[j + 1] + prev_row[j]
#         prev_row = cur_row
#     return prev_row[0]
#
#
# print(dp(4, 4))

# root_ = Node(27)
# root_.insert(30)
# root_.insert(0)
# root_.insert(26)
# root_.insert(4)
# root_.insert(0)
# heap = Heap()
# print(heap.push(24))
# print(heap.heapify())

# url = "https://blinkit.com/feed/?template_version=9"
#
# payload = {}
# headers = {
#     'lat': '23.1090643329249',
#     'lon': '72.5715186777276',
#     'auth_key': 'c761ec3633c22afad934fb17a66385c1c06c5472b4898b866b7306186d0bb477',
#     'app_client': 'consumer_web',
#     'access_token': None,
#     'accept': '*/*',
#     'accept-encoding': 'gzip, deflate, br',
#     'app_version': '52434332',
#     'platform': 'desktop_web',
#     # 'cookie': 'gr_1_deviceId=d9413d09-423f-4ef4-82e8-77d49a3fc89d; city=Ahmedabad; __cfruid=958d09f8eaaa2cb5738383cdc9cbd300b8649267-1675012644; _cfuvid=FITBxc6SCWFOZWtz8O.sh8TEb2JIbGD1jjAQ4.5Ur3U-1675012644070-0-604800000; rl_anonymous_id=%22feb81469-d604-4801-86eb-462947e3d602%22; rl_user_id=%22%22; gr_1_lat=23.1090643329249; gr_1_lon=72.5715186777276; gr_1_locality=959; gr_1_landmark=undefined; _gcl_au=1.1.1472119973.1675012646; _ga=GA1.2.1859722734.1675012647; _gid=GA1.2.1802873942.1675012647; _fbp=fb.1.1675012647018.1195449692; __cf_bm=w7rIeHVjuR42jGIK.iIVs49Ai7ucm6ywF9E7pHjBXKo-1675013612-0-AU8dwVIQ4S9L1Xrmw6RRLOuegf4f+BHKbR/sIc39kySs8WA+0QptiRby20PZyv/pfrca/+5puUdHSCjUHG5H5Zc=; AWSALBTG=WMwkl1FVbwAx1m0M9+gkSt81ozWgHSM/ZLAdVWGvWqn3JIF7RWV7YT19wvwRTnoZoWxDZuP0nGcS9KuWoNXiNfdITgM5cRFTRLE1M2ghLdNnDErKTCW4DCZK1dXbguJglL6XZQbA1Zlgzaqmo53/fHdaOyd98mi257FQXfAqJwzy; rl_trait=%7B%22device_uuid%22%3A%22d9413d09-423f-4ef4-82e8-77d49a3fc89d%22%2C%22session_uuid%22%3A%2203595d4f-6792-4d8b-9522-32d2cf79cbfb%22%2C%22install_source%22%3A%22%22%2C%22install_campaign%22%3A%22%22%2C%22phone%22%3Anull%2C%22email%22%3A%22%22%2C%22cart_id%22%3Anull%2C%22rn_bundle_version%22%3A%229.3.12%22%2C%22platform%22%3A%22desktop_web%22%2C%22segment_type%22%3Anull%2C%22monthly_orders%22%3Anull%2C%22city_id%22%3A959%2C%22chain_id%22%3A1383%2C%22longitude%22%3A72.5715186777%2C%22user_type%22%3Anull%2C%22lifetime_orders%22%3Anull%2C%22latitude%22%3A23.1090643329%2C%22city_name%22%3A%22Ahmedabad%22%2C%22merchant_id%22%3A29861%2C%22merchant_name%22%3A%22Super%20Store%20-%20Ahmedabad%20Chandkheda%20ES1%22%7D'
# }
#
# response = requests.request("GET", url, headers=headers)
#
# print(response.status_code)


# certificate_url = "https://www.udemy.com/api-2.0/users/me/certificates/?course=2648040"
# https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https://www.udemy.com/mobile/ipad/


def printSubSequences(STR, subSTR=""):
    """
    function:
        To print all subsequences of string
        concept:
            Pick and Don’t Pick
        variables:
            STR = string
            subSTR = to store subsequence
    """
    if len(STR) == 0:
        print(subSTR, end=" ")
        return
    a = STR[:-1]
    b = subSTR + STR[-1]
    # we add adding 1st character in string
    printSubSequences(a, b)
    c = STR[:-1]

    d = subSTR
    # print(c, d)
    printSubSequences(c, d)
    return

f = "pwwkew"
printSubSequences(f)
char = set()
print("=======")
print("f", f)
for i in f:
    print(i)
    char.add(i)


