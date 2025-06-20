# HTTP-File-Extraction-from-Packet-Captures

This project demonstrates how to extract HTTP-transferred files from a `.pcap` file using **Wireshark** and a **Python script with PyShark**. The project was created as part of my internship learning in network security.

---

## 📌 Project Purpose

The purpose of this project is to learn and demonstrate how to extract files from network traffic — both manually using Wireshark and programmatically using a Python script with the PyShark library. This is useful for analyzing malicious files, reconstructing transferred content, or digital forensics.

---


## ⚙️ Tools Used

- **Wireshark** — for visual analysis and manual extraction of files
- **Python** — for scripting automated file extraction
- **PyShark** — Python wrapper for Tshark to process `.pcap` files
- **Demo PCAP File** — downloaded for HTTP traffic containing a file transfer

---

## 📁 File Structure

```text
file-extraction-wireshark/
├── extracted_files/ # Directory where extracted files are saved
├── screenshots/
│ ├── http-object-wireshark.png # Screenshot of HTTP file in Wireshark
├── extract_file.py # Python script to extract files from PCAP
├── sample.pcap # Demo PCAP file with HTTP traffic
├── README.md # Project documentation
```

---

## 🚀 How to Run

1. Install the required Python library:
   ```bash
   pip install pyshark
   ```
2. Download or use a .pcap file containing HTTP traffic.
3. Run the Python script to extract files:
   ```bash
   python extract_file.py
   ```
4. Extract files manually in Wireshark:

  -Open .pcap file in Wireshark.

  -Go to: File > Export Objects > HTTP

  -Choose a file and click "Save As".

---

## 🧠 How It Works
  -Wireshark parses HTTP packets and allows manual extraction of objects transferred in the session.

  -The Python script uses PyShark to read through the .pcap file, locate HTTP packets, and reconstruct the data into a file.

---

## 💻 Code Explanation
Below is a key part of the Python script used to extract HTTP file data from a .pcap file using PyShark

```python
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
```
### 🔍 What This Code Does
  - Iterates through each packet in the PCAP file.

  - Checks if the packet contains HTTP data.

  - If the packet contains file data:

    - Extracts the file contents from the packet in raw binary format.

    - Identifies the file type using the Content-Type header (e.g., image/jpeg, application/pdf).

  - Saves the extracted data to disk with a proper file extension (e.g., .jpeg, .pdf).

  - If the packet doesn't have the required data, it's skipped safely using a try-except block.

---

## 📚 What I Learned
  - How to analyze HTTP file transfers in Wireshark.

  - How to manually extract files from captured traffic using Wireshark’s export tools.

  - How to automate file extraction from .pcap using Python and the PyShark library.

  - The importance of file reconstruction in digital forensics and malware analysis.





