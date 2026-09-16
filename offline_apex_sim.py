import os
import json

# Simulate an offline Apex code repository
# In a real scenario, this would be a local file system, Git repo, or a dedicated service.
OFFLINE_APEX_REPO = {
    "AccountTrigger": "trigger AccountTrigger on Account (before insert, before update) { /* ... */ }",
    "ContactService": "public with sharing class ContactService { /* ... */ }",
    "OpportunityTrigger": "trigger OpportunityTrigger on Opportunity (after delete) { /* ... */ }"
}

# Simulate a local Apex compiler/linter
def compile_apex(apex_code):
    print(f"Simulating compilation for Apex code: {apex_code[:50]}...")
    # In a real scenario, this would invoke a local Apex compiler or a mocked service.
    if "trigger" in apex_code.lower() or "class" in apex_code.lower():
        print("Compilation successful (simulated).")
        return True
    else:
        print("Compilation failed (simulated).")
        return False

# Simulate sending Apex code to a deployment service (which is offline)
def send_to_deployment_service(apex_name, apex_code):
    print(f"Attempting to send '{apex_name}' to deployment service...")
    # Simulate that the Salesforce org/deployment service is unavailable
    is_salesforce_available = False # This is the core simulation of the outage

    if not is_salesforce_available:
        print("Salesforce deployment service is OFFLINE. Queuing for later deployment.")
        # In a real scenario, this would be saved to a local queue or persistent storage.
        queued_deployments.append({"name": apex_name, "code": apex_code})
        return False
    else:
        print(f"Successfully deployed '{apex_name}' (simulated).")
        return True

# --- Main Simulation Logic ---

print("--- Dreamforce 2026 Offline Apex Development Simulation ---")

# Simulate checking if Salesforce org is accessible
def is_salesforce_org_accessible():
    # This function would normally check network connectivity and org status.
    # For this simulation, we hardcode it to be unavailable.
    return False

queued_deployments = []

# Simulate developer working on Apex code offline
print("\nDeveloper is working on new Apex code...")
new_apex_code_1 = OFFLINE_APEX_REPO["AccountTrigger"]
new_apex_name_1 = "AccountTrigger"

# Compile locally first
if compile_apex(new_apex_code_1):
    # Attempt to send to deployment service, which will fail due to simulated outage
    send_to_deployment_service(new_apex_name_1, new_apex_code_1)

new_apex_code_2 = OFFLINE_APEX_REPO["ContactService"]
new_apex_name_2 = "ContactService"

if compile_apex(new_apex_code_2):
    send_to_deployment_service(new_apex_name_2, new_apex_code_2)

print("\n--- Development session ended. Queued for deployment: ---")
if queued_deployments:
    for deployment in queued_deployments:
        print(f"- {deployment['name']}")
else:
    print("No Apex code was queued for deployment.")

print("\nWhen Salesforce becomes available again, the queued deployments can be processed.")
