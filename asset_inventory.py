"""
Cybersecurity Asset Inventory System
--------------------------------------
Weekly Mini Project - 01

Allows a security administrator to add, search, update, delete,
and display information about an organization's IT assets.
Assets are classified by type and security risk level, and the
data is persisted to data/assets.json between runs.
"""

import json
import os

# Path to the JSON file used for persistence (data/assets.json)
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "assets.json")

VALID_ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
VALID_RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
VALID_SECURITY_STATUSES = ["Secure", "Warning", "Vulnerable"]


# ----------------------------- Persistence -----------------------------

def load_assets():
    """Load the asset list from the JSON data file, if it exists."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_assets(assets):
    """Persist the current asset list to the JSON data file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(assets, f, indent=4)


# ----------------------------- Input Helpers -----------------------------

def get_choice_input(prompt, valid_options):
    """Repeatedly prompt the user until a valid option is entered."""
    options_str = "/".join(valid_options)
    while True:
        value = input(f"{prompt} ({options_str}): ").strip().title()
        if value in valid_options:
            return value
        print(f"  Invalid input. Please choose one of: {options_str}")


def get_non_empty_input(prompt):
    """Repeatedly prompt the user until a non-empty value is entered."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  This field cannot be empty.")


def asset_id_exists(assets, asset_id):
    return any(a["asset_id"].lower() == asset_id.lower() for a in assets)


# ----------------------------- Core Features -----------------------------

def add_asset(assets):
    """Prompt for a single asset's details and add it to the inventory."""
    print("\n--- Add New Asset ---")
    asset_id = get_non_empty_input("Asset ID: ")
    if asset_id_exists(assets, asset_id):
        print(f"  Asset ID '{asset_id}' already exists. Asset not added.")
        return

    asset = {
        "asset_id": asset_id,
        "asset_name": get_non_empty_input("Asset Name: "),
        "asset_type": get_choice_input("Asset Type", VALID_ASSET_TYPES),
        "ip_address": get_non_empty_input("IP Address: "),
        "os": get_non_empty_input("Operating System: "),
        "department": get_non_empty_input("Owner/Department: "),
        "risk_level": get_choice_input("Risk Level", VALID_RISK_LEVELS),
        "security_status": get_choice_input("Security Status", VALID_SECURITY_STATUSES),
    }
    assets.append(asset)
    save_assets(assets)
    print(f"  Asset '{asset_id}' added successfully.")


def add_multiple_assets(assets):
    """Bulk-entry mode matching the sample input format (Enter number of assets)."""
    try:
        count = int(input("Enter number of assets: ").strip())
    except ValueError:
        print("  Please enter a valid number.")
        return
    for i in range(1, count + 1):
        print(f"\nAsset {i}")
        add_asset(assets)


def find_asset(assets, asset_id):
    for a in assets:
        if a["asset_id"].lower() == asset_id.lower():
            return a
    return None


def search_asset(assets):
    print("\n--- Search Asset ---")
    asset_id = get_non_empty_input("Enter Asset ID to search: ")
    asset = find_asset(assets, asset_id)
    if asset:
        print("\nAsset found:")
        print_asset(asset)
    else:
        print(f"  No asset found with ID '{asset_id}'.")


def update_asset(assets):
    print("\n--- Update Asset ---")
    asset_id = get_non_empty_input("Enter Asset ID to update: ")
    asset = find_asset(assets, asset_id)
    if not asset:
        print(f"  No asset found with ID '{asset_id}'.")
        return

    print("Leave a field blank to keep its current value.")
    name = input(f"Asset Name [{asset['asset_name']}]: ").strip()
    if name:
        asset["asset_name"] = name

    ip = input(f"IP Address [{asset['ip_address']}]: ").strip()
    if ip:
        asset["ip_address"] = ip

    os_name = input(f"Operating System [{asset['os']}]: ").strip()
    if os_name:
        asset["os"] = os_name

    dept = input(f"Owner/Department [{asset['department']}]: ").strip()
    if dept:
        asset["department"] = dept

    risk = input(f"Risk Level [{asset['risk_level']}] "
                 f"({'/'.join(VALID_RISK_LEVELS)}): ").strip().title()
    if risk:
        if risk in VALID_RISK_LEVELS:
            asset["risk_level"] = risk
        else:
            print("  Invalid risk level, keeping previous value.")

    status = input(f"Security Status [{asset['security_status']}] "
                    f"({'/'.join(VALID_SECURITY_STATUSES)}): ").strip().title()
    if status:
        if status in VALID_SECURITY_STATUSES:
            asset["security_status"] = status
        else:
            print("  Invalid security status, keeping previous value.")

    save_assets(assets)
    print(f"  Asset '{asset_id}' updated successfully.")


def delete_asset(assets):
    print("\n--- Delete Asset ---")
    asset_id = get_non_empty_input("Enter Asset ID to delete: ")
    asset = find_asset(assets, asset_id)
    if not asset:
        print(f"  No asset found with ID '{asset_id}'.")
        return

    confirm = input(f"Are you sure you want to delete '{asset_id}'? (y/n): ").strip().lower()
    if confirm == "y":
        assets.remove(asset)
        save_assets(assets)
        print(f"  Asset '{asset_id}' deleted successfully.")
    else:
        print("  Deletion cancelled.")


# ----------------------------- Display -----------------------------

def print_asset(asset):
    print(f"Asset ID    : {asset['asset_id']}")
    print(f"Asset Name  : {asset['asset_name']}")
    print(f"Asset Type  : {asset['asset_type']}")
    print(f"IP Address  : {asset['ip_address']}")
    print(f"OS          : {asset['os']}")
    print(f"Department  : {asset['department']}")
    print(f"Risk Level  : {asset['risk_level']}")
    print(f"Status      : {asset['security_status']}")


def display_assets(assets):
    print("\n=========================================")
    print(" CYBERSECURITY ASSET INVENTORY")
    print("=========================================")

    if not assets:
        print("No assets found.")
        print("=========================================")
        return

    for asset in assets:
        print_asset(asset)
        print("-----------------------------------------")

    print_summary(assets, header=False)


def print_summary(assets, header=True):
    total = len(assets)
    critical = sum(1 for a in assets if a["risk_level"] == "Critical")
    high = sum(1 for a in assets if a["risk_level"] == "High")
    medium = sum(1 for a in assets if a["risk_level"] == "Medium")
    low = sum(1 for a in assets if a["risk_level"] == "Low")
    vulnerable = sum(1 for a in assets if a["security_status"] == "Vulnerable")
    warning = sum(1 for a in assets if a["security_status"] == "Warning")
    secure = sum(1 for a in assets if a["security_status"] == "Secure")

    if header:
        print("\n=========================================")
        print(" SECURITY SUMMARY")
        print("=========================================")

    print(f"Total Assets      : {total}")
    print(f"Critical Assets   : {critical}")
    print(f"High Risk Assets  : {high}")
    print(f"Medium Risk Assets: {medium}")
    print(f"Low Risk Assets   : {low}")
    print(f"Secure Assets     : {secure}")
    print(f"Warning Assets    : {warning}")
    print(f"Vulnerable Assets : {vulnerable}")
    print("=========================================")


# ----------------------------- Main Menu -----------------------------

def print_menu():
    print("\n===== CYBERSECURITY ASSET INVENTORY SYSTEM =====")
    print("1. Add Asset")
    print("2. Add Multiple Assets (bulk entry)")
    print("3. Display All Assets")
    print("4. Search Asset")
    print("5. Update Asset")
    print("6. Delete Asset")
    print("7. Security Summary")
    print("8. Exit")


def main():
    assets = load_assets()

    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_asset(assets)
        elif choice == "2":
            add_multiple_assets(assets)
        elif choice == "3":
            display_assets(assets)
        elif choice == "4":
            search_asset(assets)
        elif choice == "5":
            update_asset(assets)
        elif choice == "6":
            delete_asset(assets)
        elif choice == "7":
            print_summary(assets)
        elif choice == "8":
            print("Exiting. All data has been saved. Goodbye!")
            break
        else:
            print("  Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()