# Running multiple filters and combining them in parallel

When filtering the PCAP file with multiple filters, it may be faster to run them in parallel, and merge them.

This can be done by getting the PID of each `tshark` process:

```sh
command-to-run &
pid=$!
```

And then waiting on the PIDs:

```sh
wait $pid1 $pid2 $pid3 $pid4 # ...
```

## Example

The following script applies multiple `frame.time` filters in parallel and combines the result.

```sh
#!/bin/sh

# Define variables for file names
original_pcap="hamiltona_network_log.pcapng"
filtered_pcap1="filtered_0830_0900.pcapng"
filtered_pcap2="filtered_1030_1200.pcapng"
filtered_pcap3="filtered_1500_1630.pcapng"
filtered_pcap4="filtered_1630_1745.pcapng"
combined_pcap="filtered_combined.pcapng"

# Filter specific time periods in parallel
tshark -r $original_pcap -Y 'frame.time >= "Sep  4, 2020 08:30:00" && frame.time <= "Sep  4, 2020 09:00:00"' -w $filtered_pcap1 &
pid1=$!
tshark -r $original_pcap -Y 'frame.time >= "Sep  4, 2020 10:30:00" && frame.time <= "Sep  4, 2020 12:00:00"' -w $filtered_pcap2 &
pid2=$!
tshark -r $original_pcap -Y 'frame.time >= "Sep  4, 2020 15:00:00" && frame.time <= "Sep  4, 2020 16:30:00"' -w $filtered_pcap3 &
pid3=$!
tshark -r $original_pcap -Y 'frame.time >= "Sep  4, 2020 16:30:00" && frame.time <= "Sep  4, 2020 17:45:00"' -w $filtered_pcap4 &
pid4=$!

# Wait for all background processes to complete
wait $pid1 $pid2 $pid3 $pid4

# Combine filtered PCAP files
mergecap -w $combined_pcap $filtered_pcap1 $filtered_pcap2 $filtered_pcap3 $filtered_pcap4

# Cleanup intermediate files
rm $filtered_pcap1 $filtered_pcap2 $filtered_pcap3 $filtered_pcap4

echo "Filtering and merging completed successfully."
```
