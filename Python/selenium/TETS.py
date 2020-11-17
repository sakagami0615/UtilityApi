from chromedriver import ChromeDriver


if __name__ == '__main__':

	web_driver = ChromeDriver(wait_sec=5, is_hidden=False)

	web_driver.driver.get('https://www.google.com')
	web_driver.Sleep()
