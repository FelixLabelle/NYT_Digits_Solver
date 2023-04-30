from itertools import permutations,product

# NOTE: Define your numbers here
#num_list = [2,3,4,5,10,25]
#target = 64
#num_list = [25,5,3,2,10,15]
#target = 124
#num_list = [3,4,6,11,15,25]
#target = 296
#num_list = [8,3,4,6,15,9]
#target = 351
num_list = [19,25,5,3,9,13]
target = 477
# Sanity check to make sure the target is not in the number list
assert(target not in num_list)

# Defining all possible operators here
OPERATORS = ['-','+','/','*']

# Function to make op tuple ([NUMBERS], op1, .. opN) into a string
def op_tuple_to_string(op_val_tuple):
    return str(op_val_tuple[0][0]) + ''.join([f"{op}{num}" for num, op in zip(op_val_tuple[0][1:],op_val_tuple[1:])])
    
# NOTE: This doesn't work because of how eval handles order of operations
# so I implemented eval_tuple2 below (which is also quite a bit faster)
def eval_op_tuple(op_val_tuple):
    # op_val_tuple is a tuple where ([LIST NUMS], op1,.. opn)
    return eval(op_tuple_to_string(op_val_tuple))

# Function that iterates through the number and operator lists and evalutes it
def eval_op_tuple2(op_val_tuple):
    nums, *ops = op_val_tuple
    result = nums[0]
    for i, op in enumerate(ops):
        num = nums[i+1]
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '/':
            # NOTE: Makes sure that result is a whole number,
            # if not it assigns a value target could not have to result and 
            # exits the loop (and function)
            if result % num != 0:
                result = -1
                break
            result /= num
    return result
    
results = []
# Iterate through the list of numbers
for i in range(2,len(num_list)+1):
    # Operations are somewhat order invariant, so permutations are used to get all possible combinations 
    for elems in permutations(num_list,i):
        # iterate through all possible combinations of numbers and operations
        for curr_op_val_tuple in product([elems],*([OPERATORS]*(i-1))):
            # evaluate current combination
            result = eval_op_tuple2(curr_op_val_tuple)
            # Store combination if valid
            if result == target:
                results.append(curr_op_val_tuple)
                
# NOTE: read results right to left, using the previous numbers together
# You can revert to the tuple format by just printing results              
print([op_tuple_to_string(result) for result in results])
print(len(results))