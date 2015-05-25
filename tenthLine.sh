
## Solution 1: making use of the head together with tail to get the 10th line
line=`wc -l file.txt`; num=`echo $line | awk '{print $1}'`; if(($num < 10));then echo 'Less than 10 lines!'; else head -10 file.txt | tail -1 ;fi

## Solution 2: making use of sed to get the 10th line
line=`wc -l file.txt`; num=`echo $line | awk '{print $1}'`; if(($num < 10));then echo 'Less than 10 lines!'; else sed -n '10p' file.txt ;fi

## Solution 3: making use of the 'cat -n' option to get the 10th line
line=`wc -l file.txt`; num=`echo $line | awk '{print $1}'`; if(($num < 10));then echo 'Less than 10 lines!'; else cat -n file.txt | awk '{if($1==10){$1="";print}}' | sed 's/^ //' ;fi


