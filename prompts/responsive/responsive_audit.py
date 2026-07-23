"""Responsive layout audit for Stock Insight Explorer."""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

WIDTHS = [320, 360, 375, 390, 414, 480, 768, 820, 1024, 1280, 1440, 1920]
BASE_URL = "http://localhost:8501"


def overflow_metrics(page) -> dict:
    return page.evaluate(
        """() => {
            const doc = document.documentElement;
            const body = document.body;
            const sidebar = document.querySelector('[data-testid="stSidebar"]');
            const main = document.querySelector('[data-testid="stAppViewContainer"]');
            const overflowing = [...document.querySelectorAll('*')].filter(el => {
                const style = getComputedStyle(el);
                if (style.display === 'none' || style.visibility === 'hidden') return false;
                const rect = el.getBoundingClientRect();
                if (rect.width <= 0 || rect.height <= 0) return false;
                return rect.right > window.innerWidth + 2;
            }).slice(0, 8).map(el => ({
                tag: el.tagName,
                testid: el.getAttribute('data-testid'),
                className: (el.className || '').toString().slice(0, 80),
                right: el.getBoundingClientRect().right,
            }));
            return {
                innerWidth: window.innerWidth,
                scrollWidth: doc.scrollWidth,
                clientWidth: doc.clientWidth,
                bodyScrollWidth: body.scrollWidth,
                hasOverflow: doc.scrollWidth > doc.clientWidth + 1,
                sidebarVisible: sidebar ? sidebar.getBoundingClientRect().width > 0 && sidebar.getBoundingClientRect().right > 0 : false,
                sidebarExpanded: sidebar ? sidebar.getAttribute('aria-expanded') === 'true' : null,
                mainVisible: main ? main.getBoundingClientRect().width > 0 : false,
                sidebarLeft: sidebar ? sidebar.getBoundingClientRect().left : null,
                mainLeft: main ? main.getBoundingClientRect().left : null,
                sidebarToggle: !!document.querySelector('[data-testid="stSidebarCollapsedControl"]'),
                overflowing,
            };
        }"""
    )


def wait_for_app(page, timeout_ms: int = 30000) -> None:
    page.wait_for_function(
        "document.title.includes('Stock Insight Explorer')",
        timeout=timeout_ms,
    )
    page.wait_for_selector('[data-testid="stAppViewContainer"]', timeout=timeout_ms)


def open_sidebar_if_needed(page) -> None:
    sidebar = page.locator('[data-testid="stSidebar"]')
    if sidebar.count() == 0:
        return
    if sidebar.get_attribute("aria-expanded") == "true":
        return
    toggle = page.locator('[data-testid="stExpandSidebarButton"]')
    if toggle.count() > 0 and toggle.first.is_visible():
        toggle.first.click()
        page.wait_for_timeout(800)


def enter_symbol(page, symbol: str) -> None:
    open_sidebar_if_needed(page)
    input_box = page.get_by_role("textbox", name="Stock symbol")
    input_box.click()
    input_box.fill("")
    input_box.type(symbol, delay=50)
    input_box.press("Enter")
    page.wait_for_timeout(2500)


def main() -> int:
    results: list[dict] = []
    screenshots_dir = Path(__file__).resolve().parent / "responsive_screenshots"
    screenshots_dir.mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for width in WIDTHS:
            context = browser.new_context(
                viewport={"width": width, "height": 900},
                device_scale_factor=1,
            )
            page = context.new_page()
            page.goto(BASE_URL, wait_until="networkidle")
            wait_for_app(page)
            enter_symbol(page, "AAPL")
            metrics = overflow_metrics(page)
            metrics["width"] = width
            metrics["state"] = "statistics_with_symbol"
            shot = screenshots_dir / f"aapl_{width}.png"
            page.screenshot(path=str(shot), full_page=True)
            metrics["screenshot"] = str(shot)
            results.append(metrics)
            context.close()

        # Mobile sidebar access check (empty state)
        context = browser.new_context(viewport={"width": 375, "height": 812})
        page = context.new_page()
        page.goto(BASE_URL, wait_until="networkidle")
        wait_for_app(page)
        mobile_empty = overflow_metrics(page)
        mobile_empty["width"] = 375
        mobile_empty["state"] = "empty_mobile"
        page.screenshot(path=str(screenshots_dir / "empty_375.png"), full_page=True)
        results.append(mobile_empty)
        context.close()

        browser.close()

    report_path = Path(__file__).resolve().parent / "responsive_audit_report.json"
    report_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
