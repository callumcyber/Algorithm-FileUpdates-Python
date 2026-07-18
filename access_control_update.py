# Assign `import_file` to the target access control list
import_file = "allow_list.txt"

# Assign `remove_list` to IP addresses flagged for revocation
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build `with` statement to safely read the initial contents of the file
with open(import_file, "r") as file:

    # Use `.read()` to ingest the file data and store it in the `ip_addresses` variable
    ip_addresses = file.read()

# Use `.split()` to convert the raw string into a list of individual IP elements
ip_addresses = ip_addresses.split()

# Iterate through the allowlist array to identify addresses flagged for removal
for element in ip_addresses:
    
    # Evaluate if the current IP element matches a record inside `remove_list`
    if element in remove_list:

        # Revoke access by removing the flagged record from the main dataset
        ip_addresses.remove(element)

# Convert `ip_addresses` back into a space-delimited string for file storage
ip_addresses = " ".join(ip_addresses)

# Open the file in write mode ('w') to safely overwrite the historical data
with open(import_file, "w") as file:

    # Commit the audited list, updating the perimeter access controls
    file.write(ip_addresses)
