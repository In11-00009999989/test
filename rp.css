#include <stdio.h>

int MAXSIZE = 7;
int stack[8];
int top = -1;

int isempty() {

   if(top == -1)
      return 1;
   else
      return 0;
}

int isfull() {

   if(top == MAXSIZE)
      return 1;
   else
      return 0;
}

int peek() {
   return stack[top];
}

int pop() {
   int data;

   if(!isempty()) {
      data = stack[top];
      top = top - 1;
      return data;
   } else {
      printf("Could not retrieve data, Stack is empty.\n");
   }
}

int push(int data) {

   if(!isfull()) {
      top = top + 1;
      stack[top] = data;
   } else {
      printf("Could not insert data, Stack is full.\n");
   }
}

int main() {
   // push items on to the stack
  // push(3);
   //push(5);
   //push(9);
   //push(1);
   //push(12);
   //push(15);

   //printf("Element at top of the stack: %d\n" ,peek());
   //printf("Elements: \n");

   // print stack data
   //while(!isempty()) {
     // int data = pop();
      //printf("%d\n",data);
   //}


//push(7);
//push(7);
//push(7);
 //push(7);
 //push(7);
 //push(7);
 //push(7);
 //push(7);
 //printf("Stack full: %s\n" , isfull()?"true":"false");
  // printf("Stack empty: %s\n" , isempty()?"true":"false");/"



  int op[5];
  op[0]=30;
  op[1]=20;
  op[2]=5;

  op[3]=-1;
  op[4]=-4;



   for(int i=0; i<5; i++){


       printf("%i  ",op[i]);

       if (op[i]>=0){
           push(op[i]);
       } else if(op[i]==-1){
           push( pop()+ pop());
       }else if (op[i]==-2){
           push (-1*pop()+ pop()) ;
       }else if(op[i]==-3){
           push (pop()*pop());
       }else if (op[i]==-4){
           push(1.0/pop()*pop());
       }

   }
printf("%i",pop());


   return 0;
}
