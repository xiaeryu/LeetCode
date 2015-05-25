

awk '{printf $1 " "}' test | sed 's/ $/\n/'; awk '{printf $2 " "}' test | sed 's/ $/\n/'
