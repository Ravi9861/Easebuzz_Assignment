from playwright.sync_api import sync_playwright

def test_ui_elements():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://rahulshettyacademy.com/AutomationPractice/")

        # Select Radio Button
        page.click("input[value='radio2']")

        # Select Dropdown
        page.select_option("#dropdown-class-example", "option2")

        # Checkbox
        page.check("#checkBoxOption1")

        # Handle Alert BEFORE clicking
        page.on("dialog", lambda dialog: dialog.accept())

        # Input and Alert
        page.fill("#name", "Nishant")
        page.click("#alertbtn")

        browser.close()