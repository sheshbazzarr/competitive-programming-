function insertionSort(array){
	
	for(let i=1;i<array.length;i++){
		for(let j=i;j>0;j--){
		if(array[j]<array[j-1]{
			const temp=array[i];
			array[j]=array[j-1];
			array[j-1]=temp;
		}
			else{break;}}}
	return array;
	

}
insertionSort([1,4,2,8,345,43,32,543,67,8])
