read_dir(){
    for file in `ls -a $1`
    do
        if [ -d $1"/"$file ]
        then
            if [[ $file != '.' && $file != '..' ]]
            then
                read_dir $1"/"$file
            fi
        else
            echo $1"/"$file
		cp $1"/"$file /home/tony_chen_x19/floorplan_image/${n}_$file
	    n=$(($n+1))
	    echo $n
        fi
    done
}


n=1
read_dir "/home/tony_chen_x19/code/FloorplanTransformation/code/floorplan_image/"
