import re
from playwright.sync_api import Page, expect


# Test 1: Forsiden kan åbnes
def test_forside_kan_aabnes(page: Page):
    page.goto("https://zealand.dk")

    expect(page).to_have_title(re.compile(".+"))


# Test 2: Zealand-logoet er synligt
def test_logo_er_synligt(page: Page):
    page.goto("https://zealand.dk")

    logo = page.get_by_role("link", name="Logo")

    expect(logo).to_be_visible()


# Test 3: Navigationen er synlig
def test_navigation_er_synlig(page: Page):
    page.goto("https://zealand.dk")

    navigation = page.get_by_text("Uddannelser", exact=True).first

    expect(navigation).to_be_visible()


# Test 4: Sproget kan ændres til engelsk
def test_sprog_kan_aendres_til_engelsk(page: Page):
    page.goto("https://zealand.dk")

    english_link = page.get_by_text("EN", exact=True)

    english_link.click()

    expect(page).to_have_url("https://zealand.com/")
    expect(
        page.get_by_role("heading", name="Your next step starts at Zealand")
    ).to_be_visible()