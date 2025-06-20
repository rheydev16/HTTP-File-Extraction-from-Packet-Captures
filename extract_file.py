import pyshark
import os

# Path to your pcap file
pcap_path = 'sample.pcap'
output_dir = 'extracted_files'

# Create output directory if not exists
os.makedirs(output_dir, exist_ok=True)

# Load only HTTP packets to save memory
capture = pyshark.FileCapture(pcap_path, display_filter='http')

file_count = 0

for packet in capture:
    try:
        if 'HTTP' in packet:
            http_layer = packet.http

            if hasattr(http_layer, 'file_data'):
                # Extract raw file data
                file_data = bytes.fromhex(http_layer.file_data.replace(':', ''))

                # Optional: Determine file type from Content-Type or guess from headers
                content_type = getattr(http_layer, 'content_type', 'application/octet-stream')
                extension = content_type.split('/')[-1].split(';')[0]

                # Save to disk
                file_name = f'file_{file_count}.{extension}'
                file_path = os.path.join(output_dir, file_name)

                with open(file_path, 'wb') as f:
                    f.write(file_data)

                print(f'[+] Saved: {file_path}')
                file_count += 1

    except AttributeError:
        continue

capture.close()

if file_count == 0:
    print("[-] No files found in HTTP traffic.")
else:
    print(f"[+] Extracted {file_count} file(s).")
