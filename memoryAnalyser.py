#!/usr/bin/env python3
import subprocess
import sys
import os
import re

def run(cmd):
    """Execute a shell command (list) and return its full output (stdout and stderr) as one string."""
    proc = subprocess.run(cmd,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          text=True)
    return proc.stdout + proc.stderr


def main():
    if len(sys.argv) != 2:
        print("Usage: python memoryAnalyser.py <memory_dump_file>")
        sys.exit(1)

    memfile = sys.argv[1]
    if not os.path.isfile(memfile):
        print(f"Error: File not found: {memfile}")
        sys.exit(1)

    base = os.path.splitext(os.path.basename(memfile))[0]
    outfile = base + ".txt"

    # Determine location of volatility executable (set to working dir)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    VOL = os.path.join(script_dir, "volatility_2.6_win64_standalone.exe")
    if not os.path.isfile(VOL):
        print(f"Error: Volatility executable not found at {VOL}")
        sys.exit(1)

    with open(outfile, "w") as f:
        # 1) imageinfo - Detect profile 
        cmd = [VOL, "-f", memfile, "imageinfo"]
        f.write(f"$ {' '.join(cmd)}\n")
        out = run(cmd)
        f.write(out + "\n")

        # Parse the first Suggested Profile
        profile = None
        for line in out.splitlines():
            m = re.search(r"Suggested Profile\(s\) ?: ?(.+)", line)
            if m:
                profile = m.group(1).split(",")[0].strip()
                break

        if not profile:
            f.write("ERROR: Could not auto-detect profile. Exiting.\n")
            print(f"[!] No profile detected. See {outfile} for imageinfo output.")
            sys.exit(1)

        f.write(f"? Using profile: {profile}\n\n")

        # 2) Volatility plugins to run
        plugins = [
            "pslist", "pstree", "psxview", "psscan",
            "connscan", "sockets", "netscan",
            "cmdline", "consoles", "cmdscan",
            "hivelist", "printkey"
        ]

        for plugin in plugins:
            cmd = [VOL, "-f", memfile, f"--profile={profile}", plugin]
            if plugin == "printkey":
                # (registry key; adjust as needed)
                cmd += ["-K", "MyPath"]

            f.write(f"$ {' '.join(cmd)}\n")
            out = run(cmd)
            f.write(out + "\n" + ("="*80) + "\n\n")

    print(f"[+] Analysis complete. Results in {outfile}")


if __name__ == "__main__":
    main()
