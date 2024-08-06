import requests
import re
import os
import time

# 使用时间戳作为文件名称
def get_time():
    timestamp = int(time.time())
    return timestamp

# 实现从网页图片保存到本地，输入为图片网址和保存路径
def image_save(image_url, path):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            image_name = f"推文封面{get_time()}.jpg"
            save_path = os.path.join(path, image_name)  # 指定图片保存路径
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f'图片已保存为: {save_path}')
        else:
            print(f'下载图片失败，状态码: {response.status_code}')
    except Exception as e:
        print(f'下载图片时发生错误: {e}')

# 微信公众号获取封面并保存，输入网址
def get_image(wechat_url):
    try:
        response = requests.get(wechat_url)
        if response.status_code == 200:
            source_code = response.text
            url_pattern = re.compile(r'var msg_cdn_url = "(.*?)";')
            matches = url_pattern.findall(source_code)
            if matches:
                print("封面图片URL: ", matches[0])
                # 获取当前脚本文件所在目录
                current_dir = os.path.dirname(os.path.abspath(__file__))
                # 将图片保存在脚本所在目录下
                image_save(matches[0], current_dir)
            else:
                print("未找到封面图片URL.")
        else:
            print(f'获取网页失败，状态码: {response.status_code}')
    except Exception as e:
        print(f'请求网页时发生错误: {e}')

if __name__ == "__main__":
    while True:
        print("微信公众号推文封面提取工具v1.0")
        print("作者：Cchong_dada")
        print("！！请确保运行本软件的设备已联网！！")
        print("  ")
        # 从用户获取目标网页的URL
        url = input("请输入微信公众号文章的URL: ")
        get_image(url)
        # 询问用户是否继续
        cont = input("是否继续提取封面图片？(y/n): ")
        if cont.lower() != 'y':
            break
