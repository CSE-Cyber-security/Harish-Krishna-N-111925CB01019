# Week 01 – Cybersecurity Asset Inventory System

## Problem Statement
An organization maintains several IT assets such as computers, servers, routers, switches, and
software applications. This command-line program lets a security administrator **add, search,
update, delete, and display** information about the organization's IT assets, and classifies each
asset by **type** and **security risk level**.

## Features
- Add a single asset, or bulk-add several assets in one go (matching the assignment's sample input flow)
- Search for an asset by Asset ID
- Update any field of an existing asset (blank input keeps the current value)
- Delete an asset (with a confirmation prompt)
- Display all assets in the exact formatted layout required by the assignment
- Security summary: total assets, and counts by risk level / security status
- Input validation: Asset Type, Risk Level, and Security Status must be one of the allowed values
- Data is persisted between runs in `data/assets.json`

## Project Structure
```
Week-01-Cybersecurity-Asset-Inventory/
├── src/
│   └── asset_inventory.py     # Main program
├── data/
│   └── assets.json            # Persisted asset data (pre-loaded with sample data)
├── tests/
│   └── test_cases.md          # Manual test cases
├── screenshots/                # Add your screenshots here (see below)
└── README.md
```

## How to Run
Requires Python 3.

```bash
cd src
python3 asset_inventory.py
```

You'll see a menu:
```
===== CYBERSECURITY ASSET INVENTORY SYSTEM =====
1. Add Asset
2. Add Multiple Assets (bulk entry)
3. Display All Assets
4. Search Asset
5. Update Asset
6. Delete Asset
7. Security Summary
8. Exit
```

## Sample Data
`data/assets.json` is pre-loaded with the 3 sample assets from the assignment (A101, A102, A103),
so choosing **3. Display All Assets** immediately reproduces the assignment's Expected Output,
including the Total/Critical/High/Vulnerable summary counts.

## Screenshots
The `screenshots/` folder is where you should save your own terminal screenshots after running
the program, named to match the required repo structure:
- `01-add-asset.png`
- `02-display-assets.png`
- `03-search-asset.png`
- `04-update-asset.png`
- `05-delete-asset.png`
- `06-security-summary.png`
- `07-input-validation.png` (e.g. entering an invalid Risk Level to show validation working)
