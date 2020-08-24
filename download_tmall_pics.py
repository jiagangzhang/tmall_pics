import requests
from bs4 import BeautifulSoup


def get_image_urls(tmall_url: str) -> [str]:
	resp = requests.get(tmall_url)
	soup = BeautifulSoup(resp.content, 'html.parser')
	img_url_list = []
	imgs = soup.find_all('img', attrs={'aria-label':'商品主图'})
	for i in imgs:
		src = i['src']
		if not (src.endswith('.jpg') or src.endswith('.webp')):
			try:
				src = i['data-src']
			except Exception as e:
				print('！！！！无法找到有效图片地址！！！！')
				print(f'当前<img> 为 {i}')
				raise e

		http_url = 'http:' + str(src)
		if http_url not in img_url_list:
			img_url_list.append(http_url)

	return img_url_list

def save_image(url: str, file_name: str):
	image = requests.get(url)
	with open(file_name, 'wb') as f:
		f.write(image.content)
		print(f'文件 {file_name} 保存成功')

def check_url_valid(url):
	import re
	pass

def main():
	tmall_url = input('输入天猫URL: ')
	file_prefix = input('输入图片文件名前缀: ')
	check_url_valid(tmall_url)
	images = get_image_urls(tmall_url)
	# image_length = len(images)
	for index, image in enumerate(images):
		file_name = f'{file_prefix}_{index+1}.jpg'
		save_image(image, file_name)


if __name__ == '__main__':
	main()