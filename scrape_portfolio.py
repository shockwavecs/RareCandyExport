import csv
import time
from playwright.sync_api import sync_playwright

def scrape_portfolio():
    with sync_playwright() as p:
        browser_context = p.chromium.launch_persistent_context(
            user_data_dir="./playwright_session", 
            headless=False
        )
        
        page = browser_context.new_page()
        page.goto("https://rarecandy.com/")
        
        input("Did you login and load full page? (Press Enter when ready): ")

        print("📊 Extracting all card data and prices from the fully loaded page...")

        scraped_items = page.evaluate("""() => {
            const tiles = document.querySelectorAll("div.grid > div");
            const items = [];
            
            tiles.forEach(tile => {
                const link = tile.querySelector("a[href*='/pokemon/sets/']");
                if (!link) return;
                
                const href = link.getAttribute('href');
                
                const img = tile.querySelector('img');
                const altText = img ? img.getAttribute('alt') : '';
                
                // Extract price
                let price = 0.0;
                try {
                    const priceSpan = tile.querySelector('span[class*="text-lime"]');
                    if (priceSpan) {
                        const priceText = priceSpan.innerText.replace('$', '').trim();
                        const parsedPrice = parseFloat(priceText);
                        if (!isNaN(parsedPrice)) {
                            price = parsedPrice;
                        }
                    }
                } catch (e) {}

                // Extract quantity
                let qty = 1;
                try {
                    const stackIcon = tile.querySelector('svg[data-icon="cards-blank"]') || tile.querySelector('svg.fa-cards-blank');
                    if (stackIcon && stackIcon.nextElementSibling) {
                        const parsed = parseInt(stackIcon.nextElementSibling.innerText.trim(), 10);
                        if (!isNaN(parsed) && parsed > 0 && parsed < 1000) {
                            qty = parsed;
                        }
                    }
                } catch (e) {}
                
                items.push({
                    href: href,
                    alt: altText,
                    quantity: qty,
                    price: price
                });
            });
            return items;
        }""")

        unique_cards = {}
        for item in scraped_items:
            href = item["href"]
            qty = item["quantity"]
            alt_text = item["alt"]
            price = item["price"]

            if href:
                if href in unique_cards:
                    if qty > unique_cards[href]["Quantity"]:
                        unique_cards[href]["Quantity"] = qty
                    if price > unique_cards[href]["Price"]:
                        unique_cards[href]["Price"] = price
                else:
                    href_parts = href.split("/")
                    set_slug = href_parts[3] if len(href_parts) > 3 else "Unknown Set"
                    set_name = set_slug.replace("-", " ").title()

                    unique_cards[href] = {
                        "Quantity": qty,
                        "Product Name": alt_text,
                        "Set Name": set_name,
                        "Condition": "Near Mint",
                        "Price": price
                    }

        # Calculate total portfolio value
        total_portfolio_value = sum(card["Quantity"] * card["Price"] for card in unique_cards.values())

        print(f"📊 Extracted {len(unique_cards)} unique card types.")
        print(f"💰 Total Estimated Portfolio Value: ${total_portfolio_value:,.2f}")
        print("Writing to CSV...")

        csv_filename = "tcgplayer_import_with_prices.csv"
        csv_columns = ["Quantity", "Product Name", "Set Name", "Condition", "Price"]
        
        with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
            writer.writeheader()
            for card_data in unique_cards.values():
                writer.writerow(card_data)

        print(f"✅ Success! Data successfully exported to {csv_filename}")
        browser_context.close()

if __name__ == "__main__":
    scrape_portfolio()