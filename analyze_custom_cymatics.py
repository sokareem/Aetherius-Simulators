
import asyncio
from playwright.async_api import async_playwright

async def main():
    # User-provided parameters
    fx = 2.9864
    fy = 2.9631
    ax_percent = 159.91
    ay_percent = 160.80

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://localhost:8000/cymatics_simulator.html")
        await page.wait_for_selector("#fxInput")

        print(f"Setting parameters: fx={fx}, fy={fy}, ax={ax_percent}%, ay={ay_percent}%")
        await page.fill("#fxInput", str(fx))
        await page.fill("#fyInput", str(fy))
        await page.fill("#axInput", str(ax_percent))
        await page.fill("#ayInput", str(ay_percent))
        
        await page.wait_for_timeout(1000) # Allow ample time for rendering
        
        filename = "cymatics_analysis_custom.png"
        await page.screenshot(path=filename)
        print(f"Screenshot captured: {filename}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
