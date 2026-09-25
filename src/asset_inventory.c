#include <stdio.h>
#include <string.h>

#define MAX 100

struct Asset {
    char id[20];
    char name[50];
    char type[30];
    char ip[30];
    char os[50];
    char department[50];
    char risk[20];
    char status[20];
};

struct Asset assets[MAX];
int count = 0;

void addAsset() {
    if (count >= MAX) {
        printf("\nAsset list is full!\n");
        return;
    }

    printf("\nEnter Asset ID: ");
    scanf(" %[^\n]", assets[count].id);

    printf("Enter Asset Name: ");
    scanf(" %[^\n]", assets[count].name);

    printf("Enter Asset Type: ");
    scanf(" %[^\n]", assets[count].type);

    printf("Enter IP Address: ");
    scanf(" %[^\n]", assets[count].ip);

    printf("Enter Operating System: ");
    scanf(" %[^\n]", assets[count].os);

    printf("Enter Department: ");
    scanf(" %[^\n]", assets[count].department);

    printf("Enter Risk Level: ");
    scanf(" %[^\n]", assets[count].risk);

    printf("Enter Security Status: ");
    scanf(" %[^\n]", assets[count].status);

    count++;

    printf("\nAsset Added Successfully!\n");
}

void displayAssets() {

    int critical = 0;
    int high = 0;
    int medium = 0;
    int vulnerable = 0;

    if (count == 0) {
        printf("\nNo Assets Available!\n");
        return;
    }

    printf("\n=========================================\n");
    printf("     CYBERSECURITY ASSET INVENTORY\n");
    printf("=========================================\n");

    for (int i = 0; i < count; i++) {

        printf("\nAsset ID       : %s\n", assets[i].id);
        printf("Asset Name     : %s\n", assets[i].name);
        printf("Asset Type     : %s\n", assets[i].type);
        printf("IP Address     : %s\n", assets[i].ip);
        printf("OS             : %s\n", assets[i].os);
        printf("Department     : %s\n", assets[i].department);
        printf("Risk Level     : %s\n", assets[i].risk);
        printf("Status         : %s\n", assets[i].status);

        printf("-----------------------------------------\n");

        if (strcmp(assets[i].risk, "Critical") == 0)
            critical++;

        if (strcmp(assets[i].risk, "High") == 0)
            high++;

        if (strcmp(assets[i].risk, "Medium") == 0)
            medium++;

        if (strcmp(assets[i].status, "Vulnerable") == 0)
            vulnerable++;
    }

    printf("\n=========================================\n");
    printf("Total Assets       : %d\n", count);
    printf("Critical Assets    : %d\n", critical);
    printf("High Risk Assets   : %d\n", high);
    printf("Medium Risk Assets : %d\n", medium);
    printf("Vulnerable Assets  : %d\n", vulnerable);
    printf("=========================================\n");
}

void searchAsset() {

    char id[20];
    int found = 0;

    printf("\nEnter Asset ID to Search: ");
    scanf(" %[^\n]", id);

    for (int i = 0; i < count; i++) {

        if (strcmp(assets[i].id, id) == 0) {

            printf("\nAsset Found!\n");

            printf("Asset ID       : %s\n", assets[i].id);
            printf("Asset Name     : %s\n", assets[i].name);
            printf("Asset Type     : %s\n", assets[i].type);
            printf("IP Address     : %s\n", assets[i].ip);
            printf("OS             : %s\n", assets[i].os);
            printf("Department     : %s\n", assets[i].department);
            printf("Risk Level     : %s\n", assets[i].risk);
            printf("Status         : %s\n", assets[i].status);

            found = 1;
            break;
        }
    }

    if (!found)
        printf("\nAsset Not Found!\n");
}

void updateAsset() {

    char id[20];
    int found = 0;

    printf("\nEnter Asset ID to Update: ");
    scanf(" %[^\n]", id);

    for (int i = 0; i < count; i++) {

        if (strcmp(assets[i].id, id) == 0) {

            printf("\nEnter New Asset Name: ");
            scanf(" %[^\n]", assets[i].name);

            printf("Enter New Asset Type: ");
            scanf(" %[^\n]", assets[i].type);

            printf("Enter New IP Address: ");
            scanf(" %[^\n]", assets[i].ip);

            printf("Enter New Operating System: ");
            scanf(" %[^\n]", assets[i].os);

            printf("Enter New Department: ");
            scanf(" %[^\n]", assets[i].department);

            printf("Enter New Risk Level: ");
            scanf(" %[^\n]", assets[i].risk);

            printf("Enter New Security Status: ");
            scanf(" %[^\n]", assets[i].status);

            printf("\nAsset Updated Successfully!\n");

            found = 1;
            break;
        }
    }

    if (!found)
        printf("\nAsset Not Found!\n");
}

void deleteAsset() {

    char id[20];
    int found = 0;

    printf("\nEnter Asset ID to Delete: ");
    scanf(" %[^\n]", id);

    for (int i = 0; i < count; i++) {

        if (strcmp(assets[i].id, id) == 0) {

            for (int j = i; j < count - 1; j++) {
                assets[j] = assets[j + 1];
            }

            count--;

            printf("\nAsset Deleted Successfully!\n");

            found = 1;
            break;
        }
    }

    if (!found)
        printf("\nAsset Not Found!\n");
}

int main() {

    int choice;

    do {

        printf("\n=====================================\n");
        printf(" CYBERSECURITY ASSET INVENTORY SYSTEM\n");
        printf("=====================================\n");

        printf("1. Add Asset\n");
        printf("2. Search Asset\n");
        printf("3. Update Asset\n");
        printf("4. Delete Asset\n");
        printf("5. Display All Assets\n");
        printf("6. Exit\n");

        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch (choice) {

            case 1:
                addAsset();
                break;

            case 2:
                searchAsset();
                break;

            case 3:
                updateAsset();
                break;

            case 4:
                deleteAsset();
                break;

            case 5:
                displayAssets();
                break;

            case 6:
                printf("\nProgram Exited Successfully!\n");
                break;

            default:
                printf("\nInvalid Choice!\n");
        }

    } while (choice != 6);

    return 0;
}
