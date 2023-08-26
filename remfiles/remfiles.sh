#!/bin/bash
#char_num=$(ls ./ | wc -m)
for char_num in $(ls | wc -m)
echo $char_num
while [[ $char_num -le 5 ]]
do echo less
done
