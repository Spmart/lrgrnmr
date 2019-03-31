import os
import sys


if os.name == "posix":
    start = "/Users/spmart"
elif os.name == "nt":
    start = sys.argv[0][0:3]  # Get a drive letter where is the script starts
else:
    print("WTF this system is? Whatever, I'm leaving!")
    sys.exit(42)

# find / -name '*.jpg-large' -print 2>/dev/null
pattern = ".jpg-large"
print("Start searching of *" + pattern +  " in " + start)

found = []
for root, dirs, files in os.walk(start):
    for f in files:
        path = os.path.join(root, f)
        if str.endswith(path, pattern):
            found.append(path)

if len(found) > 0:
    print("Found some files:")
    for path in found:
        print(path)
    print("Renaming all to *.jpg")
else:
    print("Nothing to rename")
    sys.exit(0)

renamed = 0
for path in found:
    try:
        os.rename(path, path[:-6])
        renamed += 1
    except:
        print("ERROR renaming " + path)

print("Done. Renamed: " + renamed + "/" + len(found))
