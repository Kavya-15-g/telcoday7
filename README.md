touch app.py
33mWARNING#033[0m Daemon: could not connect to Windows Agent: could not get address: could not read agent port file "/mnt/c/Users/kg001/.ubuntupro/.address": open /mnt/c/Users/kg001/.ubuntupro/.address: no such file or directory
2025-11-17T10:18:04.617515+00:00 kavya systemd-resolved[105]: Clock change detected. Flushing caches.
2025-11-17T10:18:34.531576+00:00 kavya systemd-resolved[105]: Clock change detected. Flushing caches.
2025-11-17T10:18:34.889682+00:00 kavya wsl-pro-service[2663]: #033[33mWARNING#033[0m Daemon: could not connect to Windows Agent: could not get address: could not read agent port file "/mnt/c/Users/kg001/.ubuntupro/.address": open /mnt/c/Users/kg001/.ubuntupro/.address: no such file or directory
2025-11-17T10:19:04.499995+00:00 kavya systemd-resolved[105]: Clock change detected. Flushing caches.
chmod a+x app.py
2025-11-17T10:54:56.231040+00:00 kavya systemd-timesyncd[106]: Timed out waiting for reply from 91.189.91.157:123 (ntp.ubuntu.com).
2025-11-17T10:55:05.977731+00:00 kavya systemd-resolved[105]: Clock change detected. Flushing caches.


DAY -9..............

Step 1 — Filter log for a specific event with grep

Use grep to pick only the lines that contain the event you want (example: CALL_DROP).

Step 2 — Extract a field with awk (CELL ID)

Use awk to take only the column you need from those filtered lines (example: the CELL ID column).
Step 3 — Normalize field with sed

Use sed to clean the extracted field by removing labels or extra spaces (example: remove CELL_ID=).

Step 4 — Sort and count (sort + uniq -c)

Sort the cleaned values and count how many times each value occurs.
This helps to find which cell has the most issues.

Step 5 — Add header and limit with head

Add a title to your output and use head to show only the top results if needed.

Step 6 — Extract IMSIs with call drops

Use awk on the filtered CALL_DROP lines to extract the IMSI column (to know which users got call drops).

Step 7 — Advanced: Filter call drops with RSRP worse than -105 dBm

Apply a condition to show only call drops where RSRP is very low (e.g., < -105), which indicates bad signal.
