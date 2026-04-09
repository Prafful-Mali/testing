from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # headless=False to see browser
    page = browser.new_page()

    page.goto("https://www.webpagetest.org/")

    title = page.title()
    print(title)
    page.locator("xpath=//*[@id='url']").fill("https://www.google.com")

    page.locator("#testurl").click()
    html = page.content()
    with open("output.html", "w+", encoding="utf-8") as f:
        f.write(title)
        f.write(html)
        f.seek(0)
        f.write("asdfasdf")
        temp = f.read()

    print(temp)
    browser.close()