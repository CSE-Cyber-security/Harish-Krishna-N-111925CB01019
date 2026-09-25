# Test Cases – Cybersecurity Asset Inventory System

## 1. Add Asset

| Test Case ID | Test Scenario             | Test Data                                   | Expected Result                             |
| ------------ | ------------------------- | ------------------------------------------- | ------------------------------------------- |
| TC01         | Add a valid asset         | ID: A101, Name: HR-PC-01, Type: Workstation | Asset should be added successfully          |
| TC02         | Add a Server asset        | ID: A102, Type: Server, Risk: Critical      | Server asset should be added successfully   |
| TC03         | Add a Router asset        | ID: A103, Type: Router, Risk: High          | Router asset should be added successfully   |
| TC04         | Add an invalid asset type | Type: Printer                               | System should reject the invalid asset type |

## 2. Search Asset

| Test Case ID | Test Scenario             | Test Data      | Expected Result                           |
| ------------ | ------------------------- | -------------- | ----------------------------------------- |
| TC05         | Search existing asset     | Asset ID: A101 | Correct asset details should be displayed |
| TC06         | Search non-existing asset | Asset ID: A999 | "Asset Not Found" should be displayed     |

## 3. Update Asset

| Test Case ID | Test Scenario             | Test Data            | Expected Result                              |
| ------------ | ------------------------- | -------------------- | -------------------------------------------- |
| TC07         | Update existing asset     | ID: A101, Risk: High | Asset details should be updated successfully |
| TC08         | Update non-existing asset | ID: A999             | "Asset Not Found" should be displayed        |

## 4. Delete Asset

| Test Case ID | Test Scenario             | Test Data      | Expected Result                       |
| ------------ | ------------------------- | -------------- | ------------------------------------- |
| TC09         | Delete existing asset     | Asset ID: A101 | Asset should be deleted successfully  |
| TC10         | Delete non-existing asset | Asset ID: A999 | "Asset Not Found" should be displayed |

## 5. Display Assets

| Test Case ID | Test Scenario                | Test Data        | Expected Result                              |
| ------------ | ---------------------------- | ---------------- | -------------------------------------------- |
| TC11         | Display all assets           | A101, A102, A103 | All stored asset details should be displayed |
| TC12         | Display when no assets exist | No asset data    | "No Assets Available" should be displayed    |

## 6. Risk Level Validation

The system should support the following risk levels: **Low, Medium, High, Critical**.

| Test Case ID | Test Scenario       | Test Data      | Expected Result                        |
| ------------ | ------------------- | -------------- | -------------------------------------- |
| TC13         | Low risk asset      | Risk: Low      | Asset should be classified as Low      |
| TC14         | Medium risk asset   | Risk: Medium   | Asset should be classified as Medium   |
| TC15         | High risk asset     | Risk: High     | Asset should be classified as High     |
| TC16         | Critical risk asset | Risk: Critical | Asset should be classified as Critical |

## 7. Security Status Validation

The supported security statuses are **Secure, Warning, and Vulnerable**.

| Test Case ID | Test Scenario     | Test Data          | Expected Result                          |
| ------------ | ----------------- | ------------------ | ---------------------------------------- |
| TC17         | Secure status     | Status: Secure     | Asset should be classified as Secure     |
| TC18         | Warning status    | Status: Warning    | Asset should be classified as Warning    |
| TC19         | Vulnerable status | Status: Vulnerable | Asset should be classified as Vulnerable |

## 8. Summary

| Test Case           | Expected Outcome |
| ------------------- | ---------------- |
| Total Test Cases    | 19               |
| Add Asset           | Successful       |
| Search Asset        | Successful       |
| Update Asset        | Successful       |
| Delete Asset        | Successful       |
| Display Assets      | Successful       |
| Risk Classification | Validated        |
| Security Status     | Validated        |
