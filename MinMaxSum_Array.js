function Min_MaxSum(arr){
  //Length of array
    let arr_length=arr.length;
  //One less than length of array i.e second last position of array
    let second_last=arr_length-1;
  // Setting the min_sum and max_sum values to 0
    let min_sum=0;
    let max_sum=0;
    for(let i=0;i<second_last;i++){
        min_sum+=arr[i];
        max_sum+=arr[second_last];
        second_last-=1;
    }
    console.log(min_sum,max_sum);
}
var arr=[2,4,6,8];
Min_MaxSum(arr);


