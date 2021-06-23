# %% 初始化
import requests
from datetime import datetime


host = "https://zuowei.lib.swjtu.edu.cn"

urls = {
    'login': host + '/api.php/login',
    'floor': host + '/api.php/areas/{}',
    'time': host + '/api.php/space_time_buckets',
    'area': host + '/api.php/spaces_old',
    'book': host + '/api.php/spaces/{}/book',
}

UA = 'Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) ' \
     'Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045008 Mobile Safari/537.36 MMWEBID/2220 ' \
     'MicroMessenger/7.0.8.1540(0x27000834) '

floors = [2, 3, 4, 5]  # 楼层

areas = {
    2: [
        6,   # 2-B1
        7,   # 2-B2
    ],
    3: [
        8,   # 3-A1-大厅
        9,   # 3-A2
        21,  # 3-A3
        10,  # 3-B2
        11,  # 3-B3
    ],
    4: [
        12,  # 4-A1-大厅
        14,  # 4-B1-大厅
        15,  # 4-B2
        22,  # 4-B3
        23,  # 4-C
    ],
    5: [
        16,  # 5-A1-大厅
        18,  # 5-B1
        19,  # 5-B2
    ],
}  # 区域


# %% 查询所有空闲座位
time_now = datetime.now()

for floor in floors:
    for area_id in areas.get(floor):
        response_area = requests.get(
            urls['area'],
            params={
                'area': area_id,
                'day': time_now.strftime('%Y-%m-%d'),
                'startTime': time_now.strftime('%H:%M'),
                'endTime': '22:30',
            },
        )
        free_seats = response_area.json()['data']['list']
        free_seats = map(
            lambda seat: {
                'area_id': seat['area'],
                'area_name': seat['area_name'],
                'seat_id': seat['id'],
                'seat_name': seat['name'],
            },
            filter(
                lambda seat: seat['status'] == 1,
                free_seats
            )
        )
        for seat in free_seats:
            print(seat)
        print()

# %% 预定指定座位
username = "0000123456"  # 用户名
password = "123456"  # 密码
seat_id = 444  # 座位ID (犀浦校区图书馆-3层-3-A2-014)
area_id = 9  # 区域ID (犀浦校区图书馆-3层-3-A2)

"""
2楼:
    6:  2-B1
    7:  2-B2
3楼:
    8:  3-A1-大厅
    9:  3-A2
    21: 3-A3
    10: 3-B2
    11: 3-B3
4楼:
    12: 4-A1-大厅
    14: 4-B1-大厅
    15: 4-B2
    22: 4-B3
    23: 4-C
5楼:
    16: 5-A1-大厅
    18: 5-B1
    19: 5-B2
"""

user_session = requests.session()
response_login = user_session.get(
    urls['login'],
    params={
        'username': username,
        'password': password,
        'from': 'mobile',
    },
    headers={
        'user-agent': UA,
    },
)

if response_login.json().get('status') == 1:
    print("登录成功")
    response_time = requests.get(
        urls['time'],
        params={
            'day': datetime.now().strftime('%Y-%m-%d'),
            'area': area_id,
        },
    )
    response_book = user_session.post(
        urls['book'].format(seat_id),
        data={
            **response_login.json()['data']['_hash_'],
            'segment': response_time.json()['data']['list'][0]['bookTimeId'],
            'type': 1,
        },
    )
    response_book_json = response_book.json()
    print(response_book_json.get('msg'))
    if response_book_json.get('status') == 1:
        spaceInfo = response_book_json['data']['list']['spaceInfo']
        print("%s-%s" % (spaceInfo['areaInfo']['nameMerge'], spaceInfo['name']))
else:
    print(response_login.json().get('msg'))
