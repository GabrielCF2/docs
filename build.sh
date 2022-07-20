rm -rf .retype/*

scripts=$(find /mnt/MOOKER/cumcraft/docs -name "*.py")

for s in $scripts; do
    python $s
done