import subprocess

script_order = [
    'scraper.py',
    'renamer.py',
    'testeract.py',
    'line_deleter.py',
    'extractor.py']

for script in script_order:
    try:
        subprocess.run(['python', script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"ERROR while running {script}: {e}")
    else:
        print(f"{script} Ran OK")


