from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_context(viewport={"width": 768, "height": 900}).new_page()
    page.goto("http://localhost:8502", wait_until="networkidle")
    page.wait_for_function("document.title.includes('Stock Insight Explorer')")
    page.locator('[data-testid="stExpandSidebarButton"]').click()
    page.wait_for_timeout(500)
    page.get_by_role("textbox", name="Stock symbol").fill("AAPL")
    page.get_by_role("textbox", name="Stock symbol").press("Enter")
    page.wait_for_timeout(6000)
    data = page.evaluate(
        """() => {
            const main = document.querySelector('[data-testid="stMain"]');
            const horizontals = main ? [...main.querySelectorAll('[data-testid="stHorizontalBlock"]')].map(el => ({
                flexDirection: getComputedStyle(el).flexDirection,
                childCount: el.children.length,
                childTestIds: [...el.children].map(c => c.getAttribute('data-testid')),
            })) : [];
            return {
                hasMain: !!main,
                mainTag: main?.tagName,
                horizontals,
            };
        }"""
    )
    print(json.dumps(data, indent=2))
    browser.close()
