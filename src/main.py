import subprocess

scripts = [
    'anne.py',
    'coen.py',
    'dennis.py',
    'fabian.py',
    'falco.py',
    'jacco.py',
    'jeroen.py',
    'jolanda.py',
    'marjolein.py'
]

def run_script(script_name):
    """Run a script using Python and print its output."""
    print(f"Running {script_name}...")
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    
    # Print standard output and error if any
    if result.stdout:
        print("Output:")
        print(result.stdout)
    if result.stderr:
        print("Errors:")
        print(result.stderr)

    print(f"Finished running {script_name}\n")

if __name__ == "__main__":
    for script in scripts:
        run_script(script)
