UA = 'Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) ' \
     'Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045008 Mobile Safari/537.36 MMWEBID/2220 ' \
     'MicroMessenger/7.0.8.1540(0x27000834) '

# host = "http://202.115.72.52"
host = "https://zuowei.lib.swjtu.edu.cn"

urls = {
    'login': host + '/api.php/login',  # 用户登录
    'floor': host + '/api.php/areas/{}',  # 获取区域信息
    'area_time': host + '/api.php/space_time_buckets',  # 获取可预约时间段
    'area': host + '/api.php/spaces_old',  # 获取空间预约信息
    'book': host + '/api.php/spaces/{}/book'  # 预约座位
}

ROTATION_TIME = 1  # 轮询间隔时间(单位: s)

areas = {
    2: [6, 7],
    3: [8, 9, 10, 11, 21],
    4: [14, 15, 22, 23, 12],
    5: [18, 19, 16]
}
