from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_context(viewport={"width": 375, "height": 812}).new_page()
    page.goto("http://localhost:8502", wait_until="networkidle")
    page.wait_for_function("document.title.includes('Stock Insight Explorer')")
    data = page.evaluate(
        """() => ({
            title: document.title,
            sidebarExpanded: document.querySelector('[data-testid="stSidebar"]')?.getAttribute('aria-expanded'),
            controls: [...document.querySelectorAll('button')].map(b => ({
                testid: b.getAttribute('data-testid'),
                text: (b.textContent || '').trim().slice(0, 40),
                visible: b.offsetParent !== null,
                left: b.getBoundingClientRect().left,
                width: b.getBoundingClientRect().width,
            })).filter(b => b.visible),
            mainText: document.querySelector('section.main')?.innerText?.slice(0, 300)
        })"""
    )
    print(json.dumps(data, indent=2))
    page.screenshot(path="scripts/responsive_screenshots/mobile_check.png", full_page=True)
    browser.close()
