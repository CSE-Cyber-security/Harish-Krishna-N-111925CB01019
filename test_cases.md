# Test Cases – Cybersecurity Asset Inventory System

| # | Test Case | Steps | Expected Result |
|---|-----------|-------|------------------|
| 1 | Add a valid asset | Menu → 1 → enter unique Asset ID and valid values for all fields | Asset is added and saved to `data/assets.json`; confirmation message shown |
| 2 | Add asset with duplicate ID | Menu → 1 → enter an Asset ID that already exists | Program rejects it with "Asset ID already exists" and does not add a duplicate |
| 3 | Add asset with invalid Asset Type / Risk Level / Status | Menu → 1 → type an option not in the allowed list (e.g. "Laptop") | Program re-prompts until a valid option from the fixed list is entered |
| 4 | Bulk add multiple assets | Menu → 2 → enter a number, then fill in each asset in turn | All N assets are added in one session, matching the sample input format |
| 5 | Display all assets | Menu → 3 | All assets print in the required formatted layout, ending with a summary |
| 6 | Display when inventory is empty | Delete all assets, then Menu → 3 | Program prints "No assets found." instead of erroring |
| 7 | Search for an existing asset | Menu → 4 → enter a valid Asset ID | Full asset details are displayed |
| 8 | Search for a non-existing asset | Menu → 4 → enter an ID that doesn't exist | Program prints "No asset found with ID ..." |
| 9 | Update an asset's fields | Menu → 5 → enter existing ID → change some fields, leave others blank | Only the changed fields are updated; blank fields keep their old value |
| 10 | Update with invalid Risk Level/Status | Menu → 5 → enter an invalid value for Risk Level or Status | Program keeps the previous value and warns the user |
| 11 | Delete an existing asset (confirmed) | Menu → 6 → enter valid ID → confirm with "y" | Asset is removed from the inventory and the JSON file |
| 12 | Delete an existing asset (cancelled) | Menu → 6 → enter valid ID → answer "n" | Asset remains in the inventory |
| 13 | Delete a non-existing asset | Menu → 6 → enter an ID that doesn't exist | Program prints "No asset found with ID ..." |
| 14 | Security summary counts | Menu → 7 with the 3 sample assets loaded | Total: 3, Critical: 1, High: 1, Medium: 1, Vulnerable: 1 (matches Expected Output in the assignment) |
| 15 | Data persistence across runs | Add/update/delete assets, exit (option 8), restart the program | Previously saved changes are still present, loaded from `data/assets.json` |
| 16 | Empty required field | Add an asset and press Enter without typing an Asset Name / ID / etc. | Program re-prompts "This field cannot be empty." |
