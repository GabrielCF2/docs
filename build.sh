scripts=$(find /mnt/MOOKER/survi_craft/docs -name "*.py")

for s in $scripts; do
    python $s
done