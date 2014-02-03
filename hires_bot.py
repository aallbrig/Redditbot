import praw
import requests
import time
import pyperclip
from pprint import pprint

user_agent = ("High resolution image post bot v0.1.  This bot searches google for higher resolution version of posted image.  By /u/sovietmukipz")
username = "higher_res_img_bot"
password = ""
r = praw.Reddit(user_agent=user_agent)
print "logging in..."
r.login(username, password)
print "login complete!"
def check_unread():
	# print "checking unread messages"
	pass

def get_subreddit_submissions():
	print "searching reddit"
	submissions = r.get_subreddit('militaryporn').get_hot(limit=4)
	return submissions

def search_google_image(url):
	headers = {'User-Agent':'	Mozilla/5.0 (Windows NT 6.1; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0',
							'Referer':'https://www.google.com/search?tbs=sbi:AMhZZiulL-YiyHYtT_1i5X_15dXfWCVmSf6kJrRoEwjB9bRw94SssgxHZ736hClkotw9Kai8mM3F9h-SUnesHBLPozjd1NS05TYnBDFT2GdiE3j_1NPeuZYd3pxTWkmzuAVMe9SjX7foHrGzrKyyTRAKhv3hQJuDYNrQl3r-lBTIH0K5urOfFWEcLO1sAwagnqjYYGFEa8pZuSfwwiC0cFRtMqXnlkpwpMAW569secTU3SBXj8XeGwN-y8rQ0gNQL59023KRDKd0jsdq6CvodvAa22KNg4ShYwl8APId8rSFxn_1b7MCTUK4XvxBu3sLYW4Lf8h-uTT3lbZ3eJOehqxFsBZi95nbQZFMdccRKtWJCYVVGzcw3RNCc4NFjsNV4m6O31W5CKMMtAhC8awrDgAi4dEddDMcxzCAIxSLJ4S5vkxQvi_1cRET3n73EELrC26Ei-0ww9IhACHKKTeQ8Jy8brW5cLI5eac-AXSOsXOXnP5NV9_1c7AO0sSNnnQ2z3QAshInGomaGiVoNyDQCur2FIAkN0UIfjwSDHKauU8qwdK29dOZKL9SZBmJPgSx4Bs-mj8vRw85N6RCGTBm7ctwApEtAIZNichVZJSd_1TQlXExj35bF04K-CYo_1j24ALRtSQU_1gYXxdzWveN7rXOBvtHVTGz05omsF2A9ApqPIqh8R36HHkyT4DJODB93O2wZDlD-GUvTVp57zuNGcyPhRYrYsvlv6WbFfTtEam4j28AafcDJNoNZLwT0-jf0hd2KnWZsJ2J3ndUIJlmrnERb0KMrQ4iVWU-KwQON16RsozbaGPTTc74n1F5y1hWh9qW1TrswOyNS0U3-Kbfp9EP3VP2ueGH5ZdcXRiZ_143VHuHlZ4G-KBLiCa5Rz5fq9zwV3cW_1vvysg6ZIakHf4TVfZd7APJzxDjb8LFY32ceqqIFjVeQI0UoD-AeftTt2ksrf8awdcTqdteOGfkn7boh4ThuuB13pE_1O45J8VsYKDeRkRDV4eJItSIENLSKxO-xqpuDDx0bAIlJwOpTxToVbNDhQ7HUXtIaNqmMCF6NueTvjTQJiJSOIFmvxtmkUcBLhsnT3UI8yDzKgySBvf_16eFVYz9XioKmBuBBQ-EC9qucxZy_1Dc41bE5ai19GcouWhLdjpwrEagVRvcXa1zF0QVFi6VPFA_1SJRiFJC80qhfmue0gE9wHTOs8re70E4YFlFVHK8UY44twvndoccSBOG6r-l5qzP9f-vhi-7KG98aNOrfXE0CrELBN4lJbATq4U3pOfpEue9y9k9e9pLDLa',
							'Host':'www.google.com',
							'Connection':'keep-alive',
							'Accept-Language':'en-US,en;q=0.5',
							'Accept-Encoding':'gzip, deflate',
							'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
	req = requests.get("https://www.google.com/searchbyimage?image_url="+url+"&encoded_image=&image_content=&filename=", headers=headers)
	print req.status_code
	# pprint(dir(r))
	if(req.status_code):
		print req.headers
		# pyperclip.copy(req.headers['Location']) #
	# time.sleep(5)  # throttle.

def main():
	while True:
		check_unread()
		submissions = get_subreddit_submissions()
		for submission in submissions:
			url = submission.url
			result = search_google_image(url)
		time.sleep(30)

if __name__ == '__main__':
	main()